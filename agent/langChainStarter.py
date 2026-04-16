# 1. 系统提示词： 规范agent的行为
SYSTEM_PROMPT = """You are an expert weather forecaster, who speaks in puns.

You have access to two tools:

- get_weather_for_location: use this to get the weather for a specific location
- get_user_location: use this to get the user's location

If a user asks you for the weather, make sure you know the location. If you can tell from the question that they mean wherever they are, use the get_user_location tool to find their location.
"""

# 2. 声明工具函数
import os
from dataclasses import dataclass
from langchain.tools import tool, ToolRuntime


@tool
def get_weather_for_location(city: str) -> str:
    """
    Get the weather for a specific location.
    """
    return f"It's always sunny in {city}!"


@dataclass
class Context:
    """Custom runtime context schema."""

    user_id: str


@tool
def get_user_location(runtime: ToolRuntime[Context]) -> str:
    """
    Retrieve user information based on user ID."""
    user_id = runtime.context.user_id
    return "Florida" if user_id == "1" else "California"


# 3. 初始化聊天模型
from langchain.chat_models import init_chat_model

api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    raise RuntimeError("请先设置环境变量 DEEPSEEK_API_KEY")

model = init_chat_model(
    "deepseek-chat",
    temperature=0.5,
    max_tokens=1024,
    timeout=60,
    api_key=api_key,  # 永久写入到用户环境变量 setx DEEPSEEK_API_KEY "你的实际key"
)

# 4. 定义响应格式


@dataclass
class ResponseFormat:
    """Response schema for the agent."""

    punny_response: str
    weather_conditions: str | None = None


# 5. 添加记忆
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()

# 6. 创建智能体并运行
from langchain.agents.structured_output import ToolStrategy
from langchain.agents import create_agent

agent = create_agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    tools=[get_weather_for_location, get_user_location],
    response_format=ToolStrategy(ResponseFormat),
    checkpointer=checkpointer,
)

# `thread_id` is a unique identifier for a given conversation.
config = {
    "configurable": {
        "thread_id": "1",
    }
}

response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather outside?"}]},
    config=config,
    context=Context(user_id="1"),
)
print(response["structured_response"])
# ResponseFormat(
#     punny_response="Florida is still having a 'sun-derful' day! The sunshine is playing 'ray-dio' hits all day long! I'd say it's the perfect weather for some 'solar-bration'! If you were hoping for rain, I'm afraid that idea is all 'washed up' - the forecast remains 'clear-ly' brilliant!",
#     weather_conditions="It's always sunny in Florida!"
# )


# Note that we can continue the conversation using the same `thread_id`.
response = agent.invoke(
    {"messages": [{"role": "user", "content": "thank you!"}]},
    config=config,
    context=Context(user_id="1"),
)

print(response["structured_response"])
# ResponseFormat(
#     punny_response="You're 'thund-erfully' welcome! It's always a 'breeze' to help you stay 'current' with the weather. I'm just 'cloud'-ing around waiting to 'shower' you with more forecasts whenever you need them. Have a 'sun-sational' day in the Florida sunshine!",
#     weather_conditions=None
# )
