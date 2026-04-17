## Context

当前 AI Chat 应用使用 LangChain 库但仅利用其基础的 LLM 调用能力。引入 LangChain Agent 框架可以实现 ReAct（Reasoning + Acting）模式，让 AI 能够主动调用工具来完成任务，而非仅生成文本响应。

## Goals / Non-Goals

**Goals:**
- 实现基于 LangChain ReAct 模式的 Agent
- 提供内置工具集（search, calculator, datetime）
- 通过 `agent` provider 复用现有 ChatService 架构
- 支持流式输出（工具调用过程可视化）
- API 和 CLI 均可使用 Agent 模式

**Non-Goals:**
- 不实现复杂的自定义工具注册表（V1 仅内置工具）
- 不实现多 Agent 协作
- 不实现 Agent 持久化（每次调用独立）

## Decisions

### Decision 1: 使用 LangChain Agent 框架而非自定义实现

**选择:** 使用 `langchain.agents` 的 `create_react_agent` 或 `create_openai_functions_agent`

**理由:**
- LangChain 提供成熟的 Agent 框架，减少样板代码
- ReAct 模式经过广泛验证，适合工具调用场景
- 支持流式输出，便于调试和用户理解

替代方案:
- **自定义 Agent**: 完全控制但工作量大，需要自己处理工具调用循环、状态管理等

### Decision 2: 工具实现方式

**选择:** 使用 LangChain 内置工具 + 简单自定义工具

**理由:**
- `langchain.agents.load_tools` 可加载预置工具（search, calculator）
- 自定义工具实现 `BaseTool` 接口即可
- 避免过度封装，保持与 LangChain 原生体验一致

### Decision 3: Agent 作为 Provider 而非独立服务

**选择:** 在现有 ChatService 架构中添加 `agent` provider

**理由:**
- 复用现有的对话管理、流式输出、API 路由
- 用户只需 `--provider agent` 即可切换
- 与 CLI 和 API 无缝集成

## Risks / Trade-offs

| Risk | Mitigation |
|------|------------|
| 工具调用导致响应延迟高 | 提供流式输出让用户看到思考过程 |
| Agent 工具选择可能不准确 | V1 仅提供有限工具集，减少出错概率 |
| 工具调用错误传播 | Agent 需正确处理工具异常，返回友好错误信息 |
