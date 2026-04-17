## 1. 修改 Agent Client

- [x] 1.1 在 `src/ai_chat/agent/client.py` 的 `create_agent_client` 函数添加 `base_url: str | None = None` 参数
- [x] 1.2 将 `base_url` 传递给 `ChatOpenAI`

## 2. 修改工厂函数

- [x] 2.1 在 `src/ai_chat/clients/factory.py` 的 agent 分支传递 `base_url` 参数

## 3. 修改 API Server

- [x] 3.1 在 `src/ai_chat/api/server.py` 的 `_get_llm_client` 函数，调用 `create_llm_client("agent", ...)` 时传递 `base_url`

## 4. 修改 CLI

- [x] 4.1 在 `src/ai_chat/cli/factory.py` 的 `create_llm_client_factory` 函数传递 `base_url` 给 agent client

## 5. 测试验证

- [x] 5.1 运行 pytest 确保现有测试通过 (9 passed)
- [ ] 5.2 手动测试 Agent + MiniMax 模式（如有 API Key）
