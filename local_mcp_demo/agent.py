import asyncio
import os
from google.adk.agents.llm_agent import Agent
from google.adk.runners import Runner
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from mcp.client.stdio import StdioServerParameters


github_token = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")

connection_params = StdioConnectionParams(
    server_params=StdioServerParameters(
        command="docker",
        args=[
            "run",
            "-i",
            "--rm",
            "-e",
            f"GITHUB_PERSONAL_ACCESS_TOKEN={github_token}",
            "ghcr.io/github/github-mcp-server",
        ],
    )
)

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    instruction=(
        "You are an expert GitHub assistant. You have access to tools that allow you to search repositories, read code, and manage issues. Always verify repository names before performing write actions."
    ),
    tools=[McpToolset(connection_params=connection_params)],
)
