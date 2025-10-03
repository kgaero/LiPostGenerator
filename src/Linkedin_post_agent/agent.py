"""
LinkedIn Post Generator Root Agent

This module defines the root agent for the LinkedIn Post Generator application.
It uses a sequential agent to generate the initial post followed by a refinement loop to improve the post.

"""


from google.adk.agents import LoopAgent, SequentialAgent
from .subagents.post_generator.agent import initial_post_generator
from .subagents.post_refiner.agent import post_refiner
from .subagents.post_reviewer.agent import post_reviewer


refinement_loop = LoopAgent(
    name = 'PostRefinementloop',
    max_iterations= 10,
    sub_agents= [post_reviewer, post_refiner],
    description= "Iteratively reviews and refines a LinkedIn post until quality requirements are met",
)




root_agent = SequentialAgent(
    name = "LinkedInPostGeneratorPipeline",
    sub_agents = [initial_post_generator, refinement_loop],
    description = "Generates and refines a LinkedIn post through an Iterator review process"
)
