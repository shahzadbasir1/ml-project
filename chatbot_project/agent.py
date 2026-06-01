"""
agent.py

Creates LLM and binds tools.
"""

import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage

from tools import TOOLS

# Create the LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Bind tools to the LLM
llm_with_tools = llm.bind_tools(TOOLS)

def chatbot_node(state):
    """
    Main agent node.
    """

    response = llm_with_tools.invoke(
        [
            SystemMessage(content=SYSTEM_PROMPT)
        ] + state["messages"]
    )

    return {
        "messages": [response]
    }

SYSTEM_PROMPT = """
You are an AI Business Assistant.

Tool Usage Rules:

Weather Questions:
- Use get_weather

Current Events and News:
- Use search_news

Company Research:
- Use company_research

Use company_research when users ask:
- Tell me about a company
- Company overview
- CEO information
- Products and services
- Competitors
- Vendor research

Mathematics:
- Use calculator

Knowledge Base Questions:
- Use search_knowledge_base

Always use the appropriate tool when available.
"""


def create_agent():

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    llm_with_tools = llm.bind_tools(
        TOOLS
    )

    return llm_with_tools