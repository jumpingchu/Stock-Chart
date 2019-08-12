from pandas_datareader import data  # 抓股票資料
import datetime
from bokeh.plotting import figure, show, output_file  # 畫圖
from bokeh.embed import components  # 獲取 bokeh plot 的 HTML components
from bokeh.resources import CDN  # 獲取 BokehJS code、CSS resources

start = datetime.datetime(2018, 8, 1)
end = datetime.datetime(2019, 8, 7)

df = data.DataReader(name='0050.TW', data_source='yahoo', start=start, end=end)


def incr_decr(c, o):
    if c > o:
        value = 'Increase'
    elif c < o:
        value = 'Decrease'
    else:
        value = 'Equal'
    return value


df['Status'] = [incr_decr(c, o) for c, o in zip(df.Close, df.Open)]

# 將 y 和 height 也分別新增一欄
df['Middle'] = (df.Close+df.Open)/2
df['Height'] = abs(df.Close-df.Open)

# 新增季線、5日線
df['mean_60'] = df['Close'].rolling(60).mean()
df['mean_5'] = df['Close'].rolling(5).mean()


p = figure(x_axis_type='datetime', width=1000,
           height=300, sizing_mode='scale_width')
p.title.text = 'CandleStick Chart'
p.grid.grid_line_alpha = 0.3

# 繪製長方體時 width 以毫秒 (ms) 為單位
hours_12 = 12 * 60 * 60 * 1000

# 畫上下影線: segment(X start, Y start, X end, Y end)
p.segment(df.index, df.High, df.index, df.Low, color='black')

# 畫橫線: 收盤開盤同價位
p.dash(df.index[df.Status == 'Equal'], df.Middle[df.Status == 'Equal'],
       size=12, line_color='black')

# 畫 K 線: Taiwan style
p.rect(df.index[df.Status == 'Increase'], df.Middle[df.Status == 'Increase'],
       hours_12, df.Height[df.Status == 'Increase'],
       line_color='black', fill_color='red')

p.rect(df.index[df.Status == 'Decrease'], df.Middle[df.Status == 'Decrease'],
       hours_12, df.Height[df.Status == 'Decrease'],
       line_color='black', fill_color='green')

p.line(df.index, df.mean_60, color='green', legend='季線')
p.line(df.index, df.mean_5, color='brown', legend='周線')

show(p)
