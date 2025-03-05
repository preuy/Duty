import pandas as pd
from Student import *
from init import load_students_from_json
from init import save_students_to_json



def getData(df,weeklist,lessons,Students):
    schedule=WeeklySchedule()#创建 周几到数字的索引
    classes=Daytime()# 创建每节课到数字的索引
    for week in weeklist :
        for lesson in lessons :
            i=schedule.get_day_code(week)
            j=classes.get_lesson_NU(lesson)
            print(f"[+]正在处理{week} {lesson}:")
            content=df.loc[j+4,i+1]
            #print(content)
            if isinstance(content,str):
                entries = content.split('\n')
                #print(entries)
                for entry in entries:
                    if '（' in entry and '）' in entry:
                        try: 
                            name,time=entry.split('（')
                            name=name.strip()
                            time=time.replace('）','').strip()
                            Free_num=Timestr(time)
                            Free_num.parse_time_str()
                            student=FindStudent(students=Students,Name=name)
                            if student == None :
                                print(f"[-]ta不需要值班:{name}")
                                continue
                            time_list=Free_num.getlist()
                            for num in time_list :
                                student.set_FreeTime(num-1,i,j,1)
                            
                        except:
                            entries.remove(entry)
                            print(f"[$]移出该数据:{entry}")
                print(f"[-]设置成功:{entries}")
    save_students_to_json(Students,'数据.json')

if __name__ == "__main__":
    
    Students=load_students_from_json(filename='数据.json')