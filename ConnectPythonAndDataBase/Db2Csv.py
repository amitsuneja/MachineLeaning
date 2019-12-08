import mysql.connector
import os
import my_database_variables


def remove_empty_lines(filename):

	if not os.path.isfile(filename):
		print("{} does not exist ".format(filename))
		return
	else:
		with open(filename) as filehandle:
			lines = filehandle.readlines()

	with open(filename, 'w') as filehandle:
		lines = filter(lambda x: x.strip(), lines)
		filehandle.writelines(lines)


def export_table_to_csv(table):

	csv_file_name = my_database_variables.ProjectDir+"\\"+table+".csv"

	if os.path.isfile(csv_file_name):
		os.remove(csv_file_name)

	with open(csv_file_name, "a") as my_csv_file:
		query = "SELECT * from " + table
		cur.execute(query)
		print("{0} table , {1} col,{2} records".format(table, len(cur.description), cur.rowcount))

		for column_name in cur.column_names:
			print(column_name.replace(',', "_").strip(' '), end=",", file=my_csv_file)
		print("\n", file=my_csv_file)

		for this_record in cur.fetchall():
			for value in this_record:
				try:
					print(str(value).replace(',', "_").strip(' '), end=",", file=my_csv_file)
				except:
					print(str(value).replace(',', "_").strip(' ').encode("utf-8"), end=",", file=my_csv_file)
			print("\n", file=my_csv_file)
	remove_empty_lines(csv_file_name)


db = mysql.connector.connect(
	host=my_database_variables.host_name,
	user=my_database_variables.user_name,
	passwd=my_database_variables.user_password,
	auth_plugin=my_database_variables.user_auth_plugin,
	db=my_database_variables.database_name,
	port=my_database_variables.database_port
	)

cur = db.cursor(buffered=True)


cur.execute("SHOW TABLES")
for row in cur.fetchall():
	# if row[0] == "review_photos": # or row[0] == "reviews":
	# 	pass
	# else:	export_table_to_csv(row[0])

cur.close()

