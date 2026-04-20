"""工具注册表实现。"""

from __future__ import annotations

import threading
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .base import BaseTool


class ToolRegistry:
    """工具注册表（单例模式，线程安全）。

    提供全局工具注册、获取、列举功能。
    """

    _instance: "ToolRegistry | None" = None
    _lock = threading.Lock()

    def __init__(self):
        """初始化注册表（私有化以支持单例）。"""
        self._tools: dict[str, "BaseTool"] = {}

    @classmethod
    def get_instance(cls) -> "ToolRegistry":
        """获取注册表单例实例（线程安全）。

        Returns:
            ToolRegistry 单例。
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # double-check locking
                    cls._instance = cls()
        return cls._instance

    def register(self, tool: "BaseTool") -> None:
        """注册工具到注册表（线程安全）。

        Args:
            tool: BaseTool 实现实例。

        Raises:
            ValueError: 如果工具名称已存在。
        """
        with self._lock:
            if tool.name in self._tools:
                raise ValueError(f"工具 '{tool.name}' 已注册")
            self._tools[tool.name] = tool

    def get(self, name: str) -> "BaseTool | None":
        """获取指定名称的工具（线程安全）。

        Args:
            name: 工具名称。

        Returns:
            工具实例，不存在则返回 None。
        """
        with self._lock:
            return self._tools.get(name)

    def list(self) -> list["BaseTool"]:
        """列举所有已注册的工具（线程安全，返回快照）。

        Returns:
            工具列表，按注册顺序排列。
        """
        with self._lock:
            return list(self._tools.values())

    def unregister(self, name: str) -> bool:
        """注销工具（线程安全）。

        Args:
            name: 工具名称。

        Returns:
            True 如果工具已存在并被移除，False 如果工具不存在。
        """
        with self._lock:
            if name in self._tools:
                del self._tools[name]
                return True
            return False

    @staticmethod
    def get_default_tools() -> list["BaseTool"]:
        """获取默认工具列表。

        Returns:
            包含所有默认工具的列表。
        """
        from ..agent.tools import CalculatorTool, DateTimeTool

        return [CalculatorTool(), DateTimeTool()]
