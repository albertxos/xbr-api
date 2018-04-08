network.xbr.internet.geolocation
================================

IP geolocation related interfaces.

.. xbr:namespace:: network.xbr.internet.geolocation

------------


IPGeoLocator
------------

.. xbr:interface:: IPGeoLocator

    IP geolocation API. This services allows to find information about
    the geographic location (eg country, state or city) given an IP
    address.

    .. xbr:procedure:: lookup_ipv4(ipv4)

        Lookup IPv4 address and return location information.

        :param ipv4: The IPv4 address to lookup.
        :type ipv4: str
        :returns: Location details.
        :rtype: dict
        :raises: no_location_info


IPGeoRevealer
-------------

.. xbr:interface:: IPGeoRevealer

    .. xbr:procedure:: reveal()

        Lookup IPv4 address and return location information.

        * IPv4 subnet (*) of public device IP on Internet connection
        * device location (resolution 1 km (*))
        * device local time and timezone

        The limitation of the resolution of the device IP address to
        a whole subnet (which usually carries many devices), and to
        the spatial, geographic resolution of 1 km avoids personal
        information leakage.
