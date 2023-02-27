from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    all_news = find_news()
    news_popularity = {}
    for new in all_news:
        if new["category"] not in news_popularity:
            news_popularity[new["category"]] = 1
        else:
            news_popularity[new["category"]] += 1

    sorted_popularity = sorted(
        sorted(news_popularity), key=news_popularity.get, reverse=True
    )
    return sorted_popularity


top_5_categories()
