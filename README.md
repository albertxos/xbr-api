# XBR API library

This repository contains a library of XBR APIs shared in the XBR network and community.

* [APIs](api/)


```yaml

```


If you work in open source, then it's increasingly likely that you've come across the Sphinx documentation tool. Originally written by and for the Python community, the past few years have seen an increasingly rapid adoption by non-Python projects. Recent adopters of Sphinx include the Linux kernel, Open vSwitch and the Dataplane Development Kit (DPDK), while other projects such as QEMU are preparing plans to migrate.



There is now a strong consensus that APIs should be designed from front-to-back with an emphasis on the developer usability of the API. In a crowded economy with many competing products and many competing API implementations, the easy to use and well designed APIs will have an advantage in attracting and retaining developers.

Humans are the key ingredients in API design which means that API design tools and documentation formats must be human readable and writeable. Recent API documentation standards strive to be "human-centric."

https://www.infoq.com/articles/eventlog-api-raml/


.. xbr::interface network.xbr.payment

    XBR standard payment API that every provider service
    must implement.

    .. xbr:error no_such_key(msg, key_id)

        The specified key was not found.

        @param msg: A human readable error message.
        @type msg: str

        @param key_id: The key that was specified and not found.
        @type key_id: bytes32

    .. xbr::procedure quote(key_id, duration=10)

        Get a quote for the given ``key_id``.

        @param key_id: ID of the key to get a quote for.
        @type key_id: bytes32

        @param duration: The duration in seconds for which
            the quote is requested to hold.
        @type duration: int

        @returns: A quoted price in XBR token.
        @rtype: int256

        @raises: no_such_key

    .. xbr::event on_channel_close_requested(channel_id)

        A payment channel participant has requested to closed the
        payment channel.

        @param channel_id: The ID of the channel that was requested
            to be closed.
        @type channel_id: int256
