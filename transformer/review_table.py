import csv

# Función para dividir el texto de una columna en 8 partes
def split_into_8_parts(review_text):
    parts = review_text.split(',')
    final_parts = []
    temp = []

    # Procesar cada parte para agruparlas hasta obtener 8 elementos finales
    for part in parts:
        temp.append(part.strip())  # Agregar a un temporal
        
        # Si llegamos a tener 7 elementos en final_parts o si es el último elemento, unimos el resto
        if len(final_parts) < 7:
            final_parts.append(', '.join(temp))
            temp = []
        elif len(final_parts) == 7:  # Para el último grupo, unimos todo lo que quede en temp
            final_parts.append(', '.join(temp + parts[parts.index(part)+1:]))
            break
    
    # Retornar las 8 partes como una lista
    return final_parts

# Leer el archivo CSV y procesar cada fila
with open('./data/review_table_raw.csv', 'r', newline='', encoding='latin1') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Preparar encabezados para el nuevo archivo, incluyendo las 8 partes de cada columna
    fieldnames = list(reader.fieldnames) + [f'review_title_part_{i}' for i in range(1, 9)] + [f'review_content_part_{i}' for i in range(1, 9)]
    
    # Crear el archivo CSV de salida
    with open('./data/cleaned/review_table_processed.csv', 'w', newline='', encoding='latin1') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            # Dividir 'review_title' y 'review_content' en 8 partes cada uno
            title_parts = split_into_8_parts(row['review_title'])
            content_parts = split_into_8_parts(row['review_content'])
            
            # Agregar las partes a la fila original
            for i in range(8):
                row[f'review_title_part_{i+1}'] = title_parts[i] if i < len(title_parts) else ''
                row[f'review_content_part_{i+1}'] = content_parts[i] if i < len(content_parts) else ''
            
            # Escribir la fila procesada en el archivo de salida
            writer.writerow(row)
