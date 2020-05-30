# -*- coding: utf-8 -*-
import random
import operator

# 成绩管理系统
score = {}
# 录入成绩
score = {"数学": {"小明": 90, "刚子": 80, "学霸": 90},
         "语文": {"小明": 92, "刚子": 81, "学霸": 95},
         "英语": {"小明": 94, "刚子": 83, "学霸": 96},
         "物理": {"小明": random.randint(60, 100), "刚子": random.randint(60, 100), "学霸": random.randint(80, 100)},
         "化学": {"小明": random.randint(60, 100), "刚子": random.randint(60, 100), "学霸": random.randint(80, 100)},
         "生物": {"小明": random.randint(60, 100), "刚子": random.randint(60, 100), "学霸": random.randint(80, 100)},
         }

# 查询

print("按照科目查询：")
course=input("请输入科目：\n")
print(score[course])

print("按照科目和姓名查询：")
course=input("请输入科目：\n")
stu_name=input("请输入学生姓名：\n")
print(score[course][stu_name])

print("按照姓名查询：")
stu_name=input("请输入姓名：\n")
for k in ["数学","语文","英语","物理","化学","生物"]:
   print(stu_name,':',score[k][stu_name])

#统计
sum=0
print("按照姓名统计：")
stu_name=input("请输入姓名：\n")
for k in ["数学","语文","英语","物理","化学","生物"]:
   sum+=score[k][stu_name]

print(stu_name,'的总分:',sum)
print(stu_name,'的平均分:',sum/6)

#输出所有学生总分和平均分
print("输出所有学生总分和平均分\n")
course_list=["数学","语文","英语","物理","化学","生物"]
stu_list=["小明","刚子","学霸"]
for stu in stu_list:
   total=0
   for cou in course_list:
      total+=score[cou][stu]    
   print(stu,"总分：",total,"   ",stu,"平均分：",total/6)

# 所有学生总分排名
print("输出所有学生总分排名\n")
total_dict = {}
course_list = ["数学", "语文", "英语", "物理", "化学", "生物"]
stu_list = ["小明", "刚子", "学霸"]
# ？？
for stu in stu_list:
    total = 0  # ？？
    for cou in course_list:
        total += score[cou][stu]
    total_dict[stu] = total  # ？？

# 用匿名函数lambda函数获取字典的值
jieguo = []
jieguo = sorted(total_dict.items(), key=lambda x: x[1], reverse=True)
print(jieguo)

# 用operator.itemgetter函数获取字典的值

print(sorted(total_dict.items(), key=operator.itemgetter(1), reverse=True))