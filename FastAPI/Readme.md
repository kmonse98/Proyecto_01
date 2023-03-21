## Descripción de la FastAPI

Se describirá brevemente las funciones (y sus respectivos argumentos) que usa nuestra FastAPI para ste proyecto 01.

(Tomar en cuenta que las plataformas llevan la siguinte edición: (Amazon, Netflix, Hulu, Disney))

1.- **get_max_duration(anio:int,plataforma:str,min_o_season:str)**

Devuelve la película o serie con duración máxima de acuerdo a las diferentes plataformas, recive de argumentos (año, Plataforma, tipo de duración).
Ejemplo: *get_max_duration(2018, Amazon, min)*

2.- **get_score_count(platform:str, score:float, year:int)**

Devuelve la cantidad de películas con más de cierto puntaje por plataforma y año. Sus argumentos deben ser: (plataforma, Puntaje, Año), el puntaje está entre un rango decimal de 3 a 4 puntos. Ejemplo: *get_score_count(Disney,3.5,2018)*

3.- **get_count_platform(platform:str):**

Retorna la cantidad de películas por plataforma. Solo requiere un argumento que es la plataforma. Ejemplo: get_count_platform(Amazon)

4.- **get_actor(platform:str, year:int)**

Devuelve el actor más frecuente por plataforma y año.Ejemplo: get_actor(Netflix, 2000)
