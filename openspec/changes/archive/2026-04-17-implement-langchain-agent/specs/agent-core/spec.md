## ADDED Requirements

### Requirement: Agent factory function
The system SHALL provide an `create_agent()` function that creates a LangChain Agent with the configured LLM and tools.

### Requirement: ReAct agent pattern
The agent SHALL use the ReAct (Reasoning + Acting) pattern to dynamically determine which tool to call based on user input.

### Requirement: Agent invocation
The agent SHALL accept a user message and return the agent's response, handling the full tool-call loop internally.

### Requirement: Streaming support
The agent SHALL support streaming output, yielding intermediate thoughts and tool calls as they occur.

#### Scenario: Create agent with default tools
- **WHEN** `create_agent()` is called with default settings
- **THEN** an agent is returned with the configured LLM and default tools loaded

#### Scenario: Agent processes a user query
- **WHEN** user asks "What's 15 * 23?"
- **THEN** agent invokes the calculator tool and returns the result "345"

#### Scenario: Agent streaming output
- **WHEN** agent is invoked with streaming enabled
- **THEN** intermediate tool calls and thoughts are yielded as they occur
