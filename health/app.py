from flask import Flask

from health.covid.jhu import realtime_growth, deaths_report, daily_report, recovered_report, confirmed_report, \
    daily_deaths, daily_confirmed, percentage_trends, global_cases

app = Flask(__name__)


@app.route('/global')
def cases():
    data = realtime_growth().to_json()
    return data


@app.route('/deaths')
def deaths():
    data = deaths_report().to_json()
    return data


@app.route('/daily_report')
def daily_report():
    data = daily_report().to_json
    return data


@app.route('/recovered_report')
def recovered_report():
    data = recovered_report().to_json
    return data


@app.route('/confirmed_report')
def daily_report():
    data = confirmed_report().to_json
    return data


@app.route('/daily_confirmed')
def daily_confirmed():
    data = daily_confirmed().to_json
    return data


@app.route('/daily_deaths')
def daily_deaths():
    data = daily_deaths().to_json
    return data


@app.route('/percentage_trends')
def percentage_trends():
    data = percentage_trends().to_json
    return data


@app.route('/global_confirmed')
def global_confirmed():
    data = global_cases().to_json()
    return data


# daily_deaths, daily_confirmed, percentage_trends, global_cases
if __name__ == '__main__':
    app.run()
