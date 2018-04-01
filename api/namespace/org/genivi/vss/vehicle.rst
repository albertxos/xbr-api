org.genivi.vss.vehicle
======================

Highlevel vehicle data.

.. xbr:namespace:: org.genivi.vss.vehicle

IVehicle
--------

.. xbr:interface:: IVehicle

    FIXME


    .. xbr:event:: on_acceleration__lateral(new_value)

        :param new_value: Vehicle acceleration in Y (lateral acceleration).
        :type new_value: int
        :vss_id: 1106 
        
        :vss_type: Int32 
        :vss_unit: m/s2 
        :vss_sensor: Accelerometer 
        


    .. xbr:event:: on_acceleration__longitudinal(new_value)

        :param new_value: Vehicle acceleration in X (longitudinal acceleration).
        :type new_value: int
        :vss_id: 1105 
        
        :vss_type: Int32 
        :vss_unit: m/s2 
        :vss_sensor: Accelerometer 
        


    .. xbr:event:: on_acceleration__vertical(new_value)

        :param new_value: Vehicle acceleration in Z (vertical acceleration).
        :type new_value: int
        :vss_id: 1107 
        
        :vss_type: Int32 
        :vss_unit: m/s2 
        :vss_sensor: Accelerometer 
        


    .. xbr:event:: on_travelled_distance(new_value)

        :param new_value: Odometer reading
        :type new_value: float
        :vss_id: 1103 
        
        :vss_type: Float 
        :vss_unit: km 
        :vss_sensor: Odometer 
        


    .. xbr:event:: on_idle_time(new_value)

        :param new_value: Accumulated idle time in seconds.
        :type new_value: int
        :vss_id: 47 
        
        :vss_type: UInt32 
        :vss_unit: s 
        :vss_sensor: Timer 
        


    .. xbr:event:: on_ambient_air_temperature(new_value)

        :param new_value: Ambient air temperature
        :type new_value: float
        :vss_id: 51 
        
        :vss_type: Float 
        :vss_unit: celsius 
        :vss_sensor: Thermometer 
        


    .. xbr:event:: on_angular_velocity__yaw(new_value)

        :param new_value: Vehicle rotation rate along Z (vertical).
        :type new_value: int
        :vss_id: 1110 
        
        :vss_type: Int16 
        :vss_unit: degrees/s 
        :vss_sensor: Gyroscope 
        


    .. xbr:event:: on_angular_velocity__roll(new_value)

        :param new_value: Vehicle rotation rate along X (longitudinal).
        :type new_value: int
        :vss_id: 1108 
        
        :vss_type: Int16 
        :vss_unit: degrees/s 
        :vss_sensor: Gyroscope 
        


    .. xbr:event:: on_angular_velocity__pitch(new_value)

        :param new_value: Vehicle rotation rate along Y (lateral).
        :type new_value: int
        :vss_id: 1109 
        
        :vss_type: Int16 
        :vss_unit: degrees/s 
        :vss_sensor: Gyroscope 
        


    .. xbr:event:: on_drive_time(new_value)

        :param new_value: Accumulated drive time in seconds.
        :type new_value: int
        :vss_id: 46 
        
        :vss_type: UInt32 
        :vss_unit: s 
        :vss_sensor: Timer 
        


    .. xbr:event:: on_ignition_off_time(new_value)

        :param new_value: Accumulated ignition off time in seconds.
        :type new_value: int
        :vss_id: 45 
        
        :vss_type: UInt32 
        :vss_unit: s 
        :vss_sensor: Timer 
        


    .. xbr:event:: on_trip_meter_reading(new_value)

        :param new_value: Current trip meter reading
        :type new_value: float
        :vss_id: 1104 
        
        :vss_type: Float 
        :vss_unit: km 
        :vss_sensor: Odometer 
        


    .. xbr:event:: on_speed(new_value)

        :param new_value: Vehicle speed, as sensed by the gearbox.
        :type new_value: int
        :vss_id: 48 
        
        :vss_type: Int32 
        :vss_unit: km/h 
        :vss_sensor: Speedometer 
        


    .. xbr:event:: on_ignition_on_time(new_value)

        :param new_value: Accumulated ignition on time in seconds.
        :type new_value: int
        :vss_id: 44 
        
        :vss_type: UInt32 
        :vss_unit: s 
        :vss_sensor: Timer 
        
