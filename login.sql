-- Database: login

-- DROP DATABASE IF EXISTS login;

CREATE DATABASE login
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
	CREATE TABLE users (
    id bigint primary key generated always as identity,
    username text unique not null,
    password_hash text not null,
    email text unique not null,
    created_at timestamp with time zone default now(),
    last_login timestamp with time zone
);