def is_negativ(lista):
    '''
    Verificare daca este negativ nenul in lista
    :param lista: nr intreg
    :return: True daca n este negativ si False, altfel
    '''
    rez=[]

    for n in lista:
        if n<0:
            return True
    return False
pass

def test_is_negativ():
    assert is_negativ(-56) == True
    assert is_negativ(342) == False

test_is_negativ ()

def is_prim(n):
    if n<2:
        return False
    if n==2:
        return True
    for d in range(2,n//2+1):
        if n%d==0:
            return False
    return True

def is_superprime(lista) -> bool :
    '''
    Verificare daca este superprim in lista
    :param lista: nr intreg
    :return: True daca n este superprim si False, altfel
    '''
    rez=[]

    for n in lista:
        while (n!=0):
            if (is_prim(n) == False):
                return False
            n = n // 10
        return True
pass

def test_is_superprime():
    assert is_superprime(233) == True
    assert is_superprime(237) == False

test_is_superprime ()

def read_list():
    lista = []
    x = int(input("Introduceti numarul de elem din lista"))
    for i in range(x):
        n = int(input("a[{}]=".format(i+1)))
        lista.append(n)
    return lista

def show_menu():
    print('''
    1. Citire lista
    2. Afisare 
    x. Iesire
    ''')

def run_UI():
    lista=[]
    while True:
        show_menu()
        cmd= input ("Comanda:")
        if cmd == '1':
            lista=read_list()
        else:
            if cmd == '2':
                list_is_negativ=is_negativ(lista)
                print(list_is_negativ)
                list_is_superprime=is_superprime(lista)
                print(list_is_superprime)
            elif cmd == 'x':
                break
            else:
                print("Comanda invalida")

run_UI()

