# Design: 修复 Tool-Calling Code Review 问题

## 1. 线程安全修复

### 问题
`ToolRegistry` 单例的 `get_instance()` 和 `register()` 在多线程环境下存在竞态条件。

### 方案
使用 `threading.Lock` 实现 double-check locking：

```python
import threading

class ToolRegistry:
    _instance: "ToolRegistry | None" = None
    _lock = threading.Lock()

    def __init__(self):
        self._tools: dict[str, "BaseTool"] = {}

    @classmethod
    def get_instance(cls) -> "ToolRegistry":
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # double-check
                    cls._instance = cls()
        return cls._instance

    def register(self, tool: "BaseTool") -> None:
        with self._lock:  # register 也需要锁保护
            if tool.name in self._tools:
                raise ValueError(f"工具 '{tool.name}' 已注册")
            self._tools[tool.name] = tool
```

为了避免 `list()` 在并发 `register()` / `unregister()` 时读取到变化中的字典，`get()`、`list()`、`unregister()` 也应统一使用同一把锁；其中 `list()` 应在锁内构造快照后返回。

### 新增 unregister 方法
```python
def unregister(self, name: str) -> bool:
    """注销工具。"""
    with self._lock:
        if name in self._tools:
            del self._tools[name]
            return True
        return False
```

---

## 2. LangChain Adapter 修复

### 问题
`StructuredTool(args_schema=..., func=...)` 参数组合不兼容。

### 方案
移除 `args_schema`，使用纯 `func` 模式：

```python
def create_langchain_tool(tool: BaseTool) -> StructuredTool:
    return StructuredTool(
        name=tool.name,
        description=tool.description,
        func=_create_sync_wrapper(tool),
    )
```

---

## 3. AST 验证补全

### 问题
函数调用参数的递归验证不完整，`ast.Call.args` 和 `ast.keyword.value` 都可能成为绕过入口。

### 方案
```python
elif isinstance(n, ast.Call):
    if not isinstance(n.func, ast.Name) or n.func.id not in ALLOWED_MATH_NAMES:
        raise ValueError(f"不允许的函数: {ast.dump(n.func)}")
    return all(check_node(arg) for arg in n.args) and all(check_node(keyword) for keyword in n.keywords)
elif isinstance(n, ast.keyword):
    return check_node(n.value)  # 递归验证 keyword value
```

这里需要补充说明：仅验证 `ast.keyword` 还不够，`ast.Call.args` 中的嵌套表达式同样必须递归检查，否则像 `abs(__import__("os").system("ls"))` 这类输入仍可能绕过校验。

---

## 4. 其他优化

### 错误消息格式
`CalculatorTool.invoke` 文档说 `RuntimeError`，实际返回错误字符串。统一为返回错误字符串（已有行为）。

### UTC 时间格式化
```python
# 简化前
datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
# 简化后
datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
```

---

## 文件修改清单

| 文件 | 修改内容 |
|------|----------|
| `app/tools/registry.py` | 添加 `_lock`，实现 double-check locking，添加 `unregister()` |
| `app/tools/adapter.py` | 移除 `args_schema` 参数 |
| `app/agent/tools.py` | 修复 AST 验证，简化 UTC 格式化 |
| `tests/test_tools.py` | 使用 `unregister()` 清理测试数据，并补充并发与恶意嵌套输入回归测试 |
