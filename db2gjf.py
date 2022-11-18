import sqlite3

con = sqlite3.connect('ts.db')
cur = con.cursor()
table_name = cur.execute("SELECT name FROM sqlite_master").fetchone()
print('filename: '+table_name[0]+'.db')
natom = cur.execute("SELECT natom from ts").fetchone()[0]
print("number of atoms: ",natom)
for row in cur.execute("SELECT name, geom FROM ts ORDER BY name"):
    #print(row)
    name,geom  = row[0],row[1]
    filename = str(name) + '.gjf'
    #print (filename)
    with open(filename,'x') as f:
        f.write("# HF/3-21G\n");f.write('\n');f.write("Title Card Required\n");f.write('\n');f.write('0 1\n')
        f.write(geom)
        f.write('\n\n')
print("check files in the current folder")