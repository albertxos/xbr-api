from typing import Iterable
from abc import ABC, abstractmethod

import asyncio


def greet_all(usernames: Iterable[str]) -> None:
    for _username in usernames:
        print('Hello, {}'.format(_username))


def greeting(username: str) -> str:
    return 'Hello ' + username


async def spam(ignored: int) -> str:
    return 'spam'


async def foo() -> None:
    bar = await spam(42)  # type: str
    print(bar)


class IWelcome(ABC):

    @abstractmethod
    async def welcome(self, username: object) -> object:
        """
        Welcomes you.

        :param username: Whom to welcome.
        :returns: A personalized welcome message.
        """


class Welcome1(IWelcome):

    async def welcome(self, username: str) -> str:
        """
        Welcomes you.

        :param username: Whom to welcome.
        :returns: A personalized welcome message.
        """
        print('sleeping ..')
        await asyncio.sleep(1.)
        return 'Hello ' + username


IWelcome.register(Welcome1)


TEST_NAMES = ['Homer', 3, None]


greeting(222)


def test():
    for username in TEST_NAMES:
        msg = greeting(username)
        print(msg)


async def run():
    welcome1 = Welcome1()
    for username in TEST_NAMES:
        msg = greeting(username)
        print(msg)
        msg = await welcome1.welcome(username)
        print(msg)


test()
loop = asyncio.get_event_loop()
loop.run_until_complete(run())
loop.close()
