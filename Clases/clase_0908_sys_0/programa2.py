import sys
from func_auxiliares import suma
import ejercicio_clase

if len(sys.argv) != 3:
    print('tiene que ingresar 2 argumentos')
    sys.exit()
    
a = int(sys.argv[1])
b = int(sys.argv[2])
suma(a, b)

print( ejercicio_clase.es_par(1) )

