import asyncio

async def test():
    print("never scheduled")

async def main():
    # await  test()  # Correct
    test()           # Wrong

asyncio.run(main(), debug=True)