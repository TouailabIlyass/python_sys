#!/usr/bin/python
import MySQLdb

bd=MySQLdb.connect("touailab",'root',"","myDB")
if bd is None:
    print("no")
else:
    print("good")
    c=bd.cursor()
    c.execute("""create table user222(
        id int not null,
        nom varchar(20),
        prenom varchar(20),
        primary key (id))
         """)
    user=(1,"ilyase","touailab")


