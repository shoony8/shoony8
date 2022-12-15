# import pandas as pd
# import pymysql
# bmi = pd.read_csv("myPackage/data/bmi.csv")
# print(bmi.info())
# height = bmi['height']
# weight = bmi['weight']
# label = bmi['label']
# config = {
#      'host' : '127.0.0.1',
#      'user': 'shoon',
#      'password': 'tiger',
#      'database': 'work',
#      'port': 3306,
#      'charset' : 'utf-8',
#      "use_unicode": True
#  }
# try:
#     conn = pymysql.connect(**config)
#     cursor = conn.cursor()
#     cursor.execute("show tables")
#     tables = cursor.fetchall()
#     sw = False
#     for table in tables:
#         if table[0] == 'bmi_tab':
#             sw = True
#     if not sw:
#         print('테이블 없음')
#         sql = """create table bmi_tab(
#         height int not null,
#         weight int not null,
#         label varchar[15] not null)"""
#         cursor.execute(sql)
#