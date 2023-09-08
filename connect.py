from sqlalchemy import types, create_engine
import pyodbc
import cx_Oracle
from sqlalchemy import text

def connect(srv, db):

	if srv == 'MES':

		engine = create_engine(
		    'mssql+pyodbc://CIMADMIN:theil4893701@10.21.150.108/'+db+'?charset=utf8mb4&driver=ODBC Driver 18 for SQL Server&TrustServerCertificate=yes')
		#con = engine.connect()  # 建立連線

	elif srv == 'CIM':

		engine = create_engine(
		    'mysql+pymysql://thiler:thil1234@10.21.40.126/'+db+'?charset=utf8mb4',pool_recycle=5)
		#con = engine.connect()  # 建立連線

	elif srv == 'SAP':

		engine = cx_Oracle.connect("thmes","qxmk2965","10.21.1.32:1521/LTINTER",encoding="UTF-8")


#		con = create_engine(
#		"oracle+cx_oracle://thmes:qxmk2965@10.21.1.32:1521/?service_name=LTINTER")
	 #con = engine.connect()  # 建立連線

	#con = cx_Oracle.connect('thmes/qxmk2965@10.21.1.32:1521/LTINTER',
	#                        encoding='UTF-8', nencoding='UTF-8')  
	return engine
