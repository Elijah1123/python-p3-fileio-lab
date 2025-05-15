from pathlib import Path

def write_file(file_name, file_content):
    
    path = Path(file_name)
    
    
    if path.suffix != '.txt':
        path = path.with_suffix('.txt')
    
    
    with open(path, 'w') as f:
        f.write(file_content)


def append_file(file_name, append_content):
    path = Path(file_name)
    if path.suffix != '.txt':
        path = path.with_suffix('.txt')
    with open(path, 'a') as f:
        f.write(append_content)


def read_file(file_name):
    path = Path(file_name)
    if path.suffix != '.txt':
        path = path.with_suffix('.txt')
    with open(path, 'r') as f:
        return f.read()
