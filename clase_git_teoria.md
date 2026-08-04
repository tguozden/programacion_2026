# Clase: Introducción a git y GitHub (Unidad 17)

**Objetivo de la clase:** que cada uno termine con un repositorio propio en GitHub, con al menos un commit y un push hechos por ellos mismos. Ese va a ser el repo que van a usar para entregar TPs de acá en adelante.


---
## 1. ¿Para qué?

A veces nos encontramos con archivos que así:
```
trabajo_final.py
trabajo_final_v2.py
trabajo_final_v2_BUENO.py
trabajo_final_v2_BUENO_ahora_si.py
trabajo_final_v2_BUENO_ahora_si_DEFINITIVO.py
```

Eso es control de versiones hecho a mano: no sabés qué cambió entre versión y versión, ocupa espacio de 5 archivos, y no permite colaborar sobre el mismo archivo.

**git** resuelve esto: guarda el *historial* de cambios de tu código, permite volver atrás, comparar versiones, y trabajar en paralelo con otras personas sin pisarse.

---
## 2. Historia

Git fue creado por Linus Torvalds el 3 de abril de 2005 debido a la revocación de la licencia gratuita del sistema de control de versiones propietario BitKeeper, el cual se usaba para el desarrollo del kernel de Linux. En poco más de una semana, Torvalds diseñó una herramienta libre, rápida y distribuida que cambió para siempre la programación.

### Origen y Creación
El problema de la licencia: La comunidad de Linux usaba BitKeeper gratis, pero tras un conflicto sobre ingeniería inversa, la empresa dueña canceló el acceso gratuito.
### El nacimiento en 10 días
Torvalds se enojó y decidió programar su propio sistema enfocado en la velocidad y en evitar los errores de otras herramientas.
### El nombre
Linus le puso Git (una grosería en inglés británico que significa tipo desagradable o molesto) bromeando con que él mismo era un egoísta y nombraba a sus proyectos según su propia personalidad.

### Otro versionador: Mercurial
Nació en abril de 2005, la misma semana que Git y con el mismo propósito exacto: reemplazar a BitKeeper para gestionar el código de Linux. Aunque técnicamente era excelente y para muchos más fácil de usar que Git, terminó perdiendo la batalla comercial y quedando relegado a un nicho. 
### La historia de Mercurial (Hg) El duelo de 2005
 Cuando BitKeeper canceló sus licencias libres, Matt Mackall lanzó Mercurial pocos días antes de que Linus Torvalds presentara Git. Ambos sistemas resolvían el mismo problema de forma distribuida.Simplicidad vs. Fuerza bruta: Mercurial se diseñó en Python y C, priorizando una interfaz intuitiva, comandos limpios y una documentación impecable. Git, por el contrario, nació como un conjunto de herramientas internas de bajo nivel muy complejas, pero extremadamente rápidas.
### El "Efecto GitHub"
 La razón principal por la que Mercurial no prosperó a gran escala fue la comunidad. En 2008 nació GitHub, que facilitó enormemente el uso social de Git. Mercurial tuvo su equivalente llamado Bitbucket, pero no logró el mismo impacto masivo y, años después, dejó de dar soporte a Mercurial para centrarse solo en Git.
### ¿Qué pasó con él?
No está completamente muerto, pero tiene apenas cerca del 2% de cuota de mercado corporativo

---
## 3. Instalación y configuración rápida

Chequeá si ya tenés git instalado:

```bash
git --version
```

Si no lo tenés: [git-scm.com/downloads](https://git-scm.com/downloads)

Configuración inicial (una sola vez por máquina) — git necesita saber quién sos para "firmar" tus commits:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@ejemplo.com"
```

**Chequeo:**
```bash
git config --list
```


---
## BLOQUE A — git local

Todo lo que viene ahora pasa **sin internet**. Es git hablando solo con tu carpeta.


### 3.1 `git init` — crear un repositorio

Un repositorio ("repo") es una carpeta que git está vigilando. Convertir una carpeta común en un repo:

```bash
mkdir mi_primer_repo
cd mi_primer_repo
git init
```

Esto crea una carpeta oculta `.git/` adentro — ahí es donde git guarda TODO el historial. Si borrás esa carpeta, perdés el historial (pero no tus archivos actuales).

**Ejercicio 1:** Creen la carpeta, hagan `git init`, y con `ls -la` (o `dir` en Windows) confirmen que apareció `.git/`.


### 3.2 El ciclo de vida de un archivo: `git status`

Creemos un archivo:

```bash
echo "print('hola mundo')" > saludo.py
git status
```

git nos va a decir que `saludo.py` es un archivo **untracked** (no rastreado) — existe en la carpeta, pero git todavía no le está prestando atención.

`git status` es el comando que más van a usar en su vida. Úsenlo después de cada paso, sin miedo.


### 3.3 `git add` — la zona de staging

```bash
git add saludo.py
git status
```

Ahora el archivo pasó a estar **staged** (en el "área de preparación"). Esto NO es guardar el cambio todavía — es decirle a git "este es el cambio que quiero incluir en la próxima foto".

Para agregar todo lo que cambió de una:
```bash
git add .
```

**¿Por qué existe este paso intermedio?** Porque te permite armar commits prolijos: si modificaste 5 archivos pero en realidad son dos cambios lógicos distintos, podés hacer `git add` de a grupos y hacer dos commits separados, en vez de uno gigante que mezcla todo.


### 3.4 `git commit` — la foto

```bash
git commit -m "Agrego script de saludo"
```

Un commit es una **foto** (snapshot) del estado de tus archivos en ese momento, con un mensaje que explica qué cambió. Cada commit queda guardado para siempre en el historial (a menos que hagan cosas raras para borrarlo).

**Buenas prácticas de mensajes de commit:**
- Verbo en presente/infinitivo: "Agrego función de validación", no "agregué" ni "agregando"
- Corto y descriptivo — qué cambió
- Un commit = un cambio lógico coherente (no mezclar 10 cosas distintas en un commit gigante)

**Ejercicio 2:** Modifiquen `saludo.py` (agreguen una línea más), y hagan `add` + `commit` de nuevo con un mensaje distinto.


### 3.5 `git log` y `git status`

```bash
git log --oneline
git status
```

`status` dice en qué rama estás y si hay cambios sin commitear. `log` muestra el historial de commits.

**Nota — HEAD attached/detached:** `HEAD` normalmente apunta a una rama (`attached`). Si hacés `git checkout <hash_de_commit>` (en vez de un nombre de rama), `HEAD` pasa a apuntar directo a ese commit — estado `detached HEAD`. `git status` te avisa: `HEAD detached at <hash>`. Ahí se puede mirar código viejo, pero si commiteás en ese estado y después volvés a una rama, esos commits quedan "sueltos" y se pueden perder. Salir: `git checkout main`.


---
## BLOQUE B — GitHub (remoto)

Ahora sí: vamos a llevar ese repo a la nube.


### 4.1 Crear cuenta y repositorio en GitHub

1. Crear cuenta en [github.com](https://github.com) (si no tienen)
2. Click en "New repository"
3. Ponerle un nombre (ej: `programacion-1-2026`)
4. **No** tildar "Initialize with README" — vamos a subir el repo que ya tenemos local, así que preferimos que el remoto empiece vacío, para evitar conflictos por un README que no existe de nuestro lado

GitHub les va a mostrar un par de comandos para conectar el repo local con el remoto. Son básicamente los siguientes dos:


### 4.2 `git remote add` — conectar local con remoto

```bash
git remote add origin https://github.com/USUARIO/repo.git
git remote -v
```

- `origin` es solo un alias (convención, no una palabra reservada) para "ese remoto".
- `add`: cuando el remoto **no existe** todavía.
- `set-url`: cuando el remoto **ya existe** y querés cambiarle la URL.
```bash
git remote set-url origin https://github.com/USUARIO/repo.git
```


### 4.3 `git push` — subir los commits

```bash
git push -u origin main
```

- `origin` = a qué remoto. `main` = qué rama. Un repo puede tener varias ramas; git necesita saber cuál sincronizar.
- `-u` (`--set-upstream`): asocia la rama local con la remota, una sola vez. Después alcanza con `git push` a secas.
- `push` sube solo los commits nuevos de **esa rama**, no "todo el repo". Otras ramas con commits sin pushear no se suben (`git branch -vv` para chequear estado de cada rama).

**Ejercicio 3:** Hagan push y verifiquen en GitHub que apareció.


### 4.3.1 Autenticación — por qué el `push` les puede fallar

Al hacer `git push` por HTTPS, GitHub les va a pedir usuario y contraseña. **Importante: desde 2021 GitHub no acepta la contraseña de la cuenta para esto.** Si la ponen, les va a tirar error de autenticación (`Support for password authentication was removed`), y ahí se traban 10 minutos sin entender por qué si la contraseña es correcta.

Hay dos formas de autenticarse correctamente. Para la clase de hoy alcanza con la primera:

**Opción 1 — Personal Access Token (PAT), la más rápida para hoy:**

1. En GitHub: `Settings` → `Developer settings` → `Personal access tokens` → `Tokens (classic)` → `Generate new token`
2. Marcar el permiso `repo` (acceso a repositorios)
3. Copiar el token generado (¡solo se muestra una vez!)
4. Al hacer `git push`, cuando pida contraseña, **pegan el token en lugar de la contraseña**

El sistema operativo suele guardarlo en caché (Keychain en Mac, Credential Manager en Windows) así que no lo van a tener que pegar cada vez.

**Opción 2 — SSH keys, más prolija para el resto del año (no imprescindible hoy):**

```bash
ssh-keygen -t ed25519 -C "tu-email@ejemplo.com"
cat ~/.ssh/id_ed25519.pub
```

Ese resultado se pega en GitHub: `Settings` → `SSH and GPG keys` → `New SSH key`. Después, la URL del remoto cambia de `https://github.com/...` a `git@github.com:...` (esa opción también aparece al crear el repo).

Con SSH configurado, no vuelven a tipear usuario/contraseña/token nunca más en esa máquina. Si tienen tiempo en la clase que viene, vale la pena migrar a esto — pero **hoy, con PAT alcanza**.


### 4.3.1.1 Clonar con token embebido (práctica)

```bash
git clone https://USUARIO:TOKEN@github.com/usuario/repo.git
```
o, ya clonado:
```bash
git remote set-url origin https://USUARIO:TOKEN@github.com/usuario/repo.git
```

**Al terminar conviene sacar el token:**
```bash
git remote set-url origin https://github.com/usuario/repo.git
git remote -v    # verificar que no queda el token
```


### 4.3.2 Visibilidad y colaboradores — quién puede ver o escribir


| | Público | Privado |
|---|---|---|
| ¿Quién lo ve? | Cualquiera con el link, sin necesidad de cuenta | Solo el dueño + quienes fueron invitados explícitamente |
| ¿Quién puede escribir (push)? | Solo el dueño (a menos que agregue colaboradores) | Solo el dueño (a menos que agregue colaboradores) |
| Uso típico acá | **Recomendado para los TPs de la materia** — así el profesor puede ver/clonar sin que cada alumno tenga que agregarlo como colaborador uno por uno | Si el alumno prefiere que no sea público (ej: no quiere que otros compañeros copien), pero entonces SÍ o SÍ tiene que agregar al profesor como colaborador, o el profesor no va a poder acceder |

**Ver o escribir no es lo mismo.** Que un repo sea público solo da permiso de **lectura** a cualquiera — nadie más puede hacer `push` salvo que sea agregado explícitamente como colaborador con permiso de escritura.

**Cómo agregar un colaborador (necesario solo si el repo es privado):**

`Settings` del repositorio → `Collaborators` → `Add people` → buscar por usuario de GitHub → elegir el nivel de permiso:

- **Read**: puede ver y clonar, no puede hacer push
- **Write**: puede ver, clonar y hacer push directo
- **Admin**: además puede cambiar configuración del repo, borrarlo, gestionar colaboradores

Para que el docente pueda corregir sin necesitar escribir nada, **Read alcanza y sobra**.

**Recomendación para la materia:** que todos los repos de entrega sean **públicos**. Va a ser lo más fácil para todos.


### 4.4 `git pull` y `git clone` — traer cambios

- **`git pull`**: trae y aplica cambios que estén en el remoto pero no en tu copia local (útil si trabajás desde dos máquinas, o alguien más subió algo)
- **`git clone`**: descarga un repositorio remoto completo por primera vez, creando la carpeta local con todo el historial incluido

```bash
git clone https://github.com/OTRO_USUARIO/algun_repo.git
```

**Ejercicio 4:** clonen el repo de un compañero (con su permiso) en otra carpeta, y hagan `git log` ahí para ver que el historial completo viajó con el clone.


---
## 5. El flujo completo, de una

Este es el ciclo que van a repetir todo el cuatrimestre:

```
modificás archivos
      ↓
git add .
      ↓
git commit -m "mensaje descriptivo"
      ↓
git push
```

Y cuando arrancás a trabajar en algo (o en otra máquina):

```
git clone <url>     (primera vez)
git pull             (siguientes veces)
```


---
## 6. Cierre y tarea

**Objetivos para hoy**

1. Cuenta de GitHub creada
2. Un repositorio propio creado (público) — este va a ser el repo de la materia, donde van a entregar TPs
3. Al menos 1 commit y 1 push hechos por ustedes mismos, no copiado de nadie
4. Mandarme el link a su repo por [canal que corresponda]

**para la próxima clase:** ¿qué pasa si dos personas hacen `push` sobre el mismo archivo, con cambios distintos? existen herramientas para lidiar con esto: branches y resolución de conflictos (merge).
