from google.adk.agents.llm_agent import Agent
from pydantic import BaseModel, Field


# Defining input schema
class GreetingsInputSchema(BaseModel):
    language: str = Field(description="The language to greet user in.")


# Defining input schema
class GreetingsOutputSchema(BaseModel):
    greeting_message: str = Field(description="the final, formatted greeting message.")
    query_resolution: bool = Field(
        description="True if the user query is resolved and False if not."
    )


root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="A helpful assistant for user questions.",
    instruction="Answer user questions to the best of your knowledge",
    # passing input and output schemas
    input_schema=GreetingsInputSchema,
    output_schema=GreetingsOutputSchema,
    output_key="final_greeting",
)
