network.xbr.consumer.analytics
==============================

Consumer analytics related interfaces.

.. xbr:namespace:: network.xbr.consumer.analytics

------------


ISportsFan
----------

.. xbr:interface:: ISportsFan

    Fan profile and character card API.

    .. xbr:procedure:: get_favorites(email_hash, level=0)

        Lookup favorite sport clubs or athletes for the person
        with the given email (the hash thereof).

        :price: N USD (paid in XBR) per 1,000 calls at ``level==0``.
            Higher prices apply for higher detail levels.
        :param email_hash: The SHA256 of the UTF8 encoded email address.
        :type email_hash: bytes
        :param level: Level of detail to return.
        :type level: int
        :returns: Fan favorites details.
        :rtype: dict
        :raises: email_not_found
