from google.adk.agents.llm_agent import Agent
from google.genai import types

def greeting_tool() -> str:
    return "Hello from the greeting tool!"

def ask_name() -> str:
    return "May I know your GOOD name, please."

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge. Whenever the user greets you, you MUST use the greeting_tool to respond. Whenever someone asks about wheather, you MUST use ask_name tool to respond.',
    tools=[greeting_tool, ask_name],
    # Controlling response generation using generate_content_config
    generate_content_config=types.GenerateContentConfig(
        temperature=0.5,
        max_output_tokens=100,
        safety_settings=[
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
            )
        ]
    )
)
