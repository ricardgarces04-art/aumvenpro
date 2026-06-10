import os
import pandas as pd
import plotly.express as px

# Código Senior para levantar gráficos interactivos premium
print("🚀 Encendiendo el Motor de Gráficos de AUMVEN Pro...")

# Datos simulados de tus primeros almacenes para la prueba gráfica de hoy
datos = {
    'Local': ['Cariñitos Box', 'Nony', 'Restoran Nony', 'Xl Sandwichs'],
    'Juegos Totales': [0, 0, 0, 0],
    'Utilidad ($)': [50000, 0, 0, 0]
}

df = pd.DataFrame(datos)

# Crear un gráfico de barras interactivo con Plotly
fig = px.bar(df, x='Local', y='Utilidad ($)', color='Local',
             title='📊 Dashboard Gerencial - Utilidades en Vivo por Sucursal (AUMVEN)',
             text_auto='.2s', template='plotly_dark')

fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
fig.show()
