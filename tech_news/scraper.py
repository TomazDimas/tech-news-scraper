import requests
import time
from tech_news.database import create_news
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    headers = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, timeout=3, headers=headers)
        print(response)
        if response.status_code == 200:
            return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    url_list = selector.css(
        ".cs-overlay.cs-overlay-hover a::attr(href)"
    ).getall()
    return url_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_url = selector.css("a.next.page-numbers::attr(href)").get()
    print(next_url)
    return next_url


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    reading_time = int(
        selector.css(".meta-reading-time::text").get().split(" ")[0]
    )
    summary = selector.css(".entry-content > p:first-of-type *::text").getall()
    category = selector.css(".label::text").get()

    news_dict = {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": "".join(summary).strip(),
        "category": category,
    }
    return news_dict


# Requisito 5
def get_tech_news(amount):
    html_content = fetch("https://blog.betrybe.com/")
    news_urls = scrape_updates(html_content)

    while len(news_urls) < amount:
        html_content = fetch(scrape_next_page_link(html_content))
        news_urls.extend(scrape_updates(html_content))

    scrapped_news = [scrape_news(fetch(url)) for url in news_urls[:amount]]
    create_news(scrapped_news)
    return scrapped_news
