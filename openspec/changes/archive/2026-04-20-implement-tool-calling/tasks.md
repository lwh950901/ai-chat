## 1. 创建 tools 模块目录

- [x] 1.1 创建 `app/tools/` 目录结构
- [x] 1.2 创建 `app/tools/__init__.py`，导出 BaseTool, ToolRegistry

## 2. 实现 BaseTool 抽象基类

- [x] 2.1 在 `app/tools/base.py` 定义 `BaseTool` ABC
- [x] 2.2 定义 `name`, `description` 属性
- [x] 2.3 定义 `invoke(input: str) -> str` 抽象方法

## 3. 实现 ToolRegistry

- [x] 3.1 在 `app/tools/registry.py` 实现 `ToolRegistry` 单例类
- [x] 3.2 实现 `register(tool: BaseTool)` 注册方法
- [x] 3.3 实现 `get(name: str) -> BaseTool | None` 获取方法
- [x] 3.4 实现 `list() -> list[BaseTool]` 列举方法
- [x] 3.5 实现 `get_default_tools() -> list[BaseTool]` 工厂方法

## 4. 实现 LangChain 适配器

- [x] 4.1 在 `app/tools/adapter.py` 实现 `create_langchain_tool()`
- [x] 4.2 处理参数模式转换（BaseTool → StructuredTool schema）

## 5. 重构现有工具

- [x] 5.1 重构 `CalculatorTool` 实现 `BaseTool` 接口
- [x] 5.2 重构 `DateTimeTool` 实现 `BaseTool` 接口
- [x] 5.3 移除旧 `@tool` 装饰器函数，统一使用 ToolRegistry 路径
- [x] 5.4 重构 `app/agent/service.py` 使用 ToolRegistry

## 6. 重构 Agent Factory

- [x] 6.1 修改 `app/agent/factory.py` 使用 `ToolRegistry.get_default_tools()`
- [x] 6.2 使用 `create_langchain_tool()` 转换为 LangChain 工具

## 7. 补充依赖和测试

- [x] 7.1 添加 `python-multipart` 到 `pyproject.toml` 依赖
- [x] 7.2 创建 `tests/test_tools.py` 单元测试

## 8. 验证

- [x] 8.1 运行 `pytest tests/` - 81 个测试全部通过
- [x] 8.2 测试 CLI: `ai-chat main "What's 15 * 23?" --provider agent`
- [x] 8.3 测试 datetime 工具: `ai-chat main "What time is it?" --provider agent`
