## 1. Base LLM Client Module

- [x] 1.1 创建 `src/ai_chat/clients/__init__.py` - 客户端模块初始化
- [x] 1.2 创建 `src/ai_chat/clients/base.py` - 定义 BaseLLMClient 抽象类和异常类

## 2. OpenAI Client

- [x] 2.1 创建 `src/ai_chat/clients/openai_client.py` - OpenAIClient 实现
- [x] 2.2 实现 `send_message()` 方法
- [x] 2.3 实现 `stream_message()` 方法

## 3. Anthropic Client

- [x] 3.1 创建 `src/ai_chat/clients/anthropic_client.py` - AnthropicClient 实现
- [x] 3.2 实现 `send_message()` 方法
- [x] 3.3 实现 `stream_message()` 方法

## 4. Client Factory

- [x] 4.1 创建 `src/ai_chat/clients/factory.py` - 客户端工厂函数

## 5. Verification

- [x] 5.1 验证 OpenAIClient 可正常实例化
- [x] 5.2 验证 AnthropicClient 可正常实例化
- [x] 5.3 验证客户端可从 Settings 读取配置
