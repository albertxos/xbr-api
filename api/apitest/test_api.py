import asyncio
from typing import Iterator

from xbr.hub.mobility.roadtrack import welcome, OnWelcome


def fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b


def moo() -> None:
    r = fib(10)
    print(r)


#moo()


def foo():
    s: int
    s = 'hello'
    s += 2

#foo()


async def run():
    session = None

    #def on_welcome(payload: OnWelcome.Payload, _: object) -> None:
    #    print('Name: ' + payload.username)
    #    print('Message: ' + payload.msg)

    #await OnWelcome.subscribe(session, on_welcome)

    call = await welcome.call(session, welcome.params('Betsy', count=3))
    result = await call.result
    print(result.msg)

    call = await welcome.call(session, welcome.params('Jack', 5, 0.9))
    result = await call.result

    print('msg="{}", duration={}'.format(result.msg, result.duration))



loop = asyncio.get_event_loop()
loop.run_until_complete(run())
loop.close()
