import pandas as pd
from Student import Student 
import json
import os



def save_students_to_json(students, filename):
    # 将 Student 实例转换为 JSON 可序列化的字典
    students_dict = []
    for student in students:
        students_dict.append({
            "name": student.name,
            "FreeTime": student.FreeTime,
            "ordered": student.Ordered,
            "department": student.department,
            "phonenumber": student.phonenumber
        })
    
    with open(filename, "w",encoding="utf-8") as f:
        json.dump(students_dict, f, indent=2,ensure_ascii=False)

    print(f"[*]->所有数据保存至:{filename}")

def load_students_from_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        students_dict = json.load(f)
    
    # 从字典中创建 Student 实例
    student_list = []
    for student_data in students_dict:
        student = Student(student_data["name"],student_data['department'],student_data['phonenumber'],student_data["ordered"])
        student.FreeTime = student_data["FreeTime"]
        student_list.append(student)
    print("[*]->成功加载数据")
    return student_list

def init_json():
    folder_path='空课表'
    file=f'{folder_path}/干事名单.xlsx'
    ColumnName=['姓名','手机号','部门']
    df=pd.read_excel(file)
    lenth=len(df[ColumnName[0]])
    students=[]
    for i in range(lenth) :
        name=df.iloc[i,0]
        phonenumber=str(df.iloc[i,1])
        department=df.iloc[i,2]
        student=Student(name,department,phonenumber,0)
        students.append(student)  
    save_students_to_json(students=students,filename='数据.json')

if __name__=="__main__" :
    init_json()
        