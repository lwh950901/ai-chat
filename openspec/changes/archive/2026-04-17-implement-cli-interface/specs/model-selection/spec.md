## ADDED Requirements

### Requirement: Provider selection via --provider
The CLI SHALL accept a `--provider` flag to select the LLM provider, with supported values: `openai`, `anthropic`.

### Requirement: Model selection via --model
The CLI SHALL accept a `--model` flag to specify the model name. If not provided, the CLI SHALL use the default model for the selected provider.

### Requirement: Provider and model configuration
The CLI SHALL read provider configuration (API keys, base URLs) from the same settings used by the API server.

#### Scenario: Specify provider
- **WHEN** user runs `ai-chat --provider anthropic "Hello"`
- **THEN** CLI uses the Anthropic client to send the message
- **AND** uses the default Anthropic model unless `--model` is also specified

#### Scenario: Specify both provider and model
- **WHEN** user runs `ai-chat --provider openai --model gpt-4o "Hello"`
- **THEN** CLI uses the OpenAI client with model `gpt-4o`

#### Scenario: Default provider
- **WHEN** user runs `ai-chat "Hello"` without `--provider`
- **THEN** CLI uses `openai` as the default provider
- **AND** uses the default OpenAI model
