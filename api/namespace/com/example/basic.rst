com.example.basic
=================

A couple of very basic interface examples.

.. xbr:namespace:: com.example.basic

------------


IMath
-----

.. xbr:interface:: IMath

    Do some awesome calculations using this interface;)

    :version: 1
    :uuid: 144a86774cab49d58afb947521f315cd

    .. xbr:procedure:: add(x, y)

        Returns the sum of two (integer) numbers.

        :param x: The first number.
        :type x: int
        :param y: The second number.
        :type y: int
        :returns: The sum of both numbers.
        :rtype: int

    .. xbr:procedure:: square(x, delay=0)

        Returns the square of an (integer) number.

        :param x: The number to square.
        :type x: int
        :param delay: Optional delay in seconds before
            the call returns, to simulate a long running
            computation.
        :type delay: int
        :returns: The square of the number.
        :rtype: int


ITime
-----

.. xbr:interface:: ITime

    Local service time API.

    Services that implement :xbr:interface:`ITime` just expose one method that returns the current time in UTC, and publish one event per second again
    with the current time.

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


IHello
------

.. xbr:interface:: IHello

    Hello world API. The most basic of all;)

    Services that implement :xbr:interface:`IHello` just expose one method that trivially returns a greeting message, and publishes an event.

    :version: 1
    :uuid: a7cbf72f44ec4ba38d2031f805f462d6

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
