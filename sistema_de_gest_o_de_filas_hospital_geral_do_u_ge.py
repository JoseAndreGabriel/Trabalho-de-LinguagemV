# ==============================================================================
# PROJETO: Sistema de Gestão de Filas de Espera e Atendimento de Utentes
# INSTITUIÇÃO: Hospital Geral do Uíge
# AUTOR: José André Gabriel
# ==============================================================================

# Listas para guardar os utentes que chegam (separados por prioridade)
fila_prioritaria = []
fila_normal = []

# Contador para gerar os números de atendimento (senhas) por ordem de chegada
numero_senha = 1

print("=================================================================")
print("   BEM-VINDO AO SISTEMA DE GESTÃO - HOSPITAL GERAL DO UÍGE")
print("=================================================================")

# Ciclo principal para o programa continuar a correr até escolher Sair
while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1. Registar novo utente (Chegada)")
    print("2. Chamar próximo utente para atendimento")
    print("3. Ver filas de espera atuais")
    print("4. Sair do sistema")
    
    opcao = input("Escolha uma opção (1 a 4): ")

    # OPÇÃO 1: REGISTAR UTENTE
    if opcao == "1":
        print("\n--- NOVO REGISTO ---")
        nome_utente = input("Nome do utente: ")
        
        print("Qual o tipo de atendimento?")
        print("1 - Prioritário (Emergência clínica, idosos, gestantes, crianças)")
        print("2 - Normal (Ordem de chegada)")
        tipo = input("Escolha (1 ou 2): ")

        # Criar a senha (ex: P-1 para prioritário, N-2 para normal)
        if tipo == "1":
            senha = "P-" + str(numero_senha)
        else:
            senha = "N-" + str(numero_senha)
            
        numero_senha = numero_senha + 1

        # Encaminhamento para a sala e equipa médica correspondente
        print("\nEscolha a especialidade / encaminhamento:")
        print("1 - Clínica Geral")
        print("2 - Pediatria")
        print("3 - Urgência / Triagem")
        especialidade = input("Escolha (1, 2 ou 3): ")

        if especialidade == "1":
            sala = "Sala 01 - Clínica Geral"
            medico = "Dr. António Manuel"
            enfermeiro = "Enf.ª Maria Teresa"
        elif especialidade == "2":
            sala = "Sala 02 - Pediatria"
            medico = "Dra. Isabel Domingos"
            enfermeiro = "Enf. João Baptista"
        else:
            sala = "Sala 03 - Urgência"
            medico = "Dr. Carlos Alberto"
            enfermeiro = "Enf.ª Ana Paula"

        # Guardar os dados do utente num dicionário simples
        utente = {
            "senha": senha,
            "nome": nome_utente,
            "sala": sala,
            "medico": medico,
            "enfermeiro": enfermeiro
        }

        # Adicionar à fila correspondente
        if tipo == "1":
            fila_prioritaria.append(utente)
        else:
            fila_normal.append(utente)

        # Mostrar o comprovativo de encaminhamento ao utente
        print("\n==========================================")
        print("REGISTO CONCLUÍDO COM SUCESSO!")
        print("Senha atribuída : " + senha)
        print("Utente          : " + nome_utente)
        print("Encaminhamento  : " + sala)
        print("Médico(a)       : " + medico)
        print("Enfermeiro(a)   : " + enfermeiro)
        print("==========================================")

    # OPÇÃO 2: CHAMAR PRÓXIMO UTENTE
    elif opcao == "2":
        print("\n--- CHAMADA PARA ATENDIMENTO ---")
        # Primeiro verifica-se sempre se há alguém na fila prioritária
        if len(fila_prioritaria) > 0:
            # .pop(0) retira o primeiro utente que entrou na lista
            proximo = fila_prioritaria.pop(0)
            print(">>> ATENDIMENTO PRIORITÁRIO <<<")
            print("Senha: " + proximo["senha"] + " | Utente: " + proximo["nome"])
            print("Dirigir-se à: " + proximo["sala"])
            print("Equipa: " + proximo["medico"] + " e " + proximo["enfermeiro"])
            
        # Se não houver prioritários, chama-se da fila normal
        elif len(fila_normal) > 0:
            proximo = fila_normal.pop(0)
            print(">>> ATENDIMENTO NORMAL <<<")
            print("Senha: " + proximo["senha"] + " | Utente: " + proximo["nome"])
            print("Dirigir-se à: " + proximo["sala"])
            print("Equipa: " + proximo["medico"] + " e " + proximo["enfermeiro"])
            
        else:
            print("Não existem utentes em espera neste momento.")

    # OPÇÃO 3: VER FILAS DE ESPERA
    elif opcao == "3":
        print("\n--- ESTADO ATUAL DAS FILAS ---")
        print("Utentes em Fila Prioritária: " + str(len(fila_prioritaria)))
        for u in fila_prioritaria:
            print("  - [" + u["senha"] + "] " + u["nome"] + " -> " + u["sala"])

        print("\nUtentes em Fila Normal: " + str(len(fila_normal)))
        for u in fila_normal:
            print("  - [" + u["senha"] + "] " + u["nome"] + " -> " + u["sala"])

    # OPÇÃO 4: SAIR
    elif opcao == "4":
        print("\nA encerrar o sistema do Hospital Geral do Uíge. Bom trabalho!")
        break

    # CASO O UTILIZADOR DIGITE ALGO INVÁLIDO
    else:
        print("\nOpção inválida! Por favor, escolha um número de 1 a 4.")