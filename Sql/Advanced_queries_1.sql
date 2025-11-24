drop table if EXISTS persons;

create table persons(
    p_id serial PRIMARY key,  
    name VARCHAR(50) not null ,
   city VARCHAR(50) not null ,
    age varchar(50) not null 
);


insert into persons( name , city , age ) values 
 ('Tanjumul' , 'Gaibandha','25'),
 ('Maria', 'Dhaka', '28'),
('John', 'Chittagong', '32'),
('Fatima', 'Sylhet', '22'),
('Raj', 'Khulna', '35'),
('Aisha', 'Rajshahi', '29'),
('David', 'Barisal', '31'),
('Sophia', 'Rangpur', '26');

select * from persons; 

alter table persons add column smoker varchar(20); 