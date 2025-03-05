# 怎么使用
 python版本：3.11.7
 Arrange 是其中的核心脚本，其他脚本都导入在这
 ```python
 python Arrange.py #  运行此脚本
 ```
![Arrange](https://picture.gptkong.com/20250303/062091e5de01044e039647189348882e7d.png)
选项1会执行`init.py`,这通过名单创造一个`Students` ，并以`json`保存，所有数据初始化为0
![1](https://picture.gptkong.com/20250303/0627606b28855b4278923772c2c5ecd2a4.png)
选项2会执行`getData.py`，这将读取各部门的空课表，并修改json中对应同学对应时间的空闲状态
![2](https://picture.gptkong.com/20250303/062950cd4b210b4843a238132a92f9a62f.png)
选项3会执行`Duty.py`,这将生成1-18周的值班表，并修改json中 同学的被安排次数
![3](https://picture.gptkong.com/20250303/063032daed301b4bbbb42dbb44dda2270e.png)

当然你可以直接`python filename` 来运行其他脚本

# 注意事项 

    课表的excel文件中，逗号和扩号要求使用中文字符
    “2-18”，中间要求只用“-”。(说实话，看不出区别来)

    如果不按要求，那么脚本会报错 ，格式有问题

    一定要确保空课表的表格是按格式写的，否则就会报错

# 修改数据
 因为数据保存在json中，你可以手动去修改相关据。
 这里推荐使用vscode
 ![json](https://picture.gptkong.com/20250303/06388c9b76e6dc435abfb66d137d0a278a.png)

# 各脚本功能 

Students.py : 主要定义了多个class 类，类似对象。
init.py : 定义了两个方法，一个将list数据保存为json，一个从json 中 读取数据到list
getDate.py :定义了一个方法，可以从EXCEL中把单元格里的数据，处理，并修改list 中的Student
Duty.py : 实现值班功能。优先级：同一时间，处于空闲（即没课），且值班次数最少，在list中的顺序靠前的同学，会被优先安排值班