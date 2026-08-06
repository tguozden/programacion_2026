# Ejercicio: merge y resolución de conflictos

## 0. Intro de `branch` y `checkout`

- `git branch` — muestra las ramas que existen, o crea una nueva (sin moverte a ella)
- `git checkout` — coloca el repositorio en una rama que preexistente.

```bash
git branch                # ver en que rama estoy
git branch nombre-rama     # crear una rama nueva (no me muevo)
git branch                 # la rama nueva aparece en la lista, pero sigo en la misma que antes
git checkout nombre-rama   # ahora si me muevo a la rama nueva
git branch                 # el * ahora esta en nombre-rama
```
(branch y checkout se suelen juntar en un solo comando *checkout -b*)

## 1. Preparar el repo

```bash
mkdir ejercicio_merge
cd ejercicio_merge
git init
git branch -M main
echo "Hola mundo" > saludo.txt
git add .
git commit -m "commit inicial"
git log --oneline
```

## 2. Crear una rama y modificar el archivo ahí

```bash
git branch rama-pruebo
git status
git checkout rama-pruebo
git status
```

Hacer algún cambio en `saludo.txt`.

```bash
git status
git commit -am "cambio saludo en rama-pruebo"
git log --oneline
```

## 3. Volver a `main` y hacer una modificación distinta.

```bash
git checkout main
git status
cat saludo.txt
```
Observar que hay en el archivo ahora.

Hacer otro cambio en `saludo.txt`, distinto al que hicimos en *rama-pruebo*, en la misma línea.

```bash
git status
git commit -am "cambio saludo en main"
git log --oneline --all --graph
```

## 4. Intentar el merge

```bash
git merge rama-pruebo
```

Notar que este comando da un error `CONFLICT`.

Podemos rechequear el estado del repositorio y el archivo.

```bash
git status
cat saludo.txt
```

## 5. Resolver el conflicto

Para resolver hay que editar `saludo.txt`. Veremos allí texto similar al siguiente:

```
<<<<<<< HEAD
Hola a todos
=======
Hola gente
>>>>>>> rama-pruebo
```
Git hizo esto porque no puede resolver cómo queremos la versión final luego de *merge*. Para esto necesitamos borrar las líneas `<<<<<<<`, `=======`, `>>>>>>>`, y dejar el contenido final que deseado.

Luego:
```bash
git add saludo.txt
git commit -m "resuelvo conflicto en saludo.txt"
```

## 6. Verificar

```bash
git log --all --graph
```
(*all* para ver todas las ramas)

Deberíamos ver un commit de merge con dos ramas convergiendo.

