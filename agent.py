# agent.py
import asyncio
import os
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.models.openai._model_info import ModelInfo
from tools import getvideotranscript, get_transcript_with_timestamps

load_dotenv()
OPENROUTER_API_KEY = os.getenv("open_router")
if not OPENROUTER_API_KEY:
    raise RuntimeError("OPENROUTER_API_KEY is missing in .env file")

# Initialize the model client
from autogen_ext.models.openai._model_info import ModelInfo

from autogen_ext.models.openai._model_info import ModelInfo
from autogen_core.models import ModelFamily

from autogen_ext.models.openai._model_info import ModelInfo

model_client = OpenAIChatCompletionClient(
    model="openai/gpt-oss-20b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
    model_info=ModelInfo(
        max_tokens=4096,
        input_variables=["messages"],
        output_parser=None,
        vision=False,                # required
        function_calling=None,       # required
        json_output=None,            # required
        allowed_tools=None,          # required
        family="openai",             # pass as string instead of Enum
        include_name_in_message=False # optional
    )
)

async def AskAgent(url: str, query_text: str):
    """
    Runs the AssistantAgent to answer questions or summarize a YouTube video.
    """
    system_prompt = """
You are a highly intelligent assistant specialized in YouTube videos.
Read video transcripts and provide clear, concise summaries.
Answer questions strictly based on the transcript.
If the answer is not found, respond with "I don't know".
If no transcript is available, clearly state that the video does not provide captions
and that automatic transcription is required.
Do not hallucinate content.
"""

    agent = AssistantAgent(
        name="youtube_proxy_agent",
        model_client=model_client,
        tools=[getvideotranscript, get_transcript_with_timestamps],
        system_message=system_prompt.strip(),
    )

    task_text = f"This is the video URL:\n{url}\n\nUser question:\n{query_text}"

    messages = []

    try:
        async for msg in agent.on_messages_stream(
            messages=[TextMessage(content=task_text, source="user")],
            cancellation_token=CancellationToken(),
        ):
            if hasattr(msg, "content") and msg.content:
                # Ensure it's a string
                if isinstance(msg.content, list):
                    # flatten list to string
                    messages.append(" ".join(str(c) for c in msg.content))
                else:
                    messages.append(str(msg.content))
    except Exception as e:
        messages.append(f"Error: {e}")

    return "\n".join(messages)
