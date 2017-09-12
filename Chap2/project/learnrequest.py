import requests
import json
i = 0
unit = 'c'
forecast_data=[]
history_list=[]
help_info=['h', 'help', '帮助','history','历史记录','退出','exit','预报',
           'forecast','c','f']

def get_weather (location,unit):

    test = requests.get('https://api.seniverse.com/v3/weather/daily.json', params={
        'key': '6wigdcbodjnntfog',
        'location': location,
        'language': 'zh-Hans',
        'unit': unit
    }, timeout=20)
    return test.json()


def print_response(weather,order):
    if weather['status_code'] == 'AP010010':
        print("城市名称错误，请检查后重新输入\n")
    elif weather['status_code'] == 'AP010002':
        print("You are not allowed to access this API\n")
    elif weather['status_code'] == 'AP010006':
        print("免费用户不允许查询 %s 的天气" % order, '\n')
    return 0

def format_weather(result,i ):
    daily = result['results'][0]['daily'][i]
    date = daily['date']
    day_weather = daily['text_day']
    night_weather = daily['text_night']
    tem_high = daily['high']
    tem_low = daily['low']
    wind_direc = daily['wind_direction']
    wind_scale = daily['wind_scale']
    weather_info =f'{date}, \n{order}日间:{day_weather},夜间:{night_weather}.\n\
最高气温{tem_high}度,最低气温{tem_low}度\n{wind_direc}风{wind_scale}级.\''
    return weather_info

def format_forecast(result):
    forecast =  result['results'][0]['daily']
    update_time = result['results'][0]['last_update'][:-6].replace('T', ' ')
    for day in forecast:
        date = day['date']
        day_weather = day['text_day']
        night_weather = day['text_night']
        tem_high = day['high']
        tem_low = day['low']
        wind_direc = day['wind_direction']
        wind_scale = day['wind_scale']
        weather_info1 = f'{date}, \n{order}日间:{day_weather},夜间:{night_weather}.\
        最高气温{tem_high}度,最低气温{tem_low}度\n{wind_direc}风{wind_scale}级.'
        forecast_data.append(weather_info1)
    return (forecast_data,update_time)



while True:

    order= input("请输入需要查询的城市名称或指令:") .strip()
    if order in help_info[:]:
        print("您输入的是指令：",order)
        command = order.lower()
        if command in ['h', 'help', '帮助'] :
            print('''
            输入城市名，查询该城市天气
            输入帮助,获取帮助文档
            输入历史记录,获取查询历史
            输入c，切换为摄氏度模式
            输入f，切换为华氏度模式
            输入forecast或预报，获取三日天气预报
            输入exit或退出，退出程序''')
        elif command in ['c', 'f']:
            unit=command
            print("已切换温度表达方式")
            continue
        elif command in [ 'history' ,'历史记录']:
            print( "您的查询记录是：",history_list)
            continue
        elif command in  ['exit', '退出']:
            print('退出查询')
            break
        elif command in['预报', 'forecast']:
            print("%s 未来三天的天气预报是："% city ,'\n')
            for days in output_3days:
                print(days)
            print ("最后更新时间：",last_update)
            continue

    else:
        print("您输入的是城市：",order)
        city = order
        result= get_weather(city , 'c')
        if 'status' in result:
            print_response(result, city)
        else:
           # print(result)
        #print_response(result)
            output_today= format_weather(result, i)
            output_3days ,last_update= format_forecast(result)
            history_list.append(city)
            print (output_today)
            continue