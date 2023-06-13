# PI_MLOps
Primer proyecto individual de Data Science



En este archivo de instrucciones, encontrarás toda la documentación necesaria para utilizar la API que se ha desarrollado según los requerimientos solicitados.

Contexto del proyecto:
El proyecto se basa en un conjunto de datos de la industria cinematográfica que abarca películas producidas desde 1874 hasta 2020. Este conjunto de datos proporciona información relevante como fechas de lanzamiento, presupuestos, recaudaciones, duración, puntuación, productoras y más. Con esta valiosa información, es posible realizar análisis y exploraciones de datos para descubrir tendencias y patrones en la industria cinematográfica.

Desafíos enfrentados:
El proceso de extracción, transformación y carga de datos (ETL) puede ser un desafío, especialmente cuando se trata de archivos con estructuras complejas, como JSON. En el caso particular de este conjunto de datos cinematográficos, uno de los desafíos más importantes fue manejar las columnas anidadas en formato JSON, las cuales requerían una limpieza y un preprocesamiento cuidadoso. Además, la presencia de numerosos valores nulos y formatos de datos inadecuados también representaron desafíos adicionales que requirieron soluciones creativas.

Se han completado los siguientes objetivos:

Proceso de ETL.
Análisis exploratorio de los datos.
Implementación de la API.

Endpoints de la API:
La API cuenta con los siguientes endpoints:

► Cantidad de películas estrenadas en un mes.
► Cantidad de películas estrenadas en un día.
► Título, año de estreno y puntuación de una película específica.
► Título, cantidad de votos y valor promedio de votación de una película con al menos 2000 valoraciones.
► Nombre de un actor, su éxito medido por el retorno de inversión, cantidad de películas en las que ha participado y promedio de retorno de inversión.
► Nombre de un director, su éxito medido por el retorno de inversión, lista de películas en las que ha participado con la fecha de lanzamiento, retorno de inversión individual, costo y ganancia de cada una.
► Sistema de recomendación de películas similares.

Deployment:
Para implementar esta aplicación, se utilizó FastAPI y RENDER.

Para la realización de es
