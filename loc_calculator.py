import os

def get_python_files(directory):
    """Recursively get all Python files in a directory"""
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

def calculate_loc_and_modules(directory):
    """Calculate total LOC, total modules, and average module size"""
    python_files = get_python_files(directory)
    total_loc = 0
    for file in python_files:
        with open(file, 'r', encoding='utf-8') as f:
            total_loc += sum(1 for _ in f)
    total_modules = len(python_files)
    avg_module_size = total_loc / total_modules if total_modules != 0 else 0
    return total_loc, total_modules, avg_module_size

if __name__ == '__main__':
    project_directory = input("Enter the path to your project directory: ")
    total_loc, total_modules, avg_module_size = calculate_loc_and_modules(project_directory)
    print(f"Total LOC: {total_loc}")
    print(f"Total Modules: {total_modules}")
    print(f"Average Module Size: {avg_module_size:.2f} LOC")
