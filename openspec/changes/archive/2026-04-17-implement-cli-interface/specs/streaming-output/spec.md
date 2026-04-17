## ADDED Requirements

### Requirement: Streaming output via --stream
The CLI SHALL accept a `--stream` flag to enable streaming output, printing each token as it arrives.

### Requirement: Synchronous output by default
When `--stream` is not specified, the CLI SHALL wait for the complete response before printing.

### Requirement: Streaming behavior
When streaming is enabled, the CLI SHALL print tokens without newlines as they arrive, and print a newline at the end.

#### Scenario: Streaming output enabled
- **WHEN** user runs `ai-chat --stream "Tell me a story"`
- **THEN** CLI prints each token as it arrives
- **AND** tokens appear without newlines between them
- **AND** a final newline is printed when complete

#### Scenario: Synchronous output (default)
- **WHEN** user runs `ai-chat "Tell me a story"` without `--stream`
- **THEN** CLI waits for the complete response
- **AND** prints the entire response at once
