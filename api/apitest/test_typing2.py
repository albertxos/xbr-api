import ./xbr

from typing import Callable


def on_hello_handler(name: str, msg: str) -> None:
    """
    Event published when a welcome message was generated and returned.

    :param name: The name that was welcome.
    :param msg: The complete welcome message.
    """


def on_hello_subscribe(handler: Callable[[str, str], None]) -> None:
    """
    Subscribe to event.

    :param handler: Event handler.
    """


def my_on_hello(name: str, msg: str) -> int:
    print('Name: ' + name)
    print('Message: ' + msg)
    return 23


subscribe_on_hello(my_on_hello)
