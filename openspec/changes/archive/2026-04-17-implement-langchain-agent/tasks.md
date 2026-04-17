## 1. Agent 核心模块

- [x] 1.1 创建 `src/ai_chat/agent/` 目录结构
- [x] 1.2 创建 `src/ai_chat/agent/__init__.py`
- [x] 1.3 实现 `create_agent()` 工厂函数
- [x] 1.4 实现 `AgentService` 类封装

## 2. 内置工具集

- [x] 2.1 实现 `calculator` 工具（安全数学计算）
- [x] 2.2 实现 `datetime` 工具（获取当前时间）
- [x] 2.3 搜索工具（暂不使用外部依赖，简化为占位）
- [x] 2.4 添加工具到 Agent

## 3. Agent 与 ChatService 集成

- [x] 3.1 在 `clients/factory.py` 添加 `agent` provider 分支
- [x] 3.2 在 `ChatService` 添加 `agent` provider 支持（通过通用 client 接口）
- [x] 3.3 实现 Agent 流式输出支持

## 4. API 端点

- [x] 4.1 在 `/chat` 端点支持 `provider=agent`
- [x] 4.2 在 `/chat/stream` 端点支持 `provider=agent`
- [x] 4.3 添加 Agent 错误处理

## 5. CLI 集成

- [x] 5.1 在 CLI 添加 `--provider agent` 选项支持
- [x] 5.2 在 CLI 显示 Agent 模式标识
- [x] 5.3 测试 Agent CLI 模式

## 6. 测试

- [x] 6.1 编写 Agent 单元测试
- [x] 6.2 测试 Calculator 工具
- [x] 6.3 测试 Datetime 工具
- [x] 6.4 测试 Agent API 端点

## 7. 文档

- [x] 7.1 更新 README.md 添加 Agent 使用说明
- [x] 7.2 更新 MEMORY.md
- [x] 7.3 更新 ai-chat-project-plan.md
