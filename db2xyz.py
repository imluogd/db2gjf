import sqlite3

conn=sqlite3.connect("prod-2.db")
cursor=conn.cursor()


nrow=cursor.execute("SELECT COUNT(*) FROM prod").fetchone()[0]
print("Total number of rows: ",nrow)
natom=cursor.execute("SELECT natom from prod").fetchone()[0]
print(natom)
# for i in range(1,nrow+1):
#     geom_i=cursor.execute("select geom from prod-2 where id={0}".format(i))
#     print(i,geom_i.fetchone()[0])
    
for row in cursor.execute("SELECT name,formula, geom FROM prod"):
    #print(row[0],row[1],row[2])
    with open(row[0]+"_"+row[1]+".xyz","w") as f:
        f.write(str(natom)+"\n")
        f.write(str(row[1])+"\n")
        f.write(str(row[2])+"\n")
