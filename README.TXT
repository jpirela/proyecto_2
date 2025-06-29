# Auth-Flow: Aplicación de Autenticación con Expo y Backend Node.js

## 📌 Descripción

Proyecto de autenticación completo con:
- Frontend móvil desarrollado con **Expo (React Native)**
- Backend API desarrollado con **Node.js y TypeScript**
- Sistema de autenticación con registro y login

## 🚀 Características principales

### Frontend (Expo)
- Navegación entre pantallas
- Formularios validados
- Diseño responsive

### Backend (Node.js)
- API RESTful
- Base de datos SQL (MSSQL)
- Sistema de autenticación seguro
- Endpoints protegidos
- Validación de datos

## 📂 Estructura del proyecto
proyecto_2/
├── auth-flow/ # Frontend Expo
│ ├── app/ # Componentes principales
│ ├── assets/ # Recursos multimedia
│ ├── constants/ # Constantes de la app
│ ├── Screens/ # Pantallas de la aplicación
│ └── ... # Otros archivos de configuración
│
├── auth-flow-back/ # Backend Node.js
│ ├── src/
│ │ ├── config/ # Configuraciones
│ │ ├── modules/ # Módulos del backend
│ │ │ └── auth/ # Lógica de autenticación
│ │ └── db.ts # Conexión a base de datos
│ └── ... # Otros archivos de configuración
└── ...

text

## 🛠️ Requisitos del sistema

- Node.js v16+
- npm v8+ o yarn
- Expo CLI instalado globalmente
- SQL Server (para backend)

## ⚙️ Configuración inicial

### Frontend
```bash
cd auth-flow
npm install
expo start
Backend
bash
cd auth-flow-back
npm install
# Configurar variables de entorno en .env
npm run dev
🔧 Variables de entorno (Backend)
Crear archivo .env en auth-flow-back con:

🏗️ Estructura de módulos principales
Módulo de Autenticación (/modules/auth)
index.ts: Exporta todos los controladores

auth.controller.ts: Maneja lógica de endpoints

auth.interfaces.ts: Tipos TypeScript

auth.service.ts: Lógica de negocio

📜 Scripts disponibles
Frontend
bash
npm start       # Inicia el servidor de desarrollo
npm run android # Ejecuta en emulador Android
npm run ios     # Ejecuta en simulador iOS
Backend
bash
npm run dev     # Modo desarrollo (con nodemon)
npm run build   # Compila TypeScript
npm start       # Inicia en producción