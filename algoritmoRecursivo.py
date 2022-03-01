
import string


listaAnalizar = ["g","i","t","a"]
listaAnalizar.reverse()

def punto():
    if(comprobarSiguiten()==False):
        # # # print("YA NO HAY MAS A ANALIZAR")
        return False
    letraAnalizar = listaAnalizar.pop()
    if(letraAnalizar=="."):
        print("PASO EL PUNTO")
        return True
    print("NO PASO EL PUNTO")
    return False

def numero():
    if(comprobarSiguiten()==False):
        # # # print("YA NO HAY MAS A ANALIZAR")
        return False
    letraAnalizar = listaAnalizar.pop()
    if(str.isdigit(letraAnalizar)):
        print( "PASO D")
        return True
    print( "NO PASO D")
    listaAnalizar.append(letraAnalizar)
    return False

def letras():
    if(comprobarSiguiten()==False):
        # # # print("YA NO HAY MAS A ANALIZAR")
        return False
    letraAanalizar = listaAnalizar.pop()
    if(string.ascii_lowercase.__contains__(letraAanalizar)):
        print( "PASO L CON MINUSCULA")
        return True
    if(string.ascii_uppercase.__contains__(letraAanalizar)):
        print( "PASO L CON MAYUSCULA")
        return True

    print( "NO PASO L")
    listaAnalizar.append(letraAanalizar)
    return False

def Rletras():
    if(letras()):
        Rletras()
    if(numero()):
        Rletras()
    print("PASO RL")
    return True

def letrasMinusculas():
    if(comprobarSiguiten()==False):
        # # # print("YA NO HAY MAS A ANALIZAR")
        return False
    letraAanalizar = listaAnalizar.pop()
    if(string.ascii_lowercase.__contains__(letraAanalizar)):
        print( "PASO LM CON MINUSCULA")
        return True
    print( "NO PASO LM")
    return False

def RletrasMinusculas():
    if(letrasMinusculas()):
        RletrasMinusculas()
    return True

def git():
    if(comprobarSiguiten()==False):
        # # print("YA NO HAY MAS A ANALIZAR")
        return False
    letraAnalizar = listaAnalizar.pop()
    if(letraAnalizar=="g"):
        if(comprobarSiguiten()==False):
            # # print("YA NO HAY MAS A ANALIZAR")
            return False
        letraAnalizar = listaAnalizar.pop()

        if(letraAnalizar=="i"):
            if(comprobarSiguiten()==False):
                # # print("YA NO HAY MAS A ANALIZAR")
                return False
            letraAnalizar = listaAnalizar.pop()
   
            if(letraAnalizar=="t"):
                # print("PASO EL GIT")   
                return "PASO EL GIT"
    return "NO PASO EL GIT"

def add():
    if(comprobarSiguiten()==False):
        # # print("YA NO HAY MAS A ANALIZAR")
        return False
    letraAnalizar = listaAnalizar.pop()
    if(letraAnalizar=="a"):
        if(comprobarSiguiten()==False):
            # # print("YA NO HAY MAS A ANALIZAR")
            return False
        letraAnalizar = listaAnalizar.pop()
        if(letraAnalizar=="d"):
            if(comprobarSiguiten()==False):
                # # print("YA NO HAY MAS A ANALIZAR")
                return False
            letraAnalizar = listaAnalizar.pop()
            if(letraAnalizar=="d"):  
                return "PASO EL add"
    return "NO PASO EL add"


def produccion():

    # print(listaAnalizar)
    bandera = git()
    if(bandera == False):
        print(listaAnalizar)
        return "no paso"
    # print(listaAnalizar)
    bandera = add()
    if(bandera == False):
        print(listaAnalizar)
        return "no paso"
    # print(listaAnalizar)
    bandera = letras()
    if(bandera == False):
        print(listaAnalizar)
        return "no paso"
    # print(listaAnalizar)
    bandera = Rletras()
    if(bandera == False):
        print(listaAnalizar)
        return "no paso"
    # print(listaAnalizar)
    bandera = punto()
    if(bandera == False):
        print(listaAnalizar)
        return "no paso"
    # print(listaAnalizar)
    bandera = letrasMinusculas()
    if(bandera == False):
        print(listaAnalizar)
        return "no paso"
    # print(listaAnalizar)
    bandera = RletrasMinusculas()
    if(bandera == False):
        print(listaAnalizar)
        return "no paso"
    # print(listaAnalizar)


def comprobarSiguiten():
    if(len(listaAnalizar)>0):
        return True
    return False


print(produccion())
