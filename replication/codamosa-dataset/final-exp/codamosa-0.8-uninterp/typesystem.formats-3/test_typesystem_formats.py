# Automatically generated by Pynguin.
import typesystem.formats as module_0
import datetime as module_1

def test_case_0():
    date_time_format_0 = module_0.DateTimeFormat()

def test_case_1():
    date_time_format_0 = module_0.DateTimeFormat()
    str_0 = '2020-05-12T15:32:38+08:00'
    datetime_0 = date_time_format_0.validate(str_0)

def test_case_2():
    date_time_format_0 = module_0.DateTimeFormat()
    str_0 = '2019-06-06T11:00:00Z'
    datetime_0 = date_time_format_0.validate(str_0)
    optional_0 = date_time_format_0.serialize(datetime_0)

def test_case_3():
    date_time_format_0 = module_0.DateTimeFormat()
    str_0 = '2018-12-13T18:31:07.971151'
    datetime_0 = date_time_format_0.validate(str_0)

def test_case_4():
    date_time_format_0 = module_0.DateTimeFormat()
    str_0 = '2020-05-12T15:32:38+08:00'
    datetime_0 = date_time_format_0.validate(str_0)
    optional_0 = date_time_format_0.serialize(datetime_0)
    date_time_format_1 = module_0.DateTimeFormat()

def test_case_5():
    time_0 = module_1.time()
    time_format_0 = module_0.TimeFormat()
    optional_0 = time_format_0.serialize(time_0)

def test_case_6():
    date_format_0 = module_0.DateFormat()
    var_0 = None
    optional_0 = date_format_0.serialize(var_0)
    date_format_1 = module_0.DateFormat()

def test_case_7():
    time_0 = module_1.time()
    time_format_0 = module_0.TimeFormat()
    optional_0 = time_format_0.serialize(time_0)
    time_format_1 = module_0.TimeFormat()
    var_0 = None
    optional_1 = time_format_1.serialize(var_0)

def test_case_8():
    date_time_format_0 = module_0.DateTimeFormat()
    str_0 = '1946-12-07T00:00:00Z'
    datetime_0 = date_time_format_0.validate(str_0)
    date_time_format_1 = module_0.DateTimeFormat()
    str_1 = '1946-12-07T00:00:00.000000Z'
    datetime_1 = date_time_format_1.validate(str_1)
    date_time_format_2 = module_0.DateTimeFormat()
    str_2 = '1946-12-07T00:00:00.000023Z'
    datetime_2 = date_time_format_2.validate(str_2)
    date_time_format_3 = module_0.DateTimeFormat()
    str_3 = '1946-12-07T00:00:00.000023-03'
    datetime_3 = date_time_format_3.validate(str_3)