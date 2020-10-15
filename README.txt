

PostgreSQL requirements:

1) JSON source named data.json with key data and a list of JSON objects as a value.
The program will ask you to insert the filepath endinging with data.json and do its job.


2)The program works with a target database "postgres" which has 3 columns:
-key - primary key, not null, char
-value - char
-ts - char
Below is the SQL code to create a table called "etl_db" in the default tablespace:

CREATE TABLE public.etl_db
(
    value character varying COLLATE pg_catalog."default",
    key character varying COLLATE pg_catalog."default" NOT NULL,
    ts character varying COLLATE pg_catalog."default",
    CONSTRAINT etl_db_pkey PRIMARY KEY (key)
)

TABLESPACE pg_default;

ALTER TABLE public.etl_db
    OWNER to postgres;