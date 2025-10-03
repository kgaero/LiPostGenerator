import asyncio
import uuid

from dotenv import load_dotenv
from google.adk.runners import InMemoryRunner
from google.genai import types

from Linkedin_post_agent.agent import root_agent

load_dotenv()

initial_state = {
    "user_name": "kg",
    "user_preference": """
     Looking at Google ADK, OpenAI has also Agentic AI framework called Swarm which I am also interested in.
    """,
}

APP_NAME = "kg Bot"
USER_ID = "kg1"
SESSION_ID = str(uuid.uuid4())


async def main() -> None:
    runner = InMemoryRunner(agent=root_agent, app_name=APP_NAME)
    session_service = runner.session_service

    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=initial_state,
    )

    print("Created new session:")
    print(f"\t Session ID: {SESSION_ID}")

    new_message = types.Content(
        role="user",
        parts=[
            types.Part(
                text=(
                    "Provide a post on similarility of google adk with Microsoft Agent framework."
                )
            )
        ],
    )

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=new_message,
    ):
        if event.is_final_response() and event.content and event.content.parts:
            print(f"Final response: {event.content.parts[0].text}")

    print("======Session Event Exploration =====")
    session = await session_service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    print("==== Final Session state =======")
    for key, value in session.state.items():
        print(f"{key}:{value}")


if __name__ == "__main__":
    asyncio.run(main())
