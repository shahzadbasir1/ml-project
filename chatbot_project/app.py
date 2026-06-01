"""
app.py

Gradio Interface for AI Chatbot
"""

import uuid

import gradio as gr

from langchain_core.messages import HumanMessage

from graph import build_graph


# ---------------------------------
# Build Graph
# ---------------------------------

graph = build_graph()


# ---------------------------------
# Session Memory
# ---------------------------------

session_threads = {}


def get_thread_id(session_id):

    if session_id not in session_threads:
        session_threads[session_id] = str(uuid.uuid4())

    return session_threads[session_id]


# ---------------------------------
# Chat Function
# ---------------------------------

def chat(message, history, session_id):

    thread_id = get_thread_id(session_id)

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=message)
            ]
        },
        config=config
    )

    response = result["messages"][-1].content

    return response


# ---------------------------------
# Gradio UI
# ---------------------------------

with gr.Blocks(
    title="AI Chatbot"
) as demo:

    gr.Markdown(
        """
        # AI Chatbot

        Features:

        - Weather Lookup (Tool: Weather)
        - News Search (Tool: Tavily)
        - Company Search (Tool: Serper)
        - Calculator (Tool: Calculator)
        - Knowledge Base Search (RAG)
        - Memory (Session)
        - LangGraph Agent
        """
    )

    session_id = gr.State(
        str(uuid.uuid4())
    )

    chatbot = gr.ChatInterface(
        fn=lambda message, history:
        chat(
            message,
            history,
            session_id.value
        )
    )



if __name__ == "__main__":

    demo.launch(
        share=False
    )