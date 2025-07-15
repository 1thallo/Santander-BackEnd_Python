def funcao_principal():
    print("Executando função principal!")

    def funcao_interna():
        print("Executando função interna!")
    
    def funcao_interna2():
        print("Executando função interna 2!")
    
    funcao_interna()
    funcao_interna2()

funcao_principal()