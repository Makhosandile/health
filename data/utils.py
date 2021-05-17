import pandas as pd

confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data' \
            '/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv '
recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data' \
            '/csse_covid_19_time_series/time_series_covid19_recovered_global.csv '
deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data' \
         '/csse_covid_19_time_series/time_series_covid19_deaths_global.csv '
deaths = pd.read_csv(deaths)
recovered = pd.read_csv(recovered)
confirmed = pd.read_csv(confirmed)


def total_confirmed():
    df = confirmed.iloc[:, 4:].sum().max()
    return df


def total_deaths():
    df = deaths.iloc[:, 4:].sum().max()
    return df


def total_recovered():
    df = recovered.iloc[:, 4:].sum().max()
    return df


def complete_world_df():
    df = pd.DataFrame({
        'Confirmed': [total_confirmed()],
        'Deaths': [total_deaths()],
        'Recovered': [total_recovered()],
        'Active': [total_confirmed() - total_deaths() - total_recovered()]
    })
    return df


def world_perc_df():
    df = pd.DataFrame({
        'Death Rate': [total_deaths() / total_confirmed() * 100],
        'Recovery Rate': [total_recovered() / total_confirmed() * 100],
        # 'Active': [total_confirmed() - total_deaths() - total_recovered()]
    })
    df
    return df


def daily_confirmed():
    df = confirmed.iloc[:, 4:].sum(axis=0)
    df.index = pd.to_datetime(df.index)
    # df /= 1_000_000
    return df


def daily_deaths():
    df = deaths.iloc[:, 4:].sum(axis=0)
    df.index = pd.to_datetime(df.index)
    return df


def daily_recovered():
    df = recovered.iloc[:, 4:].sum(axis=0)
    df.index = pd.to_datetime(df.index)
    return df


def daily_active():
    df = daily_confirmed() - daily_deaths() - daily_recovered()
    pd.index = pd.to_datetime(df.index)
    return df


def all_cases():
    df = pd.DataFrame({
        'Confirmed': daily_confirmed(),
        'Deaths': daily_deaths(),
        'Recovered': daily_recovered(),
        'Active': daily_active(),
    }, index=daily_confirmed().index)

    return df


def all_cases_long():
    df = pd.DataFrame({
        'Confirmed': daily_confirmed(),
        'Deaths': daily_deaths(),
        'Recovered': daily_recovered(),
        'Active': daily_active(),
    }, index=daily_confirmed().index)
    return df



