# nice to meet you
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。 (OK)
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。 (OK)
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面： (OK)
	 * 焦點新聞列表
	 * 新聞詳情頁面
4. 以 Pull-Request 的方式將代碼提交。(OK)
	
## 進階要求
1. 使用 Scrapy。(OK)
2. 實現爬蟲自動定時抓取。(OK)
3. 使用 Websocket 服務，抓取到新的新聞時立即通知前端頁面。 (TODO)
4. 将本 demo 部署至服务器并可正确运行。(OK)
https://nicetomeetyou-sleep.herokuapp.com/
5. 所實現新聞列表 API 可承受 100 QPS 的壓力測試。 (TODO)

爬蟲的的部分方便demo沒有爬完全部資料\
自動更新只會更新最新的資料\
爬蟲自動定時抓取功能在heroku上尚未完成...\
第3第5點正在進行中...