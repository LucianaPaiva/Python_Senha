import string

def verificar_senha(senha):
    """
    Verifica se a senha atende aos critérios de segurança.
    """
    tem_8_digitos = len(senha) >= 8
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tem_caracter_especial = any(c in string.punctuation for c in senha)

    total_atendidos = sum([tem_8_digitos, tem_maiuscula, tem_minuscula, tem_numero, tem_caracter_especial])

    if total_atendidos <= 2:
        return "Sua senha não presta"
    elif total_atendidos <= 4:
        return "Sua senha é marromeno"
    return "Sua senha é uma fortaleza"

def main():
    """
    Função principal para interagir com o usuário.
    """
    while True:
        senha_digitada = input("Digite sua senha: ")
        resultado = verificar_senha(senha_digitada)
        print(resultado)
        if resultado == "Sua senha é uma fortaleza":
            break

if __name__ == "__main__":
    main()
