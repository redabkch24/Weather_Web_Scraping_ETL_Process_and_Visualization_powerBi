import pandas as pd


def transform_function(url): #url : 'weather_dataset.csv'
        #extract data
    data = pd.read_csv(url)
    df = pd.DataFrame(data=data)

    df['High temp'] = df['High temp'].str.replace('°','')
    df['Low temp'] = df['Low temp'].str.replace('°','')
    df['Low temp'] = df['Low temp'].str.replace('/','')
    df['Precip'] = df['Precip'].str.replace('\n','')
    df['Precip'] = df['Precip'].str.replace('\t','')
    df['Precip'] = df['Precip'].str.replace('%','')

        #converting Date column to date
    df['Date'] = df['Date']+'/2024'
    df['Date'] = pd.to_datetime(df['Date'])

        #converting precip, high and low tempreture columns to numerical type
    df['High temp'] = pd.to_numeric(df['High temp'])
    df['Low temp'] = pd.to_numeric(df['Low temp'])
    df['Precip'] = pd.to_numeric(df['Precip'])
    return df

