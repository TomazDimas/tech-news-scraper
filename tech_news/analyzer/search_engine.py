from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    response = search_news(query)
    tuple_list = [(new["title"], new["url"]) for new in response]
    return tuple_list


search_by_title("Notícia bacana")


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
