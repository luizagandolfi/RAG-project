# Projeto RAG - Ambiental

# Arquitetura
O projeto foi construido utilizando Python, FastAPI (backend) e Html, CSS e Javascript (Frontend);
Como modelos, utilizamos DeepSeek R-1 (GPT) e BGE-M3 (embedding dos documentos).


## Configuração do Arquivo .env

Utilize o arquivo [.env_template](.env-template) como base para a criação do .env 

```bash
cp .env_template .env
```

## Como Executar

1 - Clone o repositório:

```bash
git clone 
```

2 - Instale os requirements (recomendamos criar um venv ou conda-env com python=3.11 ou superior)

```bash
pip install -r requirements.txt
```

3 - Execute no seu terminal o comando para executar o servidor

```bash
uvicorn application_main:app --reload
```

- Caso não tenha os documentos no repositório data/documentos_ambientais, o download dos documentos será efetuado.
- Após o download dos arquivos, a criação do vectordb irá iniciar (esse processo pode levar um tempo)

4 - No navegador, entre em <http://localhost:8000/rag-ambiental> para acessar o front.

Nessa página é possível ser redirecionado para os dois módulos que foram desenvolvidos.

* O **módulo de chat** que é um *Question & Answer* livre sobre escopo leis e legistações brasileiras sobre o tema ambiental.

* O **módulo de formulário** que é um *Question & Answer* com um direcionamento de questões típicas e importantes para avaliações de um projeto voltado para exploração ambiental. O objetivo desse formulário é gerar pontos de atenção sobre projetos, de modo que estejam de acordo com as leis ambientais.


# Vídeo

Link para vídeo de apresentação do projeto:

# Autores
* Álysson Soares
* Luiza Gandolfi 