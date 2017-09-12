# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 12:40:57 2017

@author: retec
"""
from textwrap import dedent
##引入不缩进输出方式

class weather(object):
    
    def __init__(self):
        with open('weather_info.txt','r' ,encoding='utf-8') as weather_info:
       # weather_info=open("weather_info.txt",'r',encoding = "utf-8")
        #解码方式ufc-8
            self.weather_dic={city.strip():weather.strip() for city,\
                              weather in (line.split(',') for line in weather_info)}
        #读取weather_info 中的所有信息，以，为分割，将信息存储到weather_info这个字典中
        #将城市名存为city,将天气情况存为weather
#        weather_info.close()
        
    def getweather(self,city):
        if city in self.weather_dic:
            each_time=userinput+" "+self.weather_dic[userinput]
            history.append(each_time)

        else:
            error_info()
        return self.weather_dic.get(city,f"不存在{city}的天气记录！")
      
    #加入信息不存在的城市
#设置一个类--存储天气信息  
    
    
def get_help_info():
    print(dedent("""
    输入城市名，返回该城市的天气数据；
    输入“帮助”指令，获取帮助文档；
    输入“历史查询记录”指令，获取历史查询信息；
    输入“退出”指令，退出程序；
    """))
#帮助信息模块

    
def get_history_info():
    if history:
        print("您的历史查询记录是：")
        print(history)
    else:
        print ("没有查询记录")
##历史信息模块      
        
def end_check():
    print("感谢您的使用")
    
def error_info():
    print ('''你输入的指令错误或者城市名称不存在，请重新输入。
    - 如果不清楚指令，可以输入帮助，获取帮助。
    ''')

 
    
    
current_weather = weather()
history = []

while True:

    userinput = input("请输入指令或您要查询的城市名：").strip()

    if userinput == "帮助":
        get_help_info()
     
       

    elif userinput == "退出":
        get_history_info()
        end_check()
        break

    elif userinput == "历史查询记录":
        get_history_info()
  

    else:
        print(current_weather.getweather(userinput))

        
