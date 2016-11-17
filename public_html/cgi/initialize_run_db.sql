--CREATE DATABASE mile_run;
-- To start SQL shell: psql -U postgres  -d mile_run

/*CREATE TYPE runner_choice AS ENUM ('Jacob', 'Benny', 'Hershey');

CREATE TYPE min_sec AS (
   min int,
   sec int
); */


drop table results;

-- Time is stored in seconds
CREATE TABLE results(
   id		    SERIAL PRIMARY KEY,
   runner_name  varchar(20)    NOT NULL,
   distance     real      NOT NULL,
   date         date,
   run_time     int
);

--insert into results(runner_name,date,run_time) values ('Jacob','None','23:22')"

insert into results(runner_name,distance,date,run_time) values ('Jacob', 1.0, '16-11-2016',466);
insert into results(runner_name,distance,date,run_time) values ('Benny', 1.0, '16-11-2016', 545);

select * from results;
