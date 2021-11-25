import sys

def agenda_amigos():
    lin, cols = int(input("Quantos contatos deseja inserir? ")), 10
    contatos = []
    print(contatos)
    for i in range(lin):
        print("\nInsira os detalhes do n° %d na seguinte ordem:" % (i+1))
        print("NOTE: * obrigatório")
        print("....................................................................")
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Nome*: ")))
                if temp[j] == '' or temp[j] == ' ':
                    j = input(
                        "O nome do contato é obrigatório! Insira um nome para prosseguir: ")
            if j == 1:
                temp.append(str(input("Apelido: ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 2:
                temp.append(int(input("Telefone*: ")))
                if temp[j] == '' or temp[j] == ' ':
                    j = input(
                        "O Telefone do contato é obrigatório! Insira um número de telefone para prosseguir: ")
            if j == 3:
                temp.append(int(input("Celular*: ")))  
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 4:
                temp.append(str(input("E-mail: ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
                     
            if j == 5:
                temp.append(str(input("Observações: ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
        contatos.append(temp)
    print(contatos)
    return contatos
 
def menu():
    print("********************************************************************")
    print("\t\t\tMENU PRINCIPAL", flush=False)
    print("********************************************************************")
    print("\tMenu de Opções\n")
    print("1. Adicionar um contato")
    print("2. Remover um contato")
    print("3. Alterar dados de um contato")
    print("4. Excluir um contato")
    print("5. Copiar a agenda")
    print("6. Excluir todos os contatos")
    print("6. Finalizar programa")
    escolha = int(input("Selecione uma opção: "))
     
    return escolha
 
def adicionar_contato(pb):
    dip = []
    if i == 0:
        temp.append(str(input("Nome*: ")))
        if temp[i] == '' or temp[i] == ' ':
            i = input(
                "O nome do contato é obrigatório! Insira um nome para prosseguir: ")
    if i == 1:
        temp.append(str(input("Apelido: ")))
        if temp[i] == '' or temp[i] == ' ':
            temp[i] = None
    if i == 2:
        temp.append(int(input("Telefone*: ")))
        if temp[i] == '' or temp[i] == ' ':
            i = input(
                "O Telefone do contato é obrigatório! Insira um número de telefone para prosseguir: ")
    if i == 3:
         temp.append(int(input("Celular*: ")))  
         if temp[i] == '' or temp[i] == ' ':
            temp[i] = None
    if i == 4:
        temp.append(str(input("E-mail: ")))
        if temp[i] == '' or temp[i] == ' ':
            temp[i] = None
                     
    if i == 5:
        temp.append(str(input("Observações: ")))
        if temp[i] == '' or temp[i] == ' ':
            temp[i] = None
    pb.append(dip)
    return pb
 
def remover_contato(pb):
    query = str(
        input("Insira o nome do contato que deseja remover: "))
    temp = 0
    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            print(pb.pop(i))
            print("Seu contato foi removido")
            return pb
    if temp == 0:
        print("Sem resultados disponíveis! Tente outra hora.")
         
        return pb
 
def apagar_todos(pb):
    return pb.clear()
 
def consultar_contato(pb):
    choice = int(input("Qual seu critério de busca?\n\n\
    1. Nome\n2. Apelido\n3. Telefone-id\n4. Celular\n5. E-mail\
    \nPlease enter: "))
     
    temp = []
    check = -1
     
    if choice == 1:
        query = str(
            input("Insira o nome do contato que deseja consultar: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])
                 
    elif choice == 2:
        query = int(
            input("Insira o apelido do contato que deseja consultar: "))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i
                temp.append(pb[i])
                 
    elif choice == 3:
        query = str(input("Insira o Telefone do contato que deseja consultar: "))
        for i in range(len(pb)):
            if query == pb[i][2]:
                check = i
                temp.append(pb[i])
                 
    elif choice == 4:
        query = str(input("Insira o celular do contato que deseja consultar: "))
        for i in range(len(pb)):
            if query == pb[i][3]:
                check = i
                temp.append(pb[i])
                 
    elif choice == 5:
        query = str(
            input("Insira o E-mail do contato que deseja consultar: "))
        for i in range(len(pb)):
            if query == pb[i][4]:
                check = i
                temp.append(pb[i])
         
    else:
        print("Inválido!")
        return -1
     
    if check == -1:
        return -1
    else:
        copiar_contatos(temp)
        return check
def mostrar_todos(pb):
    if not pb:
        print("Lista vazia: []")
    else:
        for i in range(len(pb)):
            print(pb[i])
 
def thanks():
    print("********************************************************************")
    print("Obrigado por usar o menu de contatos.")
    print("Volte sempre!")
    print("********************************************************************")
    sys.exit("Até mais! Tenha um bom dia!")
print("....................................................................")
print("Olá, usuário! Bem-vindo ao menu de contatos")
print("Expore à vontade!")
print("....................................................................")
ch = 1
pb = agenda_amigos()
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        pb = adicionar_contato(pb)
    elif ch == 2:
        pb = remover_contato(pb)
    elif ch == 3:
        pb = apagar_todos(pb)
    elif ch == 4:
        d = consultar_contato(pb)
        if d == -1:
            print("The contact does not exist. Please try again")
    elif ch == 5:
        mostrar_todos(pb)
    else:
        thanks()
