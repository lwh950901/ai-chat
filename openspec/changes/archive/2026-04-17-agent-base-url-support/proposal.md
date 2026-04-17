## Why

当前 Agent 模式无法使用 MiniMax M2.7，因为 `create_agent_client` 没有传递 `base_url` 参数给底层的 `ChatOpenAI`。当用户在 `.env` 中配置 `OPENAI_BASE_URL=https://api.minimaxi.com/v1` 时，Agent 仍然使用 OpenAI 官方地址，导致无法调用 MiniMax。

## What Changes

- 修改 `create_agent_client` 函数，增加 `base_url` 参数传递
- 修改 `create_llm_client` 工厂函数，在 agent 分支传递 `base_url`
- 确保 API server 和 CLI 调用 agent 时传递 `base_url`

## Capabilities

### New Capabilities
- `agent-base-url`: Agent 支持通过 base_url 配置使用 MiniMax 等 OpenAI 兼容 API

## Impact

- `src/ai_chat/clients/factory.py` - 传递 base_url 给 agent 分支
- `src/ai_chat/agent/client.py` - 接收并传给 ChatOpenAI
- `src/ai_chat/agent/factory.py` - 创建 Agent 时注入 base_url
