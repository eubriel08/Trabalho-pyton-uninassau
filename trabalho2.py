total = 0
Alta = 0
Media = 0
Baixa = 0

while True:

    menu = ["1 - Novo chamado", "2 - Relatório", "3 - Sair"]

    for alternativa in menu:
        print(alternativa)

    escolha = input("Escolha uma alternativa: ")

    if escolha == "1":

        funcionario = input("Informe seu nome: ")

        print("\nEscolha o problema:")

        problemas = ["1 - Computador",
                     "2 - Internet",
                     "3 - Sistema",
                     "4 - Impressora"]

        for problema in problemas:
            print(problema)

        escolha_problema = input("Opção: ")

        if escolha_problema == "1":
            problema = "Computador"
        elif escolha_problema == "2":
            problema = "Internet"
        elif escolha_problema == "3":
            problema = "Sistema"
        elif escolha_problema == "4":
            problema = "Impressora"
        else:
            print("Problema inválido.")


        Descricao = input("Descreva o problema: ")

        print("\nImpacto do problema:")
        print("1 - Impede completamente o funcionario de trabalhar")
        print("2 - Prejudica,mas não impede o trabalho")
        print("3 - Não interfere significativamente")

        prioridade = input("Informe o grau de prioridade: ")

        if prioridade == "1":
            nivel = "Alta"
            Alta += 1

        elif prioridade == "2":
            nivel = "Média"
            Media += 1

        elif prioridade == "3":
            nivel = "Baixa"
            Baixa += 1

        else:
            print("Impacto inválido.")
            

        total += 1

        print("\nChamado cadastrado com sucesso!")
        print("Funcionário:", funcionario)
        print("Problema:", problema)
        print("Descrição:", Descricao)
        print("Prioridade:", nivel)

    elif escolha == "2":

        print("\n========== RELATÓRIO ==========")

        print("Total de chamados:", total)
        print("Alta prioridade:", Alta)
        print("Média prioridade:", Media)
        print("Baixa prioridade:", Baixa)

        quantidade_prioridades = Alta + Media + Baixa

        print("Total contabilizado:", quantidade_prioridades)

        if total == 0:
            print("Ainda não existem chamados cadastrados.")

        elif quantidade_prioridades == total:
            print("Contagem dos chamados conferida com sucesso.")

        else:
            print("Há uma diferença na contagem.")

    elif escolha == "3":

        print("\nEncerrando o sistema...")

    else:

        print("\nOpção inexistente. Escolha uma alternativa de 1 a 3. ")
        
        
        
