# Sistema de Busca Semântica com Google Generative AI Descrição

Este repositório contém um exemplo de sistema de busca semântica simples construído com o Google Generative AI Studio. O sistema utiliza embeddings de texto para encontrar o documento mais relevante para uma determinada consulta.


## Instalação

1. Clonar o repositório:
git clone https://github.com/seu-usuario/seu-repositorio.git

2. Instalar as dependências:
pip install -r requirements.txt

3. Configuração:
    1. Obter uma chave de API do Google Cloud:
    2. Acesse o Google Cloud Console.
    3. Crie um projeto ou selecione um existente.
    4. Ative a API Generative AI.
    5. Crie uma chave de API.

4. Definir a chave de API no código:
GOOGLE_API_KEY = "SUA_CHAVE_DE_API"  # Substitua pela sua chave
genai.configure(api_key=GOOGLE_API_KEY)

5. Uso:
Executar o script principal:
python main.py

6. Inserir a consulta:
O programa irá solicitar que você digite a consulta.
Visualizar o resultado:
O sistema irá retornar o conteúdo do documento mais relevante para a sua consulta.
Exemplo
**Consulta:** Como trocar marchas em um Google Car?

**Resultado:** 
Seu Google Car tem uma transmissão automática. Para mudar de marcha, simplesmente mova a alavanca de câmbio para a posição desejada.
...

7. Tecnologias Utilizadas
Google Generative AI Studio: Para gerar embeddings de texto.
Python: Linguagem de programação.
Bibliotecas:
google.generativeai
pandas
numpy
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.



