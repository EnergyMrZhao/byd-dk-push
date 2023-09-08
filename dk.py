import requests

def sendMsg():
    data = {
        "token": "8906471ad908426db7f4e17d229bf46a",
        "title": "通行码",
        "content": "打卡！",
    }
    requests.post(url="http://www.pushplus.plus/send/", data=data)

if __name__ == '__main__':
    sendMsg()
