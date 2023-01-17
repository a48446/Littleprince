import re
import json
import requests
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from config import *
from datetime import datetime, timezone, timedelta
from story_const import *


def time_now():
    timedata = timezone(timedelta(hours=+8))
    nowtime = datetime.now(timedata).strftime('%Y-%m-%d %H:%M:%S')
    return nowtime


def get_user(methob, event):
    user_Id = event.source.user_id
    user_profile = line_bot_api.get_profile(user_Id)
    print(f"當前用戶為: {user_profile.display_name}")
    print(f"操作時間為: {time_now()}")
    if methob == "1":
        print(f"傳入訊息為: {event.message.text}")

    elif methob == "2":
        print(f"主選單選擇: {event.postback.data}")

    elif methob == "3":
        story_number = "".join(re.findall(r"\d+\.?\d*", event.postback.data))
        print(f"小王子故事選擇第 {story_number} 章")
        return story_number

    return {
        "status": "succes"
    }


def FristResponse():
    contents = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "小王子來囉",
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "功能列表",
                                    "color": "#aaaaaa",
                                    "size": "md",
                                    "flex": 3,
                                    "margin": "xs"
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第 1 ~ 5 章",
                        "data": "第1-5章",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第 6 ~ 10 章",
                        "data": "第6-10章",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第 11 ~ 15 章",
                        "data": "第11-15章",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第 16 ~ 20 章",
                        "data": "第16-20章",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第 21 ~ 27 章",
                        "data": "第21-27章",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "天氣資訊查詢",
                        "data": "天氣資訊查詢",
                        "displayText": "小王子說 >///<"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "降雨量圖查詢",
                        "data": "降雨量圖查詢",
                        "displayText": " 小王子幫妳找到了！！"
                    }
                },
                {
                    "type": "spacer",
                    "size": "sm"
                }
            ],
            "flex": 0
        }
    }
    return contents


def SecondResponse_1to5():
    contents = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "章節列表",
                    "weight": "bold",
                    "size": "xl",
                    "align": "center"
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第一章",
                        "data": "第章1",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第二章",
                        "data": "第章2",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第三章",
                        "data": "第章3",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第四章",
                        "data": "第章4",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第五章",
                        "data": "第章5",
                        "displayText": "好滴，馬上找妳看"
                    }
                }
            ],
            "flex": 0
        }
    }
    return contents


def SecondResponse_6to10():
    contents = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "章節列表",
                    "weight": "bold",
                    "size": "xl",
                    "align": "center"
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第六章",
                        "data": "第章6",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第七章",
                        "data": "第章7",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第八章",
                        "data": "第章8",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第九章",
                        "data": "第章9",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第十章",
                        "data": "第章10",
                        "displayText": "好滴，馬上找妳看"
                    }
                }
            ],
            "flex": 0
        }
    }
    return contents


def SecondResponse_11to15():
    contents = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "章節列表",
                    "weight": "bold",
                    "size": "xl",
                    "align": "center"
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第十一章",
                        "data": "第章11",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第十二章",
                        "data": "第章12",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第十三章",
                        "data": "第章13",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第十四章",
                        "data": "第章14",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第十五章",
                        "data": "第章15",
                        "displayText": "好滴，馬上找妳看"
                    }
                }
            ],
            "flex": 0
        }
    }
    return contents


def SecondResponse_16to20():
    contents = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "章節列表",
                    "weight": "bold",
                    "size": "xl",
                    "align": "center"
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第十六章",
                        "data": "第章16",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第十七章",
                        "data": "第章17",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第十八章",
                        "data": "第章18",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第十九章",
                        "data": "第章19",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第二十章",
                        "data": "第章20",
                        "displayText": "好滴，馬上找妳看"
                    }
                }
            ],
            "flex": 0
        }
    }
    return contents


def SecondResponse_21to27():
    contents = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "章節列表",
                    "weight": "bold",
                    "size": "xl",
                    "align": "center"
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第二十一章",
                        "data": "第章21",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第二十二章",
                        "data": "第章22",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第二十三章",
                        "data": "第章23",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第二十四章",
                        "data": "第章24",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第二十五章",
                        "data": "第章25",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第二十六章",
                        "data": "第章26",
                        "displayText": "好滴，馬上找妳看"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "postback",
                        "label": "第二十七章",
                        "data": "第章27",
                        "displayText": "好滴，馬上找妳看"
                    }
                }
            ],
            "flex": 0
        }
    }
    return contents


def WeatherNows():
    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001"
    params = {
        "Authorization": "CWB-FAAAB794-6455-4A1A-8515-D22146C53557",
        "locationName": "臺中市",
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = json.loads(response.text)

        location = data["records"]["location"][0]["locationName"]
        weather_elements = data["records"]["location"][0]["weatherElement"]
        start_time = weather_elements[0]["time"][0]["startTime"]
        end_time = weather_elements[0]["time"][0]["endTime"]
        weather_state = weather_elements[0]["time"][0]["parameter"]["parameterName"]
        rain_prob = weather_elements[1]["time"][0]["parameter"]["parameterName"]
        max_tem = weather_elements[4]["time"][0]["parameter"]["parameterName"]
        min_tem = weather_elements[2]["time"][0]["parameter"]["parameterName"]
        comfort = weather_elements[3]["time"][0]["parameter"]["parameterName"]

        contents = f"城市：{location}" + "\n" + \
            f"預測始末時間：{start_time} ~ {end_time}" + "\n" + \
            f"天氣狀態：{weather_state}" + "\n" + \
            f"降雨機率： {rain_prob}%" + "\n" + \
            f"最大溫度：{max_tem}" + "\n" + \
            f"最小溫度：{min_tem}" + "\n" + \
            f"體感狀況：{comfort}"

    else:
        contents = "抱歉，現在找不到資訊ＱＱ"

    return contents
