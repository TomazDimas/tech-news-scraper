import pytest
from unittest.mock import patch
from tech_news import database
from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501


@pytest.fixture
def group_news_response_mock():
    return {
        "readable": [
            {
                "unfilled_time": 0,
                "chosen_news": [
                    (
                        (
                            "5 exemplos de algoritmos "
                            "na vida real e na computação"
                        ),
                        5,
                    )
                ],
            },
            {
                "unfilled_time": 0,
                "chosen_news": [
                    (
                        (
                            "5 exemplos de algoritmos"
                            " na vida real e na computação"
                        ),
                        5,
                    )
                ],
            },
        ],
        "unreadable": [
            ("Protocolo TCP/IP: o que é e exemplos de como funciona", 9),
            ("Programação em Arduino para iniciantes em 11 passos!", 14),
            (
                "Sistema Operacional Windows: versões, dicas e como instalar?",
                18,
            ),
            (
                (
                    "TrybeTalks — Gaules: os ensinamentos"
                    " de um dos maiores streamers do Brasil"
                ),
                9,
            ),
            ("Protocolo TCP/IP: o que é e exemplos de como funciona", 9),
            ("Programação em Arduino para iniciantes em 11 passos!", 14),
            (
                "Sistema Operacional Windows: versões, dicas e como instalar?",
                18,
            ),
            (
                (
                    "TrybeTalks — Gaules: os ensinamentos"
                    " de um dos maiores streamers do Brasil"
                ),
                9,
            ),
        ],
    }


@pytest.fixture
def find_news_mock():
    return [
        {
            "_id": "63fcf0db1fe9cbc9df2c57eb",
            "url": "https://blog.betrybe.com/tecnologia/protocolo-tcp-ip/",
            "title": "Protocolo TCP/IP: o que é e exemplos de como funciona",
            "timestamp": "17/02/2023",
            "writer": "Cairo Noleto",
            "reading_time": 9,
            "summary": (
                "A todo o instante diversos dados trafegam pela rede"
                ": seja o envio de um e-mail, uma mensagem, foto, ar"
                "quivo, esses dados partem de um ponto A para um pon"
                "to B. Mas como essa comunicação é feita? Para respond"
                "ermos a essa pergunta, vamos aprender sobre o pro"
                "tocolo TCP/IP."
            ),
            "category": "Tecnologia",
        },
        {
            "_id": "63fcf0db1fe9cbc9df2c57ec",
            "url": (
                "https://blog.betrybe.com/"
                "tecnologia/programacao-em-arduino/"
            ),
            "title": "Programação em Arduino para iniciantes em 11 passos!",
            "timestamp": "14/02/2023",
            "writer": "Cairo Noleto",
            "reading_time": 14,
            "summary": (
                "Você sabia que com a utilização de um ardui"
                "no é possível fazer sensores de led ou até me"
                "smo aqueles carrinhos autônomos bastante parecid"
                "os com um robô? Pois bem, com um arduino em mã"
                "os é possível desenvolver diversas coisas que po"
                "dem trazer algumas facilidades em seu cotidiano."
            ),
            "category": "Tecnologia",
        },
        {
            "_id": "63fcf0db1fe9cbc9df2c57ed",
            "url": (
                "https://blog.betrybe.com/tecnol"
                "ogia/sistema-operacional-windows/"
            ),
            "title": (
                "Sistema Operacional Windows: "
                "versões, dicas e como instalar?"
            ),
            "timestamp": "06/02/2023",
            "writer": "Cairo Noleto",
            "reading_time": 18,
            "summary": (
                "É fato que todo computador necessita de um sistema ope"
                "racional para funcionar. Entretanto, diversas op"
                "ções estão disponíveis no mercado, como o Win"
                "dows, o Mac OS, o Linux e suas variações."
            ),
            "category": "Tecnologia",
        },
        {
            "_id": "63fcf0db1fe9cbc9df2c57ee",
            "url": (
                "https://blog.betrybe.com/te"
                "cnologia/exemplos-de-algoritmos/"
            ),
            "title": "5 exemplos de algoritmos na vida real e na computação",
            "timestamp": "03/02/2023",
            "writer": "Lucas Custódio",
            "reading_time": 5,
            "summary": (
                "Quando falamos de algoritmos, "
                "pensamos em matemática e programação. Porém, te"
                "mos exemplos de algoritmos que estão muito p"
                "resentes nas nossas atividades cotidianas."
            ),
            "category": "Tecnologia",
        },
        {
            "_id": "63fcf0db1fe9cbc9df2c57ef",
            "url": "https://blog.betrybe.com/carreira/trybetalks-gaules/",
            "title": (
                "TrybeTalks — Gaules: os ensinamentos"
                " de um dos maiores streamers do Brasil"
            ),
            "timestamp": "30/01/2023",
            "writer": "Lucas Custódio",
            "reading_time": 9,
            "summary": (
                "Gaules, uma das maiores personalidades"
                " do mundo de esports brasileiro, divide"
                " um pouco de sua experiência de vida e "
                "carreira em um webinar com estudantes e "
                "ex-estudantes da Escola de Programação Trybe."
            ),
            "category": "Carreira",
        },
        {
            "_id": "63fcf0dd528ebabb2b4a945d",
            "url": "https://blog.betrybe.com/tecnologia/protocolo-tcp-ip/",
            "title": "Protocolo TCP/IP: o que é e exemplos de como funciona",
            "timestamp": "17/02/2023",
            "writer": "Cairo Noleto",
            "reading_time": 9,
            "summary": (
                "A todo o instante diversos dados trafegam pela rede: seja"
                " o envio de um e-mail, uma mensagem, foto, arquivo, "
                "esses dados partem de um ponto A para um ponto B. Mas "
                "como essa comunicação é feita? Para respondermos a"
                " essa pergunta, vamos aprender sobre o protocolo TCP/IP."
            ),
            "category": "Tecnologia",
        },
        {
            "_id": "63fcf0dd528ebabb2b4a945e",
            "url": (
                "https://blog.betrybe.com/tecnologia/programacao-em-arduino/"
            ),
            "title": "Programação em Arduino para iniciantes em 11 passos!",
            "timestamp": "14/02/2023",
            "writer": "Cairo Noleto",
            "reading_time": 14,
            "summary": (
                "Você sabia que com a utilização de um arduino é possível"
                " fazer sensores de led ou até mesmo aqueles carrinhos"
                " autônomos bastante parecidos com um robô? Pois bem,"
                " com um arduino em mãos é possível desenvolver diversas"
                " coisas que podem trazer algumas"
                " facilidades em seu cotidiano."
            ),
            "category": "Tecnologia",
        },
        {
            "_id": "63fcf0dd528ebabb2b4a945f",
            "url": (
                "https://blog.betrybe.com/tecnolog"
                "ia/sistema-operacional-windows/"
            ),
            "title": (
                "Sistema Operacional Windows: versões, dicas e como instalar?"
            ),
            "timestamp": "06/02/2023",
            "writer": "Cairo Noleto",
            "reading_time": 18,
            "summary": (
                "É fato que todo computador necessita de um sistema opera"
                "cional para funcionar. Entretanto, diversas opções estão"
                " disponíveis no mercado, como o Windows, "
                "o Mac OS, o Linux e suas variações."
            ),
            "category": "Tecnologia",
        },
        {
            "_id": "63fcf0dd528ebabb2b4a9460",
            "url": (
                "https://blog.betrybe.com/tecnologia/exemplos-de-algoritmos/"
            ),
            "title": "5 exemplos de algoritmos na vida real e na computação",
            "timestamp": "03/02/2023",
            "writer": "Lucas Custódio",
            "reading_time": 5,
            "summary": (
                "Quando falamos de algoritmos, pensamos em matemática e "
                "programação. Porém, temos exemplos de algoritmos que"
                " estão muito presentes nas nossas atividades cotidianas."
            ),
            "category": "Tecnologia",
        },
        {
            "_id": "63fcf0dd528ebabb2b4a9461",
            "url": "https://blog.betrybe.com/carreira/trybetalks-gaules/",
            "title": (
                "TrybeTalks — Gaules: os ensinamentos de"
                " um dos maiores streamers do Brasil"
            ),
            "timestamp": "30/01/2023",
            "writer": "Lucas Custódio",
            "reading_time": 9,
            "summary": (
                "Gaules, uma das maiores personalidades do mundo de espo"
                "rts brasileiro, divide um pouco de sua experiência de vid"
                "a e carreira em um webinar com estudantes e ex-estuda"
                "ntes da Escola de Programação Trybe."
            ),
            "category": "Carreira",
        },
    ]


def test_reading_plan_group_news(find_news_mock, group_news_response_mock):
    with patch.object(database, "find_news", return_value=find_news_mock):
        result = ReadingPlanService.group_news_for_available_time(5)

    assert result == group_news_response_mock

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)
