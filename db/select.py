import MySQLdb

bd=MySQLdb.connect("touailab",'root','','myDB')
if bd is None:
	print "erreur connection"
else:
	c=bd.cursor()
	numRows=c.execute("select * from user")
	result=c.fetchall()
	for row in result:
		print("id: {}, name: {}, lastname: {}".format(row[0],row[1],row[2]))