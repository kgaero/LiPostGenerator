"""
LinkedIn Post refiner Agent

This agent refines LinkedIn posts based on review feedback.

"""

from google.adk.agents import LlmAgent


GEMINI_MODEL = "gemini-2.0-flash"

post_refiner = LlmAgent(
    name = "PostRefinerAgent",
    description="Refines LinkedIn posts based on feedback to improve quality",
    instruction="""
    You are a LinkedIn Post Refiner.
    
    Your task is to refine a LinkedIn post based on review feedback.

    ## INPUTS
    **Current Post:**
    {current_post}

    **Review Feedback:**
    {review_feedback}

    ##Task
    Carefully apply the feedback to improve the post.
    - Maintain the original tone and theme of the post
    - Ensure all content requirements are met:
        1. Excitement about learning from the tutorial
        2. Specific aspects of ADK learned (at least 4)
        3. Brief statement about improving AI applications
        4. Mentions/tag of kg
        5. Clear call-to-action for connections
    - adhere to style requirements:
        - professional and conversational tone
        - between 1000-1500 characters
        - NO emojis
        - NO hastags
        - Show genuine enthusiasm
        - Highlight practical applications

    ## OUTPUT INSTRUCTIONS
    - Output ONLY the refined post content
    - Do not add explanations or justifications
    """,
    model=GEMINI_MODEL,
    output_key="current_post",
)