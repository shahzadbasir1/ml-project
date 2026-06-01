"""
graph.py

LangGraph workflow with:

- Conditional tool routing
- Memory checkpointing
- Tool execution
- Final response generation
"""

from typing import TypedDict
from typing_extensions import Annotated

from langgraph.graph import StateGraph
from langgraph.graph import START
from langgraph.graph.message import add_messages

from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition

from langgraph.checkpoint.memory import MemorySaver

from langchain_core.messages import SystemMessage

from agent import create_agent, SYSTEM_PROMPT
from tools import TOOLS


# ------------------------------------
# STATE
# ------------------------------------


class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


# ------------------------------------
# AGENT
# ------------------------------------


llm = create_agent()


def chatbot(state: AgentState):

    messages = state["messages"]

    # Add system prompt once
    if not any(
        isinstance(msg, SystemMessage)
        for msg in messages
    ):
        messages = [
            SystemMessage(content=SYSTEM_PROMPT)
        ] + messages

    response = llm.invoke(messages)

    return {
        "messages": [response]
    }


# ------------------------------------
# GRAPH
# ------------------------------------


def build_graph():

    builder = StateGraph(AgentState)

    # Agent Node
    builder.add_node(
        "agent",
        chatbot
    )

    # Tool Node
    builder.add_node(
        "tools",
        ToolNode(TOOLS)
    )

    # Start
    builder.add_edge(
        START,
        "agent"
    )

    # Conditional Routing
    builder.add_conditional_edges(
        "agent",
        tools_condition
    )

    # Return from tools to agent
    builder.add_edge(
        "tools",
        "agent"
    )

    # Memory
    memory = MemorySaver()

    graph = builder.compile(
        checkpointer=memory
    )

    return graph