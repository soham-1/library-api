# initial setup

flask db init <br>
flask db migrate - adds migrations into alembic table <br>
flask db upgrade - commits the changes into database

### after a bad migration we may not be able to upgrade or make any further migrations, then use
```sh
flask db stamp head
flask db migrate
flask db upgrade
```

### if the error still persists, delete the migrations folder and clear the migration records from alembic table using 
```"drop table alembic_version;"``` <br>
This will clear all migration but preserve the rest of data.
Then reinitialize the whole migration.

the [sql_test.py](./sql_test.py) folder contains some useful commands to list all tables in database, details of table, delete alembic