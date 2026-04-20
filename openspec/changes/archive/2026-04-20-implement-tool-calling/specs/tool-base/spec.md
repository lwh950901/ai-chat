## ADDED Requirements

### Requirement: BaseTool Abstract Contract

系统 SHALL 提供统一的 `BaseTool` 抽象接口，作为所有可调用工具的基础契约。

#### Scenario: Tool metadata contract
- **WHEN** 任意工具实现 `BaseTool`
- **THEN** 该工具 SHALL 暴露稳定的 `name` 属性
- **AND** 该工具 SHALL 暴露可读的 `description` 属性

#### Scenario: Tool invocation contract
- **WHEN** 调用 `tool.invoke(input)`
- **THEN** 工具 SHALL 接收字符串输入
- **AND** 工具 SHALL 返回字符串结果

#### Scenario: Tool implementation enforcement
- **WHEN** 开发者创建新的工具类
- **THEN** 未实现 `name`、`description` 或 `invoke` 的工具 SHALL 不能被当作完整工具使用

#### Scenario: Reusable tool abstraction
- **WHEN** Agent 或未来其他 LLM 客户端接入工具系统
- **THEN** 它们 SHALL 依赖 `BaseTool` 抽象而不是某个具体工具类实现

#### Scenario: Tool error semantics
- **WHEN** 工具收到无效输入或执行失败
- **THEN** 工具 SHALL 返回明确错误信息或抛出受控异常
- **AND** 调用方 SHALL 能够区分正常结果与失败情况