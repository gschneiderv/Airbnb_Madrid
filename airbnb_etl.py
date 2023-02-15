
import pandas as pd
import numpy as np

import psycopg2
from sqlalchemy import create_engine#

# Importamos el dataset de los datos de Airbnb, el delimeter marca las separación en columnas. [Extract]
df = pd.read_csv("airbnb-listings.csv", delimiter=";")


# Seleccionamos las columnas que nos servirán para realizar el análisis [Transform]
df_madrid = df.filter(["Host Total Listing", "Street", "Neighbourhood Cleansed","Neighbourhood Group Cleansed","City", "State", "Zipcode", "Smart Location","Country Code","Latitude", "Longitude", "Property Type", "Room Type","Accommodates", "Bathrooms", "Bedrooms", "Beds", "Bed Type", "Amenities","Square Feet", "Price", "Security Deposit", "Cleaning Fee", "Guests Included", "Extra People", "Minimum Nights", "Maximum Nights", "Number of Reviews", "Review Scores Rating", "Cancellation Policy", "Reviews per Month"],axis=1)

# Filtramos los datos por la columna City==Madrid"
# Nos Faltó ver como incluir las palabras "mal escritas",normalizar estos datos. Se probó de utilizar:
#df_airbnb_madrid = df_madrid[df_madrid["City"].str.contains("Madrid", case = False)], pero la presencia de NaN impidió realizar este tipo de filtro.

df_airbnb_madrid = df_madrid[df_madrid["City"] == "Madrid"]

#En el caso que se hubiese utilizado, por ej la columna "Bathrooms", se debería haber pasado del tipo de dato "float" a "integer", para que tuviese sentido.
#df_airbnb_madrid['Bathrooms'] = df_airbnb_madrid['Bathrooms'].astype(pd.Int32Dtype())

#Otra transformación que se puede realizar en este punto es el tratamiento de los NaN pero no quisimos perder datos a la hora de realizar los estudios estadisticos.

#Lo cargamos a la base de datos (postgress)[Load] , quedando ya  disponible para su posterior utilización en el análisis estadístico y visual. 

engine = create_engine('postgresql://usuario:contraseña@trumpet.db.elephantsql.com/Database')
df_airbnb_madrid.to_sql('airbnb_list_complete', engine)

