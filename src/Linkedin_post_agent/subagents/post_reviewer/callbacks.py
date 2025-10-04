from google.genai import types
from typing import Any, Dict, Optional
from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_request import LlmRequest
from google.adk.models.llm_response import LlmResponse
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext


def before_tool_callback(tool: BaseTool, args: Dict[str, Any], tool_context: ToolContext
) -> Optional[Dict]:
    """
    Simple callback that print the tool called
    """

    print(f"[before_tool_callback] Tool's Agent name : {tool_context.agent_name}")
    print(f"[before_tool_callback] Tool's state: {tool_context.state}")
    tool_name = tool.name
    print(f"[before_tool_callback] Before tool call for {tool_name}")
    # print(f"[before_tool_callback] Original args: {args}")


def after_tool_callback(
    tool: BaseTool,
    args: Dict[str, Any],
    tool_context: ToolContext,
    tool_response: Dict,
) -> Optional[Dict]:
    """
    Simple callback that print the tool called
    """
    print(f"[after_tool_callback] Tool's Agent name : {tool_context.agent_name}")
    print(f"[after_tool_callback] Tool's state: {tool_context.state}")
    tool_name = tool.name
    print(f"[after_tool_callback] After tool call for {tool_name}")
    print(f"[after_tool_callback] Original args: {args}")
    # print(f"[after_tool_callback] Tool response: {tool_response}")


def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    """
    Simple callback that print the tool called
    """
    print(f"[before_model_callback] Model's Agent name : {callback_context.agent_name}")
    print(f"[before_model_callback] Model's state: {callback_context.state}")
    print(f"[before_model_callback] Before model call for {llm_request}")

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    """
    Simple callback that print the tool called
    """
    print(f"[after_model_callback] Model's Agent name : {callback_context.agent_name}")
    print(f"[after_model_callback] Model's state: {callback_context.state}")
    print(f"[after_model_callback] After model call for {llm_response}")


def before_agent_callback(callback_context: CallbackContext) -> Optional[types.Content]:
    """
    Simple callback that print the tool called
    """
    print(f"[before_agent_callback] Agent's Agent name : {callback_context.agent_name}")
    print(f"[before_agent_callback] Agent's state: {callback_context.state}")

def after_agent_callback(callback_context: CallbackContext) -> Optional[types.Content]:
    """
    Simple callback that print the tool called
    """
    print(f"[after_agent_callback] Agent's Agent name : {callback_context.agent_name}")
    print(f"[after_agent_callback] Agent's state: {callback_context.state}")
