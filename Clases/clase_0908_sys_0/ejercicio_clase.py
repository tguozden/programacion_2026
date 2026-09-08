# ~ ejercicicio en clase
# ~ escribir un archivo que:                                                                      

# 1. Defina una función (por ejemplo, que reciba un número y diga si es par o impar). 

# 2. Use  sys.argv  para recibir ese número desde la terminal.                    

# ~ 3. Tenga un bloque  if __name__ == "__main__":  que llame a la función con el   valor recibido.                                                                 
                                                                       
                                                                       # 4. Pueda importarse desde otro archivo sin que se dispare nada raro.                                                                                   

import sys

def es_par(n:int)->bool:
    a = n%2
    if a == 0:
        return True
    else:
        return False

if __name__ == '__main__':  #si la variable de ambiente es la ppal
    
    if len(sys.argv) == 2:
        
        try:
            n = int(sys.argv[1])
        except Exception as e:
            print('fallo el parseo')
            sys.exit()
            
    else:
        print('ingrese un argumento')
        sys.exit()
    if es_par(n):
        print('es par')
    else:
        print('es impar')
       

