## ADDED Requirements

### Requirement: Calculator tool
The system SHALL provide a calculator tool that evaluates mathematical expressions using Python's `eval()` or equivalent safe evaluation.

### Requirement: Datetime tool
The system SHALL provide a datetime tool that returns the current date and time in ISO format.

### Requirement: Search tool
The system SHALL provide a search tool that queries DuckDuckGo for real-time information.

### Requirement: Tool naming convention
Each tool SHALL have a descriptive name and docstring for the agent to understand its purpose.

#### Scenario: Calculator evaluates expression
- **WHEN** agent calls the calculator tool with "2 + 2 * 10"
- **THEN** the tool returns "22"

#### Scenario: Datetime returns current time
- **WHEN** agent calls the datetime tool
- **THEN** the tool returns the current UTC datetime in ISO 8601 format

#### Scenario: Search returns results
- **WHEN** agent calls the search tool with "weather today"
- **THEN** the tool returns relevant search results
