## ToolRegistry 注册表

### Requirement: 单例访问

`ToolRegistry` 通过单例模式访问全局注册表。

#### Scenario: 获取注册表实例

- **WHEN** 调用 `ToolRegistry.get_instance()`
- **THEN** 返回 `ToolRegistry` 单例实例
- **AND** 多次调用返回同一实例

### Requirement: 注册工具

#### Scenario: 注册新工具

- **WHEN** 调用 `registry.register(CalculatorTool())`
- **THEN** 工具被添加到注册表
- **AND** `registry.list()` 包含该工具

#### Scenario: 注册同名工具

- **WHEN** 注册一个已存在名称的工具
- **THEN** 抛出 `ValueError` 异常

### Requirement: 获取工具

#### Scenario: 获取已注册工具

- **WHEN** 调用 `registry.get("calculator")`
- **THEN** 返回 `CalculatorTool` 实例
- **AND** `registry.get("nonexistent")` 返回 `None`

### Requirement: 列举工具

#### Scenario: 列举所有工具

- **WHEN** 调用 `registry.list()`
- **THEN** 返回所有已注册工具的列表
- **AND** 列表按注册顺序排列

---

## 默认工具集

### Requirement: CalculatorTool

`CalculatorTool` 提供安全数学计算功能，实现 `BaseTool` 接口。

#### Scenario: 基本算术

- **WHEN** 调用 `CalculatorTool().invoke("2 + 3")`
- **THEN** 返回 `"5"`

#### Scenario: 复杂表达式

- **WHEN** 调用 `CalculatorTool().invoke("sin(pi/2)")`
- **THEN** 返回接近 `"1.0"` 的结果

#### Scenario: 无效表达式

- **WHEN** 调用 `CalculatorTool().invoke("os.system('ls')")`
- **THEN** 返回包含 `"错误"` 或 `"不允许"` 的信息

### Requirement: DateTimeTool

`DateTimeTool` 提供当前时间查询功能，实现 `BaseTool` 接口。

#### Scenario: 获取当前时间

- **WHEN** 调用 `DateTimeTool().invoke("")`
- **THEN** 返回 ISO 8601 格式的 UTC 时间字符串
- **AND** 包含 "Z" 后缀表示 UTC

### Requirement: 获取默认工具

#### Scenario: 创建默认工具集

- **WHEN** 调用 `ToolRegistry.get_default_tools()`
- **THEN** 返回包含 `CalculatorTool` 和 `DateTimeTool` 的列表
- **AND** 列表长度为 2
