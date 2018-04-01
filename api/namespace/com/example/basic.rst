com.example.basic
=================

Consumer analytics related interfaces.

.. xbr:namespace:: com.example.basic

------------


IHelloWorld
-----------

Services that implement :xbr:interface:`IHelloWorld` just expose one method that trivially returns a greeting message, and publishes an event.

.. xbr:interface:: IHelloWorld

    Hello world API. The most basic of all;)

    .. xbr:procedure:: say_hello(name)

        Returns a hello message addressed to the given name.

        :param name: The name of the person to greet.
        :type name: str
        :returns: A greeting message.
        :rtype: str
        :raises: invalid_name

    .. xbr:event:: on_hello(msg)

        Event published when a hello message was sent.

        :param msg: The greeting message.
        :type msg: str


IUTCTime
--------

Services that implement :xbr:interface:`IUTCTime` just expose one method that returns the current time in UTC, and publish one event per second again
with the current time.

.. xbr:interface:: IUTCTime

    Local service time API.

    :version: 1
    :uuid: 427bffedc63740ffa8d4564560b8a200

    .. xbr:procedure:: get_time(format=None)

        Current UTC time as seen by the service that
        implements this interface.

        :param format: Optional format string for the timestamp returned,
            eg ``"%Y-%m-%dT%H:%M:%S.%f"``. If none is given, ISO 8601
            format will be used.
        :type format: str
        :returns: Get current time in UTC as ISO 8601 string,
            eg ``2018-04-01T20:21:00.877Z``.
        :rtype: str

    .. xbr:event:: on_tick(tick, timestamp)

        Event published every second with the current time in UTC.

        :param tick: Tick number starting from 1.
        :type tick: int
        :param timestamp: Current time in UTC as ISO 8601 string,
            eg ``2018-04-01T20:21:00.877Z``.
        :type timestamp: str
