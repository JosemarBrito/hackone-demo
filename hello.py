# hello.py

def saudacao(nome: str) -> str:
    """
    Retorna uma mensagem de saudação personalizada.
    
    :param nome: O nome da pessoa a ser saudada.
    :return: Uma string contendo a saudação.
    """
    if not nome:
        raise ValueError("O nome não pode ser vazio.")
    
    return f"Olá, {nome}! Bem-vindo ao hackone-demo."

# Exemplo de uso
if __name__ == "__main__":
    print(saudacao("Jose"))

