# Proposal: 修复 Tool-Calling Code Review 问题

## Why
implement-tool-calling 实现后，通过 code review 发现多个 Critical 和 Important 问题需要修复，确保生产环境稳定性。

## What Changes

### 需要修复的问题

**Critical:**
1. `ToolRegistry` 单例线程安全问题 — `get_instance()` 和 `register()` 缺少锁保护
2. LangChain Adapter `args_schema` 与 `func` 参数不兼容
3. `_safe_eval` 对函数调用参数递归验证不完整 — 不仅 `ast.keyword`，`ast.Call.args` 也可能绕过校验

**Important:**
4. `ToolRegistry.list()` 在并发注册/注销时缺少一致性约束
5. 测试直接修改 `registry._tools` 绕过保护
6. 缺少 `unregister()` 方法

**Minor:**
7. 错误消息格式不一致
8. UTC offset 硬编码

## Capabilities

### 1. 线程安全修复
- 为 `ToolRegistry` 添加 `threading.Lock`
- 实现 double-check locking 模式
- 为 `register()` 添加锁保护
- 明确 `get()` / `list()` 在并发写入期间的读一致性策略

### 2. LangChain Adapter 修复
- 验证 `StructuredTool` 参数组合
- 修复 `args_schema` 与 `func` 兼容性问题

### 3. AST 验证补全
- 对 `ast.Call.args` 和 `ast.keyword.value` 进行递归验证
- 增加恶意嵌套调用的回归测试，防止再次绕过

### 4. 添加 unregister 方法
- 实现线程安全的工具注销方法
- 测试使用 `unregister()` 替代直接修改 `_tools`

### 5. 其他优化
- 统一错误消息格式
- 简化 UTC 时间格式化

## Impact
- 提升多线程环境下的稳定性
- 修复 LangChain 工具调用兼容性
- 改善测试可维护性
