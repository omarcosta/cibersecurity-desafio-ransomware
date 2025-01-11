def get_key():
    KEY_FILE = "secret.key"
    SECRET_KEY = None
    try:
        with open(KEY_FILE, "rb") as file:
            SECRET_KEY = file.read()
            print("Chave carregada com sucesso.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{KEY_FILE}' não foi encontrado.")
    return SECRET_KEY