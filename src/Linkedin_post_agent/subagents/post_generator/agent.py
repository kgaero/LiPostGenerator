"""
LinkedIn Post Generator Agent

This agent generates the initial LinkedIn post before refinement.

"""


from google.adk.agents import LlmAgent

GEMINI_MODEL = "gemini-2.0-flash"

initial_post_generator = LlmAgent(
    name = "InitialPostGenerator",
    description= "Generates the intial LinkedIn post to start the refinement process",
    model = GEMINI_MODEL,
    instruction = """
    You are a LinkedIn Post Generator.

    Your task in to create a LinkedIn post about an Agent Development Kit(ADK) tutorial

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

    ## STYLE REUIQRMENTS
    - Professional and conversational tone
    - Between 1000-1500 characters
    - NO emojis
    - NO hashtags
    - Show genuine enthusiasm
    - Highlight practical applications

    ## OUTPUT INSTRUCTIONS
    - Return ONLY the post content
    - Do not add formatting markers or explanations

    ## Additional context about the user. Incorporate these in the post:
    Name:
    {user_name}
    Preferences:
    {user_preference}
    """,
    output_key= 'current_post',
)