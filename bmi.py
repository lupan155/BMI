# -*- coding:utf-8 -*-
height=float(input("请输入你的身高(单位:米)"))
weight=float(input("请输入你的体重(单位:公斤)"))
bmi=weight/(height*height)

if bmi<18.5:
    print("您的BMI值为:"+str(bmi))
    print("体重过轻")
if bmi>=18.5 and bmi<24.9:
    print("您的BMI值为:"+str(bmi))
    print("注意保持")
if bmi>=24.9 and bmi<29.9:
    print("您的BMI值为:"+str(bmi))
    print("体重过重")
if bmi>=29.9:
    print("您的BMI值为:"+str(bmi))
    print("肥胖")
