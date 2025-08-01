"""Docstring"""
import asyncio
import time


# def f1(x):
#     print(x ** 2)
#     time.sleep(x)
#     print('F1 работу закончила')
#
#
# def f2(x):
#     print(x ** 2)
#     time.sleep(x)
#     print('F2 работу закончила')
#
#
# def main():
#     f1(1)
#     f2(2)
#
# start = time.perf_counter()
# main()
# duration = time.perf_counter() - start
# print(duration)

# async / await
async def f1(x):
    print(x ** 2)
    await asyncio.sleep(x)
    print('F1 работу закончила')


async def f2(x):
    print(x ** 2)
    await asyncio.sleep(x)
    print('F2 работу закончила')


async def f3(x):
    print(x ** 2)
    await asyncio.sleep(x)
    print('F3 работу закончила')


async def main():
    # asyncio.create_task(f1(1))
    # asyncio.create_task(f2(2))
    # await asyncio.create_task(f3(3))
    await asyncio.gather(f1(1), f2(2), f3(3))
print(__doc__)
print(__name__)
if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    duration = time.perf_counter() - start
    print(duration)