import mysql.connector

config = {
  'user': 'gowherew',
  'password': 'Bre8kthrough2019',
  'host': 'c63254.sgvps.net',
  'database': 'gowherew_gww',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cnx.close()