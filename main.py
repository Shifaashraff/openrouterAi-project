from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

if not openrouter_api_key:
    raise ValueError("OPENROUTER_API_KEY is not set. Please define")

external_client = AsyncOpenAI(
    api_key= openrouter_api_key,
    base_url="https://openrouter.ai/api/v1"
)

model = OpenAIChatCompletionsModel(
    model="mistralai/mistral-small-3.2-24b-instruct-2506:free",
    openai_client= external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent = Agent(
    name="writer Agent",
    instructions="you are a writer. generate stories and poem."
) 

response = Runner.run_sync(
    agent,
    input= "write a short essay story on fairytail",
    run_config = config
)

print(response)

