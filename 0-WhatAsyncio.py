import asyncio

async def wait_for_seconds(seconds):
    print(f"Waiting for {seconds} seconds...")
    await asyncio.sleep(seconds)  # This line suspends execution
    print("Done waiting!")


# (Optional) Example with a future
async def another_task():
    # Simulate an asynchronous operation that returns a future
    future = asyncio.Future()
    await asyncio.sleep(2)  # Simulate some work
    future.set_result("Result from another_task")
    return future

async def GetData():
    print("Get Data Started....")
    asyncio.sleep(2)
    return [2,3,4,5,6]

async def main():
    
    task   = asyncio.create_task(GetData())
    data   = await wait_for_seconds(3)
    result = await another_task()  # await with a future
    
    data_GetData = await task
    
    print(f"Get data: {data_GetData}")
    print('Result Of wait_for_seconds : ',data)
    print('Result Of another_task : '   ,result)

asyncio.run(main())



