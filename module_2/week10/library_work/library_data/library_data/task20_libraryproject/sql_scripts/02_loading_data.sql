copy authors from '/var/lib/postgresql/imports/authors.csv' with (format csv, header true);

copy books from '/var/lib/postgresql/imports/books.csv' with (format csv, header true);

copy bookorders from '/var/lib/postgresql/imports/bookorders.csv' with (format csv, header true);

copy borrowedhistory from '/var/lib/postgresql/imports/borrowhistory.csv' with (format csv, header true, null 'NULL');

copy librarystaff from '/var/lib/postgresql/imports/librarystaff.csv' with (format csv, header true);

copy departments from '/var/lib/postgresql/imports/departments.csv' with (format csv, header true);
 
copy members from '/var/lib/postgresql/imports/members.csv' with (format csv, header true, delimiter ',', quote '"',  null '');


select * from authors limit 10;

select * from book limit 10;

select * from bookorders limit 10;

select * from borrowedhistory limit 10;

select * from librarystaff limit 10;

select * from departments limit 10;

select * from members limit 10;