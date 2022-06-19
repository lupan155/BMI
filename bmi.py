# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 12:16:54 2021

@author: win10
"""
### Create a BMI Calculation Application

"""
from pywebio.input import *
from pywebio.output import *
"""

def zhangqinghanbmi():
    height=float(input("请输入你的身高(单位:米)"))
    weight=float(input("请输入你的体重(单位:公斤)"))
    bmi=weight/(height*height)

    if bmi<18.5:
        print("您的BMI值为:%.1f"%(bmi))
        print("体重过轻")
    if bmi>=18.5 and bmi<24.9:
        print("您的BMI值为:%.1f"%(bmi))
        print("注意保持")
    if bmi>=24.9 and bmi<29.9:
        print("您的BMI值为:%.1f"%(bmi))
        print("体重过重")
    if bmi>=29.9:
        print("您的BMI值为:%.1f"%(bmi))
        print("肥胖")

def bmicalculator():
    height=float(input("Please enter the height in cm: "))
    weight=float(input("Please enter the weight in Kg: "))
    
    bmi=weight/(height/100)**2
    
    bmi_output=[(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]
    
    for tuple1,tuple2 in bmi_output:
        print('tuple1:%s , tuple2:%s ' %(tuple1,tuple2))
        if bmi<=tuple1:
            print('Your BMI is :%.1f \nThe person is :%s'%(bmi,tuple2))
            break

def reslutlist():
    reslut=[(1,22,44), (2,33,44), (3,64,85)]

    for student,lan,Maths   in reslut:
        print ("student %d\'s"%(student),end=" reslut:")
        if lan>=60 :
            print("your lan win",end=" and ")
        else:
            print("your lan lose",end=" and ")
        if Maths>=60:
            print("your Maths win")
        else:
            print("your maths lose")    
if __name__=='__main__':
    #zhangqinghanbmi()
    #bmicalculator()
    reslutlist()
    