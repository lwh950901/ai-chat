## ADDED Requirements

### Requirement: CLI main entry point
The CLI SHALL provide an `ai-chat` command as the main entry point, registered via `console_scripts` in `pyproject.toml`.

### Requirement: Interactive conversation mode
When invoked without a message argument, the CLI SHALL enter interactive mode, presenting a `>>>` prompt and reading user input line-by-line until EOF or `exit` command.

### Requirement: Single message mode
When invoked with a message argument (`ai-chat "Hello"`), the CLI SHALL send the message to the LLM, print the response, and exit.

### Requirement: Exit command
During interactive mode, the CLI SHALL recognize `exit` or `quit` (case-insensitive) as the command to terminate the session.

#### Scenario: Interactive mode启动
- **WHEN** user runs `ai-chat` without arguments
- **THEN** CLI displays a welcome message and `>>>` prompt
- **AND** waits for user input

#### Scenario: Single message mode
- **WHEN** user runs `ai-chat "Hello, how are you?"`
- **THEN** CLI sends the message to the configured LLM provider
- **AND** prints the response
- **AND** exits immediately

#### Scenario: Exit interactive mode
- **WHEN** user types `exit` during interactive mode
- **THEN** CLI terminates the session and exits gracefully
