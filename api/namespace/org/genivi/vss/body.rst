org.genivi.vss.body
===================

All body components

.. note::

    The XBR interface description here was auto-generated
    `using a script <https://github.com/xbr/xbr-api/tree/master/extern/vss>`_
    from the
    `Vehicle Signaling Specification (VSS) <https://github.com/GENIVI/vehicle_signal_specification>`_.
    The VSS is
    `licensed <https://raw.githubusercontent.com/GENIVI/vehicle_signal_specification/master/LICENSE>`_
    under the Mozilla Public License 2.0, and the auto-generated files in this
    repository should be considered derived works.
    If you have improvements for or have found a bug in the APIs of namespace
    ``org.genivi.vss``, please head over to
    `GENIVIs issue tracker <https://github.com/GENIVI/vehicle_signal_specification/issues>`_.

.. xbr:namespace:: org.genivi.vss.body

IMirrors
--------

All mirrors.

.. xbr:interface:: IMirrors

    All mirrors


    .. xbr:event:: on_right_tilt(new_value)

        :param new_value: Mirror tilt as a percent. 0 = Center Position. 100 = Fully Upward Position. -100 = Fully Downward Position.
        :type new_value: int
        :vss_id: 110 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Mirror Tilt Sensor 
        :vss_actuator: Mirror Tilt Actuator 


    .. xbr:event:: on_right_heating_status(new_value)

        :param new_value: Mirror Heater on or off. True = Heater On. False = Heater Off.
        :type new_value: bool
        :vss_id: 1128 
        
        :vss_type: Boolean 
        
        :vss_sensor: Mirror heater 
        :vss_actuator: Mirror heater 


    .. xbr:event:: on_right_pan(new_value)

        :param new_value: Mirror pan as a percent. 0 = Center Position. 100 = Fully Left Position. -100 = Fully Right Position.
        :type new_value: int
        :vss_id: 111 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Mirror Pan Sensor 
        :vss_actuator: Mirror Pan Actuator 


    .. xbr:event:: on_left_tilt(new_value)

        :param new_value: Mirror tilt as a percent. 0 = Center Position. 100 = Fully Upward Position. -100 = Fully Downward Position.
        :type new_value: int
        :vss_id: 107 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Mirror Tilt Sensor 
        :vss_actuator: Mirror Tilt Actuator 


    .. xbr:event:: on_left_heating_status(new_value)

        :param new_value: Mirror Heater on or off. True = Heater On. False = Heater Off.
        :type new_value: bool
        :vss_id: 1127 
        
        :vss_type: Boolean 
        
        :vss_sensor: Mirror heater 
        :vss_actuator: Mirror heater 


    .. xbr:event:: on_left_pan(new_value)

        :param new_value: Mirror pan as a percent. 0 = Center Position. 100 = Fully Left Position. -100 = Fully Right Position.
        :type new_value: int
        :vss_id: 108 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Mirror Pan Sensor 
        :vss_actuator: Mirror Pan Actuator 

IHorn
-----

Horn signals.

.. xbr:interface:: IHorn

    Horn signals


    .. xbr:event:: on_is_active(new_value)

        :param new_value: Horn active or inactive. True = Active. False = Inactive.
        :type new_value: bool
        :vss_id: 86 
        
        :vss_type: Boolean 
        
        :vss_sensor: Horn System 
        :vss_actuator: Horn System 

ILights
-------

All lights.

.. xbr:interface:: ILights

    All lights


    .. xbr:event:: on_is_left_indicator_on(new_value)

        :param new_value: Is left indicator flashing
        :type new_value: bool
        :vss_id: 105 
        
        :vss_type: Boolean 
        
        :vss_sensor: Left Indicator Switch 
        :vss_actuator: Left Indicator Light 


    .. xbr:event:: on_is_low_beam_on(new_value)

        :param new_value: Is low beam on
        :type new_value: bool
        :vss_id: 97 
        
        :vss_type: Boolean 
        
        :vss_sensor: Low Beam Light Switch 
        :vss_actuator: Low Beam Light 


    .. xbr:event:: on_is_high_beam_on(new_value)

        :param new_value: Is high beam on
        :type new_value: bool
        :vss_id: 96 
        
        :vss_type: Boolean 
        
        :vss_sensor: High Beam Light Switch 
        :vss_actuator: High Beam Light 


    .. xbr:event:: on_is_front_fog_on(new_value)

        :param new_value: Is front fog light on
        :type new_value: bool
        :vss_id: 103 
        
        :vss_type: Boolean 
        
        :vss_sensor: Front Fog Light Switch 
        :vss_actuator: Front Fog Light 


    .. xbr:event:: on_is_brake_on(new_value)

        :param new_value: Is brake light on
        :type new_value: bool
        :vss_id: 101 
        
        :vss_type: Boolean 
        
        :vss_sensor: Brake Light Switch 
        :vss_actuator: Brake Light 


    .. xbr:event:: on_is_right_indicator_on(new_value)

        :param new_value: Is right indicator flashing
        :type new_value: bool
        :vss_id: 106 
        
        :vss_type: Boolean 
        
        :vss_sensor: Right Indicator Switch 
        :vss_actuator: Right Indicator Light 


    .. xbr:event:: on_is_backup_on(new_value)

        :param new_value: Is backup (reverse) light on
        :type new_value: bool
        :vss_id: 99 
        
        :vss_type: Boolean 
        
        :vss_sensor: Backup Light Switch 
        :vss_actuator: Backup Light 


    .. xbr:event:: on_is_parking_on(new_value)

        :param new_value: Is parking light on
        :type new_value: bool
        :vss_id: 100 
        
        :vss_type: Boolean 
        
        :vss_sensor: Parking Light Switch 
        :vss_actuator: Parking Light 


    .. xbr:event:: on_is_rear_fog_on(new_value)

        :param new_value: Is rear fog light on
        :type new_value: bool
        :vss_id: 102 
        
        :vss_type: Boolean 
        
        :vss_sensor: Rear Fog Light Switch 
        :vss_actuator: Rear Fog Light 


    .. xbr:event:: on_is_hazard_on(new_value)

        :param new_value: Are hazards on
        :type new_value: bool
        :vss_id: 104 
        
        :vss_type: Boolean 
        
        :vss_sensor: Hazard Light Switch 
        :vss_actuator: Hazard Light 


    .. xbr:event:: on_is_running_on(new_value)

        :param new_value: Are running lights on
        :type new_value: bool
        :vss_id: 98 
        
        :vss_type: Boolean 
        
        :vss_sensor: Running Light Switch 
        :vss_actuator: Running Light 

IHood
-----

Hood status.

.. xbr:interface:: IHood

    Hood status


    .. xbr:event:: on_is_open(new_value)

        :param new_value: hood open or closed. True = Open. False = Closed
        :type new_value: bool
        :vss_id: 83 
        
        :vss_type: Boolean 
        
        :vss_sensor: Hood Latch 
        :vss_actuator: Hood Latch 

ITrunk
------

Trunk status.

.. xbr:interface:: ITrunk

    Trunk status


    .. xbr:event:: on_is_locked(new_value)

        :param new_value: Is trunk locked or unlocked. True = Locked. False = Unlocked.
        :type new_value: bool
        :vss_id: 85 
        
        :vss_type: Boolean 
        
        :vss_sensor: Trunk Lock 
        :vss_actuator: Trunk Lock 


    .. xbr:event:: on_is_open(new_value)

        :param new_value: Trunk open or closed. True = Open. False = Closed
        :type new_value: bool
        :vss_id: 84 
        
        :vss_type: Boolean 
        
        :vss_sensor: Trunk Latch 
        :vss_actuator: Trunk Latch 

IWindshield
-----------

Windshield signals.

.. xbr:interface:: IWindshield

    Windshield signals


    .. xbr:event:: on_front_wiping_status(new_value)

        :param new_value: Front wiper status
        :type new_value: str
        :vss_id: 1123 
        :vss_enum: ['off', 'slow', 'medium', 'fast', 'interval', 'rainsensor'] 
        :vss_type: String 
        
        :vss_sensor: Wiper Switch 
        :vss_actuator: Wiper 


    .. xbr:event:: on_front_heating_status(new_value)

        :param new_value: Front windshield heater status. 0 - off, 1 - on
        :type new_value: bool
        :vss_id: 1124 
        
        :vss_type: Boolean 
        
        :vss_sensor: Windshield Heater Switch 
        :vss_actuator: Windshield Heater 


    .. xbr:event:: on_front_washer_fluid_level_low(new_value)

        :param new_value: Low level indication for washer fluid. True = Level Low. False = Level OK.
        :type new_value: bool
        :vss_id: 90 
        
        :vss_type: Boolean 
        
        :vss_sensor: Washer Fuild Level Sensor 
        


    .. xbr:event:: on_front_washer_fluid_level(new_value)

        :param new_value: Washer fluid level as a percent. 0 = Empty. 100 = Full.
        :type new_value: int
        :vss_id: 91 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Washer Fuild Level Sensor 
        


    .. xbr:event:: on_rear_wiping_status(new_value)

        :param new_value: Rear wiper status
        :type new_value: str
        :vss_id: 1125 
        :vss_enum: ['off', 'slow', 'medium', 'fast', 'interval', 'rainsensor'] 
        :vss_type: String 
        
        :vss_sensor: Wiper Switch 
        :vss_actuator: Wiper 


    .. xbr:event:: on_rear_heating_status(new_value)

        :param new_value: Rear windshield heater status. 0 - off, 1 - on
        :type new_value: bool
        :vss_id: 1126 
        
        :vss_type: Boolean 
        
        :vss_sensor: Windshield Heater Switch 
        :vss_actuator: Windshield Heater 


    .. xbr:event:: on_rear_washer_fluid_level_low(new_value)

        :param new_value: Low level indication for washer fluid. True = Level Low. False = Level OK.
        :type new_value: bool
        :vss_id: 94 
        
        :vss_type: Boolean 
        
        :vss_sensor: Washer Fuild Level Sensor 
        


    .. xbr:event:: on_rear_washer_fluid_level(new_value)

        :param new_value: Washer fluid level as a percent. 0 = Empty. 100 = Full.
        :type new_value: int
        :vss_id: 95 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Washer Fuild Level Sensor 
        

IRaindetection
--------------

Rainsensor signals.

.. xbr:interface:: IRaindetection

    Rainsensor signals


    .. xbr:event:: on_intensity(new_value)

        :param new_value: Rain intensity. 0 = Dry, No Rain. 100 = Covered.
        :type new_value: int
        :vss_id: 1122 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Rain Sensor 
        
