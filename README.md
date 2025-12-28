# Model-Context-Protocol-MCP - Documentation Search Server

## Project Overview

This project implements a Model Context Protocol (MCP) server, inspired by tools like Context7, that enables an AI assistant to:

Scrape web content

Index documentation from a GitHub repository

Perform semantic search over documentation

Expose these capabilities as MCP tools

The server is built using FastMCP, minsearch, and uv for modern Python dependency management.

## Purpose

Large language models often lack access to up-to-date or project-specific documentation.
This project solves that problem by:

Downloading real documentation

Making it searchable

Allowing an AI assistant to retrieve relevant context dynamically

### This pattern is essential for:

AI copilots

Documentation-aware chatbots

Internal knowledge assistants

Technologies Used

FastMCP — MCP server framework

minsearch — lightweight semantic search engine

uv — fast Python package & environment manager

Jina Reader — converts web pages to clean Markdown

Python 3.12


## Project Structure
```
03-mcp/
├─ main.py              # MCP server with exposed tools
├─ download.py          # Downloads documentation ZIP
├─ load_docs.py         # Reads and cleans markdown files
├─ search.py            # Builds and queries search index
├─ scrape.py            # Web scraping utility (Jina Reader)
├─ pyproject.toml       # Project metadata & dependencies
├─ uv.lock              # Locked dependency versions
├─ .gitignore           # Excludes local & generated files
└─ README.md
```

## Step-by-Step Design Explanation

### 1. Dependency Management with uv

We use uv instead of pip/venv because it:

Is significantly faster

Produces deterministic builds (uv.lock)

Simplifies project setup

uv init
uv add fastmcp minsearch requests

### 2. MCP Server (main.py)

The MCP server runs using STDIO transport, which allows AI clients to communicate via structured JSON messages.

Exposed tools:

scrape_webpage — downloads web pages as Markdown

search_docs_tool — searches indexed documentation

uv run python main.py

3. Web Scraping Tool (Jina Reader)

To retrieve clean Markdown from any URL, we prepend:

https://r.jina.ai/


This avoids HTML parsing and ensures consistent text output.

#### Purpose:

Enable AI tools to read real web content

Used in earlier homework steps and reusable for other MCP tools

### 4. Documentation Download (download.py)

We download the FastMCP GitHub repository as a ZIP file:

https://github.com/jlowin/fastmcp/archive/refs/heads/main.zip


Why ZIP?

Simple

No Git dependency

Easy to reproduce

The script skips downloading if the file already exists.

### 5. Markdown Extraction (load_docs.py)

This step:

Iterates over ZIP contents

Keeps only .md and .mdx files

Removes the top-level folder prefix

Loads content into memory

Result:

{
  "filename": "docs/getting-started/welcome.mdx",
  "content": "..."
}


This clean structure is required for indexing.

### 6. Search Indexing (search.py)

We use minsearch to build a semantic index over documentation.

Key points:

Index built once and cached

Searches over document content

Returns the most relevant files

Example:

search_docs("demo")


Returns:

examples/testing_demo/README.md

### 7. MCP Search Tool Integration

The search functionality is exposed as an MCP tool:

@mcp.tool
def search_docs_tool(query: str, limit: int = 5):
    return search_docs(query, limit)


This allows an AI assistant to:

Query documentation

Retrieve relevant context

Ground its answers in real files

Running the Project
Start the MCP server
uv run python main.py


The server runs on STDIO transport and waits for MCP client requests.

Git & Reproducibility

.venv/ and downloaded ZIP files are excluded via .gitignore

Documentation can be re-downloaded at any time

The project is fully reproducible using uv.lock

## Key Learning Outcomes

Understanding MCP architecture

Building AI-accessible tools

Creating searchable documentation indexes

Managing modern Python projects cleanly

Designing AI systems that retrieve real context

