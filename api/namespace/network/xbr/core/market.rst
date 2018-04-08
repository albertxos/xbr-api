network.xbr.core.market
=======================

.. xbr:namespace:: network.xbr.core.market


IMarket
-------

.. xbr:interface:: IMarket

    Every XBR market must implement this market API which is used by data
    consumer and providers to interact with the data market.

    .. xbr:procedure:: list_apis(private_only=False)

        Return a list of APIs registered in this market. This includes both
        public APIs and private APIs only registered in this market, and
        only implemented and provided by data providers in this private
        data market.

        :param private_only: If ``True``, only return private APIs, else return
            both public and private APIs registered in this market.
        :returns: A list of API UUIDs.
        :rtype: list(str)

    .. xbr:procedure:: get_api_metadata(api_id)

        Return metadata for the given API registered in this market.

        :param api_id: The UUID of the API to lookup metadata for.
            The XBR data API ID is unique and market independent
            in the whole XBR network.
        :type api_id: str
        :returns: A dictionary with API metadata.
        :rtype: dict

    .. xbr:procedure:: list_providers(api_id)

        Return a list of providers the offer services in this market
        which implement the given API.

        :param api_id: The UUID of the API to lookup providers for.
        :type api_id: str
        :returns: A list of provider UUIDs.
        :rtype: list(str)

    .. xbr:procedure:: get_provider_metadata(provider_id)

        Return metadata for the given data provider in this market.

        :param provider_id: The UUID of the XBR data provider to
            lookup metadata for.
            The XBR data provider ID is unique and market independent
            in the whole XBR network.
        :type provider_id: str

    .. xbr:procedure:: get_service(api_id, provider_id)

        Return a service implementing the given API, and from the given provider.

        When the API or service provider given is not registered in this market,
        an error is returned.

        When there currently is no running service for the given API and
        service provider, an error is returned.

        :param api_id: The UUID of the API the service must implement.
        :type api_id: str
        :param provider_id: The UUID of the data provider the service
            must be provided by.
        :type provider_id: str
        :returns: A pair ``(service_id, service_key)`` with the UUID and
            the WAMP-cryptosign (Ed25519) public key of the service.
        :rtype: tuple

