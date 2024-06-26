# Automatically generated by Pynguin.
import typesystem.formats as module_0
import uuid as module_1
import datetime as module_2

def test_case_0():
    date_format_0 = module_0.DateFormat()

def test_case_1():
    time_format_0 = module_0.TimeFormat()
    bool_0 = time_format_0.is_native_type(time_format_0)
    str_0 = '15:58:59.123'
    time_0 = time_format_0.validate(str_0)

def test_case_2():
    u_u_i_d_format_0 = module_0.UUIDFormat()
    str_0 = 'c38286b1-d8ce-4c87-b11d-f0dde84314a6'
    u_u_i_d_0 = u_u_i_d_format_0.validate(str_0)
    u_u_i_d_1 = module_1.UUID(str_0)

def test_case_3():
    time_format_0 = module_0.TimeFormat()
    date_format_0 = module_0.DateFormat()
    bool_0 = False
    bool_1 = date_format_0.is_native_type(bool_0)

def test_case_4():
    time_format_0 = module_0.TimeFormat()
    str_0 = '15:58:59.123'
    time_0 = time_format_0.validate(str_0)

def test_case_5():
    date_time_format_0 = module_0.DateTimeFormat()
    str_0 = '2010-12-26T12:30:06.123456'
    datetime_0 = date_time_format_0.validate(str_0)

def test_case_6():
    date_time_format_0 = module_0.DateTimeFormat()
    str_0 = '2010-12-26T12:30:06'
    datetime_0 = date_time_format_0.validate(str_0)

def test_case_7():
    date_time_format_0 = module_0.DateTimeFormat()
    str_0 = '2010-12-26T12:30:06'
    datetime_0 = date_time_format_0.validate(str_0)
    optional_0 = date_time_format_0.serialize(datetime_0)

def test_case_8():
    date_time_format_0 = module_0.DateTimeFormat()
    str_0 = '2019-12-02T00:00:00.000Z'
    datetime_0 = date_time_format_0.validate(str_0)
    str_1 = '2019-12-02T00:00:00.000+00:00'
    datetime_1 = date_time_format_0.validate(str_1)
    str_2 = '2019-12-02T00:00:00.000+01:00'
    datetime_2 = date_time_format_0.validate(str_2)
    datetime_3 = date_time_format_0.validate(str_2)
    str_3 = '2019-12-02T00:00:00.000-01:00'
    datetime_4 = date_time_format_0.validate(str_3)
    date_format_0 = module_0.DateFormat()

def test_case_9():
    date_time_format_0 = module_0.DateTimeFormat()
    str_0 = '2019-12-02T00:00:00.000Z'
    datetime_0 = date_time_format_0.validate(str_0)
    str_1 = '2019-12-02T00:00:00.000+00:00'
    datetime_1 = date_time_format_0.validate(str_1)
    str_2 = '2019-12-02T00:00:00.000+01:00'
    datetime_2 = date_time_format_0.validate(str_2)
    datetime_3 = date_time_format_0.validate(str_2)
    str_3 = '2019-12-02T00:00:00.000-01:00'
    datetime_4 = date_time_format_0.validate(str_3)
    str_4 = '2019-12-02T00:00:00.000-01'
    datetime_5 = date_time_format_0.validate(str_4)

def test_case_10():
    time_format_0 = module_0.TimeFormat()
    int_0 = 5
    int_1 = 1
    time_0 = module_2.time()
    optional_0 = time_format_0.serialize(time_0)