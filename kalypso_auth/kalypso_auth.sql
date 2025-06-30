-- Crear la base de datos (si no la tienes aún)
CREATE DATABASE kalypso_db;

-- Conectar a la base de datos
\c kalypso_db;

-- Tabla de usuarios
CREATE TABLE users (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- Tabla de intentos de login
CREATE TABLE login_attempts (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    user_id BIGINT REFERENCES users(id),
    username TEXT,
    attempt_time TIMESTAMPTZ DEFAULT now(),
    success BOOLEAN NOT NULL
);
