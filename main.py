# comando para instalar as bibliotecas "python3 -m pip install nome_da_biblioteca"
import requests
import google.generativeai as genai
import numpy as np
import pandas as pd

GOOGLE_API_KEY="AIzaSyCQM-l52J0JZ7arXtbf5XNH03JpagUhg0g"
genai.configure(api_key=GOOGLE_API_KEY)


# Listagem de documentos que serao buscados
DOCUMENT1 = {
    "title": "AUDI A1 1.4, A3 1.6, A4 2.0",
    "content": "Oleo sintetico 5w40 sn 502"}
DOCUMENT2 = {
    "title": "prisma, corsa, onix",
    "content": "Oleo Sintetico 5w30"}
DOCUMENT3 = {
    "title": "Palio, uno, strada",
    "content": "Oleo Sintetico 5w40 rs"}
DOCUMENT4 = {
    "title": "Renegate, compass,",
    "content": "Oleo Sintetico 5w30 c2"
}

documents = [DOCUMENT1, DOCUMENT2, DOCUMENT3, DOCUMENT4]



df = pd.DataFrame(documents)
df.columns = ["Titulo", "Conteudo"]


model ="models/embedding-001"

def embed_fn(title, text):
    return genai.embed_content(model=model, 
                                 content=text,
                                 title=title,
                                 task_type="RETRIEVAL_DOCUMENT")["embedding"]


df["Embeddings"] = df.apply(lambda row: embed_fn(row["Titulo"], row["Conteudo"]), axis=1)

# funcao que faz a pesquisa
def gerar_e_buscar_consulta(consulta, base, model):
    embedding_da_consulta = genai.embed_content(model=model,
                                                content=consulta,
                                                task_type="RETRIEVAL_QUERY")
    
    produtos_escalares = np.dot(np.stack(df["Embeddings"]), embedding_da_consulta["embedding"])

    indice = np.argmax(produtos_escalares)
    return df.iloc[indice]["Conteudo"]

# fazendo consulta
print("========          Troca de Oleo          ========")
print("Para teste somente alguns carros foram inseridos")
consulta = input("Qual o modelo : ")

trecho = gerar_e_buscar_consulta(consulta, df, model)
print(trecho)