""" Бот по выводу определенной суммы"""
# 6gFDmF4ohM.T5SNvB&%9xj!h^1Hy:%Yc
# TXforrAh79JExWk8
import json
import requests
import  asyncio
import websockets
# from bot import *
from models import SummClient
# wss://stream.binance.com:9443/stream?streams=ethusdt@miniTicker
# wss://stream.binance.com:9443/stream?streams=btcusdt@kline_3m
x = SummClient.objects.all()[1]
btc_max = []
btc_min = []
# x = input("Введите сумму:")
async def main():
    url = "wss://stream.binance.com:9443/stream?streams=btcusdt@kline_5m"
    async with websockets.connect(url) as client:
        data = json.loads(await client.recv())['data']
        btc_min.append(data['k']['h'])
        btc_max.append(data['k']['c'])
        print (btc_max)

        while x > max(btc_max):
            data = json.loads(await client.recv())['data']
            print (f"Открытие - {data['k']['o']}, Максимум - {data['k']['h']}, Минимум - {data['k']['l']}, Закрытие - {data['k']['c']} ")
            # print (type(data['k']['h']))
            btc_max.append(data['k']['h'])
            btc_min.append(data['k']['c'])


            print ("Цена не достигла заданного значения ")
            await asyncio.sleep(2)
        else:
            print ("Сумма есть!")
            # bot.polling()
            await asyncio.sleep(2)
            btc_max.clear()
            btc_min.clear()

            # print(btc)
async def test():
    while x not in btc_max:
        await asyncio.sleep(3)
    #x = "32817.77000000"
        print ("NO")

async def loops():
    task_main = asyncio.create_task(main())
    # task_test = asyncio.create_task(test())
    await task_main
    # await task_test
if __name__ =='__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(loops())

