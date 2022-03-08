import string

class AlgoritmoRecursivo:
    
    def __init__(self, listaAnalizar: list):
        self.listaAnalizar = listaAnalizar
        self.reverseList()

    def reverseList(self):
        self.listaAnalizar.reverse()

    def punto(self):
        if(self.comprobarSiguiten()==False):
            return False
        letraAnalizar = self.listaAnalizar.pop()
        if(letraAnalizar=="."):
            print("PASO EL PUNTO")
            return True
        print("NO PASO EL PUNTO")
        return False

    def numero(self):
        if(self.comprobarSiguiten()==False):
            # # # print("YA NO HAY MAS A ANALIZAR")
            return False
        letraAnalizar = self.listaAnalizar.pop()
        if(str.isdigit(letraAnalizar)):
            print( "PASO D")
            return True
        print( "NO PASO D")
        self.listaAnalizar.append(letraAnalizar)
        return False

    def letras(self):
        if(self.comprobarSiguiten()==False):
            return False

        letraAanalizar = self.listaAnalizar.pop()
        if(string.ascii_lowercase.__contains__(letraAanalizar)):
            print( "PASO L CON MINUSCULA")
            return True
        if(string.ascii_uppercase.__contains__(letraAanalizar)):
            print( "PASO L CON MAYUSCULA")
            return True

        print( "NO PASO L")
        self.listaAnalizar.append(letraAanalizar)
        return False

    def Rletras(self):
        if(self.letras()):
            self.Rletras()
        if(self.numero()):
            self.Rletras()
        print("PASO RL")
        return True

    def letrasMinusculas(self):

        if(self.comprobarSiguiten()==False):
            return False
        letraAanalizar = self.listaAnalizar.pop()
        if(letraAanalizar == "."):
            self.listaAnalizar.append(letraAanalizar)
            self.listaAnalizar.append(".")
            return False

        
        print(letraAanalizar)
        if(string.ascii_lowercase.__contains__(letraAanalizar)):
            print( "PASO LM CON MINUSCULA")
            return True
        print( "NO PASO LM")
        self.listaAnalizar.append(letraAanalizar)
        return False

    def RletrasMinusculas(self):
        if(self.letrasMinusculas()):
            self.RletrasMinusculas()
        return True

    def git(self):
        if(self.comprobarSiguiten()==False):
            # # print("YA NO HAY MAS A ANALIZAR")
            return False
        letraAnalizar = self.listaAnalizar.pop()
        if(letraAnalizar=="g"):
            if(self.comprobarSiguiten()==False):
                # # print("YA NO HAY MAS A ANALIZAR")
                return False
            letraAnalizar = self.listaAnalizar.pop()

            if(letraAnalizar=="i"):
                if(self.comprobarSiguiten()==False):
                    # # print("YA NO HAY MAS A ANALIZAR")
                    return False
                letraAnalizar = self.listaAnalizar.pop()
    
                if(letraAnalizar=="t"):
                    # print("PASO EL GIT")   
                    return True
        return False

    def add(self):
        if(self.comprobarSiguiten()==False):
            # # print("YA NO HAY MAS A ANALIZAR")
            return False
        letraAnalizar = self.listaAnalizar.pop()
        if(letraAnalizar=="a"):
            if(self.comprobarSiguiten()==False):
                # # print("YA NO HAY MAS A ANALIZAR")
                return False
            letraAnalizar = self.listaAnalizar.pop()
            if(letraAnalizar=="d"):
                if(self.comprobarSiguiten()==False):
                    # # print("YA NO HAY MAS A ANALIZAR")
                    return False
                letraAnalizar = self.listaAnalizar.pop()
                if(letraAnalizar=="d"):  
                    return True
        return False


    def produccion(self):
        print('entro a produccion')
        print(self.listaAnalizar)
        bandera = self.git()
        if(bandera == False):
            print(self.listaAnalizar)
            return "no paso"
        # print(listaAnalizar)
        bandera = self.add()
        if(bandera == False):
            print(self.listaAnalizar)
            return "no paso"
        # print(listaAnalizar)
        bandera = self.letras()
        if(bandera == False):
            print(self.listaAnalizar)
            return "no paso"
        # print(listaAnalizar)
        bandera = self.Rletras()
        if(bandera == False):
            print(self.listaAnalizar)
            return "no paso"
        # print(listaAnalizar)
        bandera = self.punto()
        if(bandera == False):
            print(self.listaAnalizar)
            return "no paso"
        # print(listaAnalizar)
        bandera = self.letrasMinusculas()
        if(bandera == False):
            print(self.listaAnalizar)
            return "no paso"
        # print(listaAnalizar)
        bandera = self.RletrasMinusculas()
        if(bandera == False):
            print(self.listaAnalizar)
            return "no paso"
        
        print(self.listaAnalizar)
        print(len(self.listaAnalizar))

        if(len(self.listaAnalizar) > 0):
            return "no paso"
        else:
            return True


    def comprobarSiguiten(self):
        if(len(self.listaAnalizar)>0):
            return True
        return False
