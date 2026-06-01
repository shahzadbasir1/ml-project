"""
tools.py

Tools used by the AI Chatbot

1. Weather Tool (WeatherAPI)
2. News Tool (NewsAPI)
3. Calculator Tool
4. RAG Tool (ChromaDB)
"""

import os
import requests
from dotenv import load_dotenv
from tavily import TavilyClient
from langchain_core.tools import tool

load_dotenv()

#from langchain.tools import tool
from langchain_core.tools import tool

# -----------------------------
# WEATHER TOOL
# -----------------------------


@tool
def get_weather(city: str) -> str:
    """
    Get current weather for a city.
    """
    print("=" * 50)
    print(f"WEATHER TOOL CALLED: {city}")
    print("=" * 50)

    api_key = os.getenv("WEATHER_API_KEY")

    if not api_key:
        return "Weather API key is missing."

    url = (
        f"http://api.weatherapi.com/v1/current.json"
        f"?key={api_key}&q={city}"
    )

    try:
        response = requests.get(url)

        if response.status_code != 200:
            return "Unable to retrieve weather information."

        data = response.json()

        return (
            f"Weather in {data['location']['name']}:\n"
            f"Temperature: {data['current']['temp_c']}°C\n"
            f"Condition: {data['current']['condition']['text']}\n"
            f"Humidity: {data['current']['humidity']}%"
        )

    except Exception as e:
        return f"Weather tool error: {str(e)}"



# -----------------------------
# NEWS TOOL
# -----------------------------



# -----------------------------
# CALCULATOR TOOL
# -----------------------------


@tool
def calculator(expression: str) -> str:
    """
    Evaluate mathematical expressions.

    Example:
    25 * 4 + 10
    """

    try:
        result = eval(expression)
        print(f"CALCULATOR TOOL CALLED: {expression}")
        allowed_chars = "0123456789+-*/(). "

        if not all(c in allowed_chars for c in expression):
            return "Invalid expression."

        result = eval(expression)

        return str(result)

    except Exception as e:
        return f"Calculation error: {str(e)}"


# -----------------------------
# RAG TOOL
# -----------------------------

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


def get_vectorstore():

    embeddings = OpenAIEmbeddings()

    vectordb = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )

    return vectordb

@tool
def search_knowledge_base(query: str) -> str:
    """
    Search Employee Handbook.

    Use for:

    - PTO
    - Vacation
    - Sick Leave
    - Benefits
    - Payroll
    - Work From Home
    - Remote Work
    - Employee Conduct
    - Harassment
    - HR Policies
    """

    try:

        print("=" * 60)
        print(f"RAG TOOL CALLED: {query}")
        print("=" * 60)

        vectordb = get_vectorstore()

        docs = vectordb.similarity_search(
            query,
            k=5
        )

        if not docs:
            return "No matching HR policy found."

        return "\n\n".join(
            doc.page_content
            for doc in docs
        )

    except Exception as e:
        return f"Knowledge base error: {str(e)}"

@tool
def search_knowledge_base_old(query: str) -> str:
    """
    Search local knowledge base.
    """
    print("=" * 60)
    print(f"RAG TOOL CALLED: {query}")
    print("=" * 60)

    try:

        vectordb = get_vectorstore()

        docs = vectordb.similarity_search(
            query=query,
            k=3
        )

        if not docs:
            return "No relevant documents found."

        return "\n\n".join(
            [doc.page_content for doc in docs]
        )

    except Exception as e:
        return f"Knowledge base error: {str(e)}"


@tool
def search_news(query: str) -> str:
    """
    Search the web for current events,
    breaking news and recent information.
    """

    try:

        print("=" * 60)
        print(f"TAVILY SEARCH CALLED: {query}")
        print("=" * 60)

        client = TavilyClient(
            api_key=os.getenv(
                "TAVILY_API_KEY"
            )
        )

        result = client.search(
            query=query,
            max_results=5
        )

        output = []

        for item in result["results"]:

            output.append(
                f"Title: {item['title']}\n"
                f"Summary: {item['content']}\n"
                f"URL: {item['url']}"
            )

        return "\n\n".join(output)

    except Exception as e:
        return f"Tavily search error: {str(e)}"
    
@tool
def search_news_old(query: str):
    """
Search the internet for current information.

Use this tool whenever the user asks:
- latest news
- current events
- recent developments
- AI news
- OpenAI news
- what happened today
- what happened this week
- web searches
- technology updates

This tool provides real-time information from the internet.
    """

    print(f"TAVILY SEARCH CALLED: {query}")

    client = TavilyClient(
        api_key=os.getenv("TAVILY_API_KEY")
    )

    result = client.search(
        query=query,
        max_results=5
    )

    formatted_results = []

    for item in result.get("results", []):
        formatted_results.append(
            f"Title: {item.get('title')}\n"
            f"Summary: {item.get('content')}\n"
            f"URL: {item.get('url')}"
        )

    return "\n\n".join(formatted_results)

@tool
def company_research(company: str) -> str:
    """
    Research companies, products, executives, and business information.

    Use this tool when users ask:
    - Tell me about a company
    - Research a company
    - Who is the CEO of a company
    - Company products/services
    - Competitor information
    - Vendor information
    """

    try:

        print("=" * 60)
        print(f"SERPER COMPANY RESEARCH CALLED: {company}")
        print("=" * 60)

        api_key = os.getenv("SERPER_API_KEY")

        if not api_key:
            return "SERPER_API_KEY is missing."

        response = requests.post(
            "https://google.serper.dev/search",
            headers={
                "X-API-KEY": api_key,
                "Content-Type": "application/json"
            },
            json={
                "q": company
            }
        )

        print("STATUS CODE:", response.status_code)
        
        data = response.json()

        print("\nSERPER RESPONSE:")
        print(data)
        print("\n")

        results = []

        for item in data.get("organic", [])[:5]:

            results.append(
                f"Title: {item.get('title')}\n"
                f"Summary: {item.get('snippet')}\n"
                f"URL: {item.get('link')}"
            )

        return "\n\n".join(results)

    except Exception as e:
        return f"Company research error: {str(e)}"


TOOLS = [
    get_weather,
    search_news,
    company_research,
    calculator,
    search_knowledge_base
]