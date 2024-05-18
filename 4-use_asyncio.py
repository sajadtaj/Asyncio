
#  تسک ها همزمان اجرا می شوند

import asyncio

async def counter1(n):
    while n !=0:
        print('conuter fun_1 :',n)
        n -=1
        await asyncio.sleep(1)
    print('End of - count 1')

async def counter2(n):
    while n !=0:
        print('conuter fun_2 :',n)
        n -=1
        await asyncio.sleep(3)
    print('End of - count 2')

async def counter3(n):
    while n !=0:
        print('conuter fun_3 :',n)
        n -=1
        await asyncio.sleep(5)
    print('End of - count 3')

async def main():
    # یک لوپ ساخته می شودو تسک های 1 و2و3 درون آن ریخته میشود
    task1 = asyncio.create_task(counter1(10))
    task2 = asyncio.create_task(counter2(5))
    task3 = asyncio.create_task(counter3(3))
    
    # با اجرای کد زیر هر سه تسک اجرا میشوند چرا که دون یک لوپ قرار دارند
    # اما همین که تسک 3 تمام شود دیگر باقی تسک ها اجرا نمشوند
    # برای حل این حالت باید تمامی تسک ها را فرخوانی کنیم
    # تا باهم اجرا شوند
    # یا میتوانیم تسکی را که بیشتر از همه طول می کشد فراخوانی کنیم 
    # اما بهتر است همه را بخواینم
    
    await task3
    # await task2
    # await task1

asyncio.run(main(), debug=True)

