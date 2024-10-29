import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
import re



def preprocess(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = ' '.join(word for word in text.split() if word not in stopwords.words('spanish'))
    return text

def obtener_similitudes_y_cluster(archivo, hojas, columna):
    def leer_respuestas(archivo, hoja):
        df = pd.read_excel(archivo, sheet_name=hoja)
        respuestas = [{'respuesta': texto} for texto in df[columna]]
        return respuestas

    # Inicializar listas para almacenar resultados de ambas hojas
    resultados = []

    # Iterar sobre cada hoja
    for hoja in hojas:
        respuestas_hoja = leer_respuestas(archivo, hoja)
        textos_hoja = [preprocess(respuesta['respuesta']) for respuesta in respuestas_hoja]

        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(textos_hoja)

        def get_similarity_table(query):
            query_vec = vectorizer.transform([preprocess(query)])
            cossim = cosine_similarity(query_vec, X).flatten()

            similarity_table = pd.DataFrame({
                'Respuesta': textos_hoja,
                'Similitud': cossim
            })

            similarity_table = similarity_table.sort_values(by='Similitud', ascending=False)
            return similarity_table

        # Reducción de dimensionalidad con PCA
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X.toarray())

        # Clustering con K-Means
        kmeans = KMeans(n_clusters=3)
        clusters = kmeans.fit_predict(X_pca)

        # Ejemplo de uso
        consulta = input(f"Ingrese palabra o frase para la hoja '{hoja}': ")
        tabla_similitudes = get_similarity_table(consulta)
        print(tabla_similitudes)

        # Grafico
        plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters)
        plt.title(f"Clustering de Respuestas sobre {hoja}")
        plt.xlabel("PCA Componente 1")
        plt.ylabel("PCA Componente 2")
        plt.show()

        # Almacenar resultados para esta hoja
        resultados.append({'hoja': hoja, 'similitudes': tabla_similitudes, 'clusters': clusters})

    return resultados

# Modifica los argumentos según tus necesidades
hojas = ["24HorasTVN", "cooperativa"]
resultados = obtener_similitudes_y_cluster("compilado_MM.CC.xlsx", hojas, "text")

