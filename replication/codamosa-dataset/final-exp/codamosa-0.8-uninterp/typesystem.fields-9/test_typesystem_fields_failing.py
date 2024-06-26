# Automatically generated by Pynguin.
import typesystem.fields as module_0
import decimal as module_1

def test_case_0():
    try:
        str_0 = 'X['
        bool_0 = True
        field_0 = module_0.Field()
        validation_result_0 = field_0.validate_or_error(str_0, strict=bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ''
        number_0 = module_0.Number()
        any_0 = number_0.validate(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = None
        dict_0 = {}
        string_0 = module_0.String(**dict_0)
        any_0 = string_0.validate(float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'Hh'
        string_0 = module_0.String(pattern=str_0, format=str_0)
        str_1 = 'AtMFC8e$Ety>@L>'
        any_0 = string_0.validate(str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        date_0 = module_0.Date()
        int_0 = 2838
        str_0 = '5'
        string_0 = module_0.String(max_length=int_0, format=str_0)
        any_0 = string_0.validate(date_0)
    except BaseException:
        pass

def test_case_5():
    try:
        position_0 = None
        boolean_0 = module_0.Boolean()
        any_0 = boolean_0.validate(position_0)
    except BaseException:
        pass

def test_case_6():
    try:
        time_0 = None
        choice_0 = module_0.Choice()
        any_0 = choice_0.validate(time_0)
    except BaseException:
        pass

def test_case_7():
    try:
        integer_0 = module_0.Integer()
        var_0 = [integer_0]
        union_0 = module_0.Union(var_0)
        any_0 = union_0.validate(integer_0)
    except BaseException:
        pass

def test_case_8():
    try:
        time_0 = None
        object_0 = module_0.Object()
        any_0 = module_0.Any()
        any_1 = any_0.validate(time_0)
        any_2 = object_0.validate(time_0)
    except BaseException:
        pass

def test_case_9():
    try:
        integer_0 = None
        bool_0 = False
        const_0 = module_0.Const(integer_0)
        any_0 = const_0.validate(bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        text_0 = module_0.Text()
        const_0 = module_0.Const(text_0)
        const_1 = module_0.Const(text_0)
        any_0 = const_0.validate(const_0)
    except BaseException:
        pass

def test_case_11():
    try:
        dict_0 = {}
        time_0 = module_0.Time(**dict_0)
        const_0 = module_0.Const(time_0)
        str_0 = None
        boolean_0 = module_0.Boolean()
        field_0 = module_0.Field(description=str_0, default=boolean_0)
    except BaseException:
        pass

def test_case_12():
    try:
        date_0 = module_0.Date()
        bool_0 = True
        boolean_0 = module_0.Boolean(default=date_0, allow_null=bool_0)
        any_0 = boolean_0.validate(date_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'aCsSQL^8uPbszb}'
        field_0 = module_0.Field(default=str_0)
        union_0 = field_0.__or__(field_0)
        number_0 = module_0.Number(exclusive_minimum=union_0)
    except BaseException:
        pass

def test_case_14():
    try:
        dict_0 = {}
        int_0 = -21
        str_0 = ''
        list_0 = [str_0]
        object_0 = module_0.Object(max_properties=int_0, required=list_0)
        bool_0 = True
        any_0 = object_0.validate(dict_0, strict=bool_0)
    except BaseException:
        pass

def test_case_15():
    try:
        date_time_0 = module_0.DateTime()
        array_0 = module_0.Array()
        dict_0 = {}
        object_0 = module_0.Object(**dict_0)
        bool_0 = True
        field_0 = module_0.Field(default=array_0, allow_null=bool_0)
        object_1 = module_0.Object(additional_properties=field_0, min_properties=dict_0)
    except BaseException:
        pass

def test_case_16():
    try:
        int_0 = -67
        field_0 = module_0.Field(default=int_0)
        str_0 = 'UXF[\n'
        object_0 = module_0.Object(additional_properties=field_0, required=str_0)
        dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0}
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '1~'
        field_0 = module_0.Field(default=str_0)
        dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
        object_0 = module_0.Object(pattern_properties=dict_0, additional_properties=field_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_18():
    try:
        dict_0 = {}
        date_0 = module_0.Date(**dict_0)
        const_0 = module_0.Const(date_0, **dict_0)
        field_0 = None
        decimal_0 = module_1.Decimal()
        array_0 = module_0.Array(field_0, decimal_0, **dict_0)
    except BaseException:
        pass

def test_case_19():
    try:
        bytes_0 = b';'
        list_0 = [bytes_0, bytes_0]
        array_0 = module_0.Array()
        any_0 = array_0.validate(list_0)
        int_0 = 713
        array_1 = module_0.Array(int_0)
    except BaseException:
        pass

def test_case_20():
    try:
        time_0 = module_0.Time()
        boolean_0 = module_0.Boolean()
        any_0 = boolean_0.validate(time_0)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'test_ch*ice'
        str_1 = [str_0, str_0, str_0, str_0, str_0]
        choice_0 = module_0.Choice(choices=str_1)
        bool_0 = True
        boolean_0 = module_0.Boolean(default=str_1)
        any_0 = boolean_0.validate(choice_0, strict=bool_0)
    except BaseException:
        pass

def test_case_22():
    try:
        int_0 = 1747
        bool_0 = False
        any_0 = module_0.Any(default=bool_0)
        any_1 = any_0.validate(int_0)
        bool_1 = True
        bool_2 = False
        list_0 = [bool_0, any_0]
        dict_0 = {}
        string_0 = module_0.String(allow_blank=bool_2, trim_whitespace=bool_1, min_length=int_0, pattern=list_0, **dict_0)
    except BaseException:
        pass

def test_case_23():
    try:
        int_0 = 2249
        str_0 = 'Hh'
        string_0 = module_0.String(min_length=int_0, pattern=str_0, format=str_0)
        any_0 = string_0.validate(str_0)
    except BaseException:
        pass

def test_case_24():
    try:
        int_0 = 3553
        decimal_0 = module_0.Decimal(minimum=int_0)
        any_0 = decimal_0.serialize(int_0)
        field_0 = module_0.Field(default=int_0)
        str_0 = 't%!\x0cbp&=Nh.km\\\n\nM$'
        object_0 = module_0.Object(additional_properties=field_0, required=str_0)
        dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
        any_1 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_25():
    try:
        number_0 = module_0.Number()
        any_0 = number_0.validate(number_0)
    except BaseException:
        pass

def test_case_26():
    try:
        bool_0 = False
        any_0 = module_0.Any(default=bool_0)
        field_0 = module_0.Field()
        str_0 = None
        field_1 = module_0.Field(title=str_0, default=field_0)
    except BaseException:
        pass

def test_case_27():
    try:
        date_time_0 = None
        dict_0 = {}
        decimal_0 = module_0.Decimal(**dict_0)
        str_0 = 'KF!.:.(;'
        any_0 = decimal_0.serialize(date_time_0)
        boolean_0 = module_0.Boolean(title=str_0)
        bool_0 = True
        string_0 = module_0.String(trim_whitespace=bool_0)
        any_1 = string_0.serialize(any_0)
        field_0 = module_0.Field()
        validation_result_0 = field_0.validate_or_error(dict_0)
    except BaseException:
        pass

def test_case_28():
    try:
        str_0 = 'aCsSQL^8uPbszb}'
        field_0 = module_0.Field(default=str_0)
        dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
        object_0 = module_0.Object(properties=dict_0, additional_properties=field_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_29():
    try:
        decimal_0 = None
        int_0 = 5
        str_0 = '$\\lb&MGO'
        bool_0 = False
        string_0 = module_0.String(trim_whitespace=bool_0, max_length=int_0, min_length=int_0, format=str_0)
        any_0 = string_0.serialize(decimal_0)
        any_1 = string_0.validate(str_0, strict=bool_0)
    except BaseException:
        pass

def test_case_30():
    try:
        time_0 = module_0.Time()
        str_0 = 'UC'
        boolean_0 = module_0.Boolean(description=str_0, default=str_0)
        any_0 = boolean_0.validate(str_0)
    except BaseException:
        pass

def test_case_31():
    try:
        int_0 = -21
        str_0 = 'yU'
        bool_0 = False
        string_0 = module_0.String(trim_whitespace=bool_0, format=str_0)
        any_0 = string_0.validate(str_0, strict=bool_0)
        object_0 = module_0.Object(max_properties=int_0)
        any_1 = object_0.validate(str_0)
    except BaseException:
        pass

def test_case_32():
    try:
        time_0 = None
        object_0 = module_0.Object()
        any_0 = object_0.validate(time_0)
    except BaseException:
        pass

def test_case_33():
    try:
        decimal_0 = None
        int_0 = 5
        bool_0 = False
        dict_0 = {}
        number_0 = module_0.Number(exclusive_maximum=int_0, multiple_of=decimal_0, **dict_0)
        any_0 = number_0.validate(bool_0)
    except BaseException:
        pass

def test_case_34():
    try:
        time_0 = None
        number_0 = module_0.Number()
        any_0 = number_0.validate(time_0)
    except BaseException:
        pass

def test_case_35():
    try:
        bytes_0 = b'\xbe\t'
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
        array_0 = module_0.Array()
        any_0 = array_0.validate(list_0)
        set_0 = {bytes_0, bytes_0}
        str_0 = None
        string_0 = module_0.String(max_length=set_0, format=str_0)
    except BaseException:
        pass

def test_case_36():
    try:
        decimal_0 = None
        dict_0 = {}
        list_0 = [decimal_0, dict_0, dict_0, decimal_0]
        date_0 = module_0.Date(**dict_0)
        array_0 = module_0.Array(list_0, date_0, **dict_0)
    except BaseException:
        pass

def test_case_37():
    try:
        bool_0 = False
        var_0 = None
        float_0 = 1772.84885
        decimal_0 = module_0.Decimal(minimum=var_0, exclusive_minimum=float_0, exclusive_maximum=float_0)
        list_0 = [decimal_0, float_0]
        choice_0 = module_0.Choice(choices=list_0)
        dict_0 = {}
        bool_1 = False
        any_0 = module_0.Any(allow_null=bool_1)
        any_1 = any_0.validate(bool_0)
        float_1 = -3217.771044
        string_0 = module_0.String(format=float_1, **dict_0)
    except BaseException:
        pass

def test_case_38():
    try:
        var_0 = None
        float_0 = 1772.84885
        decimal_0 = module_0.Decimal(minimum=var_0, exclusive_minimum=float_0, exclusive_maximum=float_0)
        list_0 = [decimal_0, float_0]
        choice_0 = module_0.Choice(choices=list_0)
        str_0 = 'AtMFC8e$Ety>@L>'
        time_0 = module_0.Time()
        string_0 = module_0.String(min_length=time_0, pattern=str_0, format=str_0)
    except BaseException:
        pass

def test_case_39():
    try:
        time_0 = module_0.Time()
        object_0 = module_0.Object()
        date_0 = module_0.Date()
        bool_0 = False
        str_0 = ''
        any_0 = module_0.Any(title=str_0, description=str_0)
        any_1 = any_0.validate(str_0, bool_0)
        int_0 = 161
        integer_0 = module_0.Integer(multiple_of=int_0)
        number_0 = module_0.Number(multiple_of=integer_0)
    except BaseException:
        pass

def test_case_40():
    try:
        int_0 = 1726
        bool_0 = True
        string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_0)
        any_0 = string_0.serialize(int_0)
        number_0 = module_0.Number(exclusive_maximum=int_0, multiple_of=int_0)
        any_1 = number_0.validate(int_0)
    except BaseException:
        pass

def test_case_41():
    try:
        int_0 = 2270
        str_0 = 'J^;5V'
        number_0 = module_0.Number(exclusive_minimum=int_0, precision=str_0)
        any_0 = number_0.validate(int_0)
    except BaseException:
        pass

def test_case_42():
    try:
        number_0 = module_0.Number()
        number_1 = [number_0]
        array_0 = module_0.Array(number_1)
        bool_0 = True
        any_0 = array_0.validate(number_1, strict=bool_0)
    except BaseException:
        pass

def test_case_43():
    try:
        text_0 = module_0.Text()
        bool_0 = True
        const_0 = module_0.Const(bool_0)
        choice_0 = module_0.Choice()
        object_0 = module_0.Object(properties=const_0, required=choice_0)
    except BaseException:
        pass

def test_case_44():
    try:
        bytes_0 = b'\x8e\xba\x91_\xf8\xb6E\x17iq\x8b\xa2$\r'
        list_0 = [bytes_0, bytes_0]
        array_0 = module_0.Array()
        any_0 = array_0.validate(list_0)
        number_0 = module_0.Number()
        int_0 = 59
        bytes_1 = b'\xffz\xec0\x92m3\xdf\xa3\x01\xa8'
        object_0 = module_0.Object(min_properties=int_0, required=bytes_1)
    except BaseException:
        pass

def test_case_45():
    try:
        int_0 = 44
        number_0 = module_0.Number(exclusive_minimum=int_0)
        any_0 = number_0.validate(int_0)
    except BaseException:
        pass

def test_case_46():
    try:
        dict_0 = {}
        text_0 = module_0.Text(**dict_0)
        float_0 = -2341.1
        number_0 = module_0.Number(maximum=text_0, exclusive_minimum=float_0)
    except BaseException:
        pass

def test_case_47():
    try:
        str_0 = 'jGL&GSA=&'
        bool_0 = True
        bool_1 = True
        bool_2 = True
        dict_0 = {}
        string_0 = module_0.String(allow_blank=bool_1, trim_whitespace=bool_2, **dict_0)
        any_0 = string_0.validate(str_0, strict=bool_0)
        decimal_0 = module_0.Decimal(minimum=str_0, precision=str_0)
    except BaseException:
        pass

def test_case_48():
    try:
        str_0 = ''
        string_0 = module_0.String(pattern=str_0)
        any_0 = string_0.validate(str_0)
    except BaseException:
        pass

def test_case_49():
    try:
        dict_0 = {}
        int_0 = 2
        str_0 = ''
        object_0 = module_0.Object(pattern_properties=str_0, min_properties=int_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_50():
    try:
        number_0 = []
        array_0 = module_0.Array(number_0)
        any_0 = array_0.validate(array_0)
    except BaseException:
        pass

def test_case_51():
    try:
        time_0 = None
        array_0 = module_0.Array()
        any_0 = array_0.validate(time_0)
    except BaseException:
        pass

def test_case_52():
    try:
        str_0 = 'aCsSQL^8uPbszb}'
        field_0 = module_0.Field(default=str_0)
        dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
        object_0 = module_0.Object(pattern_properties=dict_0, additional_properties=field_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_53():
    try:
        int_0 = 5
        bool_0 = True
        int_1 = 3580
        field_0 = module_0.Field(allow_null=bool_0)
        bool_1 = False
        number_0 = module_0.Number(exclusive_maximum=int_1, multiple_of=int_1)
        any_0 = number_0.validate(int_0, strict=bool_1)
    except BaseException:
        pass

def test_case_54():
    try:
        int_0 = 1747
        float_0 = 1359.94714
        number_0 = module_0.Number(minimum=int_0, maximum=int_0, multiple_of=float_0)
        any_0 = number_0.validate(float_0)
    except BaseException:
        pass

def test_case_55():
    try:
        int_0 = -51
        field_0 = module_0.Field(default=int_0)
        bool_0 = field_0.has_default()
        str_0 = 'Z7SXHN!OSE'
        object_0 = module_0.Object(additional_properties=field_0, max_properties=int_0, required=str_0)
        dict_0 = {str_0: field_0}
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_56():
    try:
        number_0 = module_0.Number()
        date_time_0 = module_0.DateTime()
        number_1 = [number_0]
        array_0 = module_0.Array(date_time_0)
        any_0 = array_0.validate(number_1)
    except BaseException:
        pass

def test_case_57():
    try:
        number_0 = module_0.Number()
        number_1 = [number_0]
        array_0 = module_0.Array(number_1)
        any_0 = array_0.validate(number_1)
    except BaseException:
        pass

def test_case_58():
    try:
        str_0 = ''
        str_1 = '+'
        field_0 = module_0.Field(description=str_0)
        str_2 = None
        str_3 = 'SlS}K\tkS/j_`q_z?a0'
        dict_0 = {str_1: field_0, str_2: field_0, str_2: field_0, str_3: field_0}
        dict_1 = {}
        object_0 = module_0.Object(properties=dict_0, **dict_1)
    except BaseException:
        pass

def test_case_59():
    try:
        dict_0 = {}
        int_0 = -21
        str_0 = ''
        decimal_0 = module_0.Decimal(minimum=int_0, multiple_of=int_0, **dict_0)
        list_0 = [str_0, dict_0, decimal_0]
        object_0 = module_0.Object(additional_properties=list_0, required=str_0, **dict_0)
    except BaseException:
        pass

def test_case_60():
    try:
        str_0 = 'laCsSQL^8uPbsz}'
        field_0 = module_0.Field(default=str_0)
        dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
        int_0 = -715
        object_0 = module_0.Object(min_properties=int_0)
        dict_1 = {field_0: dict_0, str_0: str_0}
        any_0 = object_0.validate(dict_1)
    except BaseException:
        pass

def test_case_61():
    try:
        any_0 = module_0.Any()
        integer_0 = module_0.Integer()
        var_0 = [any_0, integer_0]
        union_0 = module_0.Union(var_0)
        list_0 = []
        field_0 = module_0.Field(default=union_0)
        bool_0 = True
        array_0 = module_0.Array(list_0, field_0, bool_0)
        any_1 = array_0.validate(any_0)
    except BaseException:
        pass

def test_case_62():
    try:
        dict_0 = {}
        str_0 = '6'
        field_0 = module_0.Field(description=str_0)
        dict_1 = {str_0: field_0, str_0: field_0}
        object_0 = module_0.Object(properties=dict_1, pattern_properties=dict_1, property_names=field_0, **dict_0)
        any_0 = object_0.validate(dict_1)
    except BaseException:
        pass

def test_case_63():
    try:
        int_0 = -21
        str_0 = '_ja\nFm|Q+\n$N.P'
        field_0 = None
        dict_0 = {str_0: field_0, str_0: field_0}
        bytes_0 = b'\xd8_\xfe)\x84\xf9F'
        object_0 = module_0.Object(pattern_properties=dict_0, max_properties=int_0, required=bytes_0)
    except BaseException:
        pass

def test_case_64():
    try:
        str_0 = "'0mzgQ"
        any_0 = module_0.Any(title=str_0)
        bool_0 = False
        int_0 = -217
        string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_0, max_length=int_0, min_length=int_0)
        any_1 = string_0.serialize(any_0)
        str_1 = '}$f[u\tqp[(7=u\t}*?}'
        float_0 = module_0.Float(exclusive_maximum=str_1, precision=str_1)
    except BaseException:
        pass

def test_case_65():
    try:
        str_0 = '6'
        bool_0 = None
        field_0 = module_0.Field(allow_null=bool_0)
        field_1 = module_0.Field(description=str_0)
        dict_0 = {str_0: field_1, str_0: field_1}
        bool_1 = False
        object_0 = module_0.Object(additional_properties=bool_1)
        any_0 = object_0.validate(dict_0, strict=bool_0)
    except BaseException:
        pass

def test_case_66():
    try:
        number_0 = module_0.Number()
        dict_0 = {}
        const_0 = module_0.Const(number_0, **dict_0)
        object_0 = module_0.Object(max_properties=const_0)
    except BaseException:
        pass

def test_case_67():
    try:
        dict_0 = {}
        int_0 = 27
        str_0 = '6'
        number_0 = module_0.Number(exclusive_maximum=int_0, **dict_0)
        number_1 = module_0.Number(exclusive_minimum=int_0, exclusive_maximum=int_0, precision=str_0)
        any_0 = number_1.validate(int_0)
    except BaseException:
        pass

def test_case_68():
    try:
        int_0 = 2
        object_0 = module_0.Object(max_properties=int_0)
        dict_0 = {}
        str_0 = '\\~\ruwfX<8w)\\'
        field_0 = None
        str_1 = 'B3*;y'
        dict_1 = {str_0: field_0, str_1: field_0, str_0: field_0}
        choice_0 = module_0.Choice(**dict_0)
        object_1 = module_0.Object(properties=dict_1, pattern_properties=dict_1, min_properties=int_0, required=choice_0)
    except BaseException:
        pass

def test_case_69():
    try:
        decimal_0 = None
        int_0 = 5
        str_0 = '$\\lb&MGO'
        bool_0 = False
        string_0 = module_0.String(trim_whitespace=bool_0, max_length=int_0, min_length=int_0, format=str_0)
        any_0 = string_0.serialize(decimal_0)
        str_1 = 'AtMFC8e$Ety>@L>'
        field_0 = module_0.Field(title=str_1, default=any_0)
        str_2 = '_{;I:PM6\tN79j Ea.\\'
        str_3 = None
        dict_0 = {str_1: field_0, str_2: field_0, str_2: field_0, str_3: field_0}
        dict_1 = {}
        object_0 = module_0.Object(pattern_properties=dict_0, **dict_1)
    except BaseException:
        pass

def test_case_70():
    try:
        bool_0 = False
        date_time_0 = module_0.DateTime()
        field_0 = module_0.Field()
        int_0 = -894
        array_0 = module_0.Array(field_0, bool_0, date_time_0, int_0)
    except BaseException:
        pass

def test_case_71():
    try:
        dict_0 = {}
        int_0 = 1
        str_0 = ''
        object_0 = module_0.Object(pattern_properties=str_0, min_properties=int_0, **dict_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_72():
    try:
        int_0 = -988
        field_0 = module_0.Field(default=int_0)
        str_0 = 'S'
        object_0 = module_0.Object(additional_properties=field_0, required=str_0)
        dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0}
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_73():
    try:
        float_0 = 421.9
        number_0 = module_0.Number(minimum=float_0, multiple_of=float_0)
        bool_0 = True
        any_0 = number_0.validate(float_0, strict=bool_0)
    except BaseException:
        pass

def test_case_74():
    try:
        int_0 = -21
        float_0 = 1359.94714
        number_0 = module_0.Number(minimum=int_0, maximum=int_0, multiple_of=float_0)
        any_0 = number_0.validate(float_0)
    except BaseException:
        pass

def test_case_75():
    try:
        dict_0 = None
        bool_0 = True
        boolean_0 = module_0.Boolean(allow_null=bool_0)
        any_0 = boolean_0.validate(dict_0)
        text_0 = module_0.Text(**dict_0)
    except BaseException:
        pass

def test_case_76():
    try:
        str_0 = ''
        bool_0 = True
        boolean_0 = module_0.Boolean(allow_null=bool_0)
        any_0 = boolean_0.validate(str_0)
        str_1 = '.O'
        dict_0 = {str_1: str_0, str_1: any_0, str_0: str_0, str_0: str_0}
        decimal_0 = module_0.Decimal(**dict_0)
    except BaseException:
        pass

def test_case_77():
    try:
        time_0 = None
        number_0 = module_0.Number(maximum=time_0)
        str_0 = '~me/1CVT{PF*-)z3wy%'
        bool_0 = True
        field_0 = module_0.Field(description=str_0, default=number_0, allow_null=bool_0)
        list_0 = [field_0]
        union_0 = module_0.Union(list_0)
        any_0 = union_0.validate(time_0)
        any_1 = number_0.validate(any_0)
    except BaseException:
        pass

def test_case_78():
    try:
        float_0 = None
        bool_0 = False
        str_0 = '_~R"Z4k'
        field_0 = module_0.Field(title=str_0)
        str_1 = '>nVx|FBL_Xw'
        field_1 = module_0.Field(title=str_1, description=str_1, default=str_1)
        union_0 = field_1.__or__(field_0)
        any_0 = union_0.validate(float_0, bool_0)
    except BaseException:
        pass

def test_case_79():
    try:
        str_0 = 'aCsSL^8.uPbszb}'
        bool_0 = True
        any_0 = module_0.Any(allow_null=bool_0)
        int_0 = 832
        object_0 = module_0.Object(property_names=any_0, min_properties=int_0)
        field_0 = module_0.Field(default=str_0)
        dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
        object_1 = module_0.Object(properties=dict_0, additional_properties=field_0)
        any_1 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_80():
    try:
        number_0 = []
        array_0 = module_0.Array(number_0)
        any_0 = array_0.serialize(array_0)
    except BaseException:
        pass

def test_case_81():
    try:
        number_0 = []
        list_0 = [number_0]
        dict_0 = {}
        choice_0 = module_0.Choice(choices=list_0, **dict_0)
    except BaseException:
        pass

def test_case_82():
    try:
        number_0 = module_0.Number()
        number_1 = [number_0]
        array_0 = module_0.Array(number_1)
        int_0 = 29
        int_1 = [int_0, int_0]
        bool_0 = False
        any_0 = array_0.validate(int_1, strict=bool_0)
    except BaseException:
        pass

def test_case_83():
    try:
        integer_0 = module_0.Integer()
        date_time_0 = module_0.DateTime()
        var_0 = [integer_0]
        union_0 = module_0.Union(var_0)
        str_0 = '$^ZlxA_'
        str_1 = 'D'
        field_0 = module_0.Field(title=str_0, description=str_1)
        bool_0 = False
        array_0 = module_0.Array(field_0, field_0, bool_0)
        any_0 = array_0.validate(var_0)
    except BaseException:
        pass

def test_case_84():
    try:
        time_0 = module_0.Time()
        list_0 = []
        str_0 = 'XzJ#\nCcyc\r%\t]T'
        field_0 = module_0.Field(description=str_0, default=str_0)
        array_0 = module_0.Array(field_0)
        bool_0 = True
        array_1 = module_0.Array(field_0, array_0, bool_0)
        any_0 = array_1.validate(list_0)
    except BaseException:
        pass

def test_case_85():
    try:
        str_0 = 'cCsSQf^8u3bSszLE}'
        field_0 = module_0.Field(default=str_0)
        dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
        object_0 = module_0.Object(pattern_properties=dict_0, additional_properties=field_0)
        int_0 = 5
        bool_0 = True
        array_0 = module_0.Array(field_0, field_0, int_0, bool_0)
        list_0 = [object_0, field_0, str_0]
        bool_1 = False
        any_0 = array_0.validate(list_0, strict=bool_1)
    except BaseException:
        pass

def test_case_86():
    try:
        integer_0 = module_0.Integer()
        number_0 = module_0.Number()
        number_1 = module_0.Number()
        var_0 = [integer_0, number_1]
        union_0 = module_0.Union(var_0)
        float_0 = 3.1
        any_0 = union_0.validate(float_0)
        number_2 = module_0.Number()
        var_1 = [integer_0, number_2]
        union_1 = module_0.Union(var_1)
        var_2 = error.messages()[any_0]
    except BaseException:
        pass