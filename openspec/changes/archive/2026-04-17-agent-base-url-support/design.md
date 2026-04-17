## Context

当前 `create_agent_client` 函数签名：
```python
def create_agent_client(api_key: str, model: str = "gpt-4", **kwargs) -> BaseLLMClient
```

`base_url` 没有被传递，导致 `ChatOpenAI` 始终使用默认的 OpenAI 地址。

## Goals / Non-Goals

**Goals:**
- 让 Agent 支持通过 `base_url` 使用 MiniMax 等 OpenAI 兼容 API

**Non-Goals:**
- 不改变 Agent 的核心功能（工具调用、ReAct 模式）
- 不添加新的 Provider

## Decisions

### Decision 1: 在 `create_agent_client` 增加 `base_url` 参数

**选择**: 在 `agent/client.py` 的 `create_agent_client` 函数中添加 `base_url: str | None = None` 参数，并传递给 `ChatOpenAI`。

**理由**:
- 最小改动，只需添加一个参数
- 与 `OpenAIClient` 的设计保持一致
- 现有的 `**kwargs` 无法传递 `base_url` 给 `ChatOpenAI`

** Alternatives**:
- 使用 `**kwargs` 传递：不够明确，`base_url` 属于常用参数
- 创建新的 `create_minimax_agent` 函数：增加复杂度，不必要

## Risks / Trade-offs

无显著风险。这是纯传递性改动，不改变任何逻辑。
