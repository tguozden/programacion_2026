# Instalación

Matplotlib, numpy y Jupyter ya están en el ambiente de Python que usan habitualmente (el ambiente principal). Lo único que falta es skyfield, y para no tocar el ambiente principal se instala en un ambiente chico dentro de la carpeta del proyecto. El ambiente chico tiene un archivo `.pth` que le permite usar también los paquetes del ambiente principal, así que desde el ambiente chico se puede usar todo: skyfield, numpy, matplotlib y Jupyter.

## Crear el ambiente chico

Con el ambiente principal activado (por ejemplo, `source ~/ambientes/principal/bin/activate`, o en Windows `C:\Users\usuario\ambientes\principal\Scripts\activate`), desde la carpeta del proyecto:

1. Crear el ambiente chico en la carpeta `.venv`:

    ```bash
    python -m venv .venv
    ```

2. Agregar al ambiente chico un archivo `.pth` con la ruta de los paquetes del ambiente principal. Python lee los archivos `.pth` al arrancar y suma esas rutas a los lugares donde busca módulos.

    Primero, con el ambiente principal todavía activado, averiguar la ruta de sus paquetes:

    ```bash
    python -c "import sysconfig; print(sysconfig.get_path('purelib'))"
    ```

    Muestra algo como `/home/usuario/ambientes/principal/lib/python3.12/site-packages` (en Windows, algo como `C:\Users\usuario\ambientes\principal\Lib\site-packages`).

    Después, crear el archivo `ambiente_principal.pth` dentro de la carpeta de paquetes del ambiente chico, con esa ruta como única línea:

    ```bash
    echo /home/usuario/ambientes/principal/lib/python3.12/site-packages > .venv/lib/python3.12/site-packages/ambiente_principal.pth
    ```

    Reemplacen la ruta por la que mostró el comando anterior, y `python3.12` por la versión que aparezca en `.venv/lib/` (es la misma del ambiente principal). En Windows la carpeta es `.venv\Lib\site-packages\`: lo más simple es crear el archivo con un editor de texto (por ejemplo, VS Code), pegar la ruta y guardarlo con ese nombre.

3. Activar el ambiente chico:

    ```bash
    source .venv/bin/activate
    ```

    En Windows: `.venv\Scripts\activate`.

4. Instalar skyfield dentro del ambiente chico:

    ```bash
    python -m pip install --no-deps skyfield sgp4 jplephem certifi
    ```

    Normalmente pip instala por su cuenta las dependencias de un paquete (los otros paquetes que necesita para funcionar). La opción `--no-deps` le indica que instale únicamente los paquetes nombrados. skyfield necesita numpy, sgp4, jplephem y certifi: se nombran todos menos numpy, que ya está en el ambiente principal. Así no quedan dos copias de numpy, que podrían ser de versiones incompatibles con matplotlib.

5. Comprobar que funciona con el comando en línea: `python -c "import skyfield, matplotlib; print(skyfield.__version__)"` tiene que mostrar la versión.

Agreguen `.venv/` al `.gitignore`: el ambiente no se sube al repositorio.

> Un ambiente no se puede mover de lugar. Si mueven o renombran la carpeta del proyecto, o si actualizan el ambiente principal a otra versión de Python, borren la carpeta `.venv` y repitan todos los pasos.

## Abrir el notebook desde la terminal

Desde la carpeta del proyecto, con el ambiente chico activado (paso 3; hay que activarlo en cada terminal nueva):

```bash
python -m jupyterlab
```

Si prefieren otra interfaz:

```bash
python -m notebook     # Jupyter Notebook
python -m nbclassic    # Jupyter clásico
```

Si tienen instalado Jupyter Notebook versión 6 o anterior, `python -m notebook` ya abre la interfaz clásica.

Para correr las pruebas, desde la misma terminal: `python tests.py`.

## Abrir el notebook desde VS Code

1. Abrir la carpeta del proyecto con File > Open Folder.
2. Abrir `informe.ipynb`.
3. Comprobar en una celda del notebook que funciona: `import skyfield, matplotlib`.

VS Code detecta el ambiente `.venv` de la carpeta del proyecto y, a través del archivo `.pth`, también los paquetes del ambiente principal. Si al ejecutar la primera celda pregunta qué kernel usar, elijan `.venv`.
