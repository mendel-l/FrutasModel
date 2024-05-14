import os

def rename_images(data_dir):
    # Definir las categorías y sus nuevas carpetas
    categories = {
        'buen_estado': 'buen_estado',
        'mal_estado': 'mal_estado',
        'estado_inmaduro': 'estado_inmaduro'
    }

    # Recorrer cada categoría y sus archivos
    for old_folder, new_folder in categories.items():
        folder_path = os.path.join(data_dir, old_folder)
        new_folder_path = os.path.join(data_dir, new_folder)
        
        # Cambiar el nombre de la carpeta si es necesario
        if old_folder != new_folder:
            os.rename(folder_path, new_folder_path)
            folder_path = new_folder_path
        
        # Lista de todos los archivos en la carpeta actual
        files = os.listdir(folder_path)
        for i, filename in enumerate(files):
            # Generar un nuevo nombre de archivo
            new_filename = f"{new_folder}_{str(i+1).zfill(3)}.jpg"
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            
            # Renombrar el archivo
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {old_file_path} to {new_file_path}")

# Ruta al directorio de datos, ajustar según sea necesario
data_dir = 'FrutasModelo/data'
rename_images(data_dir)
