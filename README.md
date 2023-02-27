# Boas vindas ao repositório do Tech News Scraper :computer:! 
Projeto criado por Tomaz Dimas durante o curso de Desenvolvimento Web da Trybe.

# Descrição

O Tech News Scraper é uma aplicação de raspagem de dados, que a partir de uma URL, realiza a requisição e tratamento de dados, inserção destes dados em um banco de dados MongoDB para posteriormente construir relatórios.

O aplicação foi desenvolvida para funcionar no blog de notícias da Trybe (https://blog.betrybe.com/), possuindo diversas funções como, a requisição da informação HTML da página, a raspagem das informações de cada notícia, a paginação dinâmica da páginas requisitadas e a inserção de todas essas informações em um banco de dados não relacional.

Após a raspagem de dados população do banco de dados, entram outras funcionalidades como a busca e filtro dessas notícias por parâmetros como título, categoria e data, além de um relatório mostrando quais categorias são mais comentadas dentro do site.

Por fim, foi desenvolvido um menu para interagir com a aplicação podendo optar como o banco de dados será populado e qual tipo de informação deseja-se retirar dele.

* O texto do menu é este formato:

```
Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair.
```

# Instalação e Inicialização

Para instalação e inicialização do projeto deve-se inicialmente clonar este repositório e instalar suas dependências, para que as dependências não sejam instaladas diretamente no seu computador, recomenda-se a criação de um ambiente virtual:

  1. **criar o ambiente virtual**

  ```bash
python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
python3 -m pip install -r dev-requirements.txt
  ```

# Ferramentas e Habilidades utilizadas

- Python;
- Pytest;
- Pytest-mock;
- Parsel;
- Requests;
- Pymongo;
- MongoDB;
- Docker;
