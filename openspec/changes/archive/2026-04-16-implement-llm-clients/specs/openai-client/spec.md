## ADDED Requirements

### Requirement: OpenAI Client Initialization

OpenAI 客户端 SHALL 使用 OpenAI API Key 和配置初始化。

#### Scenario: Initialize with valid configuration

- **WHEN** 提供有效的 OPENAI_API_KEY 和模型配置时
- **THEN** OpenAIClient SHALL 成功初始化

#### Scenario: Initialize without API key

- **WHEN** OPENAI_API_KEY 未提供或为空时
- **THEN** OpenAIClient SHALL 抛出 ConfigurationError

### Requirement: Send Message to GPT

OpenAI 客户端 SHALL 能够发送消息给 GPT 模型并接收回复。

#### Scenario: Send single message and receive response

- **WHEN** 用户发送消息 "Hello" 时
- **THEN** OpenAIClient SHALL 调用 OpenAI Chat API 并返回 AI 的回复文本

#### Scenario: Send message with system prompt

- **WHEN** 用户消息需要包含 system prompt 时
- **THEN** OpenAIClient SHALL 将 system prompt 作为第一条消息发送

### Requirement: OpenAI Response Parsing

客户端 SHALL 正确解析 OpenAI API 的响应格式。

#### Scenario: Extract content from response

- **WHEN** OpenAI API 返回成功响应时
- **THEN** 客户端 SHALL 从响应中提取 content 字段并返回纯文本
