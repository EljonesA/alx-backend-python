import asyncio

async def async_generator():
    for i in range(5):
        await asyncio.sleep(5)
        yield i

async def main():
    result = [i async for i in async_generator()]
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
