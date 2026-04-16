## Context

AI Chat 项目需要集成 OpenAI GPT 和 Anthropic Claude 两个 LLM 提供商。目前已有配置管理模块（Settings），需要在此基础上构建 LLM 客户端封装。

## Goals / Non-Goals

**Goals:**
- 提供统一的 LLM 客户端接口
- 实现 OpenAI 和 Anthropic 两个具体客户端
- 支持流式响应
- 错误处理完善

**Non-Goals:**
- 不实现 LangChain Agent 或 Chains（由 langchain-integration spec 覆盖）
- 不实现对话历史管理（后续 conversation-management change 处理）

## Decisions

### Decision 1: 统一客户端接口 + 工厂模式

定义 `BaseLLMClient` 抽象基类，提供统一接口。具体客户端继承实现。

```python
class BaseLLMClient(ABC):
    @abstractmethod
    def send_message(self, message: str, **kwargs) -> str:
        pass

    @abstractmethod
    def stream_message(self, message: str, **kwargs) -> Iterator[str]:
        pass
```

**Why:** 统一接口便于切换不同 LLM 提供商，也便于扩展新提供商。

### Decision 2: 使用原生 SDK 而非 LangChain

直接使用 `openai` 和 `anthropic` SDK，不通过 LangChain 封装。

**Why:** 
- 更直接，控制力更强
- LangChain 已在依赖中但作为可选集成
- 降低复杂度

### Decision 3: 异常处理设计

定义 `LLMError` 基类和 `ConfigurationError` 子类。

```python
class LLMError(Exception):
    """Base exception for LLM client errors"""
    pass

class ConfigurationError(LLMError):
    """Configuration related errors"""
    pass
```

**Why:** 便于调用方区分配置错误和其他运行时错误。

### Decision 4: 流式响应采用 Iterator 模式

```python
def stream_message(self, message: str, **kwargs) -> Iterator[str]:
    # yield chunks as they arrive
```

**Why:** Python 原生协程模式，内存效率高，使用方可通过 `for chunk in stream_message()` 直接消费。
