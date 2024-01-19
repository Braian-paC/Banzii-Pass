import random as rd
# import de bibliotecas

# funções
choice = 0
def senha_random():
    random_characters = "0123456789AaBbCcDdEeFfGgHhJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzçÇ]}[{?!#$%&*"
    caracteres, pass_origin = 0, ""
    while caracteres <= 5 or caracteres > 20:
        caracteres = int(input('Quantos caracteres a senha deverá ter? (de 6 a 20)\n'))
    for c in range(0, caracteres):
        pass_add = rd.choice(random_characters)
        pass_origin = pass_add + pass_origin
    print(f'Senha: "{pass_origin}"')
def randomizar_senha():
    pass_old = str(input('Digite sua senha atual: '))
    pass_new = ''.join(rd.sample(pass_old, len(pass_old)))
    print(f'Senha randomizada: {pass_new}')

# mecânica do gerador de senhas
print('-=-'*15, '\nBanzii Pass'), print('-=-'*15)
while choice != 2 and choice != 1:
    choice = int(input('O que você deseja?\n1 -> Gerar uma senha totalmente randômica\n2 -> Randomizar uma senha já existente\n'))
print('-=-'*15)
if choice == 1:
    senha_random()
if choice == 2:
    randomizar_senha()
print('-=-'*15)
