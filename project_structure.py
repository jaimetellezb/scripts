import os

def generate_project_structure(folder, output_file):
    def recorrer(path, prefix=''):
        # Obtener lista de carpetas y archivos, excluyendo carpetas no deseadas inician con . y __pycache__
        elements = sorted(os.listdir(path))
        elements = [e for e in elements if os.path.isdir(os.path.join(path, e)) and not e.startswith('.') and e != '__pycache__'] + \
                    [e for e in elements if os.path.isfile(os.path.join(path, e))]

        total = len(elements)
        for index, file_name in enumerate(elements):
            complete_path = os.path.join(path, file_name)
            is_last = (index == total - 1)
            if os.path.isdir(complete_path):
                f.write(f'{prefix}{"└── " if is_last else "├── "}{file_name}/\n')
                # Recorrer subdirectorios, ajustando el prefijo
                new_prefix = prefix + ("    " if is_last else "│   ")
                recorrer(complete_path, new_prefix)
            else:
                f.write(f'{prefix}{"└── " if is_last else "├── "}{file_name}\n')

    with open(output_file, 'w') as f:
        recorrer(folder)

# Usar la carpeta actual en la que se encuentra el script
root_folder = os.path.dirname(os.path.abspath(__file__))
output_file = 'tree.txt'

generate_project_structure(root_folder, output_file)
