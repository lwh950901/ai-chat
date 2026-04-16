"""LLM 客户端工厂函数。"""

from typing import Literal

from .anthropic_client import AnthropicClient
from .base import BaseLLMClient, ConfigurationError
from .openai_client import OpenAIClient


def create_llm_client(
    provider: Literal["openai", "anthropic"],
    api_key: str,
    model: str | None = None,
    **kwargs,
) -> BaseLLMClient:
    """创建指定提供商的 LLM 客户端。

    Args:
        provider: LLM 提供商名称（"openai" 或 "anthropic"）。
        api_key: 提供商的 API 密钥。
        model: 可选的模型覆盖。
        **kwargs: 提供商特定的其他参数。

    Returns:
        对应 LLM 客户端的实例。

    Raises:
        ValueError: 不支持的提供商。
        ConfigurationError: 缺少必要配置。
    """
    if provider == "openai":
        return OpenAIClient(api_key=api_key, model=model or "gpt-4", **kwargs)
    elif provider == "anthropic":
        return AnthropicClient(api_key=api_key, model=model or "claude-3-sonnet-20240229", **kwargs)
    else:
        raise ValueError(f"Unsupported provider: {provider}. Use 'openai' or 'anthropic'.")


def create_openai_client(api_key: str, model: str = "gpt-4", **kwargs) -> OpenAIClient:
    """创建 OpenAI 客户端。

    Args:
        api_key: OpenAI API 密钥。
        model: 模型标识符。
        **kwargs: 其他参数。

    Returns:
        OpenAIClient 实例。
    """
    return OpenAIClient(api_key=api_key, model=model, **kwargs)


def create_anthropic_client(api_key: str, model: str = "claude-3-sonnet-20240229", **kwargs) -> AnthropicClient:
    """创建 Anthropic 客户端。

    Args:
        api_key: Anthropic API 密钥。
        model: 模型标识符。
        **kwargs: 其他参数。

    Returns:
        AnthropicClient 实例。
    """
    return AnthropicClient(api_key=api_key, model=model, **kwargs)
