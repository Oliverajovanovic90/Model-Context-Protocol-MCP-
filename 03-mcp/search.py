from load_docs import load_markdown_files
from minsearch import Index

_index = None


def get_index():
    global _index
    if _index is None:
        docs = load_markdown_files()
        _index = Index(
            text_fields=["content"],
            keyword_fields=["filename"],
        )
        _index.fit(docs)
    return _index

def search_docs(query: str, limit: int = 5):
    index = get_index()
    results = index.search(query, num_results=limit)
    return [
        {
            "filename": r["filename"],
        }
        for r in results
    ]

