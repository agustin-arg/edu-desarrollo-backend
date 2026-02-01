# Gestión de Imágenes Docker: Guardar y Cargar

## Guardar una imagen de Docker

**Comando:** `docker save`

**Descripción:** Permite guardar una o más imágenes a un archivo tar.

**Uso:** `docker save -o <nombre-de-archivo.tar> <nombre-de-imagen>`

**Ejemplo:**
```bash
docker save -o ubuntu.tar ubuntu:latest
```
Este comando guarda la imagen de Ubuntu con la etiqueta "latest" en un archivo tar llamado `ubuntu.tar`.

---

## Recuperar o cargar una imagen de Docker

**Comando:** `docker load`

**Descripción:** Permite cargar una imagen desde un archivo tar.

**Uso:** `docker load -i <nombre-de-archivo.tar>`

**Ejemplo:**
```bash
docker load -i ubuntu.tar
```
Este comando carga una imagen desde el archivo `ubuntu.tar` al sistema local de Docker.

---

**Nota:** Estos comandos son muy útiles para compartir imágenes entre diferentes máquinas o para hacer backups de tus imágenes locales.
