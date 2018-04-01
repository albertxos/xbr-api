org.genivi.vss.obd
==================

OBD data.

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

.. xbr:namespace:: org.genivi.vss.obd

IOBD
----

FIXME.

.. xbr:interface:: IOBD

    FIXME


    .. xbr:event:: on_absolute_load(new_value)

        :param new_value: PID 43 - Absolute load value
        :type new_value: int
        :vss_id: 1077 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_accelerator_position_d(new_value)

        :param new_value: PID 49 - Accelerator pedal position D
        :type new_value: int
        :vss_id: 1083 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_accelerator_position_e(new_value)

        :param new_value: PID 4A - Accelerator pedal position E
        :type new_value: int
        :vss_id: 1084 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_accelerator_position_f(new_value)

        :param new_value: PID 4B - Accelerator pedal position F
        :type new_value: int
        :vss_id: 1085 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_air_status(new_value)

        :param new_value: PID 12 - Secondary air status
        :type new_value: str
        :vss_id: 1013 
        
        :vss_type: String 
        
        
        


    .. xbr:event:: on_ambient_air_temperature(new_value)

        :param new_value: PID 46 - Ambient air temperature
        :type new_value: float
        :vss_id: 1080 
        
        :vss_type: Float 
        :vss_unit: celsius 
        
        


    .. xbr:event:: on_aux_input_status(new_value)

        :param new_value: PID 1E - Auxiliary input status (power take off)
        :type new_value: bool
        :vss_id: 1039 
        
        :vss_type: Boolean 
        
        
        


    .. xbr:event:: on_barometric_pressure(new_value)

        :param new_value: PID 33 - Barometric pressure
        :type new_value: float
        :vss_id: 1068 
        
        :vss_type: Float 
        :vss_unit: kpa 
        
        


    .. xbr:event:: on_catalyst_bank1_temperature1(new_value)

        :param new_value: PID 3C - Catalyst temperature from bank 1, sensor 1
        :type new_value: float
        :vss_id: 1069 
        
        :vss_type: Float 
        :vss_unit: celsius 
        
        


    .. xbr:event:: on_catalyst_bank1_temperature2(new_value)

        :param new_value: PID 3E - Catalyst temperature from bank 1, sensor 2
        :type new_value: float
        :vss_id: 1070 
        
        :vss_type: Float 
        :vss_unit: celsius 
        
        


    .. xbr:event:: on_catalyst_bank2_temperature1(new_value)

        :param new_value: PID 3D - Catalyst temperature from bank 2, sensor 1
        :type new_value: float
        :vss_id: 1071 
        
        :vss_type: Float 
        :vss_unit: celsius 
        
        


    .. xbr:event:: on_catalyst_bank2_temperature2(new_value)

        :param new_value: PID 3F - Catalyst temperature from bank 2, sensor 2
        :type new_value: float
        :vss_id: 1072 
        
        :vss_type: Float 
        :vss_unit: celsius 
        
        


    .. xbr:event:: on_commanded_e_g_r(new_value)

        :param new_value: PID 2C - Commanded exhaust gas recirculation (EGR)
        :type new_value: int
        :vss_id: 1061 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_commanded_e_v_a_p(new_value)

        :param new_value: PID 2E - Commanded evaporative purge (EVAP) valve
        :type new_value: int
        :vss_id: 1063 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_commanded_equivalence_ratio(new_value)

        :param new_value: PID 44 - Commanded equivalence ratio
        :type new_value: float
        :vss_id: 1078 
        
        :vss_type: Float 
        :vss_unit: ratio 
        
        


    .. xbr:event:: on_control_module_voltage(new_value)

        :param new_value: PID 42 - Control module voltage
        :type new_value: float
        :vss_id: 1076 
        
        :vss_type: Float 
        :vss_unit: V 
        
        


    .. xbr:event:: on_coolant_temperature(new_value)

        :param new_value: PID 05 - Coolant temperature
        :type new_value: float
        :vss_id: 1000 
        
        :vss_type: Float 
        :vss_unit: celsius 
        
        


    .. xbr:event:: on_distance_since_d_t_c_clear(new_value)

        :param new_value: PID 31 - Distance traveled since codes cleared
        :type new_value: float
        :vss_id: 1066 
        
        :vss_type: Float 
        :vss_unit: km 
        
        


    .. xbr:event:: on_distance_with_m_i_l(new_value)

        :param new_value: PID 21 - Distance traveled with MIL on
        :type new_value: int
        :vss_id: 1042 
        
        :vss_type: UInt32 
        :vss_unit: kilometer 
        
        


    .. xbr:event:: on_drive_cycle_status_d_t_c_count(new_value)

        :param new_value: Number of Diagnostic Trouble Codes (DTC)
        :type new_value: int
        :vss_id: 1075 
        
        :vss_type: UInt32 
        
        
        


    .. xbr:event:: on_drive_cycle_status_mil(new_value)

        :param new_value: Malfunction Indicator Light (MIL) - False = Off, True = On
        :type new_value: bool
        :vss_id: 1074 
        
        :vss_type: Boolean 
        
        
        


    .. xbr:event:: on_e_g_r_error(new_value)

        :param new_value: PID 2D - Exhaust gas recirculation (EGR) error
        :type new_value: int
        :vss_id: 1062 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_e_v_a_p_vapor_pressure(new_value)

        :param new_value: PID 32 - Evaporative purge (EVAP) system pressure
        :type new_value: float
        :vss_id: 1067 
        
        :vss_type: Float 
        :vss_unit: pa 
        
        


    .. xbr:event:: on_e_v_a_p_vapor_pressure_absolute(new_value)

        :param new_value: PID 53 - Absolute evaporative purge (EVAP) system pressure
        :type new_value: float
        :vss_id: 1092 
        
        :vss_type: Float 
        :vss_unit: kpa 
        
        


    .. xbr:event:: on_e_v_a_p_vapor_pressure_alternate(new_value)

        :param new_value: PID 54 - Alternate evaporative purge (EVAP) system pressure
        :type new_value: float
        :vss_id: 1093 
        
        :vss_type: Float 
        :vss_unit: pa 
        
        


    .. xbr:event:: on_engine_load(new_value)

        :param new_value: PID 04 - Engine load in percent - 0 = no load, 100 = full load
        :type new_value: int
        :vss_id: 999 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_engine_speed(new_value)

        :param new_value: PID 0C - Engine speed measured as rotations per minute
        :type new_value: float
        :vss_id: 1137 
        
        :vss_type: Float 
        :vss_unit: rpm 
        
        


    .. xbr:event:: on_ethanol_percent(new_value)

        :param new_value: PID 52 - Percentage of ethanol in the fuel
        :type new_value: int
        :vss_id: 1091 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_freeze_d_t_c(new_value)

        :param new_value: PID 02 - DTC that triggered the freeze frame
        :type new_value: str
        :vss_id: 997 
        
        :vss_type: String 
        
        
        


    .. xbr:event:: on_fuel_injection_timing(new_value)

        :param new_value: PID 5D - Fuel injection timing
        :type new_value: int
        :vss_id: 1102 
        
        :vss_type: Int16 
        :vss_unit: degrees 
        
        


    .. xbr:event:: on_fuel_level(new_value)

        :param new_value: PID 2F - Fuel level in the fuel tank
        :type new_value: int
        :vss_id: 1064 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_fuel_pressure(new_value)

        :param new_value: PID 0A - Fuel pressure
        :type new_value: float
        :vss_id: 1005 
        
        :vss_type: Float 
        :vss_unit: kpa 
        
        


    .. xbr:event:: on_fuel_rail_pressure_absolute(new_value)

        :param new_value: PID 59 - Absolute fuel rail pressure
        :type new_value: float
        :vss_id: 1098 
        
        :vss_type: Float 
        :vss_unit: kpa 
        
        


    .. xbr:event:: on_fuel_rail_pressure_direct(new_value)

        :param new_value: PID 23 - Fuel rail pressure direct inject
        :type new_value: float
        :vss_id: 1044 
        
        :vss_type: Float 
        :vss_unit: kpa 
        
        


    .. xbr:event:: on_fuel_rail_pressure_vac(new_value)

        :param new_value: PID 22 - Fuel rail pressure relative to vacuum
        :type new_value: float
        :vss_id: 1043 
        
        :vss_type: Float 
        :vss_unit: kpa 
        
        


    .. xbr:event:: on_fuel_rate(new_value)

        :param new_value: PID 5E - Engine fuel rate
        :type new_value: float
        :vss_id: 1103 
        
        :vss_type: Float 
        :vss_unit: l/h 
        
        


    .. xbr:event:: on_fuel_status(new_value)

        :param new_value: PID 03 - Fuel status
        :type new_value: str
        :vss_id: 998 
        
        :vss_type: String 
        
        
        


    .. xbr:event:: on_fuel_type(new_value)

        :param new_value: PID 51 - Fuel type
        :type new_value: str
        :vss_id: 1090 
        
        :vss_type: String 
        
        
        


    .. xbr:event:: on_hybrid_battery_remaining(new_value)

        :param new_value: PID 5B - Remaining life of hybrid battery
        :type new_value: int
        :vss_id: 1100 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_intake_temp(new_value)

        :param new_value: PID 0F - Intake temperature
        :type new_value: float
        :vss_id: 1010 
        
        :vss_type: Float 
        :vss_unit: celsius 
        
        


    .. xbr:event:: on_long_term_fuel_trim1(new_value)

        :param new_value: PID 07 - Long Term (learned) Fuel Trim - Bank 1 - negative percent leaner, positive percent richer
        :type new_value: int
        :vss_id: 1002 
        
        :vss_type: Int8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_long_term_fuel_trim2(new_value)

        :param new_value: PID 09 - Long Term (learned) Fuel Trim - Bank 2 - negative percent leaner, positive percent richer
        :type new_value: int
        :vss_id: 1004 
        
        :vss_type: Int8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_long_term_o2_trim1(new_value)

        :param new_value: PID 56 - Long term secondary O2 trim - Bank 1
        :type new_value: int
        :vss_id: 1095 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_long_term_o2_trim2(new_value)

        :param new_value: PID 58 - Long term secondary O2 trim - Bank 2
        :type new_value: int
        :vss_id: 1097 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_maf(new_value)

        :param new_value: PID 10 - Grams of air drawn into engine per second
        :type new_value: int
        :vss_id: 1011 
        
        :vss_type: Int16 
        :vss_unit: g/s 
        
        


    .. xbr:event:: on_map(new_value)

        :param new_value: PID 0B - Intake manifold pressure
        :type new_value: float
        :vss_id: 1006 
        
        :vss_type: Float 
        :vss_unit: kpa 
        
        


    .. xbr:event:: on_max_m_a_f(new_value)

        :param new_value: PID 50 - Maximum flow for mass air flow sensor
        :type new_value: float
        :vss_id: 1089 
        
        :vss_type: Float 
        :vss_unit: g/s 
        
        


    .. xbr:event:: on_o2_bank1_sensor1_voltage(new_value)

        :param new_value: PID 14 - Sensor voltage
        :type new_value: float
        :vss_id: 1138 
        
        :vss_type: Float 
        :vss_unit: V 
        
        


    .. xbr:event:: on_o2_bank1_sensor2_voltage(new_value)

        :param new_value: PID 15 - Sensor voltage
        :type new_value: float
        :vss_id: 1139 
        
        :vss_type: Float 
        :vss_unit: V 
        
        


    .. xbr:event:: on_o2_bank1_sensor3_voltage(new_value)

        :param new_value: PID 16 - Sensor voltage
        :type new_value: float
        :vss_id: 1140 
        
        :vss_type: Float 
        :vss_unit: V 
        
        


    .. xbr:event:: on_o2_bank1_sensor4_voltage(new_value)

        :param new_value: PID 17 - Sensor voltage
        :type new_value: float
        :vss_id: 1141 
        
        :vss_type: Float 
        :vss_unit: V 
        
        


    .. xbr:event:: on_o2_bank2_sensor1_voltage(new_value)

        :param new_value: PID 18 - Sensor voltage
        :type new_value: float
        :vss_id: 1142 
        
        :vss_type: Float 
        :vss_unit: V 
        
        


    .. xbr:event:: on_o2_bank2_sensor2_voltage(new_value)

        :param new_value: PID 19 - Sensor voltage
        :type new_value: float
        :vss_id: 1143 
        
        :vss_type: Float 
        :vss_unit: V 
        
        


    .. xbr:event:: on_o2_bank2_sensor3_voltage(new_value)

        :param new_value: PID 1A - Sensor voltage
        :type new_value: float
        :vss_id: 1144 
        
        :vss_type: Float 
        :vss_unit: V 
        
        


    .. xbr:event:: on_o2_bank2_sensor4_voltage(new_value)

        :param new_value: PID 1B - Sensor voltage
        :type new_value: float
        :vss_id: 1145 
        
        :vss_type: Float 
        :vss_unit: V 
        
        


    .. xbr:event:: on_o2_w_r_sensor1_current(new_value)

        :param new_value: PID 34 - Lambda current for wide range/band oxygen sensor 1
        :type new_value: float
        :vss_id: 1147 
        
        :vss_type: Float 
        :vss_unit: A 
        
        


    .. xbr:event:: on_o2_w_r_sensor1_voltage(new_value)

        :param new_value: PID 24 - Lambda voltage for wide range/band oxygen sensor 1
        :type new_value: float
        :vss_id: 1146 
        
        :vss_type: Float 
        :vss_unit: V 
        
        


    .. xbr:event:: on_o2_w_r_sensor2_current(new_value)

        :param new_value: PID 35 - Lambda current for wide range/band oxygen sensor 2
        :type new_value: float
        :vss_id: 1149 
        
        :vss_type: Float 
        :vss_unit: A 
        
        


    .. xbr:event:: on_o2_w_r_sensor2_voltage(new_value)

        :param new_value: PID 25 - Lambda voltage for wide range/band oxygen sensor 2
        :type new_value: float
        :vss_id: 1148 
        
        :vss_type: Float 
        :vss_unit: V 
        
        


    .. xbr:event:: on_o2_w_r_sensor3_current(new_value)

        :param new_value: PID 36 - Lambda current for wide range/band oxygen sensor 4
        :type new_value: float
        :vss_id: 1151 
        
        :vss_type: Float 
        :vss_unit: A 
        
        


    .. xbr:event:: on_o2_w_r_sensor3_voltage(new_value)

        :param new_value: PID 26 - Lambda voltage for wide range/band oxygen sensor 3
        :type new_value: float
        :vss_id: 1150 
        
        :vss_type: Float 
        :vss_unit: V 
        
        


    .. xbr:event:: on_o2_w_r_sensor4_current(new_value)

        :param new_value: PID 37 - Lambda current for wide range/band oxygen sensor 4
        :type new_value: float
        :vss_id: 1153 
        
        :vss_type: Float 
        :vss_unit: A 
        
        


    .. xbr:event:: on_o2_w_r_sensor4_voltage(new_value)

        :param new_value: PID 27 - Lambda voltage for wide range/band oxygen sensor 4
        :type new_value: float
        :vss_id: 1152 
        
        :vss_type: Float 
        :vss_unit: V 
        
        


    .. xbr:event:: on_o2_w_r_sensor5_current(new_value)

        :param new_value: PID 38 - Lambda current for wide range/band oxygen sensor 5
        :type new_value: float
        :vss_id: 1155 
        
        :vss_type: Float 
        :vss_unit: A 
        
        


    .. xbr:event:: on_o2_w_r_sensor5_voltage(new_value)

        :param new_value: PID 28 - Lambda voltage for wide range/band oxygen sensor 5
        :type new_value: float
        :vss_id: 1154 
        
        :vss_type: Float 
        :vss_unit: V 
        
        


    .. xbr:event:: on_o2_w_r_sensor6_current(new_value)

        :param new_value: PID 39 - Lambda current for wide range/band oxygen sensor 6
        :type new_value: float
        :vss_id: 1157 
        
        :vss_type: Float 
        :vss_unit: A 
        
        


    .. xbr:event:: on_o2_w_r_sensor6_voltage(new_value)

        :param new_value: PID 29 - Lambda voltage for wide range/band oxygen sensor 6
        :type new_value: float
        :vss_id: 1156 
        
        :vss_type: Float 
        :vss_unit: V 
        
        


    .. xbr:event:: on_o2_w_r_sensor7_current(new_value)

        :param new_value: PID 3A - Lambda current for wide range/band oxygen sensor 7
        :type new_value: float
        :vss_id: 1159 
        
        :vss_type: Float 
        :vss_unit: A 
        
        


    .. xbr:event:: on_o2_w_r_sensor7_voltage(new_value)

        :param new_value: PID 2A - Lambda voltage for wide range/band oxygen sensor 7
        :type new_value: float
        :vss_id: 1158 
        
        :vss_type: Float 
        :vss_unit: V 
        
        


    .. xbr:event:: on_o2_w_r_sensor8_current(new_value)

        :param new_value: PID 3B - Lambda current for wide range/band oxygen sensor 8
        :type new_value: float
        :vss_id: 1161 
        
        :vss_type: Float 
        :vss_unit: A 
        
        


    .. xbr:event:: on_o2_w_r_sensor8_voltage(new_value)

        :param new_value: PID 2B - Lambda voltage for wide range/band oxygen sensor 8
        :type new_value: float
        :vss_id: 1160 
        
        :vss_type: Float 
        :vss_unit: V 
        
        


    .. xbr:event:: on_oil_temperature(new_value)

        :param new_value: PID 5C - Engine oil temperature
        :type new_value: int
        :vss_id: 1101 
        
        :vss_type: UInt8 
        :vss_unit: celsius 
        
        


    .. xbr:event:: on_pids_a(new_value)

        :param new_value: PID 00 - Bit array of the supported pids 01 to 20
        :type new_value: int
        :vss_id: 994 
        
        :vss_type: UInt32 
        
        
        


    .. xbr:event:: on_pids_b(new_value)

        :param new_value: PID 20 - Bit array of the supported pids 21 to 40
        :type new_value: int
        :vss_id: 1041 
        
        :vss_type: UInt32 
        
        
        


    .. xbr:event:: on_pids_c(new_value)

        :param new_value: PID 40 - Bit array of the supported pids 41 to 60
        :type new_value: int
        :vss_id: 1073 
        
        :vss_type: UInt32 
        
        
        


    .. xbr:event:: on_relative_accelerator_position(new_value)

        :param new_value: PID 5A - Relative accelerator pedal position
        :type new_value: int
        :vss_id: 1099 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_relative_throttle_position(new_value)

        :param new_value: PID 45 - Relative throttle position
        :type new_value: int
        :vss_id: 1079 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_run_time(new_value)

        :param new_value: PID 1F - Engine run time
        :type new_value: int
        :vss_id: 1040 
        
        :vss_type: UInt32 
        :vss_unit: s 
        
        


    .. xbr:event:: on_run_time_m_i_l(new_value)

        :param new_value: PID 4D - Run time with MIL on
        :type new_value: int
        :vss_id: 1087 
        
        :vss_type: UInt32 
        :vss_unit: min 
        
        


    .. xbr:event:: on_short_term_fuel_trim1(new_value)

        :param new_value: PID 06 - Short Term (immediate) Fuel Trim - Bank 1 - negative percent leaner, positive percent richer
        :type new_value: int
        :vss_id: 1001 
        
        :vss_type: Int8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_short_term_fuel_trim2(new_value)

        :param new_value: PID 08 - Short Term (immediate) Fuel Trim - Bank 2 - negative percent leaner, positive percent richer
        :type new_value: int
        :vss_id: 1003 
        
        :vss_type: Int8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_short_term_o2_trim1(new_value)

        :param new_value: PID 55 - Short term secondary O2 trim - Bank 1
        :type new_value: int
        :vss_id: 1094 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_short_term_o2_trim2(new_value)

        :param new_value: PID 57 - Short term secondary O2 trim - Bank 2
        :type new_value: int
        :vss_id: 1096 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_speed(new_value)

        :param new_value: PID 0D - Vehicle speed
        :type new_value: float
        :vss_id: 1008 
        
        :vss_type: Float 
        :vss_unit: km/h 
        
        


    .. xbr:event:: on_status_d_t_c_count(new_value)

        :param new_value: Number of Diagnostic Trouble Codes (DTC)
        :type new_value: int
        :vss_id: 996 
        
        :vss_type: UInt32 
        
        
        


    .. xbr:event:: on_status_mil(new_value)

        :param new_value: Malfunction Indicator Light (MIL) False = Off, True = On
        :type new_value: bool
        :vss_id: 995 
        
        :vss_type: Boolean 
        
        
        


    .. xbr:event:: on_throttle_actuator(new_value)

        :param new_value: PID 4C - Commanded throttle actuator
        :type new_value: int
        :vss_id: 1086 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_throttle_position(new_value)

        :param new_value: PID 11 - Throttle position - 0 = closed throttle, 100 = open throttle
        :type new_value: int
        :vss_id: 1012 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_throttle_position_b(new_value)

        :param new_value: PID 47 - Absolute throttle position B
        :type new_value: int
        :vss_id: 1081 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_throttle_position_c(new_value)

        :param new_value: PID 48 - Absolute throttle position C
        :type new_value: int
        :vss_id: 1082 
        
        :vss_type: UInt8 
        :vss_unit: percent 
        
        


    .. xbr:event:: on_time_since_d_t_c_cleared(new_value)

        :param new_value: PID 4E - Time since trouble codes cleared
        :type new_value: int
        :vss_id: 1088 
        
        :vss_type: UInt32 
        :vss_unit: min 
        
        


    .. xbr:event:: on_timing_advance(new_value)

        :param new_value: PID 0E - Time advance
        :type new_value: float
        :vss_id: 1009 
        
        :vss_type: Float 
        :vss_unit: degrees 
        
        


    .. xbr:event:: on_warmups_since_d_t_c_clear(new_value)

        :param new_value: PID 30 - Number of warm-ups since codes cleared
        :type new_value: int
        :vss_id: 1065 
        
        :vss_type: UInt16 
        
        
        
