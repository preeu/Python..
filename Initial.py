import asyncio

print('Hello world')
name = 'Priyanka'
answre = 'I am fine'

print(f'Hello: {name}. How are you? {answre}')

if True:
    print('Hello world')


def sum(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


async def calculation(num1, num2=6, num3=5):
    a = sum(num1, num2)
    b = sub(a, num3)
    print(f'{b}')


async def main():
    try:
        print('I am in try')
        await calculation()
        await calculation(num1=4, num3=5)
        await calculation(5, 7, 3)
    except Exception as e:
        print(f'Eception: {e}')


if _name_ == "_main_":
    asyncio.run(main())
