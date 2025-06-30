# Pokémon Showdown Sim

Simulador de batallas Pokémon inspirado en Showdown, que permite:

✅ Listar todos los Pokémon con paginación.
✅ Buscar Pokémon por nombre y por tipo.
✅ Seleccionar dos Pokémon para simular una batalla en un modal animado.
✅ Mostrar barras de vida con cambios de color según la salud del Pokémon.

Este proyecto utiliza:

* **Backend:** FastAPI (Python).
* **Frontend:** HTML, TypeScript/JavaScript, Bootstrap.
* **Consumo de API:** [PokeAPI](https://pokeapi.co/).

---

## Estructura del proyecto

## Requisitos previos

* **Python 3.10+** (recomendado)
* **Node.js 18+** (para compilar TypeScript si deseas modificar `app.ts`)


## Cómo inicializar el proyecto

### 1️⃣ Inicializar Backend

1. Abre una terminal y navega al directorio del backend:

   ```bash
   cd backend
   ```

2. Crea un entorno virtual:

   ```bash
   python -m venv env
   ```

3. Activa el entorno virtual:

     ```bash
     env\Scripts\activate
     ```
4. Instala las dependencias:

   ```bash
   pip install fastapi uvicorn httpx
   ```

5. Ejecuta el servidor:

   ```bash
   uvicorn main:app --reload
   ```


### 2️⃣ Inicializar Frontend

1. Abre otra terminal y navega al directorio del frontend:

   ```bash
   cd frontend
   ```

2. Si necesitas compilar `app.ts`:

   * Instala TypeScript de manera global (si no lo tienes):

     ```bash
     npm install -g typescript
     ```
   * Compila el archivo:

     ```bash
     tsc app.ts
     ```
   * Esto generará/actualizará `app.js`.

3. Abre `index.html` directamente en tu navegador o usa Live Server (VS Code) para actualizar automáticamente al guardar cambios.

---

## Uso

✅ Busca Pokémon por nombre o filtra por tipo.
✅ Haz clic en dos Pokémon para seleccionarlos.
✅ Pulsa **Iniciar Batalla** para abrir el modal y ver la batalla animada.


