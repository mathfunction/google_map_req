# GoogleMap 爬蟲

#### 目前僅支援搜尋後"唯一"對應抓值 , 等同於 https://www.google.com.tw/maps/search/

- cmd 

```bash
  python3 google_map_req.py --query 台北101購物中心
```

- python code

```python
from google_map_req import get_map_info
json_output = get_map_info("台北101購物中心")
print(json_output)
```

- 回傳 json

```json
{'LatLon': [25.0341222, 121.5640212],
 'status': 1,
 '名稱': '台北101購物中心',
 '地址': '110台北市信義區市府路45 號',
 '搜尋': '台北101購物中心',
 '營業時間': {'星期一': ['11:00–21:30'],
          '星期三': ['11:00–21:30'],
          '星期二': ['11:00–21:30'],
          '星期五': ['11:00–22:00'],
          '星期六': ['11:00–22:00'],
          '星期四': ['11:00–21:30'],
          '星期日': ['11:00–21:30']},
 '電話': '02 8101 8800',
 '類別': ['購物中心']}
```





