network.xbr.consumer.analytics
==============================

Consumer analytics related interfaces.

.. xbr:namespace:: network.xbr.consumer.analytics

------------


ISportsFan
----------

.. xbr:interface:: ISportsFan

    Fan profile and character card API.

    .. xbr:procedure:: get_favorites(email_hash)

        Lookup favorite sport clubs or athletes for the person
        with the given email (the hash thereof).

        :param email_hash: The SHA256 of the UTF8 encoded email address.
        :type email_hash: bytes
        :returns: Fan favorites details.
        :rtype: dict
        :raises: email_not_found
