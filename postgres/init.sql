


-- Connect to default postgres database first
\connect postgres;

-- 1️⃣ Create database if it does not exist
DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_database
      WHERE datname = 'pg_testdb_new'
   ) THEN
      EXECUTE 'CREATE DATABASE pg_testdb_new';
   END IF;
END
$$;

-- 2️⃣ Switch to target database
\connect pg_testdb_new;

-- 3️⃣ Enable vector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- 4️⃣ Create table if it does not exist
CREATE TABLE IF NOT EXISTS job_embeddings (
    id SERIAL PRIMARY KEY,
    serial_no FLOAT,
    content TEXT,
    embedding VECTOR(1024)
);







-- CREATE EXTENSION IF NOT EXISTS vector;

-- CREATE TABLE IF NOT EXISTS job_embeddings (
--     id SERIAL PRIMARY KEY,
--     serial_no FLOAT,
--     content TEXT,
--     embedding VECTOR(1024)
-- );

