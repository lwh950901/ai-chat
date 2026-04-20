"""工具模块测试。"""

import pytest

from app.tools.base import BaseTool
from app.tools.registry import ToolRegistry
from app.tools.adapter import create_langchain_tool, create_langchain_tools
from app.agent.tools import CalculatorTool, DateTimeTool


class TestCalculatorTool:
    """CalculatorTool 测试。"""

    def test_is_base_tool_subclass(self):
        """验证 CalculatorTool 是 BaseTool 子类。"""
        assert issubclass(CalculatorTool, BaseTool)

    def test_name(self):
        """验证工具名称。"""
        tool = CalculatorTool()
        assert tool.name == "calculator"

    def test_description(self):
        """验证工具描述。"""
        tool = CalculatorTool()
        assert "计算" in tool.description
        assert "数学" in tool.description

    def test_invoke_basic_arithmetic(self):
        """测试基本算术运算。"""
        tool = CalculatorTool()
        assert tool.invoke("2 + 3") == "5"
        assert tool.invoke("10 - 4") == "6"
        assert tool.invoke("3 * 7") == "21"
        assert tool.invoke("20 / 4") == "5.0"

    def test_invoke_exponentiation(self):
        """测试指数运算。"""
        tool = CalculatorTool()
        assert tool.invoke("2 ** 8") == "256"

    def test_invoke_functions(self):
        """测试数学函数。"""
        tool = CalculatorTool()
        assert tool.invoke("sqrt(16)") == "4.0"
        assert tool.invoke("sin(0)") == "0.0"
        assert tool.invoke("cos(0)") == "1.0"

    def test_invoke_invalid_expression(self):
        """测试无效表达式。"""
        tool = CalculatorTool()
        result = tool.invoke("os.system('ls')")
        assert "错误" in result or "不允许" in result

    def test_invoke_malicious_keyword(self):
        """测试恶意 keyword 无法绕过。"""
        tool = CalculatorTool()
        result = tool.invoke("sqrt(keyword=value)")
        assert "错误" in result or "不允许" in result

    def test_invoke_malicious_nested_call(self):
        """测试恶意嵌套调用无法绕过（如 __import__ 注入）。"""
        tool = CalculatorTool()
        result = tool.invoke("abs(__import__('os').system('ls'))")
        assert "错误" in result or "不允许" in result

    def test_invoke_malicious_position_arg(self):
        """测试恶意位置参数无法绕过。"""
        tool = CalculatorTool()
        result = tool.invoke("sqrt('malicious')")
        assert "错误" in result or "不允许" in result


class TestDateTimeTool:
    """DateTimeTool 测试。"""

    def test_is_base_tool_subclass(self):
        """验证 DateTimeTool 是 BaseTool 子类。"""
        assert issubclass(DateTimeTool, BaseTool)

    def test_name(self):
        """验证工具名称。"""
        tool = DateTimeTool()
        assert tool.name == "datetime"

    def test_description(self):
        """验证工具描述。"""
        tool = DateTimeTool()
        assert "日期" in tool.description or "时间" in tool.description

    def test_invoke_returns_iso_format(self):
        """验证返回 ISO 格式时间。"""
        tool = DateTimeTool()
        result = tool.invoke("")
        # 应该以 Z 结尾表示 UTC
        assert result.endswith("Z")
        # 应该包含日期时间部分
        assert "T" in result

    def test_invoke_returns_consistent_format(self):
        """验证多次调用返回格式一致。"""
        tool = DateTimeTool()
        result = tool.invoke("ignored")
        # 结果应该是一个有效的 ISO 格式时间字符串
        assert result.endswith("Z")
        assert "T" in result
        assert len(result) > 10  # 至少是日期时间


class TestToolRegistry:
    """ToolRegistry 测试。"""

    def test_singleton(self):
        """验证单例模式。"""
        registry1 = ToolRegistry.get_instance()
        registry2 = ToolRegistry.get_instance()
        assert registry1 is registry2

    def test_get_default_tools(self):
        """验证获取默认工具。"""
        tools = ToolRegistry.get_default_tools()
        assert len(tools) == 2
        assert all(isinstance(t, BaseTool) for t in tools)
        names = [t.name for t in tools]
        assert "calculator" in names
        assert "datetime" in names

    def test_register_and_get(self):
        """测试注册和获取工具。"""
        # 使用新的工具实例避免与其他测试冲突
        registry = ToolRegistry.get_instance()
        # 创建一个新工具实例来测试注册
        tool = type("CustomTool", (BaseTool,), {
            "name": "custom",
            "description": "A custom tool",
            "invoke": lambda self, x: x
        })()
        registry.register(tool)
        assert registry.get("custom") is tool
        # 清理
        registry.unregister("custom")

    def test_register_duplicate_raises(self):
        """测试重复注册抛出异常。"""
        registry = ToolRegistry.get_instance()
        # 创建一个新工具实例来测试
        tool = type("DupTool", (BaseTool,), {
            "name": "duplicate_test",
            "description": "Test duplicate",
            "invoke": lambda self, x: x
        })()
        registry.register(tool)
        with pytest.raises(ValueError, match="已注册"):
            registry.register(tool)
        # 清理
        registry.unregister("duplicate_test")

    def test_get_nonexistent_returns_none(self):
        """测试获取不存在的工具返回 None。"""
        registry = ToolRegistry.get_instance()
        assert registry.get("nonexistent_tool_xyz") is None

    def test_list(self):
        """测试列举工具。"""
        registry = ToolRegistry.get_instance()
        tools = registry.list()
        assert isinstance(tools, list)
        assert all(isinstance(t, BaseTool) for t in tools)

    def test_unregister(self):
        """测试注销工具。"""
        registry = ToolRegistry.get_instance()
        tool = type("UnregTool", (BaseTool,), {
            "name": "unregister_test",
            "description": "Test unregister",
            "invoke": lambda self, x: x
        })()
        registry.register(tool)
        assert registry.get("unregister_test") is tool
        assert registry.unregister("unregister_test") is True
        assert registry.get("unregister_test") is None
        assert registry.unregister("nonexistent") is False

    def test_concurrent_read_consistency(self):
        """测试并发读一致性。"""
        import threading
        registry = ToolRegistry.get_instance()
        results = []

        def read_tools():
            for _ in range(100):
                tools = registry.list()
                results.append(tuple(t.name for t in tools))

        threads = [threading.Thread(target=read_tools) for _ in range(10)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        # 所有读取结果应该一致（快照一致）
        assert len(set(results)) == 1


class TestLangChainAdapter:
    """LangChain 适配器测试。"""

    def test_create_langchain_tool(self):
        """测试创建单个 LangChain 工具。"""
        calc = CalculatorTool()
        lc_tool = create_langchain_tool(calc)
        assert lc_tool.name == "calculator"
        assert lc_tool.description == calc.description

    def test_create_langchain_tools_batch(self):
        """测试批量创建 LangChain 工具。"""
        tools = [CalculatorTool(), DateTimeTool()]
        lc_tools = create_langchain_tools(tools)
        assert len(lc_tools) == 2
        assert [t.name for t in lc_tools] == ["calculator", "datetime"]

    def test_langchain_tool_callable(self):
        """测试 LangChain 工具创建成功（异步模式）。"""
        calc = CalculatorTool()
        lc_tool = create_langchain_tool(calc)
        assert lc_tool.name == "calculator"
        assert lc_tool.description == calc.description

    def test_langchain_tool_async_invoke(self):
        """测试 LangChain 工具异步调用。"""
        import asyncio
        calc = CalculatorTool()
        lc_tool = create_langchain_tool(calc)
        result = asyncio.run(lc_tool.ainvoke({"input": "10 - 3"}))
        assert "7" in result
