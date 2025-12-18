CREATE TABLE if not exists tables (
    number int primary key,
    seats int,
    is_Free boolean
);

create table if not exists reservations (
    day DATE,
    timeFrom DATE,
    timeTo DATE,
    tableNumber int foreign key,
    id int primary key,
    pin int,
)

insert  into  tables values (1, 4, true), (2, 4, true), (3, 5, false);

select * from tables
where is_Free == true