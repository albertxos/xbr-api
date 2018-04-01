org.genivi.vss.cabin
====================

All in-cabin components, including doors.

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

.. xbr:namespace:: org.genivi.vss.cabin

IDoor
-----

All doors, including windows and switches.

.. xbr:interface:: IDoor

    All doors, including windows and switches


    .. xbr:event:: on_row1_left_is_child_lock_active(new_value)

        :param new_value: Is door child lock engaged. True = Engaged. False = Disengaged.
        :type new_value: bool
        :vss_id: 187 
        
        :vss_type: Boolean 
        
        :vss_sensor: Child Lock 
        


    .. xbr:event:: on_row1_left_is_locked(new_value)

        :param new_value: Is door locked or unlocked. True = Locked. False = Unlocked.
        :type new_value: bool
        :vss_id: 184 
        
        :vss_type: Boolean 
        
        :vss_sensor: Door Lock 
        :vss_actuator: Door Lock 


    .. xbr:event:: on_row1_left_is_open(new_value)

        :param new_value: Is door open or closed
        :type new_value: bool
        :vss_id: 183 
        
        :vss_type: Boolean 
        
        :vss_sensor: Door Contact Sensor 
        :vss_actuator: Door Contact Actuator 


    .. xbr:event:: on_row1_left_shade_position(new_value)

        :param new_value: Position of side window blind. 0 = Fully retracted. 100 = Fully deployed.
        :type new_value: int
        :vss_id: 189 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        :vss_actuator: RearShade Actuator 


    .. xbr:event:: on_row1_left_shade_switch(new_value)

        :param new_value: Switch controlling sliding action such as window, sunroof, or blind.
        :type new_value: str
        :vss_id: 188 
        :vss_enum: ['Inactive', 'Close', 'Open', 'OneShotClose', 'OneShotOpen'] 
        :vss_type: String 
        
        
        :vss_actuator: RearShade System 


    .. xbr:event:: on_row1_left_window_position(new_value)

        :param new_value: Window position. 0 = Fully closed 100 = Fully opened.
        :type new_value: int
        :vss_id: 185 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Window Position Sensor 
        


    .. xbr:event:: on_row1_left_window_switch(new_value)

        :param new_value: Switch controlling sliding action such as window, sunroof, or blind.
        :type new_value: str
        :vss_id: 186 
        :vss_enum: ['Inactive', 'Close', 'Open', 'OneShotClose', 'OneShotOpen'] 
        :vss_type: String 
        
        
        :vss_actuator: RearShade System 


    .. xbr:event:: on_row1_right_is_child_lock_active(new_value)

        :param new_value: Is door child lock engaged. True = Engaged. False = Disengaged.
        :type new_value: bool
        :vss_id: 194 
        
        :vss_type: Boolean 
        
        :vss_sensor: Child Lock 
        


    .. xbr:event:: on_row1_right_is_locked(new_value)

        :param new_value: Is door locked or unlocked. True = Locked. False = Unlocked.
        :type new_value: bool
        :vss_id: 191 
        
        :vss_type: Boolean 
        
        :vss_sensor: Door Lock 
        :vss_actuator: Door Lock 


    .. xbr:event:: on_row1_right_is_open(new_value)

        :param new_value: Is door open or closed
        :type new_value: bool
        :vss_id: 190 
        
        :vss_type: Boolean 
        
        :vss_sensor: Door Contact Sensor 
        :vss_actuator: Door Contact Actuator 


    .. xbr:event:: on_row1_right_shade_position(new_value)

        :param new_value: Position of side window blind. 0 = Fully retracted. 100 = Fully deployed.
        :type new_value: int
        :vss_id: 196 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        :vss_actuator: RearShade Actuator 


    .. xbr:event:: on_row1_right_shade_switch(new_value)

        :param new_value: Switch controlling sliding action such as window, sunroof, or blind.
        :type new_value: str
        :vss_id: 195 
        :vss_enum: ['Inactive', 'Close', 'Open', 'OneShotClose', 'OneShotOpen'] 
        :vss_type: String 
        
        
        :vss_actuator: RearShade System 


    .. xbr:event:: on_row1_right_window_position(new_value)

        :param new_value: Window position. 0 = Fully closed 100 = Fully opened.
        :type new_value: int
        :vss_id: 192 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Window Position Sensor 
        


    .. xbr:event:: on_row1_right_window_switch(new_value)

        :param new_value: Switch controlling sliding action such as window, sunroof, or blind.
        :type new_value: str
        :vss_id: 193 
        :vss_enum: ['Inactive', 'Close', 'Open', 'OneShotClose', 'OneShotOpen'] 
        :vss_type: String 
        
        
        :vss_actuator: RearShade System 


    .. xbr:event:: on_row2_left_is_child_lock_active(new_value)

        :param new_value: Is door child lock engaged. True = Engaged. False = Disengaged.
        :type new_value: bool
        :vss_id: 201 
        
        :vss_type: Boolean 
        
        :vss_sensor: Child Lock 
        


    .. xbr:event:: on_row2_left_is_locked(new_value)

        :param new_value: Is door locked or unlocked. True = Locked. False = Unlocked.
        :type new_value: bool
        :vss_id: 198 
        
        :vss_type: Boolean 
        
        :vss_sensor: Door Lock 
        :vss_actuator: Door Lock 


    .. xbr:event:: on_row2_left_is_open(new_value)

        :param new_value: Is door open or closed
        :type new_value: bool
        :vss_id: 197 
        
        :vss_type: Boolean 
        
        :vss_sensor: Door Contact Sensor 
        :vss_actuator: Door Contact Actuator 


    .. xbr:event:: on_row2_left_shade_position(new_value)

        :param new_value: Position of side window blind. 0 = Fully retracted. 100 = Fully deployed.
        :type new_value: int
        :vss_id: 203 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        :vss_actuator: RearShade Actuator 


    .. xbr:event:: on_row2_left_shade_switch(new_value)

        :param new_value: Switch controlling sliding action such as window, sunroof, or blind.
        :type new_value: str
        :vss_id: 202 
        :vss_enum: ['Inactive', 'Close', 'Open', 'OneShotClose', 'OneShotOpen'] 
        :vss_type: String 
        
        
        :vss_actuator: RearShade System 


    .. xbr:event:: on_row2_left_window_position(new_value)

        :param new_value: Window position. 0 = Fully closed 100 = Fully opened.
        :type new_value: int
        :vss_id: 199 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Window Position Sensor 
        


    .. xbr:event:: on_row2_left_window_switch(new_value)

        :param new_value: Switch controlling sliding action such as window, sunroof, or blind.
        :type new_value: str
        :vss_id: 200 
        :vss_enum: ['Inactive', 'Close', 'Open', 'OneShotClose', 'OneShotOpen'] 
        :vss_type: String 
        
        
        :vss_actuator: RearShade System 


    .. xbr:event:: on_row2_right_is_child_lock_active(new_value)

        :param new_value: Is door child lock engaged. True = Engaged. False = Disengaged.
        :type new_value: bool
        :vss_id: 208 
        
        :vss_type: Boolean 
        
        :vss_sensor: Child Lock 
        


    .. xbr:event:: on_row2_right_is_locked(new_value)

        :param new_value: Is door locked or unlocked. True = Locked. False = Unlocked.
        :type new_value: bool
        :vss_id: 205 
        
        :vss_type: Boolean 
        
        :vss_sensor: Door Lock 
        :vss_actuator: Door Lock 


    .. xbr:event:: on_row2_right_is_open(new_value)

        :param new_value: Is door open or closed
        :type new_value: bool
        :vss_id: 204 
        
        :vss_type: Boolean 
        
        :vss_sensor: Door Contact Sensor 
        :vss_actuator: Door Contact Actuator 


    .. xbr:event:: on_row2_right_shade_position(new_value)

        :param new_value: Position of side window blind. 0 = Fully retracted. 100 = Fully deployed.
        :type new_value: int
        :vss_id: 210 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        :vss_actuator: RearShade Actuator 


    .. xbr:event:: on_row2_right_shade_switch(new_value)

        :param new_value: Switch controlling sliding action such as window, sunroof, or blind.
        :type new_value: str
        :vss_id: 209 
        :vss_enum: ['Inactive', 'Close', 'Open', 'OneShotClose', 'OneShotOpen'] 
        :vss_type: String 
        
        
        :vss_actuator: RearShade System 


    .. xbr:event:: on_row2_right_window_position(new_value)

        :param new_value: Window position. 0 = Fully closed 100 = Fully opened.
        :type new_value: int
        :vss_id: 206 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Window Position Sensor 
        


    .. xbr:event:: on_row2_right_window_switch(new_value)

        :param new_value: Switch controlling sliding action such as window, sunroof, or blind.
        :type new_value: str
        :vss_id: 207 
        :vss_enum: ['Inactive', 'Close', 'Open', 'OneShotClose', 'OneShotOpen'] 
        :vss_type: String 
        
        
        :vss_actuator: RearShade System 


    .. xbr:event:: on_row3_left_is_child_lock_active(new_value)

        :param new_value: Is door child lock engaged. True = Engaged. False = Disengaged.
        :type new_value: bool
        :vss_id: 215 
        
        :vss_type: Boolean 
        
        :vss_sensor: Child Lock 
        


    .. xbr:event:: on_row3_left_is_locked(new_value)

        :param new_value: Is door locked or unlocked. True = Locked. False = Unlocked.
        :type new_value: bool
        :vss_id: 212 
        
        :vss_type: Boolean 
        
        :vss_sensor: Door Lock 
        :vss_actuator: Door Lock 


    .. xbr:event:: on_row3_left_is_open(new_value)

        :param new_value: Is door open or closed
        :type new_value: bool
        :vss_id: 211 
        
        :vss_type: Boolean 
        
        :vss_sensor: Door Contact Sensor 
        :vss_actuator: Door Contact Actuator 


    .. xbr:event:: on_row3_left_shade_position(new_value)

        :param new_value: Position of side window blind. 0 = Fully retracted. 100 = Fully deployed.
        :type new_value: int
        :vss_id: 217 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        :vss_actuator: RearShade Actuator 


    .. xbr:event:: on_row3_left_shade_switch(new_value)

        :param new_value: Switch controlling sliding action such as window, sunroof, or blind.
        :type new_value: str
        :vss_id: 216 
        :vss_enum: ['Inactive', 'Close', 'Open', 'OneShotClose', 'OneShotOpen'] 
        :vss_type: String 
        
        
        :vss_actuator: RearShade System 


    .. xbr:event:: on_row3_left_window_position(new_value)

        :param new_value: Window position. 0 = Fully closed 100 = Fully opened.
        :type new_value: int
        :vss_id: 213 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Window Position Sensor 
        


    .. xbr:event:: on_row3_left_window_switch(new_value)

        :param new_value: Switch controlling sliding action such as window, sunroof, or blind.
        :type new_value: str
        :vss_id: 214 
        :vss_enum: ['Inactive', 'Close', 'Open', 'OneShotClose', 'OneShotOpen'] 
        :vss_type: String 
        
        
        :vss_actuator: RearShade System 


    .. xbr:event:: on_row3_right_is_child_lock_active(new_value)

        :param new_value: Is door child lock engaged. True = Engaged. False = Disengaged.
        :type new_value: bool
        :vss_id: 222 
        
        :vss_type: Boolean 
        
        :vss_sensor: Child Lock 
        


    .. xbr:event:: on_row3_right_is_locked(new_value)

        :param new_value: Is door locked or unlocked. True = Locked. False = Unlocked.
        :type new_value: bool
        :vss_id: 219 
        
        :vss_type: Boolean 
        
        :vss_sensor: Door Lock 
        :vss_actuator: Door Lock 


    .. xbr:event:: on_row3_right_is_open(new_value)

        :param new_value: Is door open or closed
        :type new_value: bool
        :vss_id: 218 
        
        :vss_type: Boolean 
        
        :vss_sensor: Door Contact Sensor 
        :vss_actuator: Door Contact Actuator 


    .. xbr:event:: on_row3_right_shade_position(new_value)

        :param new_value: Position of side window blind. 0 = Fully retracted. 100 = Fully deployed.
        :type new_value: int
        :vss_id: 224 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        :vss_actuator: RearShade Actuator 


    .. xbr:event:: on_row3_right_shade_switch(new_value)

        :param new_value: Switch controlling sliding action such as window, sunroof, or blind.
        :type new_value: str
        :vss_id: 223 
        :vss_enum: ['Inactive', 'Close', 'Open', 'OneShotClose', 'OneShotOpen'] 
        :vss_type: String 
        
        
        :vss_actuator: RearShade System 


    .. xbr:event:: on_row3_right_window_position(new_value)

        :param new_value: Window position. 0 = Fully closed 100 = Fully opened.
        :type new_value: int
        :vss_id: 220 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Window Position Sensor 
        


    .. xbr:event:: on_row3_right_window_switch(new_value)

        :param new_value: Switch controlling sliding action such as window, sunroof, or blind.
        :type new_value: str
        :vss_id: 221 
        :vss_enum: ['Inactive', 'Close', 'Open', 'OneShotClose', 'OneShotOpen'] 
        :vss_type: String 
        
        
        :vss_actuator: RearShade System 


    .. xbr:event:: on_row4_left_is_child_lock_active(new_value)

        :param new_value: Is door child lock engaged. True = Engaged. False = Disengaged.
        :type new_value: bool
        :vss_id: 229 
        
        :vss_type: Boolean 
        
        :vss_sensor: Child Lock 
        


    .. xbr:event:: on_row4_left_is_locked(new_value)

        :param new_value: Is door locked or unlocked. True = Locked. False = Unlocked.
        :type new_value: bool
        :vss_id: 226 
        
        :vss_type: Boolean 
        
        :vss_sensor: Door Lock 
        :vss_actuator: Door Lock 


    .. xbr:event:: on_row4_left_is_open(new_value)

        :param new_value: Is door open or closed
        :type new_value: bool
        :vss_id: 225 
        
        :vss_type: Boolean 
        
        :vss_sensor: Door Contact Sensor 
        :vss_actuator: Door Contact Actuator 


    .. xbr:event:: on_row4_left_shade_position(new_value)

        :param new_value: Position of side window blind. 0 = Fully retracted. 100 = Fully deployed.
        :type new_value: int
        :vss_id: 231 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        :vss_actuator: RearShade Actuator 


    .. xbr:event:: on_row4_left_shade_switch(new_value)

        :param new_value: Switch controlling sliding action such as window, sunroof, or blind.
        :type new_value: str
        :vss_id: 230 
        :vss_enum: ['Inactive', 'Close', 'Open', 'OneShotClose', 'OneShotOpen'] 
        :vss_type: String 
        
        
        :vss_actuator: RearShade System 


    .. xbr:event:: on_row4_left_window_position(new_value)

        :param new_value: Window position. 0 = Fully closed 100 = Fully opened.
        :type new_value: int
        :vss_id: 227 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Window Position Sensor 
        


    .. xbr:event:: on_row4_left_window_switch(new_value)

        :param new_value: Switch controlling sliding action such as window, sunroof, or blind.
        :type new_value: str
        :vss_id: 228 
        :vss_enum: ['Inactive', 'Close', 'Open', 'OneShotClose', 'OneShotOpen'] 
        :vss_type: String 
        
        
        :vss_actuator: RearShade System 


    .. xbr:event:: on_row4_right_is_child_lock_active(new_value)

        :param new_value: Is door child lock engaged. True = Engaged. False = Disengaged.
        :type new_value: bool
        :vss_id: 236 
        
        :vss_type: Boolean 
        
        :vss_sensor: Child Lock 
        


    .. xbr:event:: on_row4_right_is_locked(new_value)

        :param new_value: Is door locked or unlocked. True = Locked. False = Unlocked.
        :type new_value: bool
        :vss_id: 233 
        
        :vss_type: Boolean 
        
        :vss_sensor: Door Lock 
        :vss_actuator: Door Lock 


    .. xbr:event:: on_row4_right_is_open(new_value)

        :param new_value: Is door open or closed
        :type new_value: bool
        :vss_id: 232 
        
        :vss_type: Boolean 
        
        :vss_sensor: Door Contact Sensor 
        :vss_actuator: Door Contact Actuator 


    .. xbr:event:: on_row4_right_shade_position(new_value)

        :param new_value: Position of side window blind. 0 = Fully retracted. 100 = Fully deployed.
        :type new_value: int
        :vss_id: 238 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        :vss_actuator: RearShade Actuator 


    .. xbr:event:: on_row4_right_shade_switch(new_value)

        :param new_value: Switch controlling sliding action such as window, sunroof, or blind.
        :type new_value: str
        :vss_id: 237 
        :vss_enum: ['Inactive', 'Close', 'Open', 'OneShotClose', 'OneShotOpen'] 
        :vss_type: String 
        
        
        :vss_actuator: RearShade System 


    .. xbr:event:: on_row4_right_window_position(new_value)

        :param new_value: Window position. 0 = Fully closed 100 = Fully opened.
        :type new_value: int
        :vss_id: 234 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Window Position Sensor 
        


    .. xbr:event:: on_row4_right_window_switch(new_value)

        :param new_value: Switch controlling sliding action such as window, sunroof, or blind.
        :type new_value: str
        :vss_id: 235 
        :vss_enum: ['Inactive', 'Close', 'Open', 'OneShotClose', 'OneShotOpen'] 
        :vss_type: String 
        
        
        :vss_actuator: RearShade System 

IHVAC
-----

Climate control.

.. xbr:interface:: IHVAC

    Climate control


    .. xbr:event:: on_ambient_air_temperature(new_value)

        :param new_value: Ambient air temperature
        :type new_value: float
        :vss_id: 143 
        
        :vss_type: Float 
        :vss_unit: celsius 
        :vss_sensor: Thermometer 
        


    .. xbr:event:: on_is_air_conditioning_active(new_value)

        :param new_value: Is Air conditioning active.
        :type new_value: bool
        :vss_id: 142 
        
        :vss_type: Boolean 
        
        :vss_sensor: Air Conditioning System 
        


    .. xbr:event:: on_is_front_defroster_active(new_value)

        :param new_value: Is front defroster active.
        :type new_value: bool
        :vss_id: 140 
        
        :vss_type: Boolean 
        
        :vss_sensor: Defroster 
        :vss_actuator: Defroster 


    .. xbr:event:: on_is_rear_defroster_active(new_value)

        :param new_value: Is rear defroster active.
        :type new_value: bool
        :vss_id: 141 
        
        :vss_type: Boolean 
        
        :vss_sensor: Defroster 
        :vss_actuator: Defroster 


    .. xbr:event:: on_is_recirculation_active(new_value)

        :param new_value: Is recirculation active.
        :type new_value: bool
        :vss_id: 139 
        
        :vss_type: Boolean 
        
        :vss_sensor: Recirculation System 
        :vss_actuator: Recirculation System 


    .. xbr:event:: on_row1_left_air_distribution(new_value)

        :param new_value: Direction of airstream
        :type new_value: str
        :vss_id: 117 
        :vss_enum: ['up', 'middle', 'down'] 
        :vss_type: String 
        
        :vss_sensor: Fan Sensor 
        :vss_actuator: Fan Control 


    .. xbr:event:: on_row1_left_fan_speed(new_value)

        :param new_value: Fan Speed, 0 = off. 100 = max
        :type new_value: int
        :vss_id: 115 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Fan Sensor 
        :vss_actuator: Fan Control 


    .. xbr:event:: on_row1_left_temperature(new_value)

        :param new_value: Temperature
        :type new_value: int
        :vss_id: 116 
        
        :vss_type: Int8 
        :vss_unit: celsius 
        :vss_sensor: Thermometer 
        :vss_actuator: TemperatureSwitch 


    .. xbr:event:: on_row1_right_air_distribution(new_value)

        :param new_value: Direction of airstream
        :type new_value: str
        :vss_id: 120 
        :vss_enum: ['up', 'middle', 'down'] 
        :vss_type: String 
        
        :vss_sensor: Fan Sensor 
        :vss_actuator: Fan Control 


    .. xbr:event:: on_row1_right_fan_speed(new_value)

        :param new_value: Fan Speed, 0 = off. 100 = max
        :type new_value: int
        :vss_id: 118 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Fan Sensor 
        :vss_actuator: Fan Control 


    .. xbr:event:: on_row1_right_temperature(new_value)

        :param new_value: Temperature
        :type new_value: int
        :vss_id: 119 
        
        :vss_type: Int8 
        :vss_unit: celsius 
        :vss_sensor: Thermometer 
        :vss_actuator: TemperatureSwitch 


    .. xbr:event:: on_row2_left_air_distribution(new_value)

        :param new_value: Direction of airstream
        :type new_value: str
        :vss_id: 123 
        :vss_enum: ['up', 'middle', 'down'] 
        :vss_type: String 
        
        :vss_sensor: Fan Sensor 
        :vss_actuator: Fan Control 


    .. xbr:event:: on_row2_left_fan_speed(new_value)

        :param new_value: Fan Speed, 0 = off. 100 = max
        :type new_value: int
        :vss_id: 121 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Fan Sensor 
        :vss_actuator: Fan Control 


    .. xbr:event:: on_row2_left_temperature(new_value)

        :param new_value: Temperature
        :type new_value: int
        :vss_id: 122 
        
        :vss_type: Int8 
        :vss_unit: celsius 
        :vss_sensor: Thermometer 
        :vss_actuator: TemperatureSwitch 


    .. xbr:event:: on_row2_right_air_distribution(new_value)

        :param new_value: Direction of airstream
        :type new_value: str
        :vss_id: 126 
        :vss_enum: ['up', 'middle', 'down'] 
        :vss_type: String 
        
        :vss_sensor: Fan Sensor 
        :vss_actuator: Fan Control 


    .. xbr:event:: on_row2_right_fan_speed(new_value)

        :param new_value: Fan Speed, 0 = off. 100 = max
        :type new_value: int
        :vss_id: 124 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Fan Sensor 
        :vss_actuator: Fan Control 


    .. xbr:event:: on_row2_right_temperature(new_value)

        :param new_value: Temperature
        :type new_value: int
        :vss_id: 125 
        
        :vss_type: Int8 
        :vss_unit: celsius 
        :vss_sensor: Thermometer 
        :vss_actuator: TemperatureSwitch 


    .. xbr:event:: on_row3_left_air_distribution(new_value)

        :param new_value: Direction of airstream
        :type new_value: str
        :vss_id: 129 
        :vss_enum: ['up', 'middle', 'down'] 
        :vss_type: String 
        
        :vss_sensor: Fan Sensor 
        :vss_actuator: Fan Control 


    .. xbr:event:: on_row3_left_fan_speed(new_value)

        :param new_value: Fan Speed, 0 = off. 100 = max
        :type new_value: int
        :vss_id: 127 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Fan Sensor 
        :vss_actuator: Fan Control 


    .. xbr:event:: on_row3_left_temperature(new_value)

        :param new_value: Temperature
        :type new_value: int
        :vss_id: 128 
        
        :vss_type: Int8 
        :vss_unit: celsius 
        :vss_sensor: Thermometer 
        :vss_actuator: TemperatureSwitch 


    .. xbr:event:: on_row3_right_air_distribution(new_value)

        :param new_value: Direction of airstream
        :type new_value: str
        :vss_id: 132 
        :vss_enum: ['up', 'middle', 'down'] 
        :vss_type: String 
        
        :vss_sensor: Fan Sensor 
        :vss_actuator: Fan Control 


    .. xbr:event:: on_row3_right_fan_speed(new_value)

        :param new_value: Fan Speed, 0 = off. 100 = max
        :type new_value: int
        :vss_id: 130 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Fan Sensor 
        :vss_actuator: Fan Control 


    .. xbr:event:: on_row3_right_temperature(new_value)

        :param new_value: Temperature
        :type new_value: int
        :vss_id: 131 
        
        :vss_type: Int8 
        :vss_unit: celsius 
        :vss_sensor: Thermometer 
        :vss_actuator: TemperatureSwitch 


    .. xbr:event:: on_row4_left_air_distribution(new_value)

        :param new_value: Direction of airstream
        :type new_value: str
        :vss_id: 135 
        :vss_enum: ['up', 'middle', 'down'] 
        :vss_type: String 
        
        :vss_sensor: Fan Sensor 
        :vss_actuator: Fan Control 


    .. xbr:event:: on_row4_left_fan_speed(new_value)

        :param new_value: Fan Speed, 0 = off. 100 = max
        :type new_value: int
        :vss_id: 133 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Fan Sensor 
        :vss_actuator: Fan Control 


    .. xbr:event:: on_row4_left_temperature(new_value)

        :param new_value: Temperature
        :type new_value: int
        :vss_id: 134 
        
        :vss_type: Int8 
        :vss_unit: celsius 
        :vss_sensor: Thermometer 
        :vss_actuator: TemperatureSwitch 


    .. xbr:event:: on_row4_right_air_distribution(new_value)

        :param new_value: Direction of airstream
        :type new_value: str
        :vss_id: 138 
        :vss_enum: ['up', 'middle', 'down'] 
        :vss_type: String 
        
        :vss_sensor: Fan Sensor 
        :vss_actuator: Fan Control 


    .. xbr:event:: on_row4_right_fan_speed(new_value)

        :param new_value: Fan Speed, 0 = off. 100 = max
        :type new_value: int
        :vss_id: 136 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Fan Sensor 
        :vss_actuator: Fan Control 


    .. xbr:event:: on_row4_right_temperature(new_value)

        :param new_value: Temperature
        :type new_value: int
        :vss_id: 137 
        
        :vss_type: Int8 
        :vss_unit: celsius 
        :vss_sensor: Thermometer 
        :vss_actuator: TemperatureSwitch 

IInfotainment
-------------

Infotainment system.

.. xbr:interface:: IInfotainment

    Infotainment system


    .. xbr:event:: on_media_action(new_value)

        :param new_value: Tells if the media was
        :type new_value: str
        :vss_id: 144 
        :vss_enum: ['unknown', 'Stop', 'Play', 'FastForward', 'FastBackward', 'SkipForward', 'SkipBackward'] 
        :vss_type: String 
        
        :vss_sensor: Multimedia System 
        :vss_actuator: Multimedia System 


    .. xbr:event:: on_media_declined_u_r_i(new_value)

        :param new_value: URI of suggested media that was declined
        :type new_value: str
        :vss_id: 150 
        
        :vss_type: String 
        
        :vss_sensor: Multimedia System 
        


    .. xbr:event:: on_media_played_album(new_value)

        :param new_value: Name of album being played
        :type new_value: str
        :vss_id: 147 
        
        :vss_type: String 
        
        :vss_sensor: Multimedia System 
        


    .. xbr:event:: on_media_played_artist(new_value)

        :param new_value: Name of artist being played
        :type new_value: str
        :vss_id: 146 
        
        :vss_type: String 
        
        :vss_sensor: Multimedia System 
        


    .. xbr:event:: on_media_played_source(new_value)

        :param new_value: Media selected for playback
        :type new_value: str
        :vss_id: 145 
        :vss_enum: ['unknown', 'SiriusXM', 'AM', 'FM', 'DAB', 'TV', 'CD', 'DVD', 'AUX', 'USB', 'Disk', 'Bluetooth', 'Internet', 'Voice', 'Beep'] 
        :vss_type: String 
        
        :vss_sensor: Multimedia System 
        :vss_actuator: Multimedia System 


    .. xbr:event:: on_media_played_track(new_value)

        :param new_value: Name of track being played
        :type new_value: str
        :vss_id: 148 
        
        :vss_type: String 
        
        :vss_sensor: Multimedia System 
        


    .. xbr:event:: on_media_played_uri(new_value)

        :param new_value: User Resource associated with the media
        :type new_value: str
        :vss_id: 149 
        
        :vss_type: String 
        
        :vss_sensor: Multimedia System 
        


    .. xbr:event:: on_media_selected_u_r_i(new_value)

        :param new_value: URI of suggested media that was selected
        :type new_value: str
        :vss_id: 151 
        
        :vss_type: String 
        
        :vss_sensor: Multimedia System 
        :vss_actuator: Multimedia System 


    .. xbr:event:: on_media_volume(new_value)

        :param new_value: Current Media Volume
        :type new_value: int
        :vss_id: 152 
        
        :vss_type: UInt8 
        
        :vss_sensor: Multimedia System 
        :vss_actuator: Multimedia System 


    .. xbr:event:: on_navigation_current_location_accuracy(new_value)

        :param new_value: Accuracy level of the latitude and longitude coordinates in meters.
        :type new_value: float
        :vss_id: 158 
        
        :vss_type: Double 
        :vss_unit: m 
        :vss_sensor: GPS 
        


    .. xbr:event:: on_navigation_current_location_altitude(new_value)

        :param new_value: Current elevation of the position in meters.
        :type new_value: float
        :vss_id: 159 
        
        :vss_type: Double 
        :vss_unit: m 
        
        


    .. xbr:event:: on_navigation_current_location_heading(new_value)

        :param new_value: Current magnetic compass heading, in degrees.
        :type new_value: float
        :vss_id: 157 
        
        :vss_type: Double 
        :vss_unit: degrees 
        :vss_sensor: GPS 
        


    .. xbr:event:: on_navigation_current_location_latitude(new_value)

        :param new_value: Current latitude of vehicle, as reported by GPS.
        :type new_value: float
        :vss_id: 155 
        
        :vss_type: Double 
        :vss_unit: degrees 
        :vss_sensor: GPS 
        


    .. xbr:event:: on_navigation_current_location_longitude(new_value)

        :param new_value: Current longitude of vehicle, as reported by GPS.
        :type new_value: float
        :vss_id: 156 
        
        :vss_type: Double 
        :vss_unit: degrees 
        :vss_sensor: GPS 
        


    .. xbr:event:: on_navigation_current_location_speed(new_value)

        :param new_value: Vehicle speed, as sensed by the GPS receiver.
        :type new_value: int
        :vss_id: 160 
        
        :vss_type: UInt16 
        :vss_unit: km/h 
        :vss_sensor: GPS 
        


    .. xbr:event:: on_navigation_destination_set_latitude(new_value)

        :param new_value: Latitude of destination
        :type new_value: float
        :vss_id: 153 
        
        :vss_type: Double 
        :vss_unit: degrees 
        :vss_sensor: GPS 
        :vss_actuator: GPS 


    .. xbr:event:: on_navigation_destination_set_longitude(new_value)

        :param new_value: Longitude of destination
        :type new_value: float
        :vss_id: 154 
        
        :vss_type: Double 
        :vss_unit: degrees 
        :vss_sensor: GPS 
        :vss_actuator: GPS 

ILights
-------

Interior lights signals and sensors.

.. xbr:interface:: ILights

    Interior lights signals and sensors


    .. xbr:event:: on_ambient_light(new_value)

        :param new_value: How much ambient light is detected in cabin. 0 = No ambient light. 100 = Full brightness
        :type new_value: int
        :vss_id: 1130 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Light Sensor 
        


    .. xbr:event:: on_is_dome_on(new_value)

        :param new_value: Is central dome light light on
        :type new_value: bool
        :vss_id: 168 
        
        :vss_type: Boolean 
        
        :vss_sensor: Dome Light 
        :vss_actuator: Dome Light 


    .. xbr:event:: on_is_glove_box_on(new_value)

        :param new_value: Is glove box light on
        :type new_value: bool
        :vss_id: 166 
        
        :vss_type: Boolean 
        
        :vss_sensor: Glove Box Light 
        :vss_actuator: Glove Box Light 


    .. xbr:event:: on_is_trunk_on(new_value)

        :param new_value: Is trunk light light on
        :type new_value: bool
        :vss_id: 167 
        
        :vss_type: Boolean 
        
        :vss_sensor: Trunk Light 
        :vss_actuator: Trunk Light 


    .. xbr:event:: on_light_intensity(new_value)

        :param new_value: Intensity of the interior lights. 0 = Off. 100 = Full brightness.
        :type new_value: int
        :vss_id: 170 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Light Sensor 
        


    .. xbr:event:: on_row1_is_shared_on(new_value)

        :param new_value: Is light shared across first row on
        :type new_value: bool
        :vss_id: 171 
        
        :vss_type: Boolean 
        
        :vss_sensor: Light Sensor 
        


    .. xbr:event:: on_row1_left_is_passenger_on(new_value)

        :param new_value: Is passenger light on
        :type new_value: bool
        :vss_id: 172 
        
        :vss_type: Boolean 
        
        :vss_sensor: Passenger Light 
        :vss_actuator: Passenger Light 


    .. xbr:event:: on_row1_right_is_passenger_on(new_value)

        :param new_value: Is passenger light on
        :type new_value: bool
        :vss_id: 173 
        
        :vss_type: Boolean 
        
        :vss_sensor: Passenger Light 
        :vss_actuator: Passenger Light 


    .. xbr:event:: on_row2_is_shared_on(new_value)

        :param new_value: Is light shared across second row on
        :type new_value: bool
        :vss_id: 174 
        
        :vss_type: Boolean 
        
        :vss_sensor: Light Sensor 
        


    .. xbr:event:: on_row2_left_is_passenger_on(new_value)

        :param new_value: Is passenger light on
        :type new_value: bool
        :vss_id: 175 
        
        :vss_type: Boolean 
        
        :vss_sensor: Passenger Light 
        :vss_actuator: Passenger Light 


    .. xbr:event:: on_row2_right_is_passenger_on(new_value)

        :param new_value: Is passenger light on
        :type new_value: bool
        :vss_id: 176 
        
        :vss_type: Boolean 
        
        :vss_sensor: Passenger Light 
        :vss_actuator: Passenger Light 


    .. xbr:event:: on_row3_is_shared_on(new_value)

        :param new_value: Is light shared third across row on
        :type new_value: bool
        :vss_id: 177 
        
        :vss_type: Boolean 
        
        :vss_sensor: Light Sensor 
        


    .. xbr:event:: on_row3_left_is_passenger_on(new_value)

        :param new_value: Is passenger light on
        :type new_value: bool
        :vss_id: 178 
        
        :vss_type: Boolean 
        
        :vss_sensor: Passenger Light 
        :vss_actuator: Passenger Light 


    .. xbr:event:: on_row3_right_is_passenger_on(new_value)

        :param new_value: Is passenger light on
        :type new_value: bool
        :vss_id: 179 
        
        :vss_type: Boolean 
        
        :vss_sensor: Passenger Light 
        :vss_actuator: Passenger Light 


    .. xbr:event:: on_row4_is_shared_on(new_value)

        :param new_value: Is light shared across fourth row on
        :type new_value: bool
        :vss_id: 180 
        
        :vss_type: Boolean 
        
        :vss_sensor: Light Sensor 
        


    .. xbr:event:: on_row4_left_is_passenger_on(new_value)

        :param new_value: Is passenger light on
        :type new_value: bool
        :vss_id: 181 
        
        :vss_type: Boolean 
        
        :vss_sensor: Passenger Light 
        :vss_actuator: Passenger Light 


    .. xbr:event:: on_row4_right_is_passenger_on(new_value)

        :param new_value: Is passenger light on
        :type new_value: bool
        :vss_id: 182 
        
        :vss_type: Boolean 
        
        :vss_sensor: Passenger Light 
        :vss_actuator: Passenger Light 

IRearShade
----------

Rear window shade..

.. xbr:interface:: IRearShade

    Rear window shade.


    .. xbr:event:: on_position(new_value)

        :param new_value: Position of side window blind. 0 = Fully retracted. 100 = Fully deployed.
        :type new_value: int
        :vss_id: 114 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        :vss_actuator: RearShade Actuator 


    .. xbr:event:: on_switch(new_value)

        :param new_value: Switch controlling sliding action such as window, sunroof, or blind.
        :type new_value: str
        :vss_id: 113 
        :vss_enum: ['Inactive', 'Close', 'Open', 'OneShotClose', 'OneShotOpen'] 
        :vss_type: String 
        
        
        :vss_actuator: RearShade System 

IRearviewMirror
---------------

Rearview mirror.

.. xbr:interface:: IRearviewMirror

    Rearview mirror


    .. xbr:event:: on_dimming_level(new_value)

        :param new_value: Dimming level of rearview mirror. 0 = undimmed. 100 = fully dimmed
        :type new_value: int
        :vss_id: 1129 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Dimming System 
        :vss_actuator: Dimming System 

ISeat
-----

All seats..

.. xbr:interface:: ISeat

    All seats.


    .. xbr:event:: on_row1_pos1_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 251 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row1_pos1_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 245 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row1_pos1_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 246 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row1_pos1_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 239 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row1_pos1_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 250 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row1_pos1_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 241 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row1_pos1_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 240 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row1_pos1_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 248 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row1_pos1_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 247 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row1_pos1_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 242 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row1_pos1_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 244 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row1_pos1_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 243 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row1_pos1_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 249 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row1_pos1_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 255 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos1_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 253 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row1_pos1_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 267 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos1_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 265 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos1_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 266 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos1_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 264 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos1_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 257 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos1_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 254 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos1_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 259 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row1_pos1_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 258 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row1_pos1_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 271 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos1_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 269 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row1_pos1_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 270 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos1_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 268 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row1_pos1_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 261 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row1_pos1_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 260 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row1_pos1_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 262 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos1_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 263 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos1_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 273 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos1_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 272 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos1_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 256 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos1_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 252 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 


    .. xbr:event:: on_row1_pos2_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 286 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row1_pos2_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 280 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row1_pos2_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 281 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row1_pos2_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 274 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row1_pos2_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 285 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row1_pos2_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 276 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row1_pos2_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 275 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row1_pos2_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 283 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row1_pos2_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 282 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row1_pos2_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 277 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row1_pos2_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 279 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row1_pos2_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 278 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row1_pos2_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 284 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row1_pos2_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 290 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos2_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 288 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row1_pos2_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 302 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos2_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 300 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos2_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 301 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos2_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 299 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos2_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 292 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos2_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 289 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos2_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 294 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row1_pos2_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 293 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row1_pos2_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 306 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos2_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 304 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row1_pos2_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 305 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos2_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 303 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row1_pos2_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 296 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row1_pos2_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 295 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row1_pos2_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 297 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos2_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 298 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos2_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 308 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos2_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 307 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos2_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 291 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos2_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 287 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 


    .. xbr:event:: on_row1_pos3_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 321 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row1_pos3_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 315 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row1_pos3_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 316 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row1_pos3_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 309 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row1_pos3_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 320 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row1_pos3_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 311 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row1_pos3_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 310 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row1_pos3_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 318 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row1_pos3_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 317 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row1_pos3_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 312 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row1_pos3_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 314 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row1_pos3_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 313 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row1_pos3_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 319 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row1_pos3_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 325 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos3_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 323 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row1_pos3_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 337 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos3_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 335 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos3_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 336 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos3_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 334 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos3_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 327 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos3_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 324 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos3_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 329 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row1_pos3_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 328 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row1_pos3_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 341 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos3_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 339 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row1_pos3_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 340 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos3_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 338 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row1_pos3_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 331 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row1_pos3_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 330 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row1_pos3_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 332 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos3_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 333 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos3_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 343 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos3_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 342 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos3_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 326 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos3_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 322 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 


    .. xbr:event:: on_row1_pos4_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 356 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row1_pos4_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 350 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row1_pos4_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 351 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row1_pos4_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 344 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row1_pos4_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 355 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row1_pos4_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 346 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row1_pos4_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 345 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row1_pos4_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 353 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row1_pos4_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 352 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row1_pos4_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 347 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row1_pos4_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 349 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row1_pos4_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 348 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row1_pos4_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 354 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row1_pos4_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 360 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos4_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 358 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row1_pos4_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 372 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos4_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 370 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos4_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 371 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos4_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 369 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos4_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 362 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos4_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 359 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos4_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 364 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row1_pos4_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 363 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row1_pos4_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 376 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos4_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 374 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row1_pos4_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 375 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos4_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 373 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row1_pos4_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 366 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row1_pos4_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 365 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row1_pos4_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 367 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos4_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 368 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos4_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 378 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos4_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 377 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos4_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 361 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos4_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 357 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 


    .. xbr:event:: on_row1_pos5_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 391 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row1_pos5_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 385 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row1_pos5_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 386 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row1_pos5_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 379 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row1_pos5_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 390 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row1_pos5_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 381 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row1_pos5_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 380 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row1_pos5_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 388 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row1_pos5_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 387 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row1_pos5_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 382 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row1_pos5_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 384 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row1_pos5_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 383 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row1_pos5_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 389 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row1_pos5_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 395 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos5_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 393 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row1_pos5_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 407 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos5_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 405 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos5_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 406 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos5_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 404 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row1_pos5_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 397 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos5_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 394 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos5_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 399 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row1_pos5_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 398 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row1_pos5_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 411 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos5_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 409 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row1_pos5_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 410 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos5_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 408 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row1_pos5_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 401 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row1_pos5_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 400 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row1_pos5_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 402 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos5_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 403 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos5_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 413 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos5_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 412 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row1_pos5_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 396 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row1_pos5_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 392 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 


    .. xbr:event:: on_row2_pos1_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 426 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row2_pos1_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 420 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row2_pos1_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 421 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row2_pos1_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 414 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row2_pos1_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 425 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row2_pos1_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 416 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row2_pos1_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 415 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row2_pos1_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 423 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row2_pos1_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 422 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row2_pos1_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 417 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row2_pos1_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 419 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row2_pos1_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 418 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row2_pos1_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 424 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row2_pos1_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 430 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos1_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 428 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row2_pos1_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 442 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos1_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 440 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos1_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 441 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos1_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 439 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos1_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 432 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos1_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 429 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos1_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 434 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row2_pos1_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 433 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row2_pos1_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 446 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos1_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 444 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row2_pos1_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 445 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos1_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 443 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row2_pos1_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 436 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row2_pos1_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 435 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row2_pos1_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 437 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos1_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 438 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos1_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 448 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos1_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 447 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos1_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 431 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos1_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 427 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 


    .. xbr:event:: on_row2_pos2_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 461 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row2_pos2_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 455 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row2_pos2_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 456 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row2_pos2_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 449 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row2_pos2_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 460 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row2_pos2_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 451 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row2_pos2_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 450 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row2_pos2_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 458 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row2_pos2_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 457 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row2_pos2_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 452 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row2_pos2_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 454 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row2_pos2_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 453 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row2_pos2_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 459 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row2_pos2_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 465 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos2_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 463 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row2_pos2_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 477 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos2_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 475 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos2_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 476 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos2_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 474 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos2_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 467 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos2_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 464 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos2_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 469 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row2_pos2_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 468 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row2_pos2_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 481 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos2_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 479 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row2_pos2_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 480 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos2_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 478 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row2_pos2_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 471 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row2_pos2_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 470 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row2_pos2_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 472 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos2_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 473 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos2_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 483 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos2_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 482 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos2_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 466 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos2_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 462 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 


    .. xbr:event:: on_row2_pos3_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 496 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row2_pos3_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 490 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row2_pos3_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 491 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row2_pos3_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 484 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row2_pos3_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 495 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row2_pos3_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 486 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row2_pos3_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 485 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row2_pos3_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 493 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row2_pos3_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 492 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row2_pos3_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 487 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row2_pos3_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 489 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row2_pos3_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 488 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row2_pos3_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 494 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row2_pos3_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 500 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos3_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 498 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row2_pos3_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 512 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos3_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 510 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos3_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 511 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos3_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 509 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos3_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 502 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos3_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 499 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos3_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 504 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row2_pos3_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 503 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row2_pos3_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 516 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos3_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 514 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row2_pos3_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 515 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos3_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 513 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row2_pos3_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 506 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row2_pos3_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 505 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row2_pos3_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 507 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos3_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 508 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos3_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 518 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos3_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 517 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos3_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 501 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos3_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 497 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 


    .. xbr:event:: on_row2_pos4_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 531 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row2_pos4_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 525 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row2_pos4_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 526 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row2_pos4_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 519 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row2_pos4_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 530 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row2_pos4_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 521 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row2_pos4_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 520 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row2_pos4_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 528 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row2_pos4_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 527 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row2_pos4_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 522 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row2_pos4_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 524 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row2_pos4_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 523 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row2_pos4_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 529 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row2_pos4_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 535 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos4_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 533 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row2_pos4_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 547 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos4_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 545 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos4_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 546 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos4_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 544 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos4_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 537 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos4_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 534 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos4_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 539 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row2_pos4_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 538 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row2_pos4_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 551 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos4_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 549 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row2_pos4_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 550 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos4_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 548 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row2_pos4_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 541 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row2_pos4_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 540 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row2_pos4_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 542 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos4_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 543 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos4_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 553 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos4_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 552 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos4_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 536 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos4_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 532 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 


    .. xbr:event:: on_row2_pos5_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 566 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row2_pos5_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 560 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row2_pos5_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 561 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row2_pos5_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 554 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row2_pos5_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 565 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row2_pos5_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 556 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row2_pos5_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 555 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row2_pos5_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 563 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row2_pos5_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 562 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row2_pos5_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 557 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row2_pos5_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 559 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row2_pos5_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 558 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row2_pos5_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 564 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row2_pos5_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 570 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos5_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 568 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row2_pos5_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 582 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos5_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 580 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos5_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 581 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos5_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 579 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row2_pos5_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 572 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos5_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 569 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos5_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 574 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row2_pos5_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 573 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row2_pos5_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 586 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos5_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 584 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row2_pos5_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 585 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos5_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 583 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row2_pos5_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 576 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row2_pos5_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 575 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row2_pos5_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 577 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos5_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 578 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos5_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 588 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos5_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 587 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row2_pos5_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 571 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row2_pos5_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 567 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 


    .. xbr:event:: on_row3_pos1_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 601 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row3_pos1_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 595 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row3_pos1_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 596 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row3_pos1_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 589 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row3_pos1_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 600 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row3_pos1_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 591 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row3_pos1_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 590 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row3_pos1_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 598 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row3_pos1_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 597 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row3_pos1_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 592 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row3_pos1_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 594 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row3_pos1_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 593 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row3_pos1_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 599 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row3_pos1_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 605 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos1_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 603 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row3_pos1_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 617 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos1_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 615 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos1_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 616 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos1_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 614 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos1_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 607 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos1_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 604 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos1_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 609 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row3_pos1_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 608 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row3_pos1_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 621 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos1_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 619 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row3_pos1_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 620 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos1_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 618 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row3_pos1_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 611 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row3_pos1_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 610 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row3_pos1_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 612 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos1_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 613 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos1_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 623 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos1_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 622 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos1_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 606 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos1_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 602 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 


    .. xbr:event:: on_row3_pos2_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 636 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row3_pos2_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 630 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row3_pos2_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 631 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row3_pos2_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 624 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row3_pos2_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 635 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row3_pos2_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 626 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row3_pos2_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 625 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row3_pos2_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 633 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row3_pos2_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 632 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row3_pos2_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 627 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row3_pos2_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 629 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row3_pos2_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 628 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row3_pos2_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 634 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row3_pos2_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 640 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos2_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 638 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row3_pos2_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 652 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos2_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 650 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos2_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 651 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos2_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 649 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos2_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 642 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos2_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 639 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos2_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 644 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row3_pos2_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 643 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row3_pos2_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 656 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos2_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 654 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row3_pos2_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 655 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos2_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 653 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row3_pos2_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 646 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row3_pos2_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 645 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row3_pos2_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 647 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos2_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 648 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos2_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 658 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos2_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 657 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos2_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 641 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos2_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 637 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 


    .. xbr:event:: on_row3_pos3_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 671 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row3_pos3_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 665 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row3_pos3_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 666 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row3_pos3_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 659 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row3_pos3_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 670 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row3_pos3_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 661 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row3_pos3_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 660 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row3_pos3_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 668 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row3_pos3_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 667 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row3_pos3_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 662 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row3_pos3_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 664 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row3_pos3_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 663 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row3_pos3_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 669 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row3_pos3_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 675 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos3_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 673 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row3_pos3_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 687 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos3_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 685 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos3_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 686 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos3_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 684 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos3_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 677 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos3_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 674 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos3_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 679 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row3_pos3_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 678 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row3_pos3_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 691 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos3_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 689 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row3_pos3_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 690 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos3_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 688 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row3_pos3_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 681 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row3_pos3_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 680 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row3_pos3_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 682 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos3_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 683 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos3_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 693 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos3_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 692 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos3_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 676 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos3_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 672 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 


    .. xbr:event:: on_row3_pos4_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 706 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row3_pos4_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 700 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row3_pos4_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 701 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row3_pos4_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 694 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row3_pos4_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 705 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row3_pos4_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 696 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row3_pos4_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 695 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row3_pos4_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 703 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row3_pos4_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 702 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row3_pos4_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 697 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row3_pos4_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 699 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row3_pos4_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 698 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row3_pos4_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 704 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row3_pos4_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 710 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos4_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 708 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row3_pos4_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 722 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos4_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 720 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos4_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 721 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos4_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 719 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos4_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 712 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos4_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 709 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos4_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 714 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row3_pos4_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 713 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row3_pos4_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 726 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos4_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 724 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row3_pos4_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 725 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos4_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 723 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row3_pos4_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 716 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row3_pos4_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 715 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row3_pos4_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 717 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos4_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 718 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos4_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 728 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos4_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 727 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos4_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 711 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos4_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 707 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 


    .. xbr:event:: on_row3_pos5_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 741 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row3_pos5_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 735 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row3_pos5_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 736 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row3_pos5_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 729 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row3_pos5_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 740 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row3_pos5_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 731 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row3_pos5_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 730 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row3_pos5_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 738 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row3_pos5_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 737 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row3_pos5_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 732 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row3_pos5_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 734 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row3_pos5_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 733 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row3_pos5_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 739 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row3_pos5_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 745 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos5_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 743 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row3_pos5_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 757 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos5_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 755 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos5_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 756 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos5_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 754 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row3_pos5_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 747 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos5_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 744 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos5_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 749 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row3_pos5_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 748 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row3_pos5_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 761 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos5_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 759 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row3_pos5_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 760 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos5_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 758 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row3_pos5_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 751 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row3_pos5_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 750 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row3_pos5_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 752 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos5_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 753 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos5_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 763 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos5_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 762 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row3_pos5_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 746 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row3_pos5_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 742 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 


    .. xbr:event:: on_row4_pos1_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 776 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row4_pos1_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 770 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row4_pos1_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 771 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row4_pos1_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 764 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row4_pos1_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 775 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row4_pos1_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 766 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row4_pos1_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 765 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row4_pos1_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 773 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row4_pos1_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 772 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row4_pos1_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 767 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row4_pos1_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 769 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row4_pos1_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 768 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row4_pos1_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 774 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row4_pos1_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 780 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos1_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 778 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row4_pos1_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 792 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos1_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 790 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos1_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 791 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos1_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 789 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos1_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 782 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos1_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 779 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos1_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 784 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row4_pos1_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 783 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row4_pos1_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 796 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos1_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 794 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row4_pos1_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 795 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos1_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 793 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row4_pos1_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 786 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row4_pos1_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 785 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row4_pos1_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 787 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos1_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 788 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos1_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 798 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos1_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 797 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos1_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 781 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos1_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 777 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 


    .. xbr:event:: on_row4_pos2_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 811 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row4_pos2_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 805 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row4_pos2_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 806 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row4_pos2_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 799 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row4_pos2_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 810 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row4_pos2_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 801 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row4_pos2_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 800 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row4_pos2_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 808 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row4_pos2_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 807 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row4_pos2_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 802 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row4_pos2_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 804 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row4_pos2_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 803 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row4_pos2_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 809 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row4_pos2_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 815 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos2_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 813 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row4_pos2_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 827 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos2_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 825 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos2_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 826 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos2_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 824 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos2_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 817 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos2_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 814 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos2_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 819 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row4_pos2_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 818 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row4_pos2_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 831 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos2_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 829 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row4_pos2_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 830 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos2_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 828 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row4_pos2_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 821 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row4_pos2_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 820 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row4_pos2_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 822 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos2_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 823 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos2_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 833 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos2_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 832 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos2_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 816 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos2_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 812 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 


    .. xbr:event:: on_row4_pos3_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 846 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row4_pos3_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 840 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row4_pos3_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 841 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row4_pos3_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 834 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row4_pos3_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 845 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row4_pos3_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 836 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row4_pos3_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 835 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row4_pos3_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 843 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row4_pos3_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 842 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row4_pos3_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 837 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row4_pos3_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 839 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row4_pos3_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 838 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row4_pos3_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 844 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row4_pos3_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 850 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos3_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 848 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row4_pos3_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 862 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos3_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 860 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos3_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 861 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos3_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 859 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos3_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 852 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos3_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 849 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos3_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 854 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row4_pos3_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 853 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row4_pos3_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 866 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos3_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 864 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row4_pos3_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 865 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos3_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 863 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row4_pos3_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 856 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row4_pos3_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 855 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row4_pos3_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 857 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos3_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 858 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos3_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 868 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos3_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 867 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos3_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 851 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos3_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 847 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 


    .. xbr:event:: on_row4_pos4_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 881 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row4_pos4_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 875 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row4_pos4_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 876 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row4_pos4_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 869 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row4_pos4_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 880 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row4_pos4_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 871 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row4_pos4_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 870 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row4_pos4_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 878 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row4_pos4_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 877 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row4_pos4_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 872 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row4_pos4_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 874 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row4_pos4_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 873 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row4_pos4_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 879 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row4_pos4_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 885 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos4_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 883 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row4_pos4_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 897 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos4_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 895 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos4_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 896 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos4_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 894 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos4_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 887 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos4_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 884 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos4_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 889 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row4_pos4_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 888 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row4_pos4_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 901 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos4_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 899 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row4_pos4_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 900 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos4_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 898 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row4_pos4_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 891 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row4_pos4_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 890 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row4_pos4_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 892 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos4_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 893 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos4_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 903 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos4_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 902 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos4_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 886 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos4_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 882 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 


    .. xbr:event:: on_row4_pos5_airbag_is_deployed(new_value)

        :param new_value: Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.
        :type new_value: bool
        :vss_id: 916 
        
        :vss_type: Boolean 
        
        :vss_sensor: Airbag System 
        


    .. xbr:event:: on_row4_pos5_cushion_height(new_value)

        :param new_value: Height of the seat front. 0 = Lowermost. 500 = Uppermost.
        :type new_value: int
        :vss_id: 910 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row4_pos5_cushion_length(new_value)

        :param new_value: Forward length of cushion (leg support). 0 = Rearmost. 500 = Forwardmost.
        :type new_value: int
        :vss_id: 911 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Cushion Position Sensor 
        


    .. xbr:event:: on_row4_pos5_has_passenger(new_value)

        :param new_value: Does the seat have a passenger in it.
        :type new_value: bool
        :vss_id: 904 
        
        :vss_type: Boolean 
        
        :vss_sensor: Occupant Classification System 
        


    .. xbr:event:: on_row4_pos5_head_restraint_height(new_value)

        :param new_value: Height of head restraint. 0 = Bottommost. 255 = Topmost.
        :type new_value: int
        :vss_id: 915 
        
        :vss_type: UInt8 
        :vss_unit: mm 
        :vss_sensor: Head Restraint Sensor 
        


    .. xbr:event:: on_row4_pos5_heating(new_value)

        :param new_value: Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat
        :type new_value: int
        :vss_id: 906 
        
        :vss_type: Int8 
        :vss_unit: percent 
        :vss_sensor: Seat Heater 
        


    .. xbr:event:: on_row4_pos5_is_belted(new_value)

        :param new_value: Is the belt engaged.
        :type new_value: bool
        :vss_id: 905 
        
        :vss_type: Boolean 
        
        :vss_sensor: Belt Sensor 
        


    .. xbr:event:: on_row4_pos5_lumbar_height(new_value)

        :param new_value: Lumbar support position. 0 = Lowermost. 255 = Uppermost.
        :type new_value: int
        :vss_id: 913 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row4_pos5_lumbar_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 912 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Position Sensor 
        


    .. xbr:event:: on_row4_pos5_massage(new_value)

        :param new_value: Seat massage level. 0 = off. 100 = max massage.
        :type new_value: int
        :vss_id: 907 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        :vss_sensor: Massage System 
        


    .. xbr:event:: on_row4_pos5_position(new_value)

        :param new_value: Seat horizontal position. 0 = Frontmost. 1000 = Rearmost
        :type new_value: int
        :vss_id: 909 
        
        :vss_type: UInt16 
        :vss_unit: mm 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row4_pos5_recline(new_value)

        :param new_value: Recline level. -90 = Max forward recline. 90 max backward recline
        :type new_value: int
        :vss_id: 908 
        
        :vss_type: Int8 
        :vss_unit: degrees 
        :vss_sensor: Seat Position Sensor 
        


    .. xbr:event:: on_row4_pos5_side_bolster_inflation(new_value)

        :param new_value: Lumbar support inflation. 0 = Fully deflated. 255 = Fully inflated.
        :type new_value: int
        :vss_id: 914 
        
        :vss_type: UInt8 
        
        :vss_sensor: Lumbar Pressure Sensor 
        


    .. xbr:event:: on_row4_pos5_switch_backward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 920 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos5_switch_cooler(new_value)

        :param new_value: Cooler switch for Seat heater
        :type new_value: bool
        :vss_id: 918 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Cooler 


    .. xbr:event:: on_row4_pos5_switch_cushion_backward(new_value)

        :param new_value: Seat cushion backward/shorten switch engaged
        :type new_value: bool
        :vss_id: 932 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos5_switch_cushion_down(new_value)

        :param new_value: Seat cushion down switch engaged
        :type new_value: bool
        :vss_id: 930 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos5_switch_cushion_forward(new_value)

        :param new_value: Seat cushion forward/lengthen switch engaged
        :type new_value: bool
        :vss_id: 931 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos5_switch_cushion_up(new_value)

        :param new_value: Seat cushion up switch engaged
        :type new_value: bool
        :vss_id: 929 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Cushion Position Actuator 


    .. xbr:event:: on_row4_pos5_switch_down(new_value)

        :param new_value: Seat down switch engaged
        :type new_value: bool
        :vss_id: 922 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos5_switch_forward(new_value)

        :param new_value: Seat forward switch engaged
        :type new_value: bool
        :vss_id: 919 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos5_switch_head_restraint_down(new_value)

        :param new_value: Head restraint down switch engaged
        :type new_value: bool
        :vss_id: 924 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row4_pos5_switch_head_restraint_up(new_value)

        :param new_value: Head restraint up switch engaged
        :type new_value: bool
        :vss_id: 923 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Head Restraint Actuator 


    .. xbr:event:: on_row4_pos5_switch_lumbar_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 936 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos5_switch_lumbar_down(new_value)

        :param new_value: Lumbar down switch engaged
        :type new_value: bool
        :vss_id: 934 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row4_pos5_switch_lumbar_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 935 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos5_switch_lumbar_up(new_value)

        :param new_value: Lumbar up switch engaged
        :type new_value: bool
        :vss_id: 933 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Position Actuator 


    .. xbr:event:: on_row4_pos5_switch_massage_decrease(new_value)

        :param new_value: Decrease massage level switch engaged
        :type new_value: bool
        :vss_id: 926 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row4_pos5_switch_massage_increase(new_value)

        :param new_value: Increase massage level switch engaged
        :type new_value: bool
        :vss_id: 925 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Massage System 


    .. xbr:event:: on_row4_pos5_switch_recline_backward(new_value)

        :param new_value: Seatback recline backward switch engaged
        :type new_value: bool
        :vss_id: 927 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos5_switch_recline_forward(new_value)

        :param new_value: Seatback recline forward switch engaged
        :type new_value: bool
        :vss_id: 928 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos5_switch_side_bolster_deflate(new_value)

        :param new_value: Lumbar deflation switch engaged
        :type new_value: bool
        :vss_id: 938 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos5_switch_side_bolster_inflate(new_value)

        :param new_value: Lumbar inflation switch engaged
        :type new_value: bool
        :vss_id: 937 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Lumbar Pressure Actuator 


    .. xbr:event:: on_row4_pos5_switch_up(new_value)

        :param new_value: Seat up switch engaged
        :type new_value: bool
        :vss_id: 921 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Position Actuator 


    .. xbr:event:: on_row4_pos5_switch_warmer(new_value)

        :param new_value: Warmer switch for Seat heater
        :type new_value: bool
        :vss_id: 917 
        
        :vss_type: Boolean 
        
        
        :vss_actuator: Seat Heater 

ISunroof
--------

Sun roof status..

.. xbr:interface:: ISunroof

    Sun roof status.


    .. xbr:event:: on_position(new_value)

        :param new_value: Sunroof position. 0 = Fully closed 100 = Fully opened. -100 = Fully tilted
        :type new_value: int
        :vss_id: 161 
        
        :vss_type: Int8 
        
        :vss_sensor: Sunroof Position Sensor 
        


    .. xbr:event:: on_shade_position(new_value)

        :param new_value: Position of side window blind. 0 = Fully retracted. 100 = Fully deployed.
        :type new_value: int
        :vss_id: 164 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        :vss_actuator: RearShade Actuator 


    .. xbr:event:: on_shade_switch(new_value)

        :param new_value: Switch controlling sliding action such as window, sunroof, or blind.
        :type new_value: str
        :vss_id: 163 
        :vss_enum: ['Inactive', 'Close', 'Open', 'OneShotClose', 'OneShotOpen'] 
        :vss_type: String 
        
        
        :vss_actuator: RearShade System 


    .. xbr:event:: on_switch(new_value)

        :param new_value: Switch controlling sliding action such as window, sunroof, or shade.
        :type new_value: str
        :vss_id: 162 
        :vss_enum: ['Inactive', 'Close', 'Open', 'OneShotClose', 'OneShotOpen', 'TiltUp', 'TiltDown'] 
        :vss_type: String 
        
        
        :vss_actuator: Sunroof Position Actuator 
