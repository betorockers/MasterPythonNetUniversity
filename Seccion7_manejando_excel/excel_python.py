# 1. la columna Id debe ser transformada = la primera letra de nombre
# y la ultima letra concatenando con su valor numerico
# ejemplo : JZ1

# 2. la columna nombre debe tener el nombre y el apellido comenzando con mayuscula

# 3. la columna profesion debera estar en mayusculas

# 4. Crear una nueva columna a continuacion de sueldo que sera igual a sueldo - impuesto(20 % del sueldo)
# ejemplo: 200 - 40 = 160

# 5. crear una nueva columna que se llame "indice" que sera una columna autogenerada, numerica y secuencial.
# ejemplo: 
# 1 - Juan Perez, 5 - domingo masias
# esta debe estar antes de la columna id

import pandas as pd

# LEEREMOS EL ARCHIVO EXCEL
data_personas = pd.read_excel('./datos.xlsx')

#print(data_personas.info())

print(data_personas.head())

# 1. Transformar la columna Id
data_personas['Id'] = data_personas['Nombre'].astype(str).str.upper().str[0] +\
                      data_personas['Nombre'].astype(str).str.upper().str[-1] +\
                      data_personas['Id'].astype(str)
                      
# 2. Transformar la columna Nombre
data_personas['Nombre'] = data_personas['Nombre'].astype(str).str.title()

# 3. Transformar la columna Profesion
data_personas['Profesion'] = data_personas['Profesion'].astype(str).str.upper()

# le cambiamos el nombre de la columna Sueldo a Sueldo Bruto
data_personas.rename(columns={'Sueldo': 'Sueldo Bruto'}, inplace=True)

# 4. Crear una nueva columna Sueldo liquido
data_personas['Sueldo Liquido'] = data_personas['Sueldo Bruto'] - (data_personas['Sueldo Bruto'] * 0.2)

# 5. Crear una nueva columna Indice
data_personas['Indice'] = range(1, len(data_personas) + 1)

# Reordenar las columnas para que Indice esté antes de Id
data_personas = data_personas[['Indice', 'Id', 'Nombre', 'Profesion', 'Sueldo Bruto', 'Sueldo Liquido']]

# centremos el valor de la columna indice
data_personas['Indice'] = data_personas['Indice'].astype(str).str.center(20)




data_personas.to_excel('./excel_precesado.xlsx', index=False)