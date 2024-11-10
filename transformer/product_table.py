import pandas as pd
from pathlib import Path

# Define la ruta base del proyecto
project_root = Path(__file__).resolve().parent.parent  # Cambia la profundidad según tu estructura de carpetas

# Define la ruta del archivo de entrada y salida
input_path = project_root / 'data' / 'product_table_raw.csv'
output_path = project_root / 'data' / 'cleaned' / 'product_table_processed.csv'

# Imprime las rutas para verificar
print("\n\n\n\n Ruta de entrada:", input_path,"\n\n\n\n")
print("\n\n\n\n Ruta de salida:", output_path,"\n\n\n\n")

# Cargar el archivo CSV
df = pd.read_csv(input_path, encoding='latin1')

# Crear una lista para almacenar los nuevos datos
data = []

# Iterar sobre cada fila del DataFrame
for _, row in df.iterrows():
    product_id = row['product_id']
    product_name = row["product_name"]
    category_1 = row["category_1"]
    category_2 = row["category_2"]
    category_3 = row["category_3"]
    category_4 = row["category_4"]
    category_5 = row["category_5"]
    discounted_price = row["discounted_price"]
    actual_price = row["actual_price"]
    discount_percentage = row["discount_percentage"]
    rating = row["rating"]
    rating_count = row["rating_count"]
    about_product = row["about_product"]
    img_link = row["img_link"]
    product_link = row["product_link"]
    if pd.notna(product_id) and pd.notna(product_name) and pd.notna(category_1) and pd.notna(category_2) and pd.notna(category_3) and pd.notna(category_4) and pd.notna(category_5) and pd.notna(discounted_price) and pd.notna(actual_price) and pd.notna(discount_percentage) and pd.notna(rating) and pd.notna(rating_count) and pd.notna(about_product) and pd.notna(img_link) and pd.notna(product_link):
        data.append([product_id, product_name, category_1, category_2, category_3, category_4, category_5, discounted_price, actual_price, discount_percentage, rating, rating_count, about_product, img_link, product_link])

# Crear un nuevo DataFrame con los datos combinados
result_df = pd.DataFrame(data, columns=["product_id","product_name","category_1","category_2","category_3","category_4","category_5","discounted_price","actual_price","discount_percentage","rating","rating_count","about_product","img_link","product_link"])

# Crear la carpeta de salida si no existe
output_path.parent.mkdir(parents=True, exist_ok=True)

# Guardar el resultado en un nuevo archivo CSV
result_df.to_csv(output_path, index=False)
