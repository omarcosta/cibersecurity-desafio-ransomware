import os

def list_all_files(directory):
    file_list = []
    if os.path.exists(directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list
    else:
        print(f"O caminho {directory} não existe.")
        return