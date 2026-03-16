# GitHub CLI en contenedor Ubuntu

Práctica de la herramienta GitHub CLI usando la imagen de Ubuntu.

---

## 1. Crear el contenedor

```bash
docker run -it --name gh ubuntu:latest
```

---

## 2. Instalar GitHub CLI

Siguiendo la [documentación oficial](https://github.com/cli/cli), se ejecutó el siguiente comando de instalación. Como el contenedor corre con el usuario `root`, no es necesario usar `sudo`.

```bash
(type -p wget >/dev/null || (apt update && apt install wget -y)) \
&& mkdir -p -m 755 /etc/apt/keyrings \
&& out=$(mktemp) && wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg \
&& cat $out > /etc/apt/keyrings/githubcli-archive-keyring.gpg \
&& chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
&& mkdir -p -m 755 /etc/apt/sources.list.d \
&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" > /etc/apt/sources.list.d/github-cli.list \
&& apt update \
&& apt install gh -y
```

---

## 3. Autenticación

```bash
gh auth login
```

Se seleccionaron las siguientes opciones:

- **Plataforma:** GitHub.com
- **Protocolo Git:** SSH
- **Método de autenticación:** Personal Access Token

> El token se genera en https://github.com/settings/tokens. Los scopes mínimos requeridos son `repo` y `read:org`.

---

## 4. Crear un repositorio

```bash
gh repo create
```

Otra forma equivalente con flags:

```bash
gh repo create mi-nuevo-repo --public --description "Repo desde CLI" --clone
```

---

## 5. Clonar el repositorio

Al crear el repositorio, `gh` intentó clonarlo automáticamente pero falló porque `git` no estaba instalado en el contenedor. Se resolvió instalándolo y luego clonando manualmente:

```bash
apt install git
gh repo clone https://github.com/agustin-arg/test2repo
```

---

## 6. Gestión de Issues y Pull Requests

- **Crear un issue:**

  ```bash
  gh issue create
  ```

  Solicita título y descripción de forma interactiva.

- **Ver estado de issues:**
  ```bash
  gh issue status
  ```
  Muestra los issues asignados, abiertos y en los que se fue mencionado.
