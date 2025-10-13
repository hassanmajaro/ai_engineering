--Question 1. --> 
--list all books published after 2015 along with their authors' names.
select 
    books.title, 
    books.authors_id, 
    authors.author_name, 
    books.date_of_publication
from 
    books
join 
    authors on books.authors_id = authors.authors_id
where
    extract (year from books.date_of_publication) > 2015;


--Question 2.--> 
--find all members who joined in the last 2 years and have a 'premium' membership.
select 
    members.membership_id, 
    members.member_name, 
    members.date_of_membership, 
    members.type_of_membership
from 
    members
where 
    members.date_of_membership > '2021-12-31' and members.type_of_membership = 'Premium';

--Question 3.--> 
--display the total number of books written by each author, ordered by count (descending).
select 
    authors.authors_id, 
    authors.author_name, 
    authors.number_of_books_written
from 
    authors
order by 
    number_of_books_written 
desc;


--Question 4.--> 
--show all currently borrowed books (books with no return date) along with the member's name and borrow date.
select 
    books.book_id, 
    books.title, 
    borrowedhistory.borrow_date,
    members.member_name, 
    borrowedhistory.membership_id, 
    borrowedhistory.return_date
from 
    borrowedhistory
join 
    books on books.book_id = borrowedhistory.book_id
join 
    members on members.membership_id = borrowedhistory.membership_id
where 
    borrowedhistory.return_date is null;

--Question 5.--> 
--list all library staff members working in the 'circulation' department.
select * from librarystaff
join 
    departments on departments.dept_id = librarystaff.dept_id
where 
    department_name = 'circulation'


--Question 6. -->
--calculate the total cost of all book orders placed in 2024, grouped by fulfillment status.
select 
    bookorders.fulfillment_status,
    sum(cost) as total_cost
from 
    bookorders
where
    extract (year from bookorders.order_date) = 2024
group by 
    fulfillment_status
order by 
    total_cost desc;


--Question 8. --> 
--identify members who have never borrowed a book.
select * from members
left join 
    borrowedhistory on members.membership_id =  borrowedhistory.membership_id
where 
    borrowedhistory.membership_id is null;


--Question 9. --> 
--show the average number of available copies per genre.
select 
    books.genre,
    round(avg(books.available_copies),2) as avg_available_copies
from 
    books
group by 
    books.genre
order by 
    avg_available_copies asc;


--Question 10. --> 
--list all books that are currently overdue (borrowed more than 30 days ago with no return date).
select 
    books.book_id, 
    books.title, 
    members.member_name, 
    borrowedhistory.borrow_date, 
    borrowedhistory.return_date
from 
    borrowedhistory
join 
    books on borrowedhistory.book_id = books.book_id
join 
    members on borrowedhistory.membership_id = members.membership_id
where 
    borrowedhistory.return_date is null and borrowedhistory.borrow_date < date '2024-03-30' - interval '30 days'
order by
    borrowedhistory.borrow_date asc;


--ADVANCED QUERIES
--Question 11.-->
--create a query that shows each department's staff count and the average tenure (years) of staff in that department.
select 
    departments.department_name,
    count(librarystaff.staff_id) as staff_count,
    round(avg(extract(year from age(current_date, librarystaff.hire_date))), 2) as average_tenure_years
from
    librarystaff
join 
    departments on librarystaff.dept_id = departments.dept_id
group by 
    departments.department_name
order by 
    staff_count 
desc;

--Question 12.--> 
--generate a report showing monthly borrowing trends for the past year (count of books borrowed per month).
select
    to_char(borrow_date, 'month') as month_name,
    extract(year from borrow_date) as year,
    count(*) as total_borrowed_books
from 
    borrowedhistory group by year, 
    month_name, 
    extract(month from borrow_date) order by year, 
    extract(month from borrow_date);

--Question 13.-->  
--find authors whose books have been borrowed more than 10 times in total, along with their most popular book.
select 
    authors.author_name, books.title as most_popular_book,
    count(borrowedhistory.book_id) as total_borrows
from 
    authors
join 
    books on books.authors_id = authors.authors_id
join 
    borrowedhistory on borrowedhistory.book_id = books.book_id
group by 
    authors.author_name, books.title having count(borrowedhistory.book_id) > 10
order by 
    total_borrows 
desc;

--Question 14.--> 
--calculate the total revenue from book orders per supplier, showing only suppliers with orders exceeding $5,000.
select 
    bookorders.supplier_name,
    sum(cost * quantity) as total_revenue
from 
    bookorders
group by 
    supplier_name having sum(cost * quantity) > 5000
order by 
    total_revenue 
desc;


--Question 15.--> 
--create a complex query that identifies "inactive" members (those who haven't borrowed a book in the last 6 months) who have a premium membership.
select 
    members.type_of_membership, 
    members.member_name, 
    members.membership_id, 
    members.status
from 
    members
left join 
    borrowedhistory on borrowedhistory.membership_id = members.membership_id
where 
    members.type_of_membership = 'Premium' and (borrowedhistory.borrow_date is null or borrowedhistory.borrow_date < date '2024-03-30' - interval '6 months')
group by 
    members.type_of_membership, 
    members.member_name, 
    members.membership_id, 
    members.status
