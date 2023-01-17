import os
import re
import json
import requests
import time
import librosa
from bs4 import BeautifulSoup
from random import sample
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from config import *
from select_const import *
from story_const import *
from datetime import datetime, timezone, timedelta

app = Flask(__name__)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if isinstance(event, MessageEvent):
        get_user("1", event)
        alt_text = "小王子ㄉ回覆 >///< "
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text, FristResponse())
        )


@handler.add(PostbackEvent)
def handle_postback(event):

    if event.postback.data[0] == "第" and event.postback.data[int(len(event.postback.data))-1] == "章":
        get_user("2", event)
        alt_text = "小王子ㄉ回覆 >///< "
        if event.postback.data[1:4] == "1-5":
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(alt_text, SecondResponse_1to5())
            )
        elif event.postback.data[1:5] == "6-10":
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(alt_text, SecondResponse_6to10())
            )
        elif event.postback.data[1:6] == "11-15":
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(alt_text, SecondResponse_11to15())
            )
        elif event.postback.data[1:6] == "16-20":
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(alt_text, SecondResponse_16to20())
            )
        elif event.postback.data[1:6] == "21-27":
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(alt_text, SecondResponse_21to27())
            )

    elif event.postback.data[0:6] == "天氣資訊查詢":
        print(f"主選單選擇:{event.postback.data}")
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(WeatherNows())
        )

    elif event.postback.data[0:6] == "降雨量圖查詢":
        print(f"主選單選擇:{event.postback.data}")
        url = 'https://www.cwb.gov.tw/V8/C/P/Rainfall/Rainfall_QZJ.html'
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        path = soup.find("meta", property="og:image")
        image_path = "".join(path["content"]
                             if path else "No meta url given")
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(original_content_url=image_path,
                             preview_image_url=image_path)
        )

    elif event.postback.data[0:2] == "第章":
        story_number = get_user("3", event)
        voice_long = librosa.get_duration(
            filename=f"./static/voice_{story_number}.m4a")

        text_message = TextSendMessage(text=Story[f"contents_{story_number}"])

        # https: // c7b3-211-20-7-120.ngrok.io/static/voice_1.m4a
        url_site = "https://f9df-211-20-7-115.jp.ngrok.io"
        voice_message = AudioSendMessage(
            original_content_url=f"{url_site}/static/voice_{story_number}.m4a",
            duration=int(voice_long*1000),
        )
        line_bot_api.reply_message(
            event.reply_token,
            [text_message, voice_message]
        )


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
