from fastmcp import FastMCP
import requests
from search import search_docs

mcp = FastMCP("Demo 🚀")


@mcp.tool
def scrape_webpage(url: str) -> str:
    """
    Download a web page as markdown using Jina Reader.
    """
    jina_url = f"https://r.jina.ai/{url}"
    response = requests.get(jina_url, timeout=30)
    response.raise_for_status()
    return response.text


@mcp.tool
def search_docs_tool(query: str, limit: int = 5):
    """
    Search FastMCP documentation and return top matching files.
    """
    return search_docs(query, limit)


if __name__ == "__main__":
    mcp.run()
