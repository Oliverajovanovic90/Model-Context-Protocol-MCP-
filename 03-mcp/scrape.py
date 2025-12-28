import requests

def scrape_webpage(url: str) -> str:
    """
    Download a web page as markdown using Jina Reader.
    """
    jina_url = f"https://r.jina.ai/{url}"
    response = requests.get(jina_url, timeout=30)
    response.raise_for_status()
    return response.text
