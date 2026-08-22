def menu():
    while True:
        print("-----Menu Refeições------")
        print("1-x-salada")
        print("2-carne assada")
        print("3-peixe")
        op = int(input("escolha sua refeição: "))
        cnt = input("deseja escolhe bebida?:[s/n] ")

        if cnt == "s":
            continue
        elif cnt == "n":
            break
        else:
            print("error, digite [s] ou [n]")

        print("-----Menu Bebidas------")
        print("1-coca-cola")
        print("2-fanta")
        print("3-limonada")
        op2 = int(input("escolha sua bebida: "))

menu()

#    print("-----Menu refeição------")
#    print("1-pudim")
#    print("2-milk shake")
#    print("3-petit gateau")
#    op3 = int(input("escolha sua sobremesa: "))