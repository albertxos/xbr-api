"""
Roadtrack condition monitoring interfaces.
"""

import time
import asyncio

from autobahn.wamp.interfaces import ISession
from typing import Callable, Awaitable

__all__ = (
    'register',
    'call',
    'Params',
    'Call',
    'Result',
)


class Params(object):
    """
    Parameters to the welcome procedure.
    """

    def __init__(self, username: str, count: int=1, delay: float=1.) -> None:
        """

        :param username: Your name;) The welcome service will use that.
        :param count: Repeat the welcome message this many times.
        :param delay: Delay the returning of a welcome message this many seconds.
        """
        self.username = username
        self.count = count
        self.delay = delay


class Result(object):
    """
    Result of the welcome Procedure.
    """

    def __init__(self, msg: str, duration: float) -> None:
        """

        :param msg: The welcome message.
        :param duration: The duration of the procedure call in seconds.
        """
        self.msg = msg
        self.duration = duration






class Call(object):
    """
    Type of a call of this Procedure.
    """

    def __init__(self, result: Awaitable[Result]=None) -> None:
        self.result = result


async def register(session: ISession, handler: Callable[[ISession, Params], Result]) -> None:
    """
    Register a user code handler for this Procedure.
    """


async def call(session: ISession, params: Params) -> Call:
    """
    Welcomes you.

    :param username: Whom to welcome.
    :returns: A personalized welcome message.
    """
    started = time.time()
    print('sleeping ..')
    await asyncio.sleep(params.delay)

    msg = ' '.join(('Hello ' + params.username) * params.count)
    duration = time.time() - started

    actual_res = Result(msg, duration)
    actual_res.msg = 'Hello, ' + params.username + '! Here are ' + \
                     str(params.count) + ' stars: ' + ('*' * params.count)

    res = Call()
    res.result = asyncio.Future()
    res.result.set_result(actual_res)

    return res
