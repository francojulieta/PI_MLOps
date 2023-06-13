from fastapi import FastAPI
import uvicorn
import pandas as pd

df_movies = pd.read_csv("Movies_EDA.csv", sep=",")

app = FastAPI()


@app.get("/")
async def root():
    return {"Recomendación de películas"}


# Endpoints

# Cantidad de películas estrenadas en un mes
@app.get("/Peliculas/mes/{mes}")
async def cantidad_filmaciones_mes(mes):
    # Implementación de la función cantidad_filmaciones_mes aquí
    return cantidad_filmaciones_mes(mes)

# Cantidad de filmaciones estrenadas en un día
@app.get("/Peliculas/dia/{dia}")
async def cantidad_filmaciones_dia(dia):
    # Implementación de la función cantidad_filmaciones_dia aquí
    return cantidad_filmaciones_dia(dia)

# Título, año de estreno y score de la película ingresada
@app.get("/Peliculas/score/{titulo_de_la_filmacion}")
async def score_titulo(titulo_de_la_filmacion:str):
    # Implementación de la función score_titulo aquí
    return score_titulo(titulo_de_la_filmacion)

# Título, cantidad de votos y valor promedio de las votaciones. La misma deberá contar con al menos 2000 valoraciones
@app.get("/Peliculas/votos/promedio votaciones/{titulo_de_la_filmacion}")
async def votos_titulo(titulo_de_la_filmacion):
    # Implementación de la función votos_titulo aquí
    return votos_titulo(titulo_de_la_filmacion)

# Nombre de actor, éxito del mismo medido a través del retorno, cantidad de películas en las que participó y promedio de retorno
@app.get("/Actor/retorno/cantidad peliculas/promedio retorno/{nombre_actor}")
async def get_actor(nombre_actor):
    # Implementación de la función get_actor aquí
    return get_actor(nombre_actor)

# Nombre de director, éxito del mismo medido a través del retorno, nombre de cada película en la que participó con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma
@app.get("/Director/retorno/pelicula/fecha lanzamiento/retorno/costo/ganancia/{nombre_director}")
async def get_director(nombre_director):
    # Implementación de la función get_director aquí
    return get_director(nombre_director)

# Sistema de recomendación de películas
@app.get("/Pelicula/año/duracion/{title}")
async def recommend_movies(title):
    # Implementación de la función recommend_movies aquí
    return recommend_movies(title)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
