import pandas as pd
from pathlib import Path

# Define la ruta base del proyecto
project_root = Path(__file__).resolve().parent.parent  # Cambia la profundidad según tu estructura de carpetas

# Define la ruta del archivo de entrada y salida
input_path = project_root / 'data' / 'user_table_raw.csv'
output_path = project_root / 'data' / 'cleaned' / 'user_table.csv'

# Imprime las rutas para verificar
print("\n\n\n\n Ruta de entrada:", input_path,"\n\n\n\n")
print("\n\n\n\n Ruta de salida:", output_path,"\n\n\n\n")

# Cargar el archivo CSV
df = pd.read_csv(input_path, encoding='latin1')

# Crear una lista para almacenar los nuevos datos
data = []

# Iterar sobre cada fila del DataFrame
for _, row in df.iterrows():
    # Iterar sobre los review_id, review_title y review_content
    for i in range(1, 9):
        user_id = row.get(f"user_id.{i}",None)
        user_name = row.get(f'user_name.{i}', None)
        if pd.notna(user_id) and pd.notna(user_name):
            data.append([ user_id, user_name])

# Crear un nuevo DataFrame con los datos combinados
result_df = pd.DataFrame(data, columns=["user_id", 'user_name'])

# Crear la carpeta de salida si no existe
output_path.parent.mkdir(parents=True, exist_ok=True)

# Guardar el resultado en un nuevo archivo CSV
result_df.to_csv(output_path, index=False)
