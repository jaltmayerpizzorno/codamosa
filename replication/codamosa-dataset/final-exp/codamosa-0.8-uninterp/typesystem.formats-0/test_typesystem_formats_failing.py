# Automatically generated by Pynguin.
import typesystem.formats as module_0

def test_case_0():
    try:
        str_0 = '3`YS:&'
        time_format_0 = module_0.TimeFormat()
        time_0 = time_format_0.validate(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        time_format_0 = module_0.TimeFormat()
        str_0 = 'jinja2.Environment'
        base_format_0 = module_0.BaseFormat()
        bool_0 = base_format_0.is_native_type(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '$/71=7V,DL=}-vCZ*6u'
        set_0 = {str_0, str_0, str_0, str_0}
        base_format_0 = module_0.BaseFormat()
        var_0 = base_format_0.validate(set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        base_format_0 = module_0.BaseFormat()
        str_0 = 'gwGbq]a!He7$nOEe'
        optional_0 = base_format_0.serialize(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '~V\n?+]b'
        date_format_0 = module_0.DateFormat()
        date_0 = date_format_0.validate(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        date_format_0 = module_0.DateFormat()
        base_format_0 = module_0.BaseFormat()
        date_time_format_0 = module_0.DateTimeFormat()
        optional_0 = date_format_0.serialize(base_format_0)
    except BaseException:
        pass

def test_case_6():
    try:
        date_time_format_0 = module_0.DateTimeFormat()
        time_format_0 = module_0.TimeFormat()
        bool_0 = time_format_0.is_native_type(date_time_format_0)
        str_0 = '"gY6F$'
        datetime_0 = date_time_format_0.validate(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        time_format_0 = module_0.TimeFormat()
        optional_0 = time_format_0.serialize(time_format_0)
    except BaseException:
        pass

def test_case_8():
    try:
        date_time_format_0 = module_0.DateTimeFormat()
        optional_0 = date_time_format_0.serialize(date_time_format_0)
    except BaseException:
        pass

def test_case_9():
    try:
        u_u_i_d_format_0 = module_0.UUIDFormat()
        str_0 = '2af3758e-11b1-4c0a-e6a0-45246c08e100'
        u_u_i_d_0 = u_u_i_d_format_0.validate(str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        u_u_i_d_format_0 = module_0.UUIDFormat()
        str_0 = '~V\n?+]b'
        str_1 = u_u_i_d_format_0.serialize(str_0)
        u_u_i_d_0 = u_u_i_d_format_0.validate(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        u_u_i_d_format_0 = module_0.UUIDFormat()
        date_time_format_0 = module_0.DateTimeFormat()
        bool_0 = date_time_format_0.is_native_type(u_u_i_d_format_0)
        str_0 = '~V\n?+]b'
        optional_0 = date_time_format_0.serialize(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        date_time_format_0 = module_0.DateTimeFormat()
        str_0 = '1971-02-13T04:21:00Z'
        datetime_0 = date_time_format_0.validate(str_0)
        set_0 = None
        optional_0 = date_time_format_0.serialize(set_0)
        date_format_0 = module_0.DateFormat()
        date_0 = date_format_0.validate(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        date_time_format_0 = module_0.DateTimeFormat()
        str_0 = "/GA\\e41T'\r&oDZ}[="
        datetime_0 = date_time_format_0.validate(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        base_format_0 = module_0.BaseFormat()
        date_time_format_0 = module_0.DateTimeFormat()
        time_format_0 = None
        date_format_0 = module_0.DateFormat()
        optional_0 = date_format_0.serialize(time_format_0)
        list_0 = [date_time_format_0, optional_0]
        dict_0 = {}
        base_format_1 = module_0.BaseFormat(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_15():
    try:
        date_format_0 = None
        date_0 = None
        time_format_0 = module_0.TimeFormat()
        bool_0 = time_format_0.is_native_type(date_0)
        optional_0 = time_format_0.serialize(date_0)
        date_time_format_0 = module_0.DateTimeFormat()
        bool_1 = date_time_format_0.is_native_type(date_format_0)
        date_1 = date_format_0.validate(date_format_0)
    except BaseException:
        pass

def test_case_16():
    try:
        date_format_0 = module_0.DateFormat()
        str_0 = '2020-01-32'
        date_0 = date_format_0.validate(str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        time_format_0 = module_0.TimeFormat()
        str_0 = '02:22:60'
        time_0 = time_format_0.validate(str_0)
    except BaseException:
        pass

def test_case_18():
    try:
        time_format_0 = module_0.TimeFormat()
        str_0 = '23:59:59.000000'
        time_0 = time_format_0.validate(str_0)
        date_time_format_0 = module_0.DateTimeFormat()
        datetime_0 = date_time_format_0.validate(str_0)
    except BaseException:
        pass

def test_case_19():
    try:
        date_format_0 = module_0.DateFormat()
        str_0 = '2020-05-22'
        date_0 = date_format_0.validate(str_0)
        optional_0 = date_format_0.serialize(date_0)
        time_format_0 = module_0.TimeFormat()
        date_time_format_0 = module_0.DateTimeFormat()
        datetime_0 = date_time_format_0.validate(time_format_0)
    except BaseException:
        pass

def test_case_20():
    try:
        date_time_format_0 = module_0.DateTimeFormat()
        str_0 = '1971-0-13T04:21:00Z'
        datetime_0 = date_time_format_0.validate(str_0)
    except BaseException:
        pass

def test_case_21():
    try:
        date_time_format_0 = module_0.DateTimeFormat()
        str_0 = '1971-02-3T04:21:00'
        datetime_0 = date_time_format_0.validate(str_0)
        optional_0 = date_time_format_0.serialize(str_0)
    except BaseException:
        pass

def test_case_22():
    try:
        date_time_format_0 = module_0.DateTimeFormat()
        str_0 = '1971-02-13T04:21:00'
        datetime_0 = date_time_format_0.validate(str_0)
        str_1 = '1971-02-13T04:21:00+00:00'
        optional_0 = date_time_format_0.serialize(datetime_0)
        date_format_0 = module_0.DateFormat()
        optional_1 = date_format_0.serialize(str_1)
    except BaseException:
        pass