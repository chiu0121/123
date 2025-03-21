# 台灣 PM2.5 即時數據分析平台

## 簡介
透過 Flask 建立 Web ，並使用行政院環保署的 PM2.5 即時數據，整理並顯示各縣市的空氣品質。

## 功能和特色
- 即時獲取 PM2.5 數據
- 支援數據篩選與查詢
- 以 DataTables 美化表格，支援排序與分頁
- 使用 Chart.js 呈現各縣市 PM2.5 平均值

## 技術架構
- **後端**：Flask（Python）
- **前端**：HTML、Bootstrap、DataTables
- **數據圖表**：Chart.js
- **資料來源**：行政院環保署 API

## 安裝與使用
### 1. Clone 專案
```bash
git clone https://github.com/你的帳號/pm25-flask-app.git
cd pm25-flask-app
```

### 2. 安裝相依套件
```bash
pip install -r requirements.txt
```

### 3. 啟動 Flask 伺服器
```bash
python app.py
```

在瀏覽器打開 `http://127.0.0.1:5000/` 來查看專案。

## 改進方向
- 改進即時數據更新方式，減少手動刷新需求
- 增加歷史數據查詢功能
- 增強數據篩選與可視化分析能力


