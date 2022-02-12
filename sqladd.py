# -*- coding: utf-8 -*-

# 导入必要模块
import pandas as pd
from sqlalchemy import create_engine

# 初始化数据库连接，使用pymysql模块
engine = create_engine('mysql+pymysql://root:12345678@localhost:3306/app')

# 读取本地CSV文件
df = pd.read_csv("/Users/glennou/Downloads/provisional.csv", sep=',')

# 将新建的DataFrame储存为MySQL中的数据表，不储存index列
df.to_sql('mpg', engine, index= False)

print("Write to MySQL successfully!")