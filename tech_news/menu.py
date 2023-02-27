import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories


# Requisitos 11 e 12
def analyzer_menu():
    first_option = input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair.
 """
    )
    if int(first_option) == 0:
        news_amount = input("Digite quantas notícias serão buscadas:")
        get_tech_news(int(news_amount))
        # print(("Digite quantas notícias serão buscadas:"))
    elif int(first_option) == 1:
        title = input("Digite o título:")
        response = search_by_title(title)
        print(response)
        # print(("Digite o título:"))
    elif int(first_option) == 2:
        date = input("Digite a data no formato aaaa-mm-dd:")
        response = search_by_date(date)
        print(response)
        # print(("Digite a data no formato aaaa-mm-dd:"))
    elif int(first_option) == 3:
        category = input("Digite a categoria:")
        response = search_by_category(category)
        print(response)
        # print(("Digite a data no formato aaaa-mm-dd:"))
    elif int(first_option) == 4:
        response = top_5_categories()
        print(response)
    elif int(first_option) == 5:
        print("Encerrando script")
        return
    else:
        sys.stderr.write("Opção inválida")
