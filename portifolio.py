import streamlit as st
from PIL import Image
import base64
from base64 import b64encode

st.set_page_config(
    page_title = "Brundo Donato - Portifolio Data Science",
    layout = "wide"
)


st.write("<div align='center'><h1><b>Bruno de Sousa Donato</b></h1></div>", unsafe_allow_html=True)

st.markdown("""<div style='text-align: center;'><hr style='border-top: 5px solid black'></div>""", unsafe_allow_html=True)

st.write("<div align='center'><h2><i>| Ciência de dados | Machine Learning | IA | Python | SQL |</i></h2></div>", unsafe_allow_html=True)

st.write("")
st.write("")

tab1, tab2, tab3, tab4 = st.tabs(["Sobre Mim", "Curriculo","Projetos Ciência de Dados", "Posts e Estudos"])

with tab1:
    col1, col2 = st.columns([2, 5])
    image = Image.open("data/eu_felizao.jpeg")
    
    col1.write("")
    col1.write("")
    col1.write("")
    col1.image(image, caption='Eu felizão', width = 250)

    col2.write("")
    col2.write("")
    col2.write("""
               Sou cientista de dados, graduado em fisioterapia e mestre em ciências pela UNICAMP. Desde sempre curioso sobre ciência, 
               na adolescência me tornei leitor assíduo de autores como Carl Sagan, Isaac Asimov, Frank Herbert, Bertrand Russel, Karl Popper, 
               e muitos outros que me direcionaram a vida acadêmica.
               """)
    
    col2.write("""
               No mestrado onde tive primeiro contato com estatística e me apaixonei logo de cara. Sempre gostei de aprender novas coisas, temas 
               e habilidades, e de maneira autodidata, com muita paciência, horas de dedicação e muito mais curiosidade, aprendi SPSS, e linguagens 
               de programação R, Python, SQL e ferramentas como Power BI/Excel. Sempre procurando aprimorar meus conhecimentos.
               """)
    
    col2.write("""
               Atuei como fisioterapeuta, atendendo diretamente pessoas e públicos de perfis diversos em diferentes instituições, por quase 10 anos 
               e decidi entrar no mundo dos dados para seguir meus objetivos de vida, pois procuro liberdade, possibilidade de crescimento profissional 
               e pessoal, e novos desafios.
               """)
    
    col2.write("""
               Atualmente aprimorando meus conhecimentos em ciência de dados e machine learning na TERA, consequentemente e felizmente absorvendo 
               novos conhecimentos.
               """)           
    
    col2.write("""
               Cachorreiro, amante da música, literatura, calistenia, queijos, cerveja, café e fotografia. Difundindo conhecimento e buscando 
               ser sempre melhor do que ontem.
               """)


with tab2:
    with open("data/bruno_donato_ciencia_de_dados_CV.pdf", "rb") as pdf_file:
        b64_pdf = base64.b64encode(pdf_file.read()).decode()
        href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="Bruno_Donato_Ciencia_de_Dados_CV.pdf">Download CV</a>'
        st.markdown(href, unsafe_allow_html=True)

    st.header("**Experiência Profissional**")
    st.subheader("**_CIENTISTA DE DADOS - Autônomo (01/2022 - Atual)_**")
    st.write("""
             Trabalho com empreendedores locais com análise de dados e business intelligence (métricas/KPIs), implementando pipelines e modelos, 
             de regressão, classificação (KNN, SVM, Decision Tree/Árvore de decisão, Random Forest, XGBoost), clusterização (K-means), processamento 
             de linguagem natural (NLP) utilizando webapps e dashboards para deployment de projetos. Usando criatividade para adequar o serviço ao 
             perfil de cada cliente e tornar insights acessíveis e compreensíveis para orientar tomadas de decisões.
                - Linguagens de programação: Python, R, SQL
                - Bibliotecas analise e visualização: Pandas, Numpy, Matplotlib, Seaborn, Plotly
                - Bibliotecas ML/IA: Scikit-Learn, PyCaret, SciPy, StatsModels, NLTK, Spacy, Gensim, REGEX, XGBoost, Optuna
                - Bibliotecas deploy/web: MLFlow, Streamlit, Selenium e BeautilfulSoup
                - Ferramentas: Power BI e Pacote Office
             """)
    
    st.subheader("")
    st.subheader("**_CONSULTORIA ACADÊMICA - Autônomo (09/2019 - Atual)_**")
    st.write("""
             - Elaboração de projetos e análise estatística
             - Aulas e tutorias de fundamentos de pesquisa e da estatística para a saúde (prática baseada em evidência)

             Conhecimento e experiencia em:
                - Testes de correlação e regressão
                - Modelos lineares e não-lineares
                - Teste chi-quadrado e correlatos
                - Testes paramétricos (teste-t, ANOVA) e seus correlatos não paramétricos.
    """)
    
    st.subheader("")
    st.subheader("**_FISIOTERAPEUTA/CONSULTOR - SUS Paulínia/SP (06/2019 - 03/2022)_**")
    st.write("""
            - Avaliação, diagnóstico e reabilitação de pacientes ortopédicos e dor crônica
            - Desenvolvimento de projetos e trabalho com equipes multi e interdisciplinares do sistema de saúde público
            - Responsável pela criação, gerenciamento e análise de banco de dados do serviço de reabilitação da cidade de Paulínia e seus usuários, 
            orientando políticas públicas de saúde, promovendo direcionamento apropriado para atendimento e cuidado precoce (redução de 50% do tempo
            de espera para avaliação/atendimento), através de processo de triagem e classificação, baseada em dados epidemiológicos e estatística 
            local e implementação de atendimentos em grande escala (aumento de 20% de capacidade de atendimento).
    """)
    
    st.subheader("")
    st.subheader("**_FISIOTERAPEUTA - Autônomo (01/2014 - 2022)_**")
    st.write("""
             - Atendimento em clínica e domiciliar em ortopedia e traumatologia (pré e pós operatório).
             - Experiência em reabilitação e cuidado ao idoso.
             - Atenção e manejo da dor em pacientes com dor crônica.
    """)
    
    st.subheader("")
    st.subheader("**_PESQUISADOR - UNICAMP (01/2017 - 08/2019)_**")
    st.write("""
             - Atendimento e coleta de dados dos usuários do ambulatório de reabilitação do hospital de clínica
             - Gerenciamento e análise (descritiva e inferencial) de dados do setor e projetos associados
             - 2 anos de experiência em otimização de fluxo de pacientes, coleta e armazenamento de dados para fins de pesquisa clínica/acadêmica.
    """)
    
    st.header("")
    st.header("**Educação**")
    st.subheader("**_CIÊNCIA DE DADOS & MACHINE LEARNING - TERA Ensino Superior (09/2022 - 07-2023)_**")
    st.write("""
             Aprofundamento em:
            - Banco de dados
            - Análise e visualização de dados
            - Computação paralela e distribuída (Databricks/Spark)
            - Pipelines
            - Modelos supervisionados
            - Modelos não supervisionados 
            - Inteligência artificial (IA)
            - Deployment de projetos
    """)
    
    st.subheader("")
    st.subheader("**_MESTRADO - UNICAMP (01/2017 - 08/2019)_**")
    st.write("""
             - Metodologia de pesquisa cientifica, didática acadêmica 
             - Análise estatística: descritiva e inferencial para produção científica
             - Implementação e gerenciamento de banco de dados para usuários do sistema de saúde do setor de reabilitação 
             - Análise descritiva e inferencial para trabalhos acadêmicos
             - Experiencia em coleta, gerenciamento, limpeza, análise e visualização de dados, estatística descritiva e testes de hipótese - correlações, 
             regressão linear/logística (simples/múltipla), modelos não lineares, teste chi-quadrado, paramétricos (teste t, ANOVA) e não paramétricos.
             """)
    
    st.subheader("")
    st.subheader("**_FISIOTERAPIA - PUCCAMP (01/2009 - 12/2013)_**")
    st.write("""
             - Iniciação científica: coleta, análise de dados e produção científica em linha de pesquisa de variabilidade cardíaca
             - Monitor de disciplinar cinesioterapia, anatomia e neuroanatomia
    """)

with tab3:
    st.subheader("")
    col1, col2, col3, col4, col5 = st.columns([3, 0.5, 3, 0.5, 3])
    col1.write("NLP | Webscraping")
    image1 = Image.open("data/o_mundo_assombrado.png")
    col1.image(image1, use_column_width=True)
    with col1:
        link1 = "https://github.com/Bruno-Donato/nlp_reviews_livro/blob/main/nlp_reviews_o_mundo_assombrado.ipynb"
        text1 = "Análise de Reviews - Carl Sagan"
        markdown1 = f'<a href="{link1}" target="_blank">{text1}</a>'
        st.markdown(markdown1, unsafe_allow_html=True)
    
    col3.write("Análise estatística | Webscraping")
    image3 = Image.open("data/artigos_fisio.png")
    col3.image(image3, use_column_width=True)
    with col3:
        link3 = "https://bruno-donato-artigosfisio-pedro.streamlit.app/"
        text3 = "Produção científica na fisioterapia - PEDro"
        markdown3 = f'<a href="{link3}" target="_blank">{text3}</a>'
        st.markdown(markdown3, unsafe_allow_html=True)
    
    col5.write("Modelos de classificação")
    image5 = Image.open("data/fraude2.jpg")
    col5.image(image5, use_column_width=True)
    with col5:
        link5 = "https://github.com/Bruno-Donato/classificacao_desafio_tera/blob/main/desafio_classificacao.ipynb"
        text5 = "Detecção de Fraudes - Desafio TERA"
        markdown5 = f'<a href="{link5}" target="_blank">{text5}</a>'
        st.markdown(markdown5, unsafe_allow_html=True)

    st.write("")
    
    col6, col7, col8, col9, col10 = st.columns([3, 0.5, 3, 0.5, 3])
    col6.write("Análise descritiva | NLP | Webapp deploy")
    image6 = Image.open("data/dashboard_loja.png")
    col6.image(image6, use_column_width=True)
    with col6:
        link6 = "https://bruno-donato-loja-virtual-instrumentos-musicais.streamlit.app/"
        text6 = "Dashboard loja virtual - Projeto Real"
        markdown6 = f'<a href="{link6}" target="_blank">{text6}</a>'
        st.markdown(markdown6, unsafe_allow_html=True)

    
with tab4:
    col1, col2, col3 = st.columns([0.5, 3, 5])
    col2.subheader("O que é ciência de dados?")
    image = Image.open("data/zeca_dados.jpg")
    col2.image(image, use_column_width=True)
    
    col3.header("")
    col3.header("")
    col3.write("""
               Primeiro de uma série e posts que tem como objetivo explicar a ciência de dados de maneira acessível 
               e desmistificada, com foco naqueles que assim como eu querem ou estão fazendo transição de carreira
               """)
    with col3:
        link = "https://medium.com/p/9b71108b6060"
        text = "Leia o post"
        markdown = f'<a href="{link}" target="_blank">{text}</a>'
        st.markdown(markdown, unsafe_allow_html=True)
    