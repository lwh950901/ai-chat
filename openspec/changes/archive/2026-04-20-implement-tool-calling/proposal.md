## Why

当前工具调用功能紧耦合在 LangChain Agent 中，工具（如 calculator、datetime）无法被 OpenAI/Anthropic 等标准客户端复用。引入通用 tool-calling 基础设施可以让所有 LLM 客户端共享同一套工具系统。

## What Changes

- 新增 `BaseTool` 抽象接口
- 新增 `ToolRegistry` 工具注册表，支持注册/获取/列举工具
- 重构现有 `CalculatorTool`、`DateTimeTool` 实现 `BaseTool` 接口
- `AgentClient` 改为通过 `ToolRegistry` 获取工具
- 为未来 OpenAI/Anthropic 原生 function calling 支持预留扩展点

## Capabilities

### New Capabilities

- `tool-registry`: 工具注册表（注册、获取、列举、创建默认工具集）
- `tool-base`: BaseTool 抽象基类定义工具接口
- `tool-adapter`: LangChain 工具适配器（将 BaseTool 转换为 LangChain StructuredTool）

### Modified Capabilities

- `agent-tools`: 重构为使用 ToolRegistry 而非硬编码工具列表

## Impact

- 新增 `app/tools/` 目录（BaseTool, ToolRegistry）
- 重构 `app/agent/tools.py` 实现 BaseTool 接口
- 重构 `app/agent/factory.py` 通过 ToolRegistry 获取工具
