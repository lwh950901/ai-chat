"""LangChain 工具适配器。"""

from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

from .base import BaseTool


class DefaultArgsSchema(BaseModel):
    """默认参数 schema。"""

    input: str = Field(description="工具输入参数")


def create_langchain_tool(tool: BaseTool) -> StructuredTool:
    """将 BaseTool 转换为 LangChain StructuredTool。

    Args:
        tool: BaseTool 实现实例。

    Returns:
        LangChain StructuredTool 实例。
    """

    async def wrapper(input: str) -> str:
        try:
            return tool.invoke(input)
        except Exception as e:
            return f"工具执行错误: {str(e)}"

    return StructuredTool(
        name=tool.name,
        description=tool.description,
        args_schema=DefaultArgsSchema,
        coroutine=wrapper,
    )


def create_langchain_tools(tools: list[BaseTool]) -> list[StructuredTool]:
    """批量将 BaseTool 列表转换为 LangChain StructuredTool 列表。

    Args:
        tools: BaseTool 实例列表。

    Returns:
        StructuredTool 列表。
    """
    return [create_langchain_tool(tool) for tool in tools]
