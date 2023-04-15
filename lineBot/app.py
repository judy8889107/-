from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
from flask import Flask, request, render_template

# 載入 json 標準函式庫，處理回傳的資料格式
import json
# 執行cmd指令
import os

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

access_token = 'qsYUf9sJn48pneDj/ZzESP9dFCS4j4qGrjel5pMPbk0RPE+9l4zSRI4scArCgCPFT3O2ubhfrmRxLbn2dnD7xSQY04gub9EEdoZ1GtCNUkao60EhaHkkXrSJ3tSPEvMX02dsZGwSxnigofQju3X4SwdB04t89/1O/w1cDnyilFU='
secret = '4c9573c022ad7a3f54ed20bd8cfeae7c'

# LineBot自動回覆訊息
# @app.route("/", methods=['POST'])
# def linebot():
#     body = request.get_data(as_text=True)                    # 取得收到的訊息內容
#     try:
#         json_data = json.loads(body)                         # json 格式化訊息內容
#         access_token = 'qsYUf9sJn48pneDj/ZzESP9dFCS4j4qGrjel5pMPbk0RPE+9l4zSRI4scArCgCPFT3O2ubhfrmRxLbn2dnD7xSQY04gub9EEdoZ1GtCNUkao60EhaHkkXrSJ3tSPEvMX02dsZGwSxnigofQju3X4SwdB04t89/1O/w1cDnyilFU='
#         secret = '4c9573c022ad7a3f54ed20bd8cfeae7c'
#         line_bot_api = LineBotApi(access_token)              # 確認 token 是否正確
#         handler = WebhookHandler(secret)                     # 確認 secret 是否正確
#         signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
#         handler.handle(body, signature)                      # 綁定訊息回傳的相關資訊
#         tk = json_data['events'][0]['replyToken']            # 取得回傳訊息的 Token
#         type = json_data['events'][0]['message']['type']     # 取得 LINe 收到的訊息類型
#         if type == 'text':
#             msg = json_data['events'][0]['message']['text']  # 取得 LINE 收到的文字訊息
#             print(msg)                                       # 印出內容
#             reply = msg
#         else:
#             reply = '你傳的不是文字呦～'
#         print(reply)
#         line_bot_api.reply_message(tk, TextSendMessage(reply))  # 回傳訊息
#     except:
#         print(body)                                          # 如果發生錯誤，印出收到的內容
#     return 'OK'                                              # 驗證 Webhook 使用，不能省略

# 測試用首頁說明


@app.route('/')
def home():
    return render_template('home.html')

# 發給特定使用者
# http://127.0.0.1:5000/send/userId={填入userId}&{msg=填入訊息}


@app.route('/send', methods=['GET', 'POST'])
def sendMsgToUser():
    try:
        # 取得網址參數
        userId = request.args.get('userId')
        msg = request.args.get('msg')
        # 建立lineBot object
        line_bot_api = LineBotApi(access_token)
        # userID='Ua8e7319cbcc1bbdbc09f282c5fbdf472' 我的userId
        line_bot_api.push_message(userId, TextSendMessage(text=msg))
        return f'Send message {msg} to user {userId}'
    except:
        print('error')

# request錯誤處理


@app.errorhandler(500)
def internal_error(error):
    return render_template('errorHandler.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0') #建立本機server
