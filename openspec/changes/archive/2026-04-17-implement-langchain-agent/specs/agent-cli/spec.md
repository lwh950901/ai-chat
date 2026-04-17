## ADDED Requirements

### Requirement: Agent provider CLI option
The CLI SHALL accept `--provider agent` to use the LangChain Agent instead of direct LLM calls.

### Requirement: Agent mode indicator
When using agent mode, the CLI SHALL display an indicator that agent mode is active.

### Requirement: Agent streaming in CLI
The CLI SHALL support `--stream` with agent mode, displaying tool calls and thoughts as they occur.

#### Scenario: CLI uses agent provider
- **WHEN** user runs `ai-chat --provider agent "What's the weather?"`
- **THEN** the CLI invokes the agent and displays the response

#### Scenario: CLI agent mode with streaming
- **WHEN** user runs `ai-chat --provider agent --stream "Calculate 100-50"`
- **THEN** the CLI displays tool calls as they happen, followed by the final response
