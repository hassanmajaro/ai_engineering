# Library Database Management & Analysis

## Overview
This project is a PostgreSQL-based Library Database for data analysis.  
It was developed as part of the AI Engineering Fellowship.

The system manages **books, members, staff, departments, and borrowing records**.
<!-- and performs data cleaning and analytical operations directly from SQL and Python. -->

---

## Features
- Relational database schema with 7 interconnected tables.
- Data imported from CSV files using `\COPY` and validated with constraints.
<!-- - Python integration for:
  - Data wrangling using **pandas**
  - Data visualization using **seaborn** and **matplotlib**
  - Query automation using **psycopg2**
- Cleaned datasets and insights exported for reporting. -->

---

## Database Schema
**Tables:**
- Authors  
- Books  
- Members  
- Departments  
- LibraryStaff  
- BorrowedHistory  
- BookOrders  

**Relationships:**
- Books ↔ Authors (`author_id`)
- LibraryStaff ↔ Departments (`dept_id`)
- BorrowedHistory ↔ Books & Members
- BookOrders ↔ Books

---
