network.xbr.manufacturing.machine
=================================

Write me.

.. xbr:namespace:: network.xbr.manufacturing.machine

------------

IPLCS7Monitor
-------------

.. xbr:interface:: IPLCS7Monitor

    Write me.

    .. xbr:procedure:: load(name, config)

        Write me.

        :param name: Name to load the configuration under.
        :type name: str
        :param config: S7 PLC monitoring configuration to load.
        :type config: str
        :returns: The SHA256 of the config loaded.
        :rtype: str

    .. xbr:procedure:: start(name)

        Starts a (previously loaded) monitoring configuration.

        There can be only one monitoring configuration per PLC.

        :param name: The name of the (loaded) monitoring configuration
            to start.
        :type name: str

    .. xbr:procedure:: stop(name=None)

        Stops a (currently running) monitoring configuration.

        :param name: The name of the monitoring configuration to stop
            or ``None`` to stop all.
        :type name: str or None
        :returns: A list of pairs ``(config_name, config_sha256)`` of
            configurations stopped.
        :rtype: list of tuple

    .. xbr:event:: on_data(data)

        The machine S7 PLC monitor will publish an event whenever the
        monitoring has detected a state change in the PLC.

        The event information includes:

        * ``machine_id``: a unique ID for the machine that executed
          the production step
        * ``plc_id``: a unique ID for the PLC that controlled the
          production step
        * ``fsm_id``: a unique ID for the FSM within the PLC that
          controlled the production step
        * ``fsm_state_id``: a unique ID for the FSM state within the PLC.
          *This corresponds to a production step.*

        The part that passed through a production step while the production
        step was executed is identified by:

        * ``part_id``: an unique ID for the part that passed the production
          step the event was fired for

        The time when the production step was started (by the PLC):

        * ``timestamp``: a high-resolution event timestamp inserted by
          the PLC itself when the production step was *started*

        The actual data tracked for the production step execution can include:

        * ``time``: the *time* the production step took in *seconds*.
        * ``energy``: the *energy* the production step consumed in *Joule*.
        * ``air``: the (industrial) *air* the production step consumed in *m^3*.

        The data tracked can also contain more attributes with measurements or
        outcomes for the *single* production step execution.
