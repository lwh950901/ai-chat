## ADDED Requirements

### Requirement: Anthropic Client Initialization

Anthropic 客户端 SHALL 使用 Anthropic API Key 和配置初始化。

#### Scenario: Initialize with valid configuration

- **WHEN** 提供有效的 ANTHROPIC_API_KEY 和模型配置时
- **THEN** AnthropicClient SHALL 成功初始化

#### Scenario: Initialize without API key

- **WHEN** ANTHROPIC_API_KEY 未提供或为空时
- **THEN** AnthropicClient SHALL 抛出 ConfigurationError

### Requirement: Send Message to Claude

Anthropic 客户端 SHALL 能够发送消息给 Claude 模型并接收回复。

#### Scenario: Send single message and receive response

- **WHEN** 用户发送消息 "Hello" 时
- **THEN** AnthropicClient SHALL 调用 Anthropic Messages API 并返回 AI 的回复文本

#### Scenario: Send message with system prompt

- **WHEN** 用户消息需要包含 system prompt 时
- **THEN** AnthropicClient SHALL 将 system prompt 作为单独参数发送

### Requirement: Anthropic Response Parsing

客户端 SHALL 正确解析 Anthropic API 的响应格式。

#### Scenario: Extract content from response

- **WHEN** Anthropic API 返回成功响应时
- **THEN** 客户端 SHALL 从响应中提取 content 字段并返回纯文本
