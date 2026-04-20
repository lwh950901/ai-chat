"""Agent 内置工具集。"""

import math
import ast
from datetime import datetime, timezone

from ..tools.base import BaseTool

# 允许的数学函数
ALLOWED_MATH_NAMES = {"sin", "cos", "tan", "sqrt", "log", "abs", "pow", "pi", "e"}


def _safe_eval(expr: str) -> float:
    """安全地计算数学表达式。

    Args:
        expr: 数学表达式字符串。

    Returns:
        计算结果。

    Raises:
        ValueError: 如果表达式包含不允许的内容。
    """
    # 用 AST 解析表达式，确保安全
    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError as e:
        raise ValueError(f"无效的表达式: {e}")

    # tree.body 是表达式的根节点
    node = tree.body

    # 检查节点类型
    def check_node(n):
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return True
        elif isinstance(n, ast.Name):
            if n.id not in ALLOWED_MATH_NAMES:
                raise ValueError(f"不允许的变量: {n.id}")
            return True
        elif isinstance(n, ast.BinOp):
            return check_node(n.left) and check_node(n.right)
        elif isinstance(n, ast.UnaryOp):
            return check_node(n.operand)
        elif isinstance(n, ast.Call):
            if not isinstance(n.func, ast.Name) or n.func.id not in ALLOWED_MATH_NAMES:
                raise ValueError(f"不允许的函数: {ast.dump(n.func)}")
            # 递归验证所有参数
            return all(check_node(arg) for arg in n.args) and all(
                check_node(kw) for kw in n.keywords
            )
        elif isinstance(n, ast.keyword):
            return check_node(n.value)  # 递归验证 keyword value
        return False

    if not check_node(node):
        raise ValueError(f"不支持的表达式类型: {type(node).__name__}")

    # 构建安全的命名空间
    safe_dict = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "sqrt": math.sqrt,
        "log": math.log,
        "abs": abs,
        "pow": pow,
        "pi": math.pi,
        "e": math.e,
    }

    return eval(expr, {"__builtins__": {}}, safe_dict)


class CalculatorTool(BaseTool):
    """计算器工具 - 安全数学计算，实现 BaseTool 接口。"""

    name = "calculator"
    description = "计算数学表达式。支持加减乘除、指数、三角函数等。输入有效的 Python 数学表达式。"

    def invoke(self, expression: str) -> str:
        """执行数学计算。

        Args:
            expression: 数学表达式字符串。

        Returns:
            计算结果字符串。
        """
        try:
            result = _safe_eval(expression.strip())
            return str(result)
        except Exception as e:
            return f"计算错误: {str(e)}"


class DateTimeTool(BaseTool):
    """日期时间工具 - 获取当前时间，实现 BaseTool 接口。"""

    name = "datetime"
    description = "获取当前日期和时间。返回 UTC 时区的 ISO 8601 格式日期时间。"

    def invoke(self, input: str) -> str:
        """获取当前 UTC 日期时间。

        Args:
            input: 未使用，传入空字符串即可。

        Returns:
            ISO 8601 格式的日期时间字符串。
        """
        return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def get_default_tools() -> list[BaseTool]:
    """获取默认工具列表。

    Returns:
        包含计算器和日期时间工具的列表。
    """
    return [CalculatorTool(), DateTimeTool()]
