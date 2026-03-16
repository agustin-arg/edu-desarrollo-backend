# Práctica con Docker Ubuntu

## Descripción

Este proyecto contiene un Dockerfile creado para practicar comandos de terminal dentro de un contenedor Ubuntu, enfocándose principalmente en el uso del gestor de paquetes `apt`.

## Consideraciones Iniciales

El contenedor está configurado sin un proceso activo persistente, por lo que se cierra inmediatamente después de su ejecución. Para mantenerlo activo y acceder a su terminal interactiva, es necesario utilizar el flag `-it`:

```bash
docker run -it ubuntu
```

## Comandos Practicados

### 1. Construcción y Ejecución del Contenedor

```bash
# Construir la imagen
docker build -t ubuntu .

# Ejecutar el contenedor de forma interactiva
docker run -it --name test1 ubuntu
```

#### Problema Encontrado

Al ejecutar el comando de construcción, se generó el siguiente error:

```
failed to build: failed to solve: ubuntus:24.04: failed to resolve source metadata
for docker.io/library/ubuntus:24.04: pull access denied, repository does not exist
or may require authorization: server message: insufficient_scope: authorization failed
```

**Causa:** Error tipográfico en el nombre de la imagen base dentro del Dockerfile (`ubuntus` en lugar de `ubuntu`).

**Solución:** Corregir el nombre de la imagen en el Dockerfile.

---

## Gestión de Paquetes con APT

### Verificación de Versión

```bash
apt --version
# Salida: apt 2.8.3 (amd64)
```

### Actualización de Repositorios

```bash
apt update
```

> **Nota importante:** A diferencia de Ubuntu en sistemas nativos, no es necesario utilizar `sudo` en contenedores Docker, ya que por defecto se ingresa como usuario `root` con todos los permisos necesarios.

---

## Instalación de Python 3

### Comando de Instalación

```bash
apt install python3
```

### Problemas y Soluciones

#### Error: Paquete no encontrado

**Error obtenido:**

```
E: Unable to locate package python3
```

**Causa:** No se actualizó la lista de repositorios antes de intentar instalar el paquete.

**Solución:** Ejecutar `apt update` antes de cualquier instalación.

#### Confirmación Interactiva

Durante la instalación, el sistema solicita confirmación manual. Para automatizar este proceso, agregar el flag `-y`:

```bash
apt install python3 -y
```

#### Configuración de Zona Horaria

La instalación solicita especificar la zona horaria de forma interactiva. Para automatizar esto en un Dockerfile, se recomienda utilizar la siguiente variable de entorno:

```dockerfile
ENV DEBIAN_FRONTEND=noninteractive
```

Esta configuración silencia todas las solicitudes interactivas, utilizando valores predeterminados.

Alternativamente, se puede establecer una zona horaria específica:

```dockerfile
RUN ln -fs /usr/share/zoneinfo/America/Argentina/Cordoba /etc/localtime
```

---

## Instalación de PIP

### Comando de Instalación

```bash
apt install python3-pip
```

### Observaciones

- Intenté ejecutar `apt install pip`, que técnicamente es incorrecto, ya que el nombre del paquete en Ubuntu es `python3-pip`.
- Sin embargo, `apt` reconoció automáticamente la intención y seleccionó `python3-pip` sin intervención adicional.
- **Requisito:** Python 3 debe estar instalado previamente.

---

## Desinstalación de Paquetes

Para remover Python del sistema:

```bash
apt remove python3
```

---

