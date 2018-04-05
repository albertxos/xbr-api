network.xbr.internet.connectivity
=================================

Internet device connectivity and network (link layer) information and statistics.

.. xbr:namespace:: network.xbr.internet.connectivity

------------


IDeviceConnectivityMonitor
--------------------------

.. xbr:interface:: IDeviceConnectivityMonitor

    Device connectivity monitor service instances run
    on end point device (eg smartphones) and monitor
    the device Internet connectivity.

    .. xbr:event:: on_roaming_change(is_roaming)

        Event fired when the roaming status of the
        device connection changes. Eg when a device
        is attaching to a non-home network (the device
        is "roaming"), this will fire.

        :param is_roaming: The new roaming status.
        :type is_roaming: bool
