## Why

AI Chat 应用需要与大型语言模型通信才能实现聊天功能。目前项目只有配置管理，缺少实际调用 LLM 的客户端模块。有了 LLM 客户端，应用才能发送用户消息并接收 AI 回复。

## What Changes

- 新增 OpenAI GPT 系列模型客户端封装
- 新增 Anthropic Claude 模型客户端封装
- 统一的双客户端接口设计
- 支持 LangChain 集成调用

## Capabilities

### New Capabilities
- `llm-client`: LLM 客户端核心接口和实现
- `openai-client`: OpenAI GPT 系列模型调用封装
- `anthropic-client`: Anthropic Claude 模型调用封装

### Modified Capabilities
<!-- No existing capabilities are being modified -->

## Impact

- `src/ai_chat/` - 新增 LLM 客户端模块
- `requirements.txt` - 无需新增依赖（openai, anthropic 已存在）
- `openspec/specs/langchain-integration/` - 可通过 LLM 客户端实现 LangChain 集成
