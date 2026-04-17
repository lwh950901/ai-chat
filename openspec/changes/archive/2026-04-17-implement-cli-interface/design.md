## Context

当前 AI Chat 应用通过 FastAPI Web API 提供服务，用户需要启动服务器并发送 HTTP 请求才能使用。实现 CLI 界面可让用户在终端直接对话，提升开发和调试效率。

CLI 与 API 共用相同的 `ChatService` 和 `InMemoryConversationStore`，保持行为一致。CLI 通过 `typer` 框架构建，提供交互模式和单次问答模式。

## Goals / Non-Goals

**Goals:**
- 提供 `ai-chat` 命令行入口，支持交互式对话
- 支持 `--provider` 和 `--model` 参数选择模型
- 支持流式输出（`--stream`），实时显示 AI 回复
- 提供 `history` 和 `clear` 子命令管理对话历史
- 复用现有 ChatService，确保与 API 行为一致

**Non-Goals:**
- 不实现 API Key 输入界面（通过环境变量或配置文件提供）
- 不实现多会话管理（每个 CLI 调用独立会话）
- 不实现复杂命令补全（basic shell completion 即可）

## Decisions

### Decision 1: CLI 框架选择 Typer

**选择:** Typer（基于 Click，支持 async 命令）

**理由:**
- Typer 内置 Click，支持 async def 命令，可直接 await 异步方法
- 与 FastAPI 同样基于 Click生态，completion 支持好
- 比 Click 更简洁，类型提示完善
- 缺点：比 Click 轻量，复杂交互不如 Click 灵活

替代方案:
- **Click**: 更成熟，但需要处理 async 比较繁琐
- **H丹霞**: 国内团队开发，中文文档，但生态不如 Typer

### Decision 2: 复用 ChatService 而非新建 LLM 调用逻辑

**选择:** CLI 初始化时创建 ChatService 实例，通过 settings 获取配置

**理由:**
- 与 API 保持行为一致，避免代码重复
- 流式输出直接复用 `service.stream()` 方法
- conversation store 复用 `InMemoryConversationStore`

### Decision 3: 流式输出通过 `service.stream()` 实现

CLI 调用 `service.stream()` 获取同步生成器，在 async 命令中用 `asyncio.to_thread()` 桥接到 SSE 输出。

**理由:**
- 与 API `/chat/stream` 端点行为一致
- `service.stream()` 返回 `(Iterator[str], conversation_id)`，可直接遍历打印

### Decision 4: CLI 作为 `console_scripts` 入口

**选择:** 在 `pyproject.toml` 中配置 `ai-chat` 为 console_scripts 入口点

```toml
[project.scripts]
ai-chat = "ai_chat.cli.main:app"
```

**理由:**
- 安装后直接可用 `ai-chat` 命令
- 跨平台兼容性好
- 无需修改 `PYTHONPATH` 或使用 `python -m`

## Risks / Trade-offs

| Risk | Mitigation |
|------|------------|
| 流式输出在高延迟网络下体验差 | 提供 `--no-stream` 选项降级为同步模式 |
| CLI 与 API 共享 InMemoryConversationStore | CLI 独立初始化 store，不与 API 共享状态 |
| 交互模式退出后对话历史丢失 | 提供 `history` 命令查看当前会话历史 |
