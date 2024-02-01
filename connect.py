from sqlalchemy import types, create_engine
import pyodbc
import cx_Oracle
from sqlalchemy import text
from sqlalchemy.pool import NullPool

def connect(srv, db):

    if srv == 'MES':

            engine = create_engine(
                'mssql+pyodbc://CIMADMIN:theil4893701@10.21.150.108/'+db+'?charset=utf8mb4&driver=ODBC Driver 18 for SQL Server&TrustServerCertificate=yes')
            #con = engine.connect()  # 建立連線

    elif srv == 'CIM':

            engine = create_engine(
                'mysql+pymysql://thiler:thil1234@10.21.40.126/'+db+'?charset=utf8mb4',pool_recycle=5)
            #con = engine.connect()  # 建立連線

    elif srv == 'CIM_ubuntu':

                    engine = create_engine(
                            'mysql+pymysql://cim:theil4893701@10.21.98.21/'+db+'?charset=utf8mb4',pool_recycle=5)
                    #con = engine.connect()  # 建立連線

    elif srv == 'SAP':

            if db =='SAP_Test':

                    engine = cx_Oracle.connect("thmes","qxmk2965","10.21.1.32:1521/LTINTER",encoding="UTF-8")

            elif db =='SAP_PRD':

                    engine = cx_Oracle.connect("thmes","qxmk2965","10.21.1.52:1521/LTINTER",encoding="UTF-8")

    elif srv == 'RIS':

        if db == 'RIS_Test':

            engine = cx_Oracle.connect(
#                "thmes", "qxmk2965", "10.21.1.32:1521/RIS", encoding="UTF-8")
                 "mes","ltmes","10.21.1.32:1521/RIS",encoding="UTF-8")

        elif db == 'RIS_PRD':

            engine = cx_Oracle.connect(
                "mes", "ltmes", "10.21.1.52:1521/RIS", encoding="UTF-8")

    return engine
