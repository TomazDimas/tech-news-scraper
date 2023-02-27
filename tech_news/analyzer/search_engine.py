from tech_news.database import search_news
import datetime


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    response = search_news(query)
    tuple_list = [(new["title"], new["url"]) for new in response]
    return tuple_list


# Requisito 8
def search_by_date(date):
    try:
        iso_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    new_form_date = iso_date.strftime("%d/%m/%Y")

    query = {"timestamp": new_form_date}
    response = search_news(query)

    tuple_list = [(new["title"], new["url"]) for new in response]
    return tuple_list


search_by_date("2021-04-04")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
