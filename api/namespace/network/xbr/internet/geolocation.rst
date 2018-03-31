network.xbr.internet.geolocation
================================

IP geolocation related interfaces.

.. xbr:namespace:: network.xbr.internet.geolocation

------------


IIPGeolocator
-------------

.. xbr:interface:: IIPGeolocator

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
