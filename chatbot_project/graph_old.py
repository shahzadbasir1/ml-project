"""
graph.py

LangGraph workflow
"""

from typing import TypedDict

from langgraph.graph import StateGraph
from langgraph.graph import START
from langgraph.graph import END

from langgraph.graph.message import add_messages

from typing_extensions import Annotated

from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition

from langgraph.checkpoint.memory import MemorySaver

from langchain_core.messages import SystemMessage

from agent import create_agent, SYSTEM_PROMPT
from tools import TOOLS


class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


llm = create_agent()


def chatbot(state: AgentState):

    messages = state["messages"]

    if not any(
        isinstance(m, SystemMessage)
        for m in messages
    ):
        messages = [
            SystemMessage(content=SYSTEM_PROMPT)
        ] + messages

    response = llm.invoke(messages)

    return {
        "messages": [response]
    }


def build_graph():

    graph_builder = StateGraph(
        AgentState
    )

    graph_builder.add_node(
        "agent",
        chatbot
    )

    graph_builder.add_node(
        "tools",
        ToolNode(TOOLS)
    )

    graph_builder.add_edge(
        START,
        "agent"
    )

    graph_builder.add_conditional_edges(
        "agent",
        tools_condition
    )

    graph_builder.add_edge(
        "tools",
        "agent"
    )

    graph_builder.add_edge(
        "agent",
        END
    )

    memory = MemorySaver()

    graph = graph_builder.compile(
        checkpointer=memory
    )

    return graph