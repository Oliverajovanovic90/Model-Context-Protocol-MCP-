from scrape import scrape_webpage

if __name__ == "__main__":
    url = "https://github.com/alexeygrigorev/minsearch"
    content = scrape_webpage(url)
    print(len(content))
