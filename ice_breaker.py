from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

information = """
Elon Reeve Musk FRS (Pretória, 28 de junho de 1971) é um empresário,[5] empreendedor e filantropo sul-africano, naturalizado canadense e estadunidense. É o fundador, diretor executivo e diretor técnico da SpaceX; CEO da Tesla, Inc.; um dos cofundadores da OpenAI, fundador e CEO da Neuralink; cofundador, presidente da SolarCity e proprietário do X (antigo Twitter) e Ex-Comissário do Departamento de Eficiência Governamental dos Estados Unidos durante o Segundo Governo Trump (2025). Em 2023, ele era a pessoa mais rica do mundo, com um patrimônio líquido estimado em 225 bilhões de dólares, de acordo com o Bloomberg Billionaires Index. Já a revista Forbes estimou sua fortuna em 221,3 bilhões de dólares, principalmente de suas participações acionárias nas empresas Tesla e na SpaceX.[2][3]

Musk demonstrou publicamente preocupações com a extinção humana[6] e também propôs soluções, das quais algumas são o objetivo principal de suas empresas e já estão sendo feitas na prática. Entre elas, a redução do aquecimento global, através do uso de energias renováveis, um projeto multiplanetário, mais especificamente a colonização de Marte,[7] e o desenvolvimento seguro da inteligência artificial.

Em janeiro de 2011, uma de suas empresas, a SpaceX, tornou-se a primeira empresa no mundo a vender um voo comercial à Lua. A missão, marcada para 2013, foi contratada pela empresa Astrobotic Technology, tendo como objetivo colocar um pequeno jipe na superfície lunar, o que não aconteceu. Em 2012, encerrou o projeto do Tesla Roadster, o primeiro modelo da sua autoria, um carro totalmente elétrico que custava cerca de 92 mil dólares. A Tesla já lançou quatro modelos: S, Y, X e o Modelo 3, este último com a responsabilidade de trazer os carros elétricos para as massas, partindo de um custo inicial de 35 mil dólares.[8] Em 25 de abril de 2022, ele também concordou em comprar o Twitter por 44 bilhões de dólares.[9]

Musk expressou opiniões que o tornaram uma figura polarizadora e controversa.[10] Ele foi criticado por fazer declarações não científicas, enganosas, ou endossar teorias da conspiração, incluindo sobre a pandemia de COVID-19 e a eleição presidencial nos Estados Unidos em 2020, além de endossar postagens antissemitas,[11] sendo que por este último ele se desculpou.[12] Em 2024, Musk foi o maior doador na eleição presidencial daquele ano[13] e desde então tem se destacado como um apoiador de personalidades, causas e partidos políticos de extrema-direita no mundo todo.[14][15] 
"""

if __name__ == '__main__':
    load_dotenv()
    print("hello LangChain!")
    print(os.environ['OPENAI_API_KEY'])
    
    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=['information'], template=summary_template)

    # llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    llm = ChatOllama(model='mistral')

    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": information})

    print(res)