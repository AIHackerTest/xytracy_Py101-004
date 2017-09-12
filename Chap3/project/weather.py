import requests
import re

forecast_data=[]
def get_weather (location):


    test = requests.get('https://api.seniverse.com/v3/weather/daily.json', params={
        'key': '6wigdcbodjnntfog',
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout=20)
    test = test.json()
    forecast =  test['results'][0]['daily']
    update_time = test['results'][0]['last_update']
    for day in forecast:
        date = day['date']
        day_weather = day['text_day']
        night_weather = day['text_night']
        tem_high = day['high']
        tem_low = day['low']
        wind_direc = day['wind_direction']
        wind_scale = day['wind_scale']
        weather_info1 = f'{date}，{location}的天气为：{day_weather}转{night_weather}.\
        最高气温{tem_high}度,最低气温{tem_low}度。{wind_direc}风{wind_scale}级.'
        forecast_data.append(weather_info1)
    return (forecast_data,update_time)



def change_date_format(update_time):
    expr = r"\b(?P<year>\d\d\d\d)-(?P<month>\d\d)-(?P<date>\d\d)T(?P<hour>\d\d):(?P<minute>\d\d):(?P<second>\d\d)\b"
    x = re.search(expr, update_time)

    return (x.group('year') + '-' + x.group('month') + '-' + x.group('date') + ' ' + x.group('hour') + ':'
    + x.group('minute') + ':' + x.group('second'))



