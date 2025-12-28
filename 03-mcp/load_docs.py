import zipfile

ZIP_PATH = "data/fastmcp-main.zip"


def load_markdown_files():
    docs = []

    with zipfile.ZipFile(ZIP_PATH, "r") as z:
        for name in z.namelist():
            # keep only .md and .mdx files
            if not (name.endswith(".md") or name.endswith(".mdx")):
                continue

            # remove top-level folder (fastmcp-main/)
            parts = name.split("/", 1)
            if len(parts) < 2:
                continue

            clean_name = parts[1]

            with z.open(name) as f:
                content = f.read().decode("utf-8", errors="ignore")

            docs.append(
                {
                    "filename": clean_name,
                    "content": content,
                }
            )

    return docs


if __name__ == "__main__":
    documents = load_markdown_files()
    print(f"Loaded {len(documents)} markdown files")
    print("First file:", documents[0]["filename"])
