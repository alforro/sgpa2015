
drop database sgpa;
drop user sgpa;
create user sgpa password 'sgpa';
alter user sgpa with superuser;

create database sgpa with owner sgpa;

\q

