## Keywords
**Table:** A table is a collection of related data held in a table format within a database. In relational databases, and flat file databases, a table is a set of data elements (values) using a model of vertical columns (identifiable by name) and horizontal rows, the cell being the unit where a row and column intersect.

**Trigger:** A trigger is a stored procedure in database which automatically invokes whenever a special event in the database occurs.

**Views:** A database view is a searchable object in a database that is defined by a query.

**Function:** The Database functions perform basic operations, such as Sum, Average, Count, etc., and additionally use criteria arguments, that allow you to perform the calculation only for a specified subset of the records in your Database.

**Domain:** A database domain, at its simplest, is the data type used by a column in a database. This data type can be a built-in type (such as an integer or a string) or a custom type that defines constraints on the data.

**Sequence:** A sequence is a database object which allows users to generate unique integer values.

(Source: First Google Result)

---

## About Database
The DVD rental database represents the business processes of a DVD rental store. The DVD rental database has many objects including:
- 15 tables
- 1 trigger
- 7 views
- 8 functions
- 1 domain
- 13 sequences

Tables:
- actor — contains actors data including first name and last - name.
- film — contains films data such as title, release year, length, rating, etc.
- film_actor — contains the relationships between films and actors.
- category — contains film’s categories data.
- film_category — containing the relationships between films and categories.
- store — contains the store data including manager staff and address.
- inventory — stores inventory data.
- rental — stores rental data.
- payment — stores customer’s payments.
- staff — stores staff data.
- customer — stores customer’s data.
- address — stores address data for staff and customers
- city — stores the city names.
- country — stores the country names.
- language — stores the language names.

ER Diagram:
![ERD](./assets/ERD.jpg)

---