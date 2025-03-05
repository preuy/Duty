class Student:
    ## student 类 ，名字，空课时间，是否被安排过
    # 三维数组储存空课时间，18层表示18周，7行表示一周7天，4列表示一天4节课
    def __init__(self,name,department,phonenumber,Ordered):
        self.name=name
        self.FreeTime=[[[0  for _ in range(4) ]for _ in range(5) ]for _ in range (18)]
        self.Ordered=Ordered
        self.department=department
        self.phonenumber=phonenumber

    def print_info(self):
        print(f"Name:{self.name}")
        print("FreeTime:")
        for i in self.FreeTime :
            print(i)
        print()
    
    def set_FreeTime(self,nums,week,lesson,stutas):
        # 通过这个方法直接设置和修改空课时间
        # lesson 需要mod 2 因为课表上的两节课，我算为一节课
        self.FreeTime[nums][week][lesson]=stutas

    def set_Ordered(self,stutas):
        self.Ordered=stutas

    def get_Ordered(self):
        # 设置学生的安排状态
        return self.Ordered

class WeeklySchedule:
    def __init__(self):
        # 定义从数字到中文星期名称的映射
        self.code_to_day = {
            0: "周一",
            1: "周二",
            2: "周三",
            3: "周四",
            4: "周五",
        }
        # 定义从中文星期名称到数字的映射
        self.day_to_code = {day: code for code, day in self.code_to_day.items()}

    def get_day_name(self, day_code):
        """ 根据数字代码获取中文星期名称 """
        return self.code_to_day.get(day_code, "无效的数字代码")

    def get_day_code(self, day_name):
        """ 根据中文星期名称获取数字代码 """
        return self.day_to_code.get(day_name, -1)

class getTime:
    # 对表格中的字符串作处理，获取空课时间
    # time_list 按照升序排序，其中表示有空的周数，作为student 的层数
    def __init__(self,str):
        self.str=str
        self.time_list=[]

    def parse_time_str(self):
        try :
            parts=self.str.split('，')
            for part in parts :
                part=part.strip()
                if '-' in part :
                    start,end=part.split('-')
                    self.time_list.extend(range(int(start),int(end)))
                else :
                    self.time_list.append(part)
            self.time_list.sort()
        except:
            print(f"Error!格式有问题'{self.str}'")
    
    def getlist(self):
        return self.time_list

class Daytime:
    def __init__(self):
        self.cloum_to_lesson = {
            0: "第1、2节",
            1: "第3、4节",
            2: "第5、6节",
            3: "第7、8节"
        }
        self.lesson_to_cloum={lesson: cloum for cloum,lesson in self.cloum_to_lesson.items()}
    def get_lesson_CN(self,lesson_num):
        return self.cloum_to_lesson.get(lesson_num,"这节课不上了！！！")
    def get_lesson_NU(self,lesson_cn):
        return self.lesson_to_cloum.get(lesson_cn,-1)

class Timestr:
    def __init__(self,str):
        self.str=str
        self.time_list=[]
    def parse_time_str(self):
        try :
            parts=self.str.split('，')
            for part in parts :
                part=part.strip()
                if '-' in part :
                    start,end=part.split('-')
                    self.time_list.extend(range(int(start),int(end)+1))
                else :
                    self.time_list.append(int(part))
            
            #self.list_info()
            self.time_list.sort()
            
        except:
            print(f"Error!格式有问题'{self.str}'")
    
    def getlist(self):
        return self.time_list

    def list_info(self):
        for i in self.time_list :
            print(i)

def FindStudent(students,Name):
    # 根据名字检索对应的实例
    for student in students :
        if student.name == Name :
            return student
    return None

