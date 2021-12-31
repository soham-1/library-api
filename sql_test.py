import sqlite3

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()
# cursor.execute("select name from sqlite_master where type='table';")
cursor.execute("select * from pragma_table_info('Book') as tblInfo;")
# cursor.execute("DROP TABLE alembic_version;")
print(cursor.fetchall())