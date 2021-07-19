import random
# import asyncio
#
# a = []
# async def add_():
#     while True:
#         a.append(random.randint(1,100))
#
#
# async def sravn():
#     if max(a)>50:
#         print ("Stop")
#         print(a)
#
# async def main ():
#     await asyncio.create_task(add_())
#     await asyncio.create_task(sravn())
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     loop.run_forever()
#
# print(a)

# while max(a)<99:
#     a = []
#     r = random.randint(1,100)
#     a.append(r)
#
# print (a)
#
# print (max(a))
a = []

def scet():
    a.append(random.randint(1,100))
    print (a)
    while max(a)<99:
        a.append(random.randint(1,100))
        import time
        time.sleep(3)
        print (a)
    else:
        print(a)
        print ("Stop")

if __name__ == '__main__':
    scet()


# if all(a[i] < a[i+1] for i in range(len(a)-1)):
