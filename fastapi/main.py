from fastapi import FastAPI
import uvicorn

app = FastAPI()

origins = [
    "https://moviesapp-oxeinkhcia-uc.a.run.app",
    "http://localhost",
    "http://localhost:8000",
]
# ### app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )###

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Recomendación de películas"}


# Endpoints

# Cantidad de películas estrenadas en un mes
@app.get("/Peliculas/mes/{mes}")
async def cantidad_filmaciones_mes(mes):
    return cantidad_filmaciones_mes(mes)


# Cantidad de filmaciones estrenadas en un día
@app.get("/Peliculas/dia/{dia}")
async def cantidad_filmaciones_dia(dia):
    return cantidad_filmaciones_dia(dia)


# Título, año de estreno y score de la película ingresada
@app.get("/Peliculas/score/{titulo_de_la_filmacion}")
async def score_titulo(titulo_de_la_filmacion:str):
    return score_titulo(titulo_de_la_filmacion)


# Título, cantidad de votos y valor promedio de las votaciones. La misma deberá contar con al menos 2000 valoraciones
@app.get("/Peliculas/votos/promedio votaciones/{titulo_de_la_filmacion}")
async def votos_titulo(titulo_de_la_filmacion):
    return votos_titulo(titulo_de_la_filmacion)


# Nombre de actor, éxito del mismo medido a través del retorno, cantidad de películas en las que participó y promedio de retorno
@app.get("/Actor/retorno/cantidad peliculas/promedio retorno/{nombre_actor}")
async def get_actor(nombre_actor):
    return get_actor(nombre_actor)


# Nombre de director, éxito del mismo medido a través del retorno, nombre de cada película en la que participó con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma
@app.get("/Director/retorno/pelicula/fecha lanzamiento/retorno/costo/ganancia/{nombre_director}")
async def get_director(nombre_director):
    return get_director(nombre_director)

# Sistema de recomendación de películas
@app.get("/Pelicula/año/duracion/{title}")
async def recommend_movies(title):
    return recommend_movies(title)



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
