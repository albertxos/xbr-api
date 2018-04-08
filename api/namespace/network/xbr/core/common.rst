network.xbr.core.common
=======================

.. xbr:namespace:: network.xbr.core.common

.. xbr:interface:: IPaymentChannel

    Interface of a (unidirectional) payment channel.

    .. xbr:procedure:: close(last_seq_id, last_balance_remaining, signatures)

        Can be called by a XBR Market any time to initiate closing of the payment channel
        with the XBR Provider.

        The XBR Market will annonce the ``seq_id`` and ``balance_remaining`` it wants to use
        to settle the payment channel.

        When the XBR Provider agrees (is not aware of a transaction with a higher `seq_id`
        and the associated revenue), it should return immediately with success.

        When the XBR Provider disagrees, then the XBR Provider should raise an error.

        Any party (XBR Market or XBR Provider) can initiate the closing of the payment
        channel at any time - but will bare the blockchain gas costs doing so.

        Initiating a channel close will trigger a timer that ensure the channel is indeed
        close even when the other party remains uncooperative (not providing its latest
        transaction and signing off the final agreed payment channel state).

        :param last_seq_id: The ``seq_id`` of last transaction the XBR Market has logged
            and wants to base the closing of the payment channel on.
        :type last_seq_id: int
        :returns: The price quote in XBR token. Note that all amounts and balances in
            XBR tokens are always in 256 bit integers with 19 decimal digits for
            fractional XBR amounts.
        :rtype: int256
        :raises ApplicationError: ``xbr.service.payment.error.no-such-key``

    .. xbr::event on_channel_closing(channel_id)

        A payment channel participant has requested to closed the
        payment channel.

        :param channel_id: The ID of the channel that was requested
            to be closed.
        :type channel_id: int256

    .. xbr:event:: on_channel_closed(channel_id)

        Event fired when a payment channel has finally closed.

        :param channel_id: The ID of the channel that was requested
            to be closed.
        :type channel_id: int256
