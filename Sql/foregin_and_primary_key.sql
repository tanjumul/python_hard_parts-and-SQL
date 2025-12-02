--table 1 

create table customers (

cust_id serial PRIMARY KEY,
fanme VARCHAR(100) not null
);

insert into customers (fname) values ('tanjumul'), ('tanvir') , ('garal'),('gauro');

--table 2

create table orders ( 

ord_id serial primary key,
ord_date date not null ,
price NUMERIC not null , 
cust_id integer not null, 

Foreign Key (cust_id) REFERENCES customers (cust_id)

);

insert into orders (cust_id,ord_date,price) values 
('2','2025-01-24',260),('1','2025-01-24',260),
('3','2025-01-24',260),('2','2025-01-24',460),
('1','2025-01-24',760),('3','2025-01-24',660),
('1','2025-01-24',260),('4','2025-01-24',360);