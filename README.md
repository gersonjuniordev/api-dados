            # API de Processamento de Dados

API RESTful para processamento e análise de grandes volumes de dados.

## Funcionalidades

- Processamento assíncrono de dados
- Cache com Redis
- Processamento em background
- Documentação automática

## Instalação

1. Clone o repositório 
2. Crie um ambiente virtual com Python 3.10
3. Instale as dependências com o comando `pip install -r requirements.txt`
4. Execute o comando `uvicorn app.main:app --reload` para iniciar a API
5. Acesse a documentação interativa em `http://localhost:8000/docs`

## Testes

Para rodar os testes, execute o comando `pytest`

## Documentação

A documentação automática está disponível em `http://localhost:8000/docs`

## Contribuição

Contribuições são bem-vindas! Por favor, abra uma issue ou um pull request para discutir melhorias.

Não esqueça de configurar o arquivo `.env` com as variáveis de ambiente necessárias, Redis_URL e REDIS_URL.

