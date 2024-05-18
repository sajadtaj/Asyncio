import asyncio

async def counter(n):
    while n !=0:
        print('conuter :',n)
        n -=1
        await asyncio.sleep(1)
        
        
if __name__ == "__main__":
    x= counter(5)
    # asyncio.run(counter(5))
    # loop = asyncio.get_event_loop()
    # task = loop.create_task(counter(5))