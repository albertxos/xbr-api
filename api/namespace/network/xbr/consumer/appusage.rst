network.xbr.consumer.appusage
=============================

End user application usage monitoring and reporting interfaces.

.. xbr:namespace:: network.xbr.consumer.appusage

------------

IAppUsageMonitor
----------------

.. xbr:interface:: IAppUsageMonitor

    A service that implements the application usage monitor API
    monitors and provides access to the application usage on
    the (individual) end user device is running on.

    .. xbr:procedure:: get_running_apps(top=5, sort="cpu")

        Return top N currently running apps, sorted by CPU load
        or memory, for example, with ``top=1``:

        .. code-block:: json

            [
                {
                    "executable": "chromium-browser",
                    "package": "chromium-browser",
                    "cpu": 23.43,
                    "memory": 123901344
                }
            ]

        The returned data does *not* reveal sensitive data like fully
        qualified filesystem paths, or local user names.

        :param top: Only return the top N running apps sorted
            by ``sort``.
        :type top: int
        :param sort: Sort by either ``"cpu"`` or by ``"memory"``
            incurred by the app
        :type sort: str
        :returns: A list (of length ``top``) of dicts as in the
            example above.
        :rtype: list


IAppUsageReport
---------------

.. xbr:interface:: IAppUsageReport

    A service that implements the application usage report API
    aggregates raw data from many services that implement
    :xbr:interface:`IAppUsageMonitor` and provides access to
    aggregate reports on end user application usage.

    Examples of reports:

    - weekly top-10 used apps
    - usage per country/app
