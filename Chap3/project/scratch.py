from flask import Flask, url_for, render_template, request
from weather import get_weather ,change_date_format

app = Flask(__name__)
history_list=[]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_request',methods=['get','post'])
def post_user():
    city= request.args.get('city')
    try:
        output_weather,update_time= get_weather(city)

        history_list.append(output_weather)
        return render_template('get-weather.html',output_weather=output_weather)
    except KeyError:
        if request.args.get('history')=="历史":
            return  render_template('history.html',history_list=history_list)
        elif request.args.get('help') == "帮助":
            return render_template('help.html')

        else:
            return render_template('404.html')

if __name__=="__main__":
    app.run(debug=True)