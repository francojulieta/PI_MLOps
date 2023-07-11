# MLOps Engineer

  

![Machine Learning](https://img.freepik.com/premium-vector/machine-learning-banner-web-icon-set-data-mining-algorithm-neural-network_35632-107.jpg?w=2000)
  
## Contexto:

El ciclo de vida de un proyecto de Machine Learning debe contemplar desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.

![MLOPS](https://raw.githubusercontent.com/HX-PRomero/PI_ML_OPS/main/src/DiagramaConceptualDelFlujoDeProcesos.png)
  

## Introducción:

  

Este es mi primer proyecto individual del bootcamp de Data Science de SoyHenry. En este proyecto, he trabajado en el proceso ETL (Extracción, Transformación, Carga), seguido del análisis exploratorio de datos (EDA) y, por último, he desarrollado una API para realizar consultas y crear un sistema de recomendación de películas.

  

Durante el proceso ETL, me encargué de extraer los datos necesarios, transformarlos para que estuvieran en el formato adecuado y cargarlos en un formato que permitiera un fácil manejo y análisis posterior.

  

Luego, realicé un análisis exploratorio de los datos (EDA) para comprender mejor las características de los datos, identificar patrones, tendencias y posibles relaciones entre variables. Esto me ayudó a obtener información valiosa y a generar insights para el proyecto.

  

Finalmente, desarrollé una API que permite realizar consultas a la base de datos y también implementé un sistema de recomendación de películas. Este sistema utiliza técnicas de procesamiento de lenguaje natural (NLP) y modelado de temas para ofrecer recomendaciones personalizadas basadas en los gustos del usuario.

  

Durante todo el proyecto, he aplicado diversas técnicas y habilidades aprendidas en SoyHenry, y he buscado generar un producto final que sea útil y efectivo en la recomendación de películas a los usuarios.

  

## Objetivo:

  

 - Requerimientos específicos en el ETL

  

 - Análisis más profundos a través del EDA

  

 - Funciones que se consumirán en una API

  

 - Objetivo principal del proyecto: realización de un sistema de
   recomendación de películas

  

 - Disponibilizar los datos utilizando el framework FastAPI

  
  

## Tecnologías utilizadas:

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)

  
  
  

## ETL

  
  

Transformaciones solicitadas:

  

 - Desanidar datos en las columnas que contengas diccionarios o listas
   de diccionarios en sus campos y unirlos al dataset.
 - Los valores nulos de los campos revenue, budget deben ser rellenados
   por el número 0.
 - Los valores nulos del campo release date deben eliminarse.
 - De haber fechas, deberán tener el formato AAAA-mm-dd, además deberán
   crear la columna release_year donde extraerán el año de la fecha de
   estreno.
 - Crear la columna con el retorno de inversión, llamada return con los
   campos revenue y budget, dividiendo estas dos últimas revenue /
   budget, cuando no hay datos disponibles para calcularlo, deberá tomar
   el valor 0.
 - Eliminar las columnas que no serán utilizadas,
   video,imdb_id,adult,original_title,poster_path y homepage.

  
  
  

## EDA

  

En el análisis exploratorio de datos (EDA), se continuó examinando las columnas restantes:

  

 - Se eliminaron los duplicados de la columna "id".
 - Se analizaron las columnas que contenían valores nulos, y se tomaron
   acciones como rellenar los valores faltantes o eliminar las filas
   correspondientes.
 - Se realizaron modificaciones en los tipos de datos de las columnas
   según fuera necesario.
 - Se eliminaron las columnas que no eran relevantes para el análisis.
 - Se generaron gráficas para obtener un conocimiento más profundo de
   las películas en el dataset, incluyendo:
	 - Meses y años con mayor cantidad de estrenos.
	 - Duración promedio de las películas, considerando la presencia de
	   documentales y series con varios capítulos en el dataset.
	 - Porcentaje de películas por género.
	 - Se crearon listas con las películas mejor calificadas, las más
	   rentables, los actores con mayor presencia en películas y los
	   directores con mayor cantidad de películas estrenadas.

  

## Funciones y Sistema de recomendación

  

En la etapa final de este proyecto, desarrollamos un sistema de recomendación de películas utilizando el dataset limpio. Para ello, utilizamos las palabras clave presentes en la columna "overview" de las películas. Utilizamos la técnica de similitud de coseno para buscar coincidencias en las palabras y así poder realizar recomendaciones precisas.

  

Sin embargo, la columna "overview" no fue el único factor considerado en nuestro sistema de recomendación. También tuvimos en cuenta la columna de géneros de las películas. De esta manera, pudimos combinar ambos aspectos para generar recomendaciones más precisas y personalizadas.

  

El funcionamiento del sistema es el siguiente: a partir de una película seleccionada o ingresada por el usuario, utilizamos su descripción y género para buscar películas similares en términos de contenido y temática. El sistema devuelve un conjunto de cinco películas recomendadas, cada una con su año de lanzamiento y duración.

  

Este enfoque nos permitió ofrecer recomendaciones que tienen una alta probabilidad de ser relevantes y atractivas para los usuarios, ya que se basan en aspectos clave de las películas como su contenido y género.

  

Además, es importante destacar que todas las API desarrolladas en este proyecto están normalizadas. Esto garantiza que no haya problemas al realizar consultas y que la interacción con las API sea sencilla y sin complicaciones.

  

## Deploy

  

Todo lo mencionado anteriormente se realizó en un archivo de Jupyter Notebook en VSCODE pero para la ejecución de las Apis requeridas se utilizó un archivo .py ya que es lo que se requiere para poder hacer el deploy correctamente.

  

Se empleó FastAPI para desarrollar las APIs, el cual es un framework moderno y de alto rendimiento para la creación de aplicaciones web en Python.

  

Una vez que el archivo .py se encontró listo, se utilizó Render para poner en funcionamiento las APIs de forma segura y accesible desde cualquier lugar. Render proporciona un entorno confiable para ejecutar aplicaciones web, lo que permite que las APIs estén disponibles para su uso público y brinda respuestas en tiempo real.

  

# ....

  

Link:

  

# Video

  

Link

  

# Cierre