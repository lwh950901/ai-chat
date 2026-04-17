# agent-base-url Specification

## ADDED Requirements

### Requirement: Agent 支持通过 base_url 使用 OpenAI 兼容 API

#### Scenario: 使用 MiniMax API

- **WHEN** 用户配置 `OPENAI_BASE_URL=https://api.minimaxi.com/v1` 和 `MODEL=MiniMax-M2.7`
- **AND** 调用 `create_agent_client(api_key, model, base_url)`
- **THEN** Agent 应使用传入的 `base_url` 调用 MiniMax API

#### Scenario: 未配置 base_url

- **WHEN** 用户调用 `create_agent_client(api_key, model)` 不传 `base_url`
- **THEN** Agent 应使用默认的 OpenAI API 地址

## MODIFIED Requirements

无。
