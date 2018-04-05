network.xbr.core.market
=======================

.. xbr:namespace:: network.xbr.core.market


IMarket
-------

.. xbr:interface:: IMarket

    Every XBR market must implement this market API which is used by data
    consumer and providers to interact with the data market.

    When the API or service provider given is not registered in this market,
    an error is returned.

    When there currently is no running service for the given API and
    service provider, an empty list is returned.

    .. xbr:procedure:: get_services(api_id, provider_id)

        Get services implementing a given API, and provided in the
        data market by a given provider.

        :param api_id: The UUID of the API the services listed must implement.
        :type api_id: str
        :param provider_id: The UUID of the data provider the services listed
            must be provided by.
        :type provider_id: str
        :returns: A list of pairs ``(service_id, service_key)`` with the UUID and
            the WAMP-cryptosign (Ed25519) public key of the service.
        :rtype: list
