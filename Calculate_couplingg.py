import os
import ast

def get_python_files(directory):
    """Recursively get all Python files in a directory"""
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

def find_imports(filepath):
    """Parse a Python file and find all imports"""
    with open(filepath, 'r', encoding='utf-8') as file:
        try:
            node = ast.parse(file.read(), filename=filepath)
        except SyntaxError:
            # Skip files with syntax errors (e.g., template files)
            return []
        return [n.names[0].name for n in ast.walk(node) if isinstance(n, ast.Import)]

def calculate_coupling(directory):
    """Calculate the coupling percentage for the given directory"""
    files = get_python_files(directory)
    total_dependencies = 0
    total_possible_dependencies = 0
    all_imports = {}

    for file in files:
        imports = find_imports(file)
        all_imports[file] = imports
        total_dependencies += len(imports)

    total_modules = len(files)
    total_possible_dependencies = total_modules * (total_modules - 1)

    coupling_percent = (total_dependencies / total_possible_dependencies) * 100 if total_possible_dependencies != 0 else 0
    return coupling_percent, all_imports

if __name__ == '__main__':
    project_directory = input("Enter the path to your project directory: ")
    coupling_percent, all_imports = calculate_coupling(project_directory)
    print(f"Coupling Percent: {coupling_percent:.2f}%")

    print("\nModule Dependencies:")
    for module, imports in all_imports.items():
        print(f"{module} -> {imports}")
