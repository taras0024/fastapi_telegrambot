SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

------------------------------------------------- botuser --------------------------------------------------------------
CREATE ROLE botuser PASSWORD 'kc6r&E1Kdu1M8rS!j' SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;
------------------------------------------------------------------------------------------------------------------------

----------------------------------------------- Main database ----------------------------------------------------------
DROP DATABASE IF EXISTS "magistr_db";
CREATE DATABASE "magistr_db";

GRANT ALL PRIVILEGES ON DATABASE "magistr_db" TO botuser;
ALTER DATABASE "magistr_db" OWNER TO botuser;
------------------------------------------------------------------------------------------------------------------------