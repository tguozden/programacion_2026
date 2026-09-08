import func_auxiliares
# ~ import no_me_acuerdo  error: ModuleNotFoundError
import sys


def saludar():
    print('hola mundo')
    
def saludarunpocomas():
    for i in range(10):
        print('hola mundo', i)

if __name__ == '__main__':
    saludar()
    # variables dunders __name__
    func_auxiliares.suma(2, 3)
    print('sys.path es:', sys.path)

