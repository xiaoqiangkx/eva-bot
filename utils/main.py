# encoding: utf-8
"""
    Test fastAPI async server
"""
import requests
import asyncio
import aiohttp
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect


app = FastAPI()


@app.post("/test")
async def test_handler():
    print("hello test_handler")
    await test("eurySecurity app is not working.")


async def chat(message, botId, projectId, touchPoint):
    """
        Chat with the bot
    """
    print(f"chat message:  {message}")
    async with aiohttp.ClientSession() as session:
        async with session.post(url=f'https://apps.voc.ai/api_v2/gpt/bot/{botId}/chat',
                                headers={
                                    'Content-Type': 'application/json',
                                    'cookie': 'slx-utm=www.voc.ai; _gcl_au=1.1.239580511.1718698891; _ga=GA1.1.987886249.1718698892; _fbp=fb.1.1718698892872.613949931975921456; _tt_enable_cookie=1; _ttp=RODRSZzrc7NjJH2L0we4-IUeKO8; _bl_uid=mUl3wxzRknn43py4t1vbozjoUpOw; _ga_21JG1R7V34=deleted; _token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJldWlkIjoiODFkY2U5ZDFlZWM2ODIiLCJraW5kIjoiQUNDT1VOVF9VU0VSIiwiY3JlYXRlZF9hdCI6MTcxODc4MTIxNCwiZXhwIjoxNzIwMDc3MjE0fQ.bAsgQW97MbqsZejh8NmFWPw_YPDxnhCfzeR65T9DppepEDZCJBjVZ-cP3lfiKwb4l8ZISu9x5bq-eCTm6Rx721t0dgaK72ho3pigQINgJDWd2XZP0Ds_Gg0soH2Hmb68D6BOXXWwdROUqrDoS2mRoDXlietkPvooz1acIAfXUkFgsTFLl1B7ZcXPegKRoZOzmwuxRnsmMSD9EjyRWCspZnfWSsQbCtJEb66oJr7i8O_SREZpmJEP6pg48OGi7LwNEtjwaW-gp2rS8V2dHLAJgXMjJDa7Msj_JWV5q0VsMi8r3fXJjXx4W8leWTdGL4SXU9NA0CberlKTbQ7o4Kd_2g; JSESSIONID=38936CC25D271EF7112BCEE0E492365C; _ga_21JG1R7V34=GS1.1.1718851182.6.1.1718851197.45.0.0'
                                }, json={
                                    'message': message,
                                    'botId': botId,
                                    'projectId': projectId,
                                    'touchPoint': touchPoint
                                }) as response:
            return await response.json()


async def test(message):
    result = await chat(
        message=message,
        botId=15640,
        projectId=16773,
        touchPoint="LIVE_CHAT"
    )
    print(result["content"])
    return
