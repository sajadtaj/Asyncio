#  تسک ها همزمان اجرا می شوند


import asyncio
from time import time 

async def getData_1():
    await asyncio.sleep(9)
    print('End of - count 1')
    #   Data
    return [1,2,3,4,5]

async def getData_2():
    await asyncio.sleep(10)
    print('End of - count 2')
    #   Data
    return [6,7,8,9]

async def getData_3():
    await asyncio.sleep(8)
    print('End of - count 3')
    #   Data
    return [10,11,12,13]

async def main():
    t1 = time() 
    # یک لوپ ساخته می شودو تسک های 1 و2و3 درون آن ریخته میشود
    # مجموع تسک ها باید 27 ثانیه طول بکشد اما چون با هم اجرا می شوند فقط 10 ثانیه زمان میبرد
    task1 = asyncio.create_task(getData_1())
    task2 = asyncio.create_task(getData_2())
    task3 = asyncio.create_task(getData_3())
    
    Data_1 = await task3
    Data_2 = await task2
    Data_3 = await task1
    
    print(Data_1)
    print(Data_2)
    print(Data_3)
    
    t2 = time() 
    print(f'Function executed in {(t2-t1):.4f}s')
    
asyncio.run(main(), debug=True)

