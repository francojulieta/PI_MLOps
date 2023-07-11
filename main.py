from fastapi import FastAPI
import uvicorn
import pandas as pd
from unidecode import unidecode 
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fastapi.encoders import jsonable_encoder

app = FastAPI()

df = pd.read_csv("Movies_EDA.csv", sep=",")

@app.get("/")
async def root():
    return {"Recomendación de películas"}


# Endpoints

# 1. Cantidad de películas producidas por idioma
@app.get('/Idioma/{Idioma}')
def idiomas_peliculas(idioma: str):
    idiomas = df[df['lenguages_names'].apply(lambda x: idioma in x)]
    total = len(idiomas)
    return {"Idioma": idioma, "Total de películas": total}

# 2. Duración y año de la película ingresada
@app.get('/Duración/{Duración}')
def peliculas_duracion(pelicula):
    pelicula_busqueda = pelicula.lower()
    pelicula_filtrada = df[df['title'].str.lower() == pelicula_busqueda]
    if len(pelicula_filtrada) > 0:
        duracion = pelicula_filtrada['runtime'].iloc[0].item()
        año = pelicula_filtrada['release_year'].iloc[0].item()
        return {"Película": pelicula, "Duración": duracion, "Año": año}
    else:
        return f"No se encontró información para la película: {pelicula}"
    
# 3. Cantidad de películas por franquicia, ganancia total y promedio
@app.get('/Franquicia/{Franquicia}')
def franquicia(Franquicia: str):
    franquicia_busqueda = Franquicia.lower()
    franquicia_filtrada = df[df['name_collection'].str.lower().str.contains(franquicia_busqueda)]
    
    cantidad_peliculas = len(franquicia_filtrada)
    ganancia_total = round(franquicia_filtrada['return'].sum(), 2)
    promedio_ganancia = round(franquicia_filtrada['return'].mean(), 2)
    
    return {"Franquicia": Franquicia, "Cantidad de películas": cantidad_peliculas, "Ganancia total": ganancia_total, "Promedio de ganancia": promedio_ganancia}
    
# 4. Cantidad de películas producidas por país
@app.get('/País/{País}')
def peliculas_pais(Pais: str):
    pais_busqueda = Pais.lower()
    peliculas_producidas = df[df['countries_names'].str.lower().str.contains(pais_busqueda)]
    cantidad_peliculas = len(peliculas_producidas)
    return {"País": Pais, "Cantidad de películas producidas": cantidad_peliculas}

# 5. Cantidad de películas por productora y revenue del mismo
@app.get('/Productora/{Productora}')
def productoras_exitosas(Productora: str):
    productora_busqueda = Productora.lower()
    productora_filtrada = df[df['companies_names'].str.lower().str.contains(productora_busqueda)]
    
    cantidad_peliculas = len(productora_filtrada)
    revenue_total = productora_filtrada['revenue'].sum()
    
    return {"Productora": Productora, "Cantidad de películas realizadas": cantidad_peliculas, "Revenue total": revenue_total}

# 6. Nombre de director, éxito del mismo medido a través del retorno, nombre de cada película en la que participó con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.
@app.get('/Director/{Director}')
def get_director(nombre_director):
    resultados = []
    
    for index, row in df.iterrows():
        director = row['director']
        if isinstance(director, str) and nombre_director.lower() == director.lower():
            titulo = row['title']
            fecha_lanzamiento = pd.to_datetime(row['release_date']).date()
            retorno = round(row['return'], 2)
            costo = int(row['budget'])
            ganancia = int(row['revenue'])
            
            resultado = {
                "Película": titulo,
                "Fecha de lanzamiento": fecha_lanzamiento,
                "Retorno": retorno,
                "Costo": costo,
                "Ganancia": ganancia
            }
            
            resultados.append(resultado)
    
    if len(resultados) == 0:
        resultados = "No se encontró al director especificado."

    return resultados

# 7. Sistema de recomendación
def normalize_text(text):
    if isinstance(text, str):
        text = unidecode(text.lower())
    else:
        text = text.apply(lambda x: unidecode(x.lower()))
    return text
@app.get('/Recomendación/{Pelicula}')
def recommend_movies(title):
    title = normalize_text(title)
    movie = df[normalize_text(df['title'].apply(normalize_text)) == title]
    
    if len(movie) == 0:
        return "No se encontró la película en la base de datos."

    index = movie.index[0]
    overview = df.loc[index, 'overview']
    genre = df.loc[index, 'genres_names']

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['overview'])

    overview_similarities = cosine_similarity(tfidf_matrix[index], tfidf_matrix).flatten()

    similar_movies_indices = overview_similarities.argsort()[::-1]

    similar_movies = df.loc[similar_movies_indices]
    similar_movies = similar_movies[similar_movies['genres_names'].str.contains(genre)].head(6)
    similar_movies = similar_movies[similar_movies.index != index]
    similar_movies['runtime'] = similar_movies['runtime'].astype(int)
    similar_movies['release_year'] = similar_movies['release_year'].astype(int)
    similar_movies['runtime'] = similar_movies['runtime'].astype(str) + ' min'
    
    return similar_movies[['title', 'release_year', 'runtime']].to_dict(orient='records')
