org.genivi.vss.adas
===================

All Advanced Driver Assist Systems signals

.. xbr:namespace:: org.genivi.vss.adas

IObstacleDetection
------------------

.. xbr:interface:: IObstacleDetection

    Signals form Obstacle Sensor System


    .. xbr:event:: on_distance_to_object__rear_left(new_value)

        :param new_value: Rear left distance to object in meters
        :type new_value: int
        :vss_id: 1135 
        
        :vss_type: UInt16 
        :vss_unit: m 
        :vss_sensor: Obstacle Detection Sensor 
        


    .. xbr:event:: on_distance_to_object__front_left(new_value)

        :param new_value: Front left distance to object in meters
        :type new_value: int
        :vss_id: 1133 
        
        :vss_type: UInt16 
        :vss_unit: m 
        :vss_sensor: Obstacle Detection Sensor 
        


    .. xbr:event:: on_distance_to_object__front_right(new_value)

        :param new_value: Front right distance to object in meters
        :type new_value: int
        :vss_id: 1134 
        
        :vss_type: UInt16 
        :vss_unit: m 
        :vss_sensor: Obstacle Detection Sensor 
        


    .. xbr:event:: on_distance_to_object__rear_right(new_value)

        :param new_value: Rear right distance to object in meters
        :type new_value: int
        :vss_id: 1136 
        
        :vss_type: UInt16 
        :vss_unit: m 
        :vss_sensor: Obstacle Detection Sensor 
        


    .. xbr:event:: on_is_active(new_value)

        :param new_value: Indicates if obstacle sensor system is enabled. Tue = Enabled. False = Disabled.
        :type new_value: bool
        :vss_id: 1131 
        
        :vss_type: Boolean 
        
        :vss_sensor: Obstacle Detection Sensor 
        :vss_actuator: Obstacle Detection Sensor 


    .. xbr:event:: on_error(new_value)

        :param new_value: Indicates if obstacle sensor system incurred an error condition. True = Error. False = No Error.
        :type new_value: bool
        :vss_id: 1132 
        
        :vss_type: Boolean 
        
        :vss_sensor: Obstacle Detection Sensor 
        

ITCS
----

.. xbr:interface:: ITCS

    Traction Control System signals


    .. xbr:event:: on_is_engaged(new_value)

        :param new_value: Indicates if TCS is currently regulating traction. True = Engaged. False = Not Engaged.
        :type new_value: bool
        :vss_id: 956 
        
        :vss_type: Boolean 
        
        :vss_sensor: Traction Control System 
        


    .. xbr:event:: on_is_active(new_value)

        :param new_value: Indicates if TCS is enabled. Tue = Enabled. False = Disabled.
        :type new_value: bool
        :vss_id: 954 
        
        :vss_type: Boolean 
        
        :vss_sensor: Traction Control System 
        :vss_actuator: Traction Control System 


    .. xbr:event:: on_error(new_value)

        :param new_value: Indicates if TCS incurred an error condition. True = Error. False = No Error.
        :type new_value: bool
        :vss_id: 955 
        
        :vss_type: Boolean 
        
        :vss_sensor: Traction Control System 
        

ICruiseControl
--------------

.. xbr:interface:: ICruiseControl

    Signals from Cruise Control system


    .. xbr:event:: on_speed_set(new_value)

        :param new_value: Set cruise control speed in kilometers per hour
        :type new_value: int
        :vss_id: 940 
        
        :vss_type: Int32 
        :vss_unit: km/h 
        :vss_sensor: Cruise Control System 
        :vss_actuator: Cruise Control System 


    .. xbr:event:: on_is_active(new_value)

        :param new_value: Indicates if cruise control system is enabled. True = Enabled. False = Disabled.
        :type new_value: bool
        :vss_id: 939 
        
        :vss_type: Boolean 
        
        :vss_sensor: Cruise Control System 
        :vss_actuator: Cruise Control System 


    .. xbr:event:: on_error(new_value)

        :param new_value: Indicates if cruise control system incurred and error condition. True = Error. False = NoError.
        :type new_value: bool
        :vss_id: 941 
        
        :vss_type: Boolean 
        
        :vss_sensor: Cruise Control System 
        

IABS
----

.. xbr:interface:: IABS

    Antilock Braking System signals


    .. xbr:event:: on_is_engaged(new_value)

        :param new_value: Indicates if ABS is currently regulating brake pressure. True = Engaged. False = Not Engaged.
        :type new_value: bool
        :vss_id: 953 
        
        :vss_type: Boolean 
        
        :vss_sensor: Antilock Braking System 
        


    .. xbr:event:: on_is_active(new_value)

        :param new_value: Indicates if ABS is enabled. Tue = Enabled. False = Disabled.
        :type new_value: bool
        :vss_id: 951 
        
        :vss_type: Boolean 
        
        :vss_sensor: Antilock Braking System 
        :vss_actuator: Antilock Braking System 


    .. xbr:event:: on_error(new_value)

        :param new_value: Indicates if ABS incurred an error condition. True = Error. False = No Error.
        :type new_value: bool
        :vss_id: 952 
        
        :vss_type: Boolean 
        
        :vss_sensor: Antilock Braking System 
        

IESC
----

.. xbr:interface:: IESC

    Electronic Stability Control System signals


    .. xbr:event:: on_is_engaged(new_value)

        :param new_value: Indicates if ESC is currently regulating vehicle stability. True = Engaged. False = Not Engaged.
        :type new_value: bool
        :vss_id: 959 
        
        :vss_type: Boolean 
        
        :vss_sensor: Electronic Stability Control System 
        


    .. xbr:event:: on_is_active(new_value)

        :param new_value: Indicates if ECS is enabled. Tue = Enabled. False = Disabled.
        :type new_value: bool
        :vss_id: 957 
        
        :vss_type: Boolean 
        
        :vss_sensor: Electronic Stability Control System 
        :vss_actuator: Electronic Stability Control System 


    .. xbr:event:: on_error(new_value)

        :param new_value: Indicates if ESC incurred an error condition. True = Error. False = No Error.
        :type new_value: bool
        :vss_id: 958 
        
        :vss_type: Boolean 
        
        :vss_sensor: Electronic Stability Control System 
        

ILaneDepartureDetection
-----------------------

.. xbr:interface:: ILaneDepartureDetection

    Signals from Land Departure Detection System


    .. xbr:event:: on_warning(new_value)

        :param new_value: Indicates if lane departure detection registered a lane departure
        :type new_value: bool
        :vss_id: 943 
        
        :vss_type: Boolean 
        
        :vss_sensor: Lane Departure Detection Sensor 
        


    .. xbr:event:: on_is_active(new_value)

        :param new_value: Indicates if lane departure detection system is enabled. True = Enabled. False = Disabled.
        :type new_value: bool
        :vss_id: 942 
        
        :vss_type: Boolean 
        
        :vss_sensor: Lane Departure Detection Sensor 
        :vss_actuator: Lane Departure Detection Sensor 


    .. xbr:event:: on_error(new_value)

        :param new_value: Indicates if lane departure system incurred an error condition. True = Error. False = No Error.
        :type new_value: bool
        :vss_id: 944 
        
        :vss_type: Boolean 
        
        :vss_sensor: Lane Departure Detection Sensor 
        
