# Tasks: 修复 Tool-Calling Code Review 问题

## 1. 线程安全修复

- [x] 1.1 在 `app/tools/registry.py` 添加 `import threading`
- [x] 1.2 添加类级别的 `_lock = threading.Lock()`
- [x] 1.3 修改 `get_instance()` 实现 double-check locking
- [x] 1.4 为 `register()` 添加 `with self._lock` 保护
- [x] 1.5 实现 `unregister(name: str) -> bool` 方法（线程安全）
- [x] 1.6 明确并实现 `get()` / `list()` 的并发读一致性（`list()` 返回锁内快照）
- [x] 1.7 添加并发场景测试，验证不会因同时注册/注销而出现竞态或读取异常

## 2. LangChain Adapter 修复

- [x] 2.1 在 `app/tools/adapter.py` 移除 `args_schema=DefaultArgsSchema` 参数
- [x] 2.2 移除 `DefaultArgsSchema` 类（如果不再需要）
- [x] 2.3 验证工具仍能正常工作
- [x] 2.4 更新或补充测试，明确 LangChain tool 的调用入参约定

## 3. AST 验证补全

- [x] 3.1 在 `app/agent/tools.py` 的 `_safe_eval` 中，对 `ast.Call.args` 和 `ast.keyword.value` 递归验证
- [x] 3.2 测试验证恶意 keyword 无法绕过
- [x] 3.3 测试验证恶意位置参数和嵌套调用无法绕过

## 4. UTC 时间格式化

- [x] 4.1 简化 `DateTimeTool.invoke` 中的 UTC 时间格式化
- [x] 4.2 测试验证 ISO 8601 格式仍正确

## 5. 测试优化

- [x] 5.1 在 `tests/test_tools.py` 中使用 `unregister()` 清理测试数据
- [x] 5.2 移除直接修改 `_tools` 的代码
- [x] 5.3 使用 fixture 或统一清理逻辑，降低单例状态在测试之间泄漏的风险

## 6. 验证

- [x] 6.1 运行 `pytest tests/test_tools.py -v` 确保所有测试通过
- [x] 6.2 运行 `pytest tests/ -v` 确保无回归
- [x] 6.3 使用 `ruff check app/tools/` 检查代码风格
- [x] 6.4 使用 `black --check app/tools/` 检查格式
- [x] 6.5 验证 `DateTimeTool` 输出格式是否仍满足预期精度与 ISO 8601 约束
