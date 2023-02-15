import asyncio
import time



# the following are the list of events that executes asynchronously
async def output(text, sleep):
    while sleep > 0:
        await asyncio.sleep(1)
        print(f'{text} counter: {sleep} seconds')
        sleep -= 1


async def listen_to_user(text, sleep):
    while sleep > 0:
        await asyncio.sleep(1)
        print(f'{text} counter: {sleep} seconds')
        sleep -= 1

async def listeen_to_time_event(text, sleep):
    while sleep > 0:
        await asyncio.sleep(1)
        print(f'{text} counter: {sleep} seconds')
        sleep -= 1


async def interupt_the_assesment_(text, sleep):
    #this is when the bot needs to talk in case it doesnt get what the user is saying etc.
    while sleep > 0:
        await asyncio.sleep(1)
        print(f'{text} counter: {sleep} seconds')
        sleep -= 1


async def main():
    task_1 = asyncio.create_task(output('First', 1))
    task_2 = asyncio.create_task(output('Second', 2))
    task_3 = asyncio.create_task(output('Third', 3))
    print(f"Started: {time.strftime('%X')}")
    await task_1
    await task_2
    await task_3                                 
    print(f"Ended: {time.strftime('%X')}")

if __name__ == '__main__':
    asyncio.run(main())