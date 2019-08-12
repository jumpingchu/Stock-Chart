# **<font color=#20B2AA>500 - internal server error**</font>

## <font color=#A0522D>ERROR</font>

以 pandas_datareader 和 bokeh 製作股價 K 線圖時

在 Localhost 運作正常

但部屬到 Heroku 上時就會出現 *internal server error*

## <font color=#A0522D>Heroku Logs</font>

    2019-08-09T12:40:42.852953+00:00 app[web.1]:   File "/app/script1.py", line 67, in plot

    2019-08-09T12:40:42.852955+00:00 app[web.1]:     css_url = CDN.css_files[0]

    2019-08-09T12:40:42.852963+00:00 app[web.1]: IndexError: list index out of range

顯然問題是出在

    css_url = CDN.css_files[0]

## <font color=#A0522D>解決辦法</font>

在 jupyter notebook 上確實要抓第一個 index 才是正確的 CSS 連結[0]

但把 <font color=red>[0]</font> 刪掉後就不會出現 500 error

    css_url = CDN.css_files
