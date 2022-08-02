# POE 台服官網API
- 交易API網址
  - https://web.poe.garena.tw/api/info
- API developer docs
  - 純英文的官方文檔
  - https://www.pathofexile.com/developer/docs/index
## 目標網站(台服)
- https://web.poe.garena.tw/api/trade/search/%E5%AE%88%E6%9C%9B%E8%81%AF%E7%9B%9F
  - 守望聯盟
- https://web.poe.garena.tw/api/trade/search/%E5%AE%88%E6%9C%9B%E8%81%AF%E7%9B%9F%EF%BC%88%E5%B0%88%E5%AE%B6%EF%BC%89
  - 守望聯盟（專家）
- https://web.poe.garena.tw/api/trade/search/%E6%A8%99%E6%BA%96%E6%A8%A1%E5%BC%8F
  - 標準模式
- https://web.poe.garena.tw/api/trade/search/%E5%B0%88%E5%AE%B6%E6%A8%A1%E5%BC%8F
  - 專家模式
## API使用、取得解說
### get result
目標網站 + 指定條件(payload query) json格式後會回傳100條result + 其query 的對應id
並將result 拆分成每10條一組的形式保存，記錄其queryId
### get 賣家詳細資料
get infomasion: https://web.poe.garena.tw/api/trade/fetch/
將上述網址 /fetch後段加上 result(10) + queryID，即可取得查詢資料
>無需使用 payload
## 整理資料(待補)