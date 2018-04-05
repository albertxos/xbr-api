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
