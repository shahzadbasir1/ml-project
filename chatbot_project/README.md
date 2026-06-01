# AI Chatbot

## Project Overview

AI Chatbot is an agentic AI application built using LangChain, LangGraph, OpenAI GPT-4o-mini, and Gradio.

The application demonstrates modern AI agent architecture including:

* Tool Calling
* Conditional Routing
* Memory Checkpointing
* Stateful Workflows
* External API Integration
* Retrieval Augmented Generation (RAG)
* Interactive User Interface

The chatbot can answer general questions, retrieve weather information, retrieve current news, perform calculations, search a local knowledge base, and remember previous conversations.

---

# Selected Use Case

## AI Business Assistant

The selected use case is an AI-powered business assistant capable of:

* Answering business questions
* Providing current weather information
* Retrieving latest news
* Performing calculations
* Searching local documents
* Maintaining conversation memory

This use case demonstrates real-world applicability while showcasing agentic AI workflows.

---

# Technologies Used

## Frameworks

* LangChain
* LangGraph
* Gradio

## LLM

* OpenAI GPT-4o-mini

## APIs

### Weather API

Used to retrieve real-time weather information.

Provider:
WeatherAPI

### News API

Used to retrieve current news articles.

Provider:
NewsAPI

## Vector Database

* ChromaDB

## Embeddings

* OpenAI Embeddings

---

# Project Structure

AI_Chatbot/

├── app.py

├── agent.py

├── graph.py

├── tools.py

├── requirements.txt

├── .env.example

├── README.md

├── workflow_diagram.mmd

├── screenshots/

│ ├── screenshot_1_gradio_ui.png

│ ├── screenshot_2_weather_tool.png

│ ├── screenshot_3_news_tool.png

│ └── screenshot_4_memory_demo.png

└── demo_video_script.md

---

# Tool Integration

The application integrates four tools.

## Tool 1: Weather Tool

Type:
External API Tool

Purpose:
Retrieve weather information for any city.

Example Prompt:

What is the weather in Islamabad?

---

## Tool 2: News Tool

Type:
External API Tool

Purpose:
Retrieve latest news based on a topic.

Example Prompt:

Give me the latest AI news.

---

## Tool 3: Calculator Tool

Type:
Custom Python Tool

Purpose:
Perform mathematical calculations.

Example Prompt:

Calculate 25 * 4 + 10

---

## Tool 4: Knowledge Base Tool

Type:
RAG Tool

Purpose:
Search local documents stored in ChromaDB.

Example Prompt:

What does the employee handbook say about vacation policy?

---

# LangGraph Workflow

The application uses LangGraph to orchestrate execution.

Workflow:

User Input

↓

Agent Node

↓

Conditional Routing

↓

Tool Node (if required)

↓

Agent Node

↓

Final Response

The workflow dynamically decides whether a tool is needed before generating the final response.

---

# Conditional Routing

Conditional routing is implemented using:

tools_condition()

The AI determines whether a tool should be called.

Examples:

Weather question

→ Weather Tool

News question

→ News Tool

Math question

→ Calculator Tool

General question

→ Direct LLM Response

This demonstrates agentic behavior and dynamic workflow execution.

---

# Memory Implementation

## Graph State

Graph State stores temporary information during workflow execution.

Example:

Current user message

Current tool results

Current AI response

Graph state only exists while a graph run is executing.

---

## Checkpoint Memory

Memory is implemented using:

MemorySaver()

Memory persists conversation history across multiple user interactions.

Example:

User:
My company is Payactiv.

Later:

User:
What company do I work for?

AI:
You previously told me that you work for Payactiv.

---

# RAG Implementation

Bonus Feature

The application includes Retrieval Augmented Generation (RAG).

Documents are:

1. Loaded into ChromaDB
2. Converted into embeddings
3. Retrieved using similarity search

This allows the chatbot to answer questions using private documents.

---

# Installation

## Step 1

Clone repository

git clone <repository_url>

cd AI_Chatbot

---

## Step 2

Create virtual environment

Windows:

python -m venv venv

venv\Scripts\activate

---

## Step 3

Install dependencies

pip install -r requirements.txt

---

## Step 4

Configure environment variables

Copy:

.env.example

to:

.env

Fill in:

OPENAI_API_KEY

WEATHER_API_KEY

NEWS_API_KEY

---

## Step 5

Run application

python app.py

---

# Example Prompts

## Weather

What is the weather in Lahore?

---

## News

Give me the latest AI news.

---

## Calculator

Calculate 125 * 47

---

## General Question

Explain machine learning.

---

## Memory Demonstration

My company is Payactiv.

Later:

What company do I work for?

---

# Screenshots Included

The following screenshots should be captured:

1. Gradio User Interface
2. Weather Tool Execution
3. News Tool Execution
4. Memory Demonstration

---

# Challenges Faced

1. Designing conditional routing using LangGraph.
2. Integrating multiple tools with a single agent.
3. Managing conversation memory across sessions.
4. Coordinating API responses with LLM-generated content.
5. Maintaining compatibility between LangChain and LangGraph versions.

---

# Future Improvements

1. Multi-Agent Architecture
2. Supervisor Agent
3. Human-in-the-Loop Approval
4. Database Integration
5. LangSmith Monitoring
6. Streaming Responses
7. Deployment to Hugging Face Spaces
8. Voice Interface
9. PDF Upload Interface
10. SQL Query Agent

---

# Learning Outcomes

This project demonstrates:

* Agentic AI design
* LangGraph workflows
* Tool integration
* External API usage
* Conditional routing
* Memory checkpointing
* RAG implementation
* Interactive AI interfaces

The project satisfies all mandatory assignment requirements and includes bonus features for additional credit.
