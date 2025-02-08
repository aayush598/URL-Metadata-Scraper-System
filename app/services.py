import httpx
from bs4 import BeautifulSoup

async def fetch_html(url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0"}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text

def extract_metadata(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")

    metadata = {
        "title": soup.title.string if soup.title else "N/A",
        "description": "N/A",
        "keywords": "N/A",
        "og_title": "N/A",
        "og_description": "N/A",
        "og_image": "N/A",
    }

    for meta in soup.find_all("meta"):
        if meta.get("name") == "description":
            metadata["description"] = meta.get("content", "N/A")
        if meta.get("name") == "keywords":
            metadata["keywords"] = meta.get("content", "N/A")
        if meta.get("property") == "og:title":
            metadata["og_title"] = meta.get("content", "N/A")
        if meta.get("property") == "og:description":
            metadata["og_description"] = meta.get("content", "N/A")
        if meta.get("property") == "og:image":
            metadata["og_image"] = meta.get("content", "N/A")

    return metadata
