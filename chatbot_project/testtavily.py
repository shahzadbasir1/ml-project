from tools import search_news

result = search_news.invoke(
    {"query": "latest AI news"}
)

print(result)