# Automatically generated by Pynguin.
import typesystem.formats as module_0

def test_case_0():
    date_time_format_0 = module_0.DateTimeFormat()

def test_case_1():
    date_time_format_0 = module_0.DateTimeFormat()
    str_0 = '2019-09-30T18:05:22.152712+00:00'
    datetime_0 = date_time_format_0.validate(str_0)

def test_case_2():
    u_u_i_d_format_0 = module_0.UUIDFormat()
    bool_0 = u_u_i_d_format_0.is_native_type(u_u_i_d_format_0)

def test_case_3():
    date_time_format_0 = module_0.DateTimeFormat()
    str_0 = '2019-10-01T23:59:59Z'
    datetime_0 = date_time_format_0.validate(str_0)
    optional_0 = date_time_format_0.serialize(datetime_0)

def test_case_4():
    date_time_format_0 = module_0.DateTimeFormat()
    str_0 = '2018-01-31T22:30:00'
    datetime_0 = date_time_format_0.validate(str_0)

def test_case_5():
    u_u_i_d_format_0 = module_0.UUIDFormat()
    str_0 = '9c04a4e6-7c83-4f58-a2e8-cd805518fb68'
    u_u_i_d_0 = u_u_i_d_format_0.validate(str_0)
    var_0 = u_u_i_d_0.hex
    u_u_i_d_1 = u_u_i_d_format_0.validate(str_0)
    var_1 = str(var_0)

def test_case_6():
    date_time_format_0 = module_0.DateTimeFormat()
    str_0 = '2018-01-31T22:30:00Z'
    datetime_0 = date_time_format_0.validate(str_0)
    str_1 = '2018-01-31T22:30:00'
    datetime_1 = date_time_format_0.validate(str_1)
    str_2 = '2018-01-31T22:30:00+01:00'
    datetime_2 = date_time_format_0.validate(str_2)
    datetime_3 = date_time_format_0.validate(str_0)
    optional_0 = date_time_format_0.serialize(datetime_2)

def test_case_7():
    date_format_0 = module_0.DateFormat()
    str_0 = '2020-10-22'
    date_0 = date_format_0.validate(str_0)
    optional_0 = date_format_0.serialize(date_0)
    var_0 = None
    optional_1 = date_format_0.serialize(var_0)