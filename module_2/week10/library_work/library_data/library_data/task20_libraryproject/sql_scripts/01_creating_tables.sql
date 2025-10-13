create table Authors(
	author_id int primary key,
	author_name varchar not null,
	country_of_origin varchar not null,
	number_of_books_written int
	);

create table books(
	book_id int primary key,
	title varchar not null,
	author_id int references authors(author_id),
	genre varchar not null,
	date_of_publication date,
	publisher varchar not null,
	isbn varchar not null,
	language varchar not null,
	available_copies int,
	age_rating varchar not null
);


create type fulfillment_status as enum ('Processing', 'Pending', 'Fulfilled');
create table bookorders(
	order_id int primary key,
	order_date date,
	book_id int references books(book_id),
	cost decimal,
	quantity int,
	supply_date date,
	fulfillment_status fulfillment_status default 'Processing',
	supplier_name varchar not null
);

create type status as enum ('Active', 'Suspended');
create type type_of_membership as enum ('Student','Standard', 'Premium');
create type gender as enum('Male', 'Female');
create table members(
	membership_id int primary key,
	member_name varchar not null,
	gender gender not null,
	email_address varchar not null,
	phone_number varchar not null,
	age int,
	type_of_membership type_of_membership default 'Student',
	date_of_membership date,
	status status default 'Active'
);

create table borrowedhistory(
	borrowed_id int,
	book_id int references books(book_id),
	membership_id int references members(membership_id),
	borrow_date date,
	return_date date
);

create table departments(
	dept_id int primary key,
	department_name varchar not null,
	manager_name varchar not null
);

create table librarystaff(
	staff_id int primary key,
	staff_name varchar not null,
	job_title varchar not null,
	dept_id int references departments(dept_id),
	gender gender not null,
	address varchar not null,
	phone_number varchar not null,
	hire_date date,
	manager_id int
);






