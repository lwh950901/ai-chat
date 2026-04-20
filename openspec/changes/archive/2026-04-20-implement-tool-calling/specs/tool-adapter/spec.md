## LangChain 适配器

### Requirement: 适配器函数

`create_langchain_tool()` 将 `BaseTool` 转换为 LangChain `StructuredTool`。

#### Scenario: 转换 CalculatorTool

- **WHEN** 调用 `create_langchain_tool(CalculatorTool())`
- **THEN** 返回 LangChain `StructuredTool` 实例
- **AND** 返回的工具 `name` 属性为 `"calculator"`
- **AND** 返回的工具 `description` 属性与原工具一致

#### Scenario: 转换 DateTimeTool

- **WHEN** 调用 `create_langchain_tool(DateTimeTool())`
- **THEN** 返回 LangChain `StructuredTool` 实例
- **AND** 返回的工具 `name` 属性为 `"datetime"`

### Requirement: 参数模式

适配器处理 `BaseTool` 到 LangChain schema 的转换。

#### Scenario: 参数 schema 转换

- **WHEN** `BaseTool` 有 `input_schema` 属性（dict）
- **THEN** `create_langchain_tool()` 将其映射到 LangChain 的 `args_schema`
- **AND** 生成的 LangChain 工具可被 LangChain Agent 正确调用

### Requirement: 批量转换

#### Scenario: 转换工具列表

- **WHEN** 调用 `create_langchain_tools([CalculatorTool(), DateTimeTool()])`
- **THEN** 返回对应数量的 LangChain `StructuredTool` 列表
- **AND** 每个工具独立转换

### Requirement: 与现有 Agent 兼容

#### Scenario: Agent 工厂使用适配器

- **WHEN** `create_agent_with_settings()` 被调用
- **THEN** 内部使用 `create_langchain_tools()` 转换 `ToolRegistry` 中的工具
- **AND** 生成的 Agent 行为与重构前一致
