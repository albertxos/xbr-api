network.xbr.mobility.navigation
===============================

Vehicle navigation related interfaces.

.. xbr:namespace:: network.xbr.mobility.navigation

------------


INavigationMonitor
------------------

.. xbr:interface:: INavigationMonitor

    Vehicle navigation monitoring API.

    .. warning::

        This API provides read-only, but privacy-sensitive data.

    .. xbr:event:: on_navigation_started(navigation_id, destination_name, coordinates, estimated_arrival, estimated_distance)

        Event fired when a new navigation destination has been entered
        and the navigation started.

        :param navigation_id: The ID of the navigation started. This is
            assigned by the service implementation, and only guaranteed
            to be unique within that service implementation, but for
            the lifetime of the latter.
        :type navigation_id: str
        :param destination_name: Human readable name or title of the destination.
        :type destination_name: str
        :param coordinates: GPS coordinates of the destination.
        :type coordinates: [int, int]
        :param estimated_arrival: Estimated arrival time in UTC (in
            ISO 8601 format, eg ``2018-03-31T15:13:21.978Z``).
        :type estimated_arrival: str
        :param estimated_tta: Estimated time to arrival in seconds.
        :type estimated_tta: int
        :param estimated_distance: Estimated distance to the destination in meters.
        :type estimated_distance: int

    .. xbr:event:: on_navigation_progress(navigation_id, estimated_tta, estimated_distance)

        Even fired when a navigation makes progress towards a destination.

        :param navigation_id: The ID of the navigation to the destination.
        :type navigation_id: str

        :param navigation_id: The ID of the navigation for which this
            progress event is published for.
        :type navigation_id: str
        :param estimated_tta: The new estimated time to arrival
            in seconds.
        :type estimated_tta: int
        :param estimated_distance: The new, updated estimated distance to the destination in meters.
        :type estimated_distance: int

        .. note::

            The frequency and timing of this event is service
            implementation defined. Eg an implementation might choose
            to increase the progress event frequency only as the
            destination is approaching, and publish events only rarely
            before.

    .. xbr:event:: on_navigation_ended(navigation_id, reason, ended)

        Event fired when vehicle is in navigation mode and has reached its destination.

        :param navigation_id: The ID of the navigation to the destination.
        :type navigation_id: str
        :param reason: The reason for the end of navigation. One of:
            ``"arrived"``, ``"canceled"``
        :param ended: Navigation ended at UTC (in
            ISO 8601 format, eg ``2018-03-31T15:13:21.978Z``). In case
            of destination reached, this is the actual arrival time.
        :type ended: str

    .. xbr:procedure:: get_navigation_details(navigation_id=None)

        Procedure to access navigation details of a navigation.

        .. note::

            For a currently running navigation, this procedure always returns. For a navigation that already ended, access to
            historical data is service implementation defined.

        :param navigation_id: The ID of the navigation for which to
            return navigation details. If ``None``, return details for
            current running navigation (if any).
        :type navigation_id: str
        :returns: Navigation details.
        :rtype: dict
        :raises: no_such_navigation

--------------


IAnonymousNavigationMonitor
---------------------------

.. xbr:interface:: IAnonymousNavigationMonitor

    Vehicle navigation monitoring API that does not expose personal
    information, only anonymous and functional information.

    .. note::

        This API provides read-only, and anonymous data only access.
        For an API that exposes a richer set of information, see
        :xbr:interface:`INavigationMonitor`

    .. xbr:event:: on_navigation_started(navigation_id, estimated_arrival, estimated_distance)

        Event fired when a new navigation destination has been entered
        and the navigation started.

        :param navigation_id: The ID of the navigation started. This is
            assigned by the service implementation, and only guaranteed
            to be unique within that service implementation, but for
            the lifetime of the latter.
        :type navigation_id: str
        :param estimated_arrival: Estimated arrival time in UTC (in
            ISO 8601 format, eg ``2018-03-31T15:13:21.978Z``).
        :type estimated_arrival: str
        :param estimated_tta: Estimated time to arrival in seconds.
        :type estimated_tta: int
        :param estimated_distance: Estimated distance to the destination in meters.
        :type estimated_distance: int

    .. xbr:event:: on_navigation_progress(navigation_id, estimated_tta, estimated_distance)

        Even fired when a navigation makes progress towards a destination.

        :param navigation_id: The ID of the navigation to the destination.
        :type navigation_id: str

        :param navigation_id: The ID of the navigation for which this
            progress event is published for.
        :type navigation_id: str
        :param estimated_tta: The new estimated time to arrival
            in seconds.
        :type estimated_tta: int
        :param estimated_distance: The new, updated estimated distance to the destination in meters.
        :type estimated_distance: int

        .. note::

            The frequency and timing of this event is service
            implementation defined. Eg an implementation might choose
            to increase the progress event frequency only as the
            destination is approaching, and publish events only rarely
            before.

    .. xbr:event:: on_navigation_ended(navigation_id, reason, ended)

        Event fired when vehicle is in navigation mode and has reached its destination.

        :param navigation_id: The ID of the navigation to the destination.
        :type navigation_id: str
        :param reason: The reason for the end of navigation. One of:
            ``"arrived"``, ``"canceled"``
        :param ended: Navigation ended at UTC (in
            ISO 8601 format, eg ``2018-03-31T15:13:21.978Z``). In case
            of destination reached, this is the actual arrival time.
        :type ended: str

    .. xbr:procedure:: get_navigation_details(navigation_id=None)

        Procedure to access navigation details of a navigation.

        .. note::

            For a currently running navigation, this procedure always returns. For a navigation that already ended, access to
            historical data is service implementation defined.

        :param navigation_id: The ID of the navigation for which to
            return navigation details. If ``None``, return details for
            current running navigation (if any).
        :type navigation_id: str
        :returns: Navigation details, mainly navigation status
            (reason), estimated distance and estimated
            time-to-arrival.
        :rtype: dict
        :raises: no_such_navigation
