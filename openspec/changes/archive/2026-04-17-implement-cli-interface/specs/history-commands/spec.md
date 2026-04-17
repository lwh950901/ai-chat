## ADDED Requirements

### Requirement: history subcommand
The CLI SHALL provide a `history` subcommand that displays the conversation history for the current CLI session.

### Requirement: clear subcommand
The CLI SHALL provide a `clear` subcommand that clears the conversation history for the current CLI session.

### Requirement: history shows messages
The `history` command SHALL display all messages in the current session with their roles (user/assistant) and content.

#### Scenario: View history
- **WHEN** user runs `ai-chat history`
- **THEN** CLI displays all messages in the current session
- **AND** each message shows its role and content

#### Scenario: Clear history
- **WHEN** user runs `ai-chat clear`
- **THEN** CLI clears all conversation history
- **AND** subsequent messages start a new conversation

#### Scenario: History in interactive mode
- **WHEN** user types `history` during interactive mode
- **THEN** CLI displays the conversation history
- **AND** returns to the prompt
