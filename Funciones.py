<<<<<<< HEAD
import pandas as pd
import unicodedata
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from unidecode import unidecode

df = pd.read_csv("Movies_EDA.csv", sep=",")

# API 1

df['release_date'] = pd.to_datetime(df['release_date'])

def cantidad_filmaciones_mes(mes):
    df_mes = df[df['release_date'].dt.month_name(locale='es').str.lower() == mes.lower()]
    cantidad = len(df_mes)
    return f"Cantidad: {cantidad}\nMes: {mes.capitalize()}"

# API 2

def remover_acentos(texto):
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    texto_sin_acentos = ''.join(c for c in texto_normalizado if not unicodedata.combining(c))
    return texto_sin_acentos

def cantidad_filmaciones_dia(dia):
    dia_normalizado = remover_acentos(dia)
    df_dia = df[df['release_date'].dt.day_name(locale='es').str.lower().str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8') == dia_normalizado.lower()]
    cantidad = len(df_dia)
    return f"Día: {dia.capitalize()}\nCantidad de filmaciones: {cantidad}"

# API 3

def score_titulo(titulo_de_la_filmacion):
    titulo_busqueda = titulo_de_la_filmacion.lower()
    df_filmacion = df[df['title'].str.lower() == titulo_busqueda]
    
    if len(df_filmacion) == 0:
        return "No se encontró la filmación especificada."
    
    titulo = df_filmacion['title'].values[0]
    año_estreno = df_filmacion['release_year'].values[0]
    score = round(df_filmacion['popularity'].values[0], 2)
    
    return f"Película: {titulo}\nAño de estreno: {año_estreno}\nPuntuación: {score}"

# API 4

def votos_titulo(titulo_de_la_filmacion):
    df_filmacion = df[df['title'] == titulo_de_la_filmacion]
    
    if len(df_filmacion) == 0:
        return "No se encontró la filmación especificada."
    
    titulo = df_filmacion['title'].values[0]
    cantidad_votos = int(df_filmacion['vote_count'].values[0])
    promedio_votos = round(df_filmacion['vote_average'].values[0], 2)
    año_estreno = df_filmacion['release_year'].values[0]
    
    if cantidad_votos < 2000:
        return "La película no cumple con la condición de tener al menos 2000 valoraciones."
    
    return f"Película: {titulo}\nAño de estreno: {año_estreno}\nCantidad de votos: {cantidad_votos}\nPromedio de valoraciones: {promedio_votos}"

# API 5

def get_actor(nombre_actor):
    cantidad_peliculas = 0
    total_retorno = 0

    for index, row in df.iterrows():
        nombres_actores = row['names_actors']
        retorno = row['return']

        if nombre_actor.lower() in nombres_actores.lower():
            cantidad_peliculas += 1
            total_retorno += retorno

    if cantidad_peliculas == 0:
        return "No se encontró al actor especificado."

    promedio_retorno = round((total_retorno / cantidad_peliculas), 2)

    return f"Actor: {nombre_actor}\nParticipación en películas: {cantidad_peliculas}\nPromedio de retorno: {promedio_retorno}"

# API 6

def get_director(nombre_director):
    resultado = ""

    for index, row in df.iterrows():
        director = row['director']
        if isinstance(director, str) and nombre_director.lower() == director.lower():
            titulo = row['title']
            fecha_lanzamiento = pd.to_datetime(row['release_date']).date()
            retorno = round(row['return'], 2)
            costo = int(row['budget'])
            ganancia = int(row['revenue'])
            
            resultado += f"Película: {titulo}\nFecha de lanzamiento: {fecha_lanzamiento}\nRetorno: {retorno}\nCosto: {costo}\nGanancia: {ganancia}\n\n"
    
    if resultado == "":
        resultado = "No se encontró al director especificado."

    return resultado


# API 7

def normalize_text(text):
    if isinstance(text, str):
        text = unidecode(text.lower())
    else:
        text = text.apply(lambda x: unidecode(x.lower()))
    return text

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

=======
import pandas as pd
import unicodedata
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from unidecode import unidecode

df = pd.read_csv("Movies_EDA.csv", sep=",")

# API 1

df['release_date'] = pd.to_datetime(df['release_date'])

def cantidad_filmaciones_mes(mes):
    df_mes = df[df['release_date'].dt.month_name(locale='es').str.lower() == mes.lower()]
    cantidad = len(df_mes)
    return f"Cantidad: {cantidad}\nMes: {mes.capitalize()}"

# API 2

def remover_acentos(texto):
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    texto_sin_acentos = ''.join(c for c in texto_normalizado if not unicodedata.combining(c))
    return texto_sin_acentos

def cantidad_filmaciones_dia(dia):
    dia_normalizado = remover_acentos(dia)
    df_dia = df[df['release_date'].dt.day_name(locale='es').str.lower().str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8') == dia_normalizado.lower()]
    cantidad = len(df_dia)
    return f"Día: {dia.capitalize()}\nCantidad de filmaciones: {cantidad}"

# API 3

def score_titulo(titulo_de_la_filmacion):
    titulo_busqueda = titulo_de_la_filmacion.lower()
    df_filmacion = df[df['title'].str.lower() == titulo_busqueda]
    
    if len(df_filmacion) == 0:
        return "No se encontró la filmación especificada."
    
    titulo = df_filmacion['title'].values[0]
    año_estreno = df_filmacion['release_year'].values[0]
    score = round(df_filmacion['popularity'].values[0], 2)
    
    return f"Película: {titulo}\nAño de estreno: {año_estreno}\nPuntuación: {score}"

# API 4

def votos_titulo(titulo_de_la_filmacion):
    df_filmacion = df[df['title'] == titulo_de_la_filmacion]
    
    if len(df_filmacion) == 0:
        return "No se encontró la filmación especificada."
    
    titulo = df_filmacion['title'].values[0]
    cantidad_votos = int(df_filmacion['vote_count'].values[0])
    promedio_votos = round(df_filmacion['vote_average'].values[0], 2)
    año_estreno = df_filmacion['release_year'].values[0]
    
    if cantidad_votos < 2000:
        return "La película no cumple con la condición de tener al menos 2000 valoraciones."
    
    return f"Película: {titulo}\nAño de estreno: {año_estreno}\nCantidad de votos: {cantidad_votos}\nPromedio de valoraciones: {promedio_votos}"

# API 5

def get_actor(nombre_actor):
    cantidad_peliculas = 0
    total_retorno = 0

    for index, row in df.iterrows():
        nombres_actores = row['names_actors']
        retorno = row['return']

        if nombre_actor.lower() in nombres_actores.lower():
            cantidad_peliculas += 1
            total_retorno += retorno

    if cantidad_peliculas == 0:
        return "No se encontró al actor especificado."

    promedio_retorno = round((total_retorno / cantidad_peliculas), 2)

    return f"Actor: {nombre_actor}\nParticipación en películas: {cantidad_peliculas}\nPromedio de retorno: {promedio_retorno}"

# API 6

def get_director(nombre_director):
    resultado = ""

    for index, row in df.iterrows():
        director = row['director']
        if isinstance(director, str) and nombre_director.lower() == director.lower():
            titulo = row['title']
            fecha_lanzamiento = pd.to_datetime(row['release_date']).date()
            retorno = round(row['return'], 2)
            costo = int(row['budget'])
            ganancia = int(row['revenue'])
            
            resultado += f"Película: {titulo}\nFecha de lanzamiento: {fecha_lanzamiento}\nRetorno: {retorno}\nCosto: {costo}\nGanancia: {ganancia}\n\n"
    
    if resultado == "":
        resultado = "No se encontró al director especificado."

    return resultado


# API 7

def normalize_text(text):
    if isinstance(text, str):
        text = unidecode(text.lower())
    else:
        text = text.apply(lambda x: unidecode(x.lower()))
    return text

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

>>>>>>> 51d236b5805bb3e41c5888b996a9a99dde9b694e
    return similar_movies[['title', 'release_year', 'runtime']]