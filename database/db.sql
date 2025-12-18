CREATE TABLE if not exists tables (
    number int primary key,
    seats int,
    is_Free boolean
);

insert  into  tables values (1, 4, true), (2, 4, true), (3, 5, false);

select * from tables
where is_Free == true