# Ejercicio solución de conflicto en merge

En 
`https://github.com/tguozden/misterio.git` preparé un repositorio con dos ramas. La idea es que lo clonen a un repositorio local de ustedes y *fusionen* (mergeen) la rama que hay a la rama principal.



Chusmeen la estructura de ramas con 
```
git branch --all
```
y

```
git log --oneline --all --graph
```
(el flag --all es para ver el resto de las ramas)

luego creen un repositorio vacío en su github, por ejemplo `https://github.com/jaimito/misterio_resuelto.git`

en el respositorio de ustedes cambien la dirección de la nube con
```bash
git remote set-url origin https://github.com/jaimito/misterio_resuelto.git
```

y hagan *push*


## Otra manera

Observen que origin es un sobrenombre de la nube. Es más podrían agregar otra nube

```
git remote add minube https://github.com/jaimito/misterio_resuelto.git
```

y después 
```
git push minube main
```
Fíjense las direcciones que tienen con `git remote -v`

# Por último
Suban su repositorio `https://github.com/franquito/misterio_resuelto.git` a la siguiente planilla:
<https://docs.google.com/spreadsheets/d/1h59NYiwisy13HDq_L8n8x-CoOYWQeIEqozI9pDa4f18/edit?usp=sharing>
