org.genivi.vss.drivetrain
=========================

Drivetrain data for internal combustion engines, transmissions, electric motors, etc.

.. xbr:namespace:: org.genivi.vss.drivetrain

IFuelCell
---------

.. xbr:interface:: IFuelCell

    Fuel Cell signals

IFuelSystem
-----------

.. xbr:interface:: IFuelSystem

    Fuel system signals


    .. xbr:event:: on_consumption_since_start(new_value)

        :param new_value: Fuel amount consumed since start in liters.
        :type new_value: float
        :vss_id: 81 
        
        :vss_type: Float 
        :vss_unit: l 
        :vss_sensor: Flow Sensor 
        


    .. xbr:event:: on_time_since_start(new_value)

        :param new_value: Time elapsed since start in seconds.
        :type new_value: int
        :vss_id: 82 
        
        :vss_type: UInt32 
        :vss_unit: s 
        :vss_sensor: Timer 
        


    .. xbr:event:: on_instant_consumption(new_value)

        :param new_value: Current consumption in liters per 100 km.
        :type new_value: float
        :vss_id: 79 
        
        :vss_type: Float 
        :vss_unit: l/100km 
        :vss_sensor: Flow Sensor 
        


    .. xbr:event:: on_level(new_value)

        :param new_value: Level in fuel tank as percent of capacity. 0 = empty. 100 = full.
        :type new_value: int
        :vss_id: 77 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Fuel Tank Level Sensor 
        


    .. xbr:event:: on_range(new_value)

        :param new_value: Range in meters.
        :type new_value: int
        :vss_id: 78 
        
        :vss_type: UInt32 
        :vss_unit: m 
        :vss_sensor: Fuel Tank Level Sensor 
        


    .. xbr:event:: on_average_consumption(new_value)

        :param new_value: Average consumption in liters per 100 km.
        :type new_value: float
        :vss_id: 80 
        
        :vss_type: Float 
        :vss_unit: l/100km 
        :vss_sensor: Flow Sensor 
        

ITransmission
-------------

.. xbr:interface:: ITransmission

    Transmission-specific data, stopping at the drive shafts.


    .. xbr:event:: on_travelled_distance(new_value)

        :param new_value: Odometer reading
        :type new_value: float
        :vss_id: 1121 
        
        :vss_type: Float 
        :vss_unit: km 
        :vss_sensor: Odometer 
        


    .. xbr:event:: on_gear(new_value)

        :param new_value: Current gear. 0=Neutral. -1=Reverse
        :type new_value: int
        :vss_id: 70 
        
        :vss_type: Int8 
        
        :vss_sensor: Gearbox 
        :vss_actuator: Gearbox 


    .. xbr:event:: on_performance_mode(new_value)

        :param new_value: Current gearbox performance mode.
        :type new_value: str
        :vss_id: 71 
        :vss_enum: ['normal', 'sport', 'economy', 'snow', 'rain'] 
        :vss_type: String 
        
        :vss_sensor: Drive System 
        :vss_actuator: Drive System 


    .. xbr:event:: on_clutch_wear(new_value)

        :param new_value: Clutch wear as a percent. 0 = no wear. 100 = worn.
        :type new_value: int
        :vss_id: 74 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Clutch Wear Indicator 
        


    .. xbr:event:: on_speed(new_value)

        :param new_value: Vehicle speed, as sensed by the gearbox.
        :type new_value: int
        :vss_id: 68 
        
        :vss_type: Int32 
        :vss_unit: km/h 
        :vss_sensor: Speedometer 
        


    .. xbr:event:: on_gear_change_mode(new_value)

        :param new_value: Is the gearbox in automatic or manual (paddle) mode.
        :type new_value: str
        :vss_id: 72 
        :vss_enum: ['manual', 'automatic'] 
        :vss_type: String 
        
        :vss_sensor: Drive System 
        :vss_actuator: Drive System 


    .. xbr:event:: on_temperature(new_value)

        :param new_value: The current gearbox temperature
        :type new_value: int
        :vss_id: 73 
        
        :vss_type: Int16 
        :vss_unit: celsius 
        
        

IElectricMotor
--------------

.. xbr:interface:: IElectricMotor

    Electric Motor specific signals.

IInternalCombustionEngine
-------------------------

.. xbr:interface:: IInternalCombustionEngine

    Engine-specific data, stopping at the bell housing.


    .. xbr:event:: on_engine__e_o_p(new_value)

        :param new_value: Engine oil pressure.
        :type new_value: int
        :vss_id: 1117 
        
        :vss_type: Int16 
        :vss_unit: kpa 
        :vss_sensor: Oil Pressure Sensor 
        


    .. xbr:event:: on_engine__m_a_p(new_value)

        :param new_value: Manifold air pressure possibly boosted using forced induction.
        :type new_value: int
        :vss_id: 1114 
        
        :vss_type: Int16 
        :vss_unit: kpa 
        :vss_sensor: Manifold Air Pressure Sensor 
        


    .. xbr:event:: on_engine__power(new_value)

        :param new_value: Current engine power output.
        :type new_value: int
        :vss_id: 1118 
        
        :vss_type: Int16 
        :vss_unit: kW 
        :vss_sensor: Power Meter 
        


    .. xbr:event:: on_engine__e_o_t(new_value)

        :param new_value: Engine oil temperature.
        :type new_value: int
        :vss_id: 1113 
        
        :vss_type: Int16 
        :vss_unit: celsius 
        :vss_sensor: Oil Thermometer 
        


    .. xbr:event:: on_engine__torque(new_value)

        :param new_value: Current engine torque.
        :type new_value: int
        :vss_id: 1119 
        
        :vss_type: Int16 
        :vss_unit: N.m 
        :vss_sensor: Torque Meter 
        


    .. xbr:event:: on_engine__ambient_air_temperature(new_value)

        :param new_value: Ambient (Outside) air temperature
        :type new_value: float
        :vss_id: 1120 
        
        :vss_type: Float 
        :vss_unit: celsius 
        :vss_sensor: Thermometer 
        


    .. xbr:event:: on_engine__e_c_t(new_value)

        :param new_value: Engine coolant temperature.
        :type new_value: int
        :vss_id: 1112 
        
        :vss_type: Int16 
        :vss_unit: celsius 
        :vss_sensor: Coolant Thermometer 
        


    .. xbr:event:: on_engine__t_p_s(new_value)

        :param new_value: Current throttle position.
        :type new_value: int
        :vss_id: 1116 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Throttle Position Sensor 
        


    .. xbr:event:: on_engine__m_a_f(new_value)

        :param new_value: Grams of air drawn into engine per second.
        :type new_value: int
        :vss_id: 1115 
        
        :vss_type: Int16 
        :vss_unit: g/s 
        :vss_sensor: Mass Air Flow Sensor 
        


    .. xbr:event:: on_engine__speed(new_value)

        :param new_value: Engine speed measured as rotations per minute.
        :type new_value: int
        :vss_id: 1111 
        
        :vss_type: UInt16 
        :vss_unit: rpm 
        :vss_sensor: Rotational Speed Sensor 
        

IBatteryManagement
------------------

.. xbr:interface:: IBatteryManagement

    Battery Management signals


    .. xbr:event:: on_battery_capacity(new_value)

        :param new_value: Remaining capacity of the batter pack
        :type new_value: int
        :vss_id: 76 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Battery Monitor 
        


    .. xbr:event:: on_battery_temperature(new_value)

        :param new_value: Temperature of the battery pack
        :type new_value: float
        :vss_id: 75 
        
        :vss_type: Float 
        :vss_unit: celsius 
        :vss_sensor: Thermometer 
        
