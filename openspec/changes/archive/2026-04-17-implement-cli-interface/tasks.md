## 1. 项目依赖与结构

- [x] 1.1 添加 `typer` 依赖到 `pyproject.toml`
- [x] 1.2 添加 `rich` 依赖（增强 CLI 输出）
- [x] 1.3 创建 `src/ai_chat/cli/` 目录结构

## 2. CLI 入口与基础命令

- [x] 2.1 创建 `src/ai_chat/cli/__init__.py`
- [x] 2.2 创建 `src/ai_chat/cli/main.py`，使用 Typer 构建 `app`
- [x] 2.3 配置 `pyproject.toml` 的 `console_scripts` 入口点：`ai-chat = "ai_chat.cli.main:app"`

## 3. 交互模式实现

- [x] 3.1 实现 `interactive_mode()` 函数，显示 `>>>` 提示符
- [x] 3.2 实现 `exit` / `quit` 命令识别（大小写不敏感）
- [x] 3.3 实现单次消息模式：`cli_chat()` 函数
- [x] 3.4 在 `app` 中注册主命令，支持 `ai-chat "message"` 格式

## 4. 模型选择功能

- [x] 4.1 在 `main.py` 添加 `--provider` 选项（`openai` / `anthropic`）
- [x] 4.2 添加 `--model` 选项指定模型
- [x] 4.3 默认 provider 使用 `openai`，默认模型从 settings 读取

## 5. 流式输出功能

- [x] 5.1 添加 `--stream` 选项启用流式输出
- [x] 5.2 实现 `print_streaming()` 辅助函数，实时打印 token
- [x] 5.3 实现同步输出模式（默认）

## 6. 对话历史命令

- [x] 6.1 创建 `src/ai_chat/cli/commands.py`
- [x] 6.2 实现 `history` 子命令，显示当前会话消息
- [x] 6.3 实现 `clear` 子命令，清除会话历史
- [x] 6.4 在 Typer app 中注册子命令

## 7. ChatService 集成

- [x] 7.1 初始化 `ChatService` 实例（复用现有代码）
- [x] 7.2 实现 `send_message()` 封装，同步模式
- [x] 7.3 实现 `stream_message()` 封装，流式模式
- [x] 7.4 验证 CLI 与 API 行为一致

## 8. 测试与文档

- [x] 8.1 编写 CLI 单元测试（`tests/test_cli.py`）
- [x] 8.2 更新 `README.md`，添加 CLI 使用说明
- [x] 8.3 测试 `ai-chat --help` 命令
- [x] 8.4 测试单次问答和交互模式
