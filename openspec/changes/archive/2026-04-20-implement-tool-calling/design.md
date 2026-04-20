## Context

当前 `app/agent/tools.py` 中的 `CalculatorTool` 和 `DateTimeTool` 是具体类，直接暴露给 LangChain。工具列表硬编码在 `factory.py` 中，无法被其他客户端使用。

## Goals / Non-Goals

**Goals:**
- 定义清晰的 `BaseTool` 抽象接口
- 实现 `ToolRegistry` 作为工具的单一数据源
- 保持与 LangChain 的兼容（通过适配器）
- 支持工具的热注册（运行时添加新工具）
- 统一 Agent 路径，移除旧的双重实现

**Non-Goals:**
- 不实现 OpenAI/Anthropic 原生 function calling（预留扩展点，后续实现）
- 不改变现有 Agent 的外部行为（API/CLI 接口不变）
- 不支持异步工具（仅 sync，后续扩展）

## Decisions

### Decision 1: 目录结构

```
app/tools/
├── __init__.py
├── base.py          # BaseTool 抽象基类
├── registry.py      # ToolRegistry
└── adapter.py       # LangChain 适配器
```

选择理由：独立 `tools/` 目录避免与 `agent/` 耦合，体现基础设施定位。

### Decision 2: BaseTool 接口设计

```python
class BaseTool(ABC):
    @property
    def name(self) -> str: ...

    @property
    def description(self) -> str: ...

    def invoke(self, input: str) -> str: ...
```

选择理由：最小化接口，仅暴露核心能力。LangChain 的 `@tool` 装饰器作为适配器层。

### Decision 3: ToolRegistry 单例模式

```python
class ToolRegistry:
    _instance: ToolRegistry | None = None

    @classmethod
    def get_instance(cls) -> ToolRegistry: ...

    def register(self, tool: BaseTool) -> None: ...
    def get(self, name: str) -> BaseTool | None: ...
    def list(self) -> list[BaseTool]: ...
    @staticmethod
    def get_default_tools() -> list[BaseTool]: ...
```

选择理由：全局单例确保工具注册表在应用内唯一，避免多实例状态不一致。

### Decision 4: LangChain 适配

通过 `create_langchain_tool(tool: BaseTool) -> StructuredTool` 函数转换，保持与现有 Agent 的兼容。

### Decision 5: 统一工具路径

移除旧的 `@tool` 装饰器函数，所有 Agent 组件统一通过 ToolRegistry 获取工具：
- `app/agent/factory.py` → ToolRegistry.get_default_tools() + create_langchain_tools()
- `app/agent/service.py` → ToolRegistry.get_default_tools() + create_langchain_tools()

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     ToolRegistry                        │
│  (单例, 全局工具注册表)                                   │
│  - register(tool)                                      │
│  - get(name) → BaseTool                                │
│  - list() → list[BaseTool]                             │
│  - get_default_tools() → list[BaseTool]                │
└─────────────────────────────────────────────────────────┘
              ▲                           │
              │                           ▼
    ┌─────────┴─────────┐    ┌────────────────────────┐
    │   CalculatorTool  │    │    DateTimeTool        │
    │   (实现 BaseTool)  │    │    (实现 BaseTool)    │
    └───────────────────┘    └────────────────────────┘
              │                           │
              ▼                           ▼
    ┌─────────────────────────────────────────────┐
    │           create_langchain_tool()            │
    │  (适配器: BaseTool → StructuredTool)         │
    └─────────────────────────────────────────────┘
                          │
                          ▼
              ┌─────────────────────────┐
              │   LangChain Agent      │
              │   (factory.py)         │
              └─────────────────────────┘
```

## Key Files

| File | Change |
|------|--------|
| `app/tools/__init__.py` | 新增 |
| `app/tools/base.py` | 新增 |
| `app/tools/registry.py` | 新增 |
| `app/tools/adapter.py` | 新增 |
| `app/agent/tools.py` | 重构，移除旧 @tool 函数，仅保留 BaseTool 实现 |
| `app/agent/factory.py` | 重构，使用 ToolRegistry |
| `app/agent/service.py` | 重构，使用 ToolRegistry |
| `pyproject.toml` | 添加 python-multipart 依赖 |
| `tests/test_tools.py` | 新增，21 个单元测试 |
