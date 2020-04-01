import quandl

quandl.ApiConfig.api_key = 'iNA2ncmW8Fa1ok9S3HgN'
data =quandl.get('BCHARTS/BITFLYERUSD', start_date='2020-03-28', end_date='2020-03-30')

print(data)