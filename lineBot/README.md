
## 主題：出門自動報備機器人
出門時，感應NFC，讓LineBot自動傳要出門的訊息給特定對象  

使用`python`中`Flask, linebot` module製作api

## 使用說明


  ※ 我有發email寄給妳LineBot開發的連結，應該可以用~

[LineBot console](https://developers.line.biz/console/tools)

[Line 官方帳號管理](https://manager.line.biz/account/@281qinvp/insight/friends)

打開登入應該會看到`種蕉小助手`

### Step 1

在終端機中輸入指令，或直接運行`run.bat`檔案即可

```shell
python app.py #會用flask在port 5000開啟server
flask run #也可以開啟server
```

會建立server http://127.0.0.1:5000/

### Step 2

建立外網連線

```shell
ngrok http 5000 #在port 5000建立tmp 通道
```

使用這個指令會產生一個網址(如下圖的forwarding)，外網可以連接  

※使用ngrok建立通道，每次網址都會改變

![](https://i.imgur.com/XnZz4jG.jpeg)


### Step 3

把要開啟的網址，寫入`nfc task`裡面，讓他自動開啟

