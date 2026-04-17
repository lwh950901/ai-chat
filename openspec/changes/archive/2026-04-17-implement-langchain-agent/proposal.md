## Why

当前 AI Chat 应用仅支持简单的问答交互。引入 LangChain Agent 可以让 AI 主动调用工具、查询实时信息、执行多步骤任务，从"回答问题"升级为"智能助手"。

## What Changes

- 新增 `langchain-agent` 模块，提供 Agent 核心能力
- 实现内置工具：搜索、计算器、日期时间查询
- Agent 与现有 ChatService 集成，支持 `agent` provider
- API 和 CLI 均可通过 `--provider agent` 使用 Agent 模式
- 支持工具调用流式输出

## Capabilities

### New Capabilities

- `agent-core`: Agent 核心实现，基于 LangChain ReAct 模式
- `agent-tools`: 内置工具集（search, calculator, datetime）
- `agent-api`: Agent 模式 API 端点
- `agent-cli`: Agent 模式 CLI 选项

### Modified Capabilities

- `langchain-integration`: 扩展 LangChain 使用范围（从依赖声明到实际 Agent 应用）

## Impact

- 新增 `src/ai_chat/agent/` 目录
- `src/ai_chat/clients/factory.py` 新增 `agent` provider
- API 新增 `/chat/agent` 端点（或通过 `--provider agent` 复用现有端点）
- README.md 添加 Agent 使用说明
