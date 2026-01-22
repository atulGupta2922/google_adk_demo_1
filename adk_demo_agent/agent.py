from google.adk.agents.llm_agent import Agent

def greeting_tool() -> str:
    return "Hello from the greeting tool!"

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge. Whenever the user greets you, you MUST use the greeting_tool to respond.',
    tools=[greeting_tool]
)
