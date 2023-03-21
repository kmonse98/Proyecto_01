from fastapi import FastAPI
import pandas as pd

app = FastAPI(title='Streaming',
              description='Proyecto Individual 01 - HENRY',
              version='1.0.1')

@app.get('/')
async def read_root():
    return {'Mi primera API'}
    
@app.on_event('startup')
async def startup():
    global movie_df
    movie_df = pd.read_csv('movie_set.csv') 

@app.get('/')
async def index():
    return {'Mi primera API (Monse Castillo)'}

@app.get('/about/')
async def about():
    return {'Primer Proyecto Individual de Data Science'}

# Devuelve la película o serie con duración máxima de acuerdo a las diferentes plataformas
@app.get('/get_max_duration/({year}, {platform}, {min_o_season})')
async def get_max_duration(anio:int,plataforma:str,min_o_season:str):
    #colocamos dentro de una variable llamada result, el resultado de buscar un año y la plataforma
    movie_df_filtrado = movie_df[(movie_df['release_year']==anio) & (movie_df['Plataforma']==plataforma)]
    #ahora dentro del if, la función toma en cuenta si se ingresa como parámetro la palabra "min" o "seasons", para ver si se quiere buscar una serie o una película
    if min_o_season == 'min':
    #dentro de a se va guardando en resultado maximo de la columna correspondiente a min, lo cual va llenando una lista para luego devolver la de mayor duración en esa plataforma y en ese año
        a = movie_df_filtrado['duration_int'].max()
        name = movie_df_filtrado[movie_df_filtrado['duration_int']==a] ['title']
        name = name.to_list()
        name = name[0]
    else:
        a = movie_df_filtrado['season'].max()
        #dentro de a se va guardando en resultado maximo de la columna correspondiente a seasons, lo cual va llenando una lista para luego devolver la de mayor duración en esa plataforma y en ese año
        name = movie_df_filtrado[movie_df_filtrado['season']==a] ['title']
        name = name.to_list()
        name = name[0]
    return name

# Devuelve la cantidad de películas con más de cierto puntaje por plataforma y año
@app.get('/get_score_count/({platform}, {score}, {year})')
def get_score_count(platform:str, score:float, year:int):
    # Filtramos el data frame 'movie_df' por plataforma y año
    movie_df_filtro1 = movie_df[(movie_df['release_year']==year) & (movie_df['Plataforma']==platform)]
    # Filtramos por score y asignamos la cantidad de peliculas a la variable 'cantidad'
    cantidad = movie_df_filtro1[(movie_df_filtro1['score(prom)'] > score)].shape[0]
    
    return cantidad

# Devuelve la cantidad de películas por plataforma
@app.get('/get_count_platform/({platform})')
def get_count_platform(platform:str):
    cantidad_pelis = movie_df[movie_df['Plataforma'] == platform].shape[0]

    return cantidad_pelis

# Devuelve el actor más frecuente por plataforma y año
@app.get('/get_actor/({platform},{year})')
def get_actor(platform:str, year:int):
    movie_df_filtro1 = movie_df[(movie_df['release_year']==year) & (movie_df['Plataforma']==platform)]
    
    l = movie_df_filtro1.shape[0] 

    lista_cast = []
    for i in range(0,l):
        lista = movie_df_filtro1['cast'].iloc[i].split(',')
        for elemento in lista:
            lista_cast.append(elemento)

    actor = max(lista_cast, key=lista_cast.count) 

    return actor


