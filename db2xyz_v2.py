import sqlite3
from os import mkdir,chdir


conn=sqlite3.connect("min.db")
cursor=conn.cursor()


nrow=cursor.execute("SELECT COUNT(*) FROM min").fetchone()[0]
print("Total number of rows: ",nrow)
natom=cursor.execute("SELECT natom from min").fetchone()[0]
print(natom)

mkdir("./min_xyz");chdir("./min_xyz")

for row in cursor.execute("SELECT name, geom FROM min"):
    with open(row[0]+".xyz","w") as f:
        f.write(str(natom)+"\n")
        f.write(str(row[0])+"\n")
        f.write(str(row[1])+"\n")
cursor.close()

