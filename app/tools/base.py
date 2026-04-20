"""工具抽象基类定义。"""

from abc import ABC, abstractmethod


class BaseTool(ABC):
    """工具抽象基类。

    所有可调用工具必须实现此接口。
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """工具名称。

        Returns:
            工具的唯一标识名称。
        """
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """工具描述。

        Returns:
            工具功能的可读描述。
        """
        pass

    @abstractmethod
    def invoke(self, input: str) -> str:
        """调用工具执行操作。

        Args:
            input: 工具输入参数（字符串）。

        Returns:
            工具执行结果的字符串表示。

        Raises:
            ValueError: 如果输入参数无效。
            RuntimeError: 如果工具执行失败。
        """
        pass
