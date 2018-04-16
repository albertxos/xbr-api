"""
Roadtrack condition monitoring interfaces.
"""

from typing import Callable

from autobahn.wamp.interfaces import ISession
from autobahn.wamp.types import EventDetails


class Topic(object):
    """

    """

    def __init__(self, uri: str):
        """

        :param uri:
        """


class WelcomeTopic(Topic):
    """
    Event fired when a welcome message was sent.
    """

    class Event(object):
        def __init__(self, username: str, msg: str):
            """

            :param username: The name of the user the welcome message
                was sent to.
            :param msg: The welcome message sent.
            """

    @staticmethod
    async def subscribe(session: ISession, handler: Callable[[ISession, Event, EventDetails], None]) -> None:
        """
        Subscribe to topic and process events in the event handler.

        :param session: Session on which to subscribe.
        :param handler: Event handler to process events received.
        """

    @staticmethod
    async def publish(session: ISession, event: EventPayload) -> None:
        """
        Publish the event.

        :param session: Session on which to subscribe.
        :param event: The event to publish.
        """
