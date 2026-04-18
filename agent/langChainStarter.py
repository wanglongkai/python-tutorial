# 1. 系统提示词： 规范agent的行为
SYSTEM_PROMPT = """你是一个专家天气预报员,你总是使用幽默的方式回答用户的问题."""

# 2. 声明工具函数
import os
from dataclasses import dataclass
from langchain.tools import tool, ToolRuntime


@tool
def get_weather_for_location(city: str) -> str:
    """
    获取特定位置的天气
    """
    return f"总是天气晴朗,温度适宜,适合出行 {city}!"


@dataclass
class Context:
    """自定义运行时上下文"""

    user_id: str


@tool
def get_user_location(runtime: ToolRuntime[Context]) -> str:
    """
    根据用户ID获取用户位置
    """
    user_id = runtime.context.user_id
    return "南京" if user_id == "1" else "上海"


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
    """Agent的响应格式"""

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

# `thread_id` 一个唯一标识符,用于标识一个对话。
config = {
    "configurable": {
        "thread_id": "1",
    }
}

response = agent.invoke(
    {"messages": [{"role": "user", "content": "今天天气怎么样?"}]},
    config=config,
    context=Context(user_id="1"),
)
print(response["structured_response"])


# 继续对话时，使用相同的thread_id
response = agent.invoke(
    {"messages": [{"role": "user", "content": "谢谢你!"}]},
    config=config,
    context=Context(user_id="1"),
)

print(response["structured_response"])
