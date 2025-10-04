"""
LinkedIn Post Generator Agent

This agent generates the initial LinkedIn post before refinement.

"""

import os
from pathlib import Path

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool import McpToolset, StdioConnectionParams
from mcp.client.stdio import StdioServerParameters

# Ensure LiteLLM caches use UTF-8 on Windows hosts.

os.environ.setdefault("PYTHONUTF8", "1")

OPENAI_MODEL = "openai/gpt-3.5-turbo"
GEMINI_MODEL = "gemini-2.0-flash"

model = LiteLlm(
    model=OPENAI_MODEL,
    api_key=os.environ.get("OPENAI_API_KEY"),
)

PROJECT_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_HINT_DIR = PROJECT_ROOT / "post_hints"

# hint_dir_env = os.environ.get("POST_HINT_DIR")

# if hint_dir_env:
#     hint_dir_candidate = Path(hint_dir_env).expanduser()
#     if hint_dir_candidate.is_absolute():
#         POST_HINT_DIR = hint_dir_candidate
#     else:
#         POST_HINT_DIR = PROJECT_ROOT / hint_dir_candidate
# else:
POST_HINT_DIR = DEFAULT_HINT_DIR

POST_HINT_DIR = POST_HINT_DIR.resolve(strict=False)
POST_HINT_DIR.mkdir(parents=True, exist_ok=True)

POST_HINT_FILE = (POST_HINT_DIR / "Post.txt").resolve(strict=False)

filesystem_tool = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="npx",
            args=[
                "-y",
                "@modelcontextprotocol/server-filesystem",
                str(POST_HINT_DIR),
            ],
        ),
    ),
)

initial_post_generator = LlmAgent(
    name="InitialPostGenerator",
    description="Generates the intial LinkedIn post to start the refinement process",
    model=GEMINI_MODEL,
    instruction=f"""
    You are a LinkedIn Post Generator.

    Your task is to create a LinkedIn post about an Agent Development Kit (ADK) tutorial.

    # Post Hint by User
    The hint file lives at: {POST_HINT_FILE}
    Always use the absolute path shown above when listing or reading files with the filesystem tool.
    You can list files, read files, and otherwise interact only through the filesystem_tool MCP server.

    ## CONTENT REQUIREMENTS
    Ensure the post includes:
    1. Excitement about learning from the tutorial
    2. Specific aspects of ADK learned:
       - Basic agent implementation (basic-agent)
       - Tool integration (tool-agent)
       - Using LiteLLM (litellm-agent)
       - Managing sessions and memory
       - Persistent storage and memory
       - Multi-agent orchestration
       - Stateful multi-agent systems
       - Callback systems
       - Sequential multi-agent systems
       - Parallel agents for concurrent operations
       - Loop Agents for iterative refinement
    3. Brief statement about improving AI applications
    4. Mention/tag of kg
    5. Clear call-to action for connections

    ## STYLE REQUIREMENTS
    - Professional and conversational tone
    - Between 1000-1500 characters
    - NO emojis
    - NO hashtags
    - Show genuine enthusiasm
    - Highlight practical applications

    ## OUTPUT INSTRUCTIONS
    - Return ONLY the post content
    - Do not add formatting markers or explanations
    """,
    ## Additional context about the user. Incorporate these in the post:
    # Name:
    # {user_name}
    # Preferences:
    # {user_preference}

    output_key="current_post",
    tools=[filesystem_tool],
)

