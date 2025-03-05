import pandas as pd
from Student import *
from getData import getData
from init import *
import os
from Duty import *
def get_file(folder_path,num):
    list={'办公室','纪检部','两创','青志队','体育部','文娱部','新媒体','组织部'}
    df_list=[]
    for i in list :
        file_path=f'{folder_path}/计网院第{num}届{i}空课表.xlsx'
        df=pd.read_excel(file_path,header=None)
        df_list.append(df)
    return df_list

if __name__ == "__main__":
    schedule=WeeklySchedule()#创建 周几到数字的索引
    classes=Daytime()# 创建每节课到数字的索引
    while True :
        print("1.获取值班同学名单")
        print("2.读取空课表数据")
        print("3.自动安排值班")
        print("4.exit")
        opt=input(">>")
        if opt == "1" :
            init_json()
        elif opt == "2" :
            Students=load_students_from_json('数据.json')            
            folder_path=input("请输入文件夹名：")
            num=input("第几届团学：")
            list=get_file(folder_path,num)
            for i in list :
                weeklist=i.iloc[3,1:6]
                lessons=i.iloc[4:8,0]
                getData(i,weeklist,lessons,Students)
        elif opt =="3":
            Students=load_students_from_json('数据.json')
            schedule=getTheans(Students)
            save_to_excel(schedule)
            save_students_to_json(Students,'数据.json')
        elif opt== "4" :
            exit()