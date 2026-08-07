# Ejercicio: conflicto entre dos repos (push/pull)

Simulamos dos personas trabajando sobre el mismo repo, usando un repo local como "remoto" en vez de la nube en GitHub.

## 1. Crear el remoto (bare) a partir de un repo normal

La palabra *bare* en este contexto se traduce como descubierto o expuesto
```bash
mkdir ejercicio_dosrepos
cd ejercicio_dosrepos

# primero, un repo normal con contenido, como cualquier proyecto
git init repo1
cd repo1
git config user.name "Profe"
git config user.email "profe@ejemplo.com"
echo "Hola mundo" > saludo.txt
git add .
git commit -m "commit inicial"
git branch -M main
cd ..

# ahora lo convertimos en bare (esto simula "crear el repo en GitHub" a partir de código que ya tenían)
git clone --bare repo1 remoto.git
```

Un repo "bare" no tiene directorio de trabajo (*working directory*), solo el historial. `git clone --bare` trae *todo* el historial que ya existía en `repo1`. 

Nota *remoto.git* es un directorio!

## 2. Alumno1 clona el repositorio *remoto.git*

```bash
git clone remoto.git alumno1
cd alumno1
git config user.name "Alumno1"
git config user.email "alumno1@ejemplo.com"
cat saludo.txt
git log --oneline
cd ..
```

## 3. Alumno2 clona el mismo remoto

```bash
git clone remoto.git alumno2
cd alumno2
git config user.name "Alumno2"
git config user.email "alumno2@ejemplo.com"
cat saludo.txt
git log --oneline
cd ..
```

## 4. Alumno2 modifica y pushea primero

```bash
cd alumno2
```

Editen `saludo.txt`, cambien el texto (ej: `Hola gente`).

```bash
git status
git commit -am "alumno2 cambia el saludo"
git push origin main
cd ..
```

## 5. Alumno1 modifica lo mismo, sin saber del push de alumno2

```bash
cd alumno1
```

Editen `saludo.txt` con otro texto distinto (ej: `Hola a todos`).

```bash
git status
git commit -am "alumno1 cambia el saludo"
git push origin main
```
¿Porqué -a en el commit?

Esto va a fallar con `[rejected] (fetch first)`.

## 6. Alumno1 hace pull

```bash
git pull --no-rebase origin main
git status
cat saludo.txt
```
¿porqué --no-rebase? ¿a dónde apunta *origin*?

Va a aparecer el conflicto, con los marcadores `<<<<<<<` `=======` `>>>>>>>`.

## 7. Resolver y sincronizar

Editen `saludo.txt`, saquen los marcadores, dejen el contenido final.

```bash
git add saludo.txt
git commit -m "resuelvo conflicto"
git push origin main
git log --oneline --all --graph
cd ..
```

## 8. Alumno2 se sincroniza

```bash
cd alumno2
git pull --no-rebase origin main
cat saludo.txt
```

Luego los *working directories* deberían ser iguales. Para pensar: ¿qué comandos tiene la terminal para verificar esto?
