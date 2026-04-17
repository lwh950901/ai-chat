## ADDED Requirements

### Requirement: Agent provider in chat service
The chat service SHALL accept `agent` as a valid provider value, routing to the LangChain Agent instead of direct LLM calls.

### Requirement: Agent chat endpoint
When `provider=agent` is specified, the `/chat` endpoint SHALL invoke the agent with the user's message and return the agent's response.

### Requirement: Agent streaming endpoint
When `provider=agent` is specified, the `/chat/stream` endpoint SHALL stream the agent's response including intermediate tool calls.

### Requirement: Error handling
If the agent encounters an error during tool execution, it SHALL return an error message explaining what went wrong.

#### Scenario: Chat with agent provider
- **WHEN** POST `/chat` with `{"message": "What's 5+3?", "provider": "agent"}`
- **THEN** the agent processes the message using its tools and returns the result

#### Scenario: Agent tool execution error
- **WHEN** agent attempts to call a tool that fails
- **THEN** the error is caught and returned as a user-friendly message
