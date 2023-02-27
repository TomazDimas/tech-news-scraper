import sys
# from tech_news.scraper import get_tech_news


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
    if first_option == 0:
        # news_amount = input
        print(("Digite quantas notícias serão buscadas:"))
    elif first_option == 1:
        # title = input("Digite o título:")
        print(("Digite o título:"))
    elif first_option == 2:
        # title = input("Digite a data no formato aaaa-mm-dd:")
        print(("Digite a data no formato aaaa-mm-dd:"))
    elif first_option == 3:
        # category = input("Digite a categoria:")
        print(("Digite a data no formato aaaa-mm-dd:"))
    else:
        sys.stderr.write("Opção inválida")


# analyzer_menu()
