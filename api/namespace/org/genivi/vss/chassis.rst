org.genivi.vss.chassis
======================

All signals concerning steering, suspension, wheels, and brakes.

.. xbr:namespace:: org.genivi.vss.chassis

IAccelerator
------------

.. xbr:interface:: IAccelerator

    Accelerator signals


    .. xbr:event:: on_pedal_position(new_value)

        :param new_value: Accelerator pedal position as percent. 0 = Not depressed. 100 = Fully depressed.
        :type new_value: int
        :vss_id: 992 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Pedal Position Sensor 
        

IBrake
------

.. xbr:interface:: IBrake

    Brake system signals


    .. xbr:event:: on_pedal_position(new_value)

        :param new_value: Brake pedal position as percent. 0 = Not depressed. 100 = Fully depressed.
        :type new_value: int
        :vss_id: 993 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Pedal Position Sensor 
        

IParkingBrake
-------------

.. xbr:interface:: IParkingBrake

    Parking brake signals


    .. xbr:event:: on_is_engaged(new_value)

        :param new_value: Parking brake status. True = Parking Brake is Engaged. False = Parking Brake is not Engaged.
        :type new_value: bool
        :vss_id: 988 
        
        :vss_type: Boolean 
        
        :vss_sensor: Parking Brake Sensor 
        :vss_actuator: Parking Brake Switch 

IAxle
-----

.. xbr:interface:: IAxle

    Axle signals


    .. xbr:event:: on_row1__wheel__right__brake__fluid_level(new_value)

        :param new_value: Brake fluid level as percent. 0 = Empty. 100 = Full.
        :type new_value: int
        :vss_id: 967 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Brake Fluid Level Sensor 
        


    .. xbr:event:: on_row1__wheel__right__brake__fluid_level_low(new_value)

        :param new_value: Brake fluid level status. True = Brake fluid level low. False = Brake fluid level OK.
        :type new_value: bool
        :vss_id: 968 
        
        :vss_type: Boolean 
        
        :vss_sensor: Brake Fluid Level Sensor 
        


    .. xbr:event:: on_row1__wheel__right__brake__brakes_worn(new_value)

        :param new_value: Brake pad wear status. True = Worn. False = Not Worn.
        :type new_value: bool
        :vss_id: 970 
        
        :vss_type: Boolean 
        
        :vss_sensor: Brake Pad Wear Sensor 
        


    .. xbr:event:: on_row1__wheel__right__brake__pad_wear(new_value)

        :param new_value: Brake pad wear as percent. 0 = No Wear. 100 = Worn.
        :type new_value: int
        :vss_id: 969 
        
        :vss_type: UInt8 
        
        :vss_sensor: Brake Pad Wear Sensor 
        


    .. xbr:event:: on_row1__wheel__right__tire__pressure(new_value)

        :param new_value: Tire pressure in kilo-Pascal
        :type new_value: int
        :vss_id: 971 
        
        :vss_type: UInt8 
        :vss_unit: kpa 
        :vss_sensor: Tire Pressure Monitoring System 
        


    .. xbr:event:: on_row1__wheel__right__tire__pressure_low(new_value)

        :param new_value: Tire Pressure Status. True = Low tire pressure. False = Good tire pressure.
        :type new_value: bool
        :vss_id: 972 
        
        :vss_type: Boolean 
        
        :vss_sensor: Tire Pressure Monitoring System 
        


    .. xbr:event:: on_row1__wheel__right__tire__temperature(new_value)

        :param new_value: Tire temperature in Celsius.
        :type new_value: float
        :vss_id: 973 
        
        :vss_type: Float 
        :vss_unit: celsius 
        :vss_sensor: Tire Temperature Sensor 
        


    .. xbr:event:: on_row1__wheel__left__brake__fluid_level(new_value)

        :param new_value: Brake fluid level as percent. 0 = Empty. 100 = Full.
        :type new_value: int
        :vss_id: 960 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Brake Fluid Level Sensor 
        


    .. xbr:event:: on_row1__wheel__left__brake__fluid_level_low(new_value)

        :param new_value: Brake fluid level status. True = Brake fluid level low. False = Brake fluid level OK.
        :type new_value: bool
        :vss_id: 961 
        
        :vss_type: Boolean 
        
        :vss_sensor: Brake Fluid Level Sensor 
        


    .. xbr:event:: on_row1__wheel__left__brake__brakes_worn(new_value)

        :param new_value: Brake pad wear status. True = Worn. False = Not Worn.
        :type new_value: bool
        :vss_id: 963 
        
        :vss_type: Boolean 
        
        :vss_sensor: Brake Pad Wear Sensor 
        


    .. xbr:event:: on_row1__wheel__left__brake__pad_wear(new_value)

        :param new_value: Brake pad wear as percent. 0 = No Wear. 100 = Worn.
        :type new_value: int
        :vss_id: 962 
        
        :vss_type: UInt8 
        
        :vss_sensor: Brake Pad Wear Sensor 
        


    .. xbr:event:: on_row1__wheel__left__tire__pressure(new_value)

        :param new_value: Tire pressure in kilo-Pascal
        :type new_value: int
        :vss_id: 964 
        
        :vss_type: UInt8 
        :vss_unit: kpa 
        :vss_sensor: Tire Pressure Monitoring System 
        


    .. xbr:event:: on_row1__wheel__left__tire__pressure_low(new_value)

        :param new_value: Tire Pressure Status. True = Low tire pressure. False = Good tire pressure.
        :type new_value: bool
        :vss_id: 965 
        
        :vss_type: Boolean 
        
        :vss_sensor: Tire Pressure Monitoring System 
        


    .. xbr:event:: on_row1__wheel__left__tire__temperature(new_value)

        :param new_value: Tire temperature in Celsius.
        :type new_value: float
        :vss_id: 966 
        
        :vss_type: Float 
        :vss_unit: celsius 
        :vss_sensor: Tire Temperature Sensor 
        


    .. xbr:event:: on_row2__wheel__right__brake__fluid_level(new_value)

        :param new_value: Brake fluid level as percent. 0 = Empty. 100 = Full.
        :type new_value: int
        :vss_id: 981 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Brake Fluid Level Sensor 
        


    .. xbr:event:: on_row2__wheel__right__brake__fluid_level_low(new_value)

        :param new_value: Brake fluid level status. True = Brake fluid level low. False = Brake fluid level OK.
        :type new_value: bool
        :vss_id: 982 
        
        :vss_type: Boolean 
        
        :vss_sensor: Brake Fluid Level Sensor 
        


    .. xbr:event:: on_row2__wheel__right__brake__brakes_worn(new_value)

        :param new_value: Brake pad wear status. True = Worn. False = Not Worn.
        :type new_value: bool
        :vss_id: 984 
        
        :vss_type: Boolean 
        
        :vss_sensor: Brake Pad Wear Sensor 
        


    .. xbr:event:: on_row2__wheel__right__brake__pad_wear(new_value)

        :param new_value: Brake pad wear as percent. 0 = No Wear. 100 = Worn.
        :type new_value: int
        :vss_id: 983 
        
        :vss_type: UInt8 
        
        :vss_sensor: Brake Pad Wear Sensor 
        


    .. xbr:event:: on_row2__wheel__right__tire__pressure(new_value)

        :param new_value: Tire pressure in kilo-Pascal
        :type new_value: int
        :vss_id: 985 
        
        :vss_type: UInt8 
        :vss_unit: kpa 
        :vss_sensor: Tire Pressure Monitoring System 
        


    .. xbr:event:: on_row2__wheel__right__tire__pressure_low(new_value)

        :param new_value: Tire Pressure Status. True = Low tire pressure. False = Good tire pressure.
        :type new_value: bool
        :vss_id: 986 
        
        :vss_type: Boolean 
        
        :vss_sensor: Tire Pressure Monitoring System 
        


    .. xbr:event:: on_row2__wheel__right__tire__temperature(new_value)

        :param new_value: Tire temperature in Celsius.
        :type new_value: float
        :vss_id: 987 
        
        :vss_type: Float 
        :vss_unit: celsius 
        :vss_sensor: Tire Temperature Sensor 
        


    .. xbr:event:: on_row2__wheel__left__brake__fluid_level(new_value)

        :param new_value: Brake fluid level as percent. 0 = Empty. 100 = Full.
        :type new_value: int
        :vss_id: 974 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Brake Fluid Level Sensor 
        


    .. xbr:event:: on_row2__wheel__left__brake__fluid_level_low(new_value)

        :param new_value: Brake fluid level status. True = Brake fluid level low. False = Brake fluid level OK.
        :type new_value: bool
        :vss_id: 975 
        
        :vss_type: Boolean 
        
        :vss_sensor: Brake Fluid Level Sensor 
        


    .. xbr:event:: on_row2__wheel__left__brake__brakes_worn(new_value)

        :param new_value: Brake pad wear status. True = Worn. False = Not Worn.
        :type new_value: bool
        :vss_id: 977 
        
        :vss_type: Boolean 
        
        :vss_sensor: Brake Pad Wear Sensor 
        


    .. xbr:event:: on_row2__wheel__left__brake__pad_wear(new_value)

        :param new_value: Brake pad wear as percent. 0 = No Wear. 100 = Worn.
        :type new_value: int
        :vss_id: 976 
        
        :vss_type: UInt8 
        
        :vss_sensor: Brake Pad Wear Sensor 
        


    .. xbr:event:: on_row2__wheel__left__tire__pressure(new_value)

        :param new_value: Tire pressure in kilo-Pascal
        :type new_value: int
        :vss_id: 978 
        
        :vss_type: UInt8 
        :vss_unit: kpa 
        :vss_sensor: Tire Pressure Monitoring System 
        


    .. xbr:event:: on_row2__wheel__left__tire__pressure_low(new_value)

        :param new_value: Tire Pressure Status. True = Low tire pressure. False = Good tire pressure.
        :type new_value: bool
        :vss_id: 979 
        
        :vss_type: Boolean 
        
        :vss_sensor: Tire Pressure Monitoring System 
        


    .. xbr:event:: on_row2__wheel__left__tire__temperature(new_value)

        :param new_value: Tire temperature in Celsius.
        :type new_value: float
        :vss_id: 980 
        
        :vss_type: Float 
        :vss_unit: celsius 
        :vss_sensor: Tire Temperature Sensor 
        

ISteeringWheel
--------------

.. xbr:interface:: ISteeringWheel

    Steering wheel signals


    .. xbr:event:: on_tilt(new_value)

        :param new_value: Steering wheel column tilt. 0 = Lowest position. 100 = Highest position.
        :type new_value: int
        :vss_id: 990 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Steering Wheel Position Sensor 
        :vss_actuator: Steering Wheel Position Actuator 


    .. xbr:event:: on_angle(new_value)

        :param new_value: Steering wheel angle. Positive = degrees to the left. Negative = degrees to the right.
        :type new_value: int
        :vss_id: 989 
        
        :vss_type: Int16 
        :vss_unit: degrees 
        :vss_sensor: Steering Wheel Angle Sensor 
        


    .. xbr:event:: on_extension(new_value)

        :param new_value: Steering wheel column extension from dashboard. 0 = Closest to dashboard. 100 = Furthest from dashboard.
        :type new_value: int
        :vss_id: 991 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Steering Wheel Position Sensor 
        :vss_actuator: Steering Wheel Position Actuator 
