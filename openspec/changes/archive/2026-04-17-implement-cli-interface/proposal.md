## Why

当前 AI Chat 应用仅支持 Web API 方式交互，用户需要启动 FastAPI 服务器并发送 HTTP 请求才能使用。实现 CLI 界面可让用户在终端直接与 AI 对话，降低使用门槛，提升开发调试效率。

## What Changes

- 新增 `ai-chat` 命令行入口，支持交互式对话和单次问答
- 支持选择模型提供商（OpenAI / Anthropic / MiniMax）
- 支持流式输出，实时显示 AI 回复
- 提供对话历史管理命令（查看历史、清除历史）
- CLI 与 API 共享同一 ChatService，保持行为一致

## Capabilities

### New Capabilities

- `cli-entry`: 命令行入口，支持 `ai-chat` 主命令和交互模式
- `model-selection`: 模型选择，支持 `--model` 和 `--provider` 参数
- `streaming-output`: 流式输出，实时打印 AI token
- `history-commands`: 对话历史，支持 `history` 和 `clear` 子命令

### Modified Capabilities

- 无（API 服务端能力不变，CLI 复用现有 ChatService）

## Impact

- 新增 `src/ai_chat/cli/` 目录，包含 CLI 相关代码
- `pyproject.toml` 添加 `typer` 或 `click` 依赖（CLI 框架）
- README.md 添加 CLI 使用说明
- 对现有 API 和 conversation service 无侵入
