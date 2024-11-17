# Weather using OpenWeatherMap API
需要先到 [OpenWeatherMap](https://openweathermap.org/) 申請金鑰
目前功能只有規劃到免費帳號的功能！

## 天氣即時查詢(台灣地區)

使用技術：
  - Python
  - Django
  - django-tailwind
  - Alpin.js
  - pyowm

執行環境：
- 將`OpenWeatherMap`金鑰放入`.env`檔案的`api_key`變數裡
- `poetry shell` 進入虛擬環境
- `poetry install` 下載 相依套件
- `python manage.py` tailwind start 啟動 Tailwind 模組並監視變更
- `python manage.py` runserver 啟動 Web Server
