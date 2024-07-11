while True:

    senha_digitada = str(input("Digite sua senha: "))


    req_letra_minuscula = "abcdefghijklmnopqrstuvwxyz"
    req_letra_maiuscula = req_letra_minuscula.upper()
    req_numeros = "0123456789"


    tem_8_digitos = 0
    tem_maiuscula = 0 
    tem_minuscula = 0
    tem_numero = 0
    tem_caracter_especial = 0

    if len(senha_digitada) >= 8:
        tem_8_digitos = 1

    for letra_da_vez in senha_digitada:
        if letra_da_vez in req_letra_minuscula:
            tem_minuscula = 1 
            #print("Opa, achei uma letra minuscula")
        elif letra_da_vez in req_letra_maiuscula:
            tem_maiuscula = 1
            #print("Opa, achei uma letra maiúscula")
        elif letra_da_vez in req_numeros:
            tem_numero = 1
            #print("Opa, achei um número")
        else:
            tem_caracter_especial =1
            #print("Opa, achei um caracter especial")

    total_atendidos = tem_8_digitos + tem_maiuscula + tem_minuscula + tem_numero + tem_caracter_especial

    if total_atendidos <= 2:
        print("Sua senha não presta")

    elif total_atendidos <= 4:
        print("Sua senha é marromeno")
    else:
        print("Sua senha é uma fortaleza")
        break

    # if total_atendidos == 1 or total_atendidos == 2:
    #     print("Fraca")
    # elif total_atendidos >= 3 and total_atendidos <= 4:
    #     print("Média")
    # else:
    #     print("Forte") 
        


