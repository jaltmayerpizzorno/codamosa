# Automatically generated by Pynguin.
import typesystem.fields as module_0
import decimal as module_1

def test_case_0():
    try:
        array_0 = module_0.Array()
        bool_0 = True
        any_0 = module_0.Any(allow_null=bool_0)
        any_1 = array_0.validate(array_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'Uwk'
        field_0 = module_0.Field()
        dict_0 = {str_0: field_0}
        object_0 = module_0.Object(pattern_properties=dict_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        integer_0 = module_0.Integer()
        var_0 = [integer_0]
        array_0 = module_0.Array(var_0)
        any_0 = array_0.validate(var_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_0)
        any_0 = string_0.validate(bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        array_0 = module_0.Array()
        any_0 = array_0.validate(array_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 219
        number_0 = module_0.Number(minimum=int_0, maximum=int_0, exclusive_maximum=int_0)
        any_0 = number_0.validate(int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 1882
        number_0 = module_0.Number(exclusive_minimum=int_0, multiple_of=int_0)
        any_0 = number_0.validate(number_0)
    except BaseException:
        pass

def test_case_7():
    try:
        number_0 = module_0.Number()
        bool_0 = False
        any_0 = number_0.validate(number_0, strict=bool_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'b'
        boolean_0 = module_0.Boolean()
        any_0 = boolean_0.validate(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = -2620.77
        bool_0 = True
        boolean_0 = module_0.Boolean(allow_null=bool_0)
        any_0 = boolean_0.validate(bool_0, strict=bool_0)
        any_1 = boolean_0.validate(float_0)
    except BaseException:
        pass

def test_case_10():
    try:
        sequence_0 = None
        choice_0 = module_0.Choice(choices=sequence_0)
        any_0 = choice_0.validate(sequence_0)
    except BaseException:
        pass

def test_case_11():
    try:
        choice_0 = module_0.Choice()
        const_0 = module_0.Const(choice_0)
        any_0 = choice_0.validate(choice_0)
    except BaseException:
        pass

def test_case_12():
    try:
        time_0 = module_0.Time()
        const_0 = module_0.Const(time_0)
        str_0 = '7r>ePY;I'
        dict_0 = {str_0: str_0, str_0: str_0}
        const_1 = module_0.Const(str_0, **dict_0)
    except BaseException:
        pass

def test_case_13():
    try:
        date_time_0 = module_0.DateTime()
        list_0 = []
        union_0 = module_0.Union(list_0)
        any_0 = union_0.validate(date_time_0)
    except BaseException:
        pass

def test_case_14():
    try:
        decimal_0 = None
        bool_0 = False
        str_0 = '7o\\Ilf'
        field_0 = module_0.Field(title=str_0)
        list_0 = [field_0, field_0, field_0]
        union_0 = module_0.Union(list_0)
        any_0 = union_0.validate(decimal_0, bool_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '7r>ePY;I'
        dict_0 = {str_0: str_0, str_0: str_0}
        const_0 = module_0.Const(str_0, **dict_0)
    except BaseException:
        pass

def test_case_16():
    try:
        array_0 = module_0.Array()
        bool_0 = True
        const_0 = module_0.Const(array_0)
        any_0 = const_0.validate(array_0, bool_0)
        any_1 = array_0.validate(array_0)
    except BaseException:
        pass

def test_case_17():
    try:
        bool_0 = None
        field_0 = module_0.Field(allow_null=bool_0)
        str_0 = None
        bool_1 = False
        field_1 = module_0.Field(title=str_0, default=str_0, allow_null=bool_1)
    except BaseException:
        pass

def test_case_18():
    try:
        bool_0 = False
        str_0 = ''
        int_0 = 1404
        string_0 = module_0.String(trim_whitespace=bool_0, max_length=int_0)
        any_0 = string_0.validate(str_0, strict=bool_0)
    except BaseException:
        pass

def test_case_19():
    try:
        int_0 = 5
        bytes_0 = b'k\x97\xd4\xeb\x07\x95;'
        string_0 = module_0.String(min_length=int_0)
        number_0 = module_0.Number(exclusive_maximum=int_0, precision=bytes_0)
        any_0 = number_0.validate(int_0)
    except BaseException:
        pass

def test_case_20():
    try:
        float_0 = 1585.50409
        bool_0 = None
        const_0 = module_0.Const(float_0)
        any_0 = const_0.validate(float_0, bool_0)
        integer_0 = module_0.Integer(exclusive_minimum=float_0)
        decimal_0 = module_0.Decimal(multiple_of=integer_0)
    except BaseException:
        pass

def test_case_21():
    try:
        dict_0 = {}
        bool_0 = True
        boolean_0 = module_0.Boolean(allow_null=bool_0)
        array_0 = module_0.Array(**dict_0)
        any_0 = boolean_0.validate(array_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = 'BkT6y;hBu\tRuw$mtnZ#'
        date_time_0 = module_0.DateTime()
        any_0 = module_0.Any(description=str_0)
        any_1 = any_0.validate(str_0)
        str_1 = None
        any_2 = any_0.validate(date_time_0)
        bool_0 = True
        field_0 = module_0.Field(allow_null=bool_0)
        str_2 = 'v\nw3(#_]|'
        dict_0 = {str_1: field_0, str_2: field_0}
        set_0 = set()
        object_0 = module_0.Object(pattern_properties=dict_0, additional_properties=bool_0, property_names=field_0, required=set_0)
    except BaseException:
        pass

def test_case_23():
    try:
        bool_0 = True
        string_0 = module_0.String(allow_blank=bool_0)
        array_0 = module_0.Array(bool_0)
    except BaseException:
        pass

def test_case_24():
    try:
        integer_0 = module_0.Integer()
        str_0 = 'N\rVd5?Ut'
        field_0 = module_0.Field(title=str_0)
        union_0 = integer_0.__or__(field_0)
        any_0 = union_0.validate(str_0)
    except BaseException:
        pass

def test_case_25():
    try:
        int_0 = 5
        bytes_0 = b'+\x87o\x86H,\x13\xa2\xc6\x1a\n'
        number_0 = module_0.Number(exclusive_maximum=int_0, precision=bytes_0)
        any_0 = number_0.validate(int_0)
    except BaseException:
        pass

def test_case_26():
    try:
        union_0 = None
        decimal_0 = module_0.Decimal()
        any_0 = decimal_0.serialize(union_0)
        field_0 = module_0.Field()
        bool_0 = field_0.has_default()
        date_0 = module_0.Date()
        list_0 = []
        decimal_1 = module_1.Decimal(*list_0)
        number_0 = module_0.Number(minimum=list_0, multiple_of=decimal_1)
    except BaseException:
        pass

def test_case_27():
    try:
        var_0 = None
        object_0 = module_0.Object()
        any_0 = object_0.validate(var_0)
    except BaseException:
        pass

def test_case_28():
    try:
        str_0 = 'KS'
        string_0 = module_0.String(format=str_0)
        any_0 = string_0.validate(str_0)
        const_0 = module_0.Const(string_0)
        any_1 = const_0.validate(any_0)
    except BaseException:
        pass

def test_case_29():
    try:
        str_0 = 'DT;hK(,LdzuIW6}\\&qGu'
        number_0 = module_0.Number(precision=str_0)
        any_0 = number_0.validate(str_0)
    except BaseException:
        pass

def test_case_30():
    try:
        integer_0 = module_0.Integer()
        dict_0 = {}
        const_0 = module_0.Const(integer_0, **dict_0)
        str_0 = '\n    Parse and validate a YAML string, returning positionally marked error\n    messages on parse or validation failures.\n\n    content - A YAML string or bytestring.\n    validator - A Field instance or Schema class to validate against.\n\n    Returns a two-tuple of (value, error_messages)\n    '
        bool_0 = True
        field_0 = module_0.Field(title=str_0, allow_null=bool_0)
        union_0 = integer_0.__or__(field_0)
        bool_1 = True
        bool_2 = True
        any_0 = union_0.validate(bool_1, bool_2)
    except BaseException:
        pass

def test_case_31():
    try:
        dict_0 = {}
        object_0 = module_0.Object(**dict_0)
        bool_0 = True
        choice_0 = module_0.Choice()
        any_0 = object_0.validate(choice_0, strict=bool_0)
    except BaseException:
        pass

def test_case_32():
    try:
        str_0 = None
        any_0 = module_0.Any()
        bool_0 = True
        field_0 = module_0.Field(description=str_0, default=str_0, allow_null=bool_0)
    except BaseException:
        pass

def test_case_33():
    try:
        array_0 = module_0.Array()
        bool_0 = None
        bool_1 = True
        object_0 = module_0.Object(additional_properties=bool_0, max_properties=bool_1)
        any_0 = object_0.validate(bool_0)
    except BaseException:
        pass

def test_case_34():
    try:
        dict_0 = {}
        int_0 = 125
        object_0 = module_0.Object(min_properties=int_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_35():
    try:
        decimal_0 = module_1.Decimal()
        object_0 = module_0.Object(max_properties=decimal_0)
    except BaseException:
        pass

def test_case_36():
    try:
        bool_0 = True
        pattern_0 = None
        string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_0, pattern=pattern_0)
        boolean_0 = module_0.Boolean()
        any_0 = boolean_0.validate(string_0, strict=bool_0)
    except BaseException:
        pass

def test_case_37():
    try:
        text_0 = module_0.Text()
        int_0 = 610
        str_0 = 'Mtg8uHkJx}eipcgl2'
        bool_0 = None
        field_0 = module_0.Field(title=str_0, allow_null=bool_0)
        dict_0 = {}
        union_0 = field_0.__or__(field_0)
        string_0 = module_0.String(allow_blank=bool_0, max_length=int_0, pattern=field_0, **dict_0)
    except BaseException:
        pass

def test_case_38():
    try:
        bool_0 = False
        field_0 = module_0.Field(default=bool_0)
        str_0 = '\\\x0c#u[#V_#'
        str_1 = 'o8@OKK4bDRz(z@3+%Z'
        any_0 = module_0.Any(title=str_0, description=str_1)
        int_0 = 0
        string_0 = module_0.String(max_length=any_0, min_length=int_0)
    except BaseException:
        pass

def test_case_39():
    try:
        bool_0 = True
        any_0 = module_0.Any(allow_null=bool_0)
        set_0 = {bool_0, any_0}
        str_0 = '^O@&L8bTM$'
        field_0 = module_0.Field(title=str_0)
        dict_0 = {}
        decimal_0 = module_1.Decimal(**dict_0)
        decimal_1 = module_0.Decimal(maximum=set_0, exclusive_minimum=decimal_0, **dict_0)
    except BaseException:
        pass

def test_case_40():
    try:
        bool_0 = True
        any_0 = module_0.Any()
        str_0 = 'uJmv2%\t'
        string_0 = module_0.String(trim_whitespace=bool_0, pattern=str_0)
        any_1 = string_0.validate(str_0)
    except BaseException:
        pass

def test_case_41():
    try:
        str_0 = 'uJmv2%\t'
        bool_0 = True
        string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_0, format=str_0)
        str_1 = 'DA.QxlvDthkET?nh'
        field_0 = None
        str_2 = '{| |/DEz9'
        str_3 = '=X%hL2B66S1fcC'
        dict_0 = {str_1: field_0, str_2: field_0, str_3: field_0}
        dict_1 = {}
        dict_2 = {}
        object_0 = module_0.Object(properties=dict_0, required=dict_1, **dict_2)
    except BaseException:
        pass

def test_case_42():
    try:
        str_0 = "Nx*\x0b,>'q>\rqZ_"
        bool_0 = None
        field_0 = module_0.Field(description=str_0, allow_null=bool_0)
        dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0}
        object_0 = module_0.Object(properties=dict_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_43():
    try:
        int_0 = 66
        int_1 = [int_0, int_0, int_0, int_0, int_0, int_0, int_0]
        choice_0 = module_0.Choice(choices=int_1)
        any_0 = choice_0.validate(int_0)
        str_0 = 'b\x0b%KPy+ma$bE>&p UUJ'
        field_0 = module_0.Field(description=str_0)
        field_1 = module_0.Field(default=int_1)
        union_0 = field_1.__or__(field_0)
        object_0 = module_0.Object(properties=union_0, additional_properties=field_0, min_properties=int_1)
    except BaseException:
        pass

def test_case_44():
    try:
        bool_0 = False
        int_0 = -3205
        boolean_0 = module_0.Boolean()
        string_0 = module_0.String(trim_whitespace=bool_0, min_length=int_0, format=boolean_0)
    except BaseException:
        pass

def test_case_45():
    try:
        array_0 = module_0.Array()
        any_0 = array_0.serialize(array_0)
        decimal_0 = None
        number_0 = module_0.Number(minimum=decimal_0)
        const_0 = module_0.Const(decimal_0)
        string_0 = module_0.String(min_length=const_0)
    except BaseException:
        pass

def test_case_46():
    try:
        dict_0 = {}
        str_0 = None
        field_0 = module_0.Field()
        str_1 = 'bJ'
        object_0 = module_0.Object(property_names=field_0)
        any_0 = object_0.validate(dict_0)
        time_0 = module_0.Time()
        date_0 = module_0.Date()
        boolean_0 = module_0.Boolean(description=str_1)
        boolean_1 = module_0.Boolean(title=str_1)
        int_0 = 779
        dict_1 = {str_0: field_0}
        object_1 = module_0.Object(properties=dict_1, max_properties=int_0)
    except BaseException:
        pass

def test_case_47():
    try:
        number_0 = None
        boolean_0 = module_0.Boolean()
        any_0 = boolean_0.validate(number_0)
    except BaseException:
        pass

def test_case_48():
    try:
        dict_0 = {}
        float_0 = module_0.Float(**dict_0)
        field_0 = module_0.Field()
        str_0 = 'bJ'
        object_0 = module_0.Object(property_names=field_0)
        bool_0 = field_0.has_default()
        time_0 = module_0.Time()
        boolean_0 = module_0.Boolean(title=str_0)
        object_1 = module_0.Object(properties=boolean_0)
        date_0 = module_0.Date(**dict_0)
        int_0 = -1534
        number_0 = module_0.Number(exclusive_maximum=date_0, precision=str_0, multiple_of=int_0)
    except BaseException:
        pass

def test_case_49():
    try:
        str_0 = 'k'
        string_0 = module_0.String(format=str_0)
        choice_0 = module_0.Choice()
        array_0 = module_0.Array(choice_0, string_0)
        any_0 = array_0.validate(string_0)
    except BaseException:
        pass

def test_case_50():
    try:
        float_0 = None
        number_0 = module_0.Number(exclusive_minimum=float_0)
        any_0 = number_0.validate(float_0)
    except BaseException:
        pass

def test_case_51():
    try:
        string_0 = module_0.String()
        integer_0 = module_0.Integer()
        array_0 = module_0.Array(string_0)
        any_0 = array_0.validate(array_0)
    except BaseException:
        pass

def test_case_52():
    try:
        int_0 = 88
        const_0 = module_0.Const(int_0)
        object_0 = module_0.Object(property_names=const_0)
        text_0 = module_0.Text()
        dict_0 = {int_0: text_0, int_0: object_0, text_0: object_0}
        bool_0 = True
        any_0 = object_0.validate(dict_0, strict=bool_0)
    except BaseException:
        pass

def test_case_53():
    try:
        int_0 = 490
        decimal_0 = module_1.Decimal()
        number_0 = module_0.Number(minimum=decimal_0, maximum=decimal_0, multiple_of=decimal_0)
        str_0 = '^,lxY'
        field_0 = module_0.Field(default=number_0)
        dict_0 = {str_0: field_0}
        object_0 = module_0.Object(properties=dict_0, pattern_properties=dict_0, property_names=field_0, max_properties=int_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_54():
    try:
        int_0 = 501
        decimal_0 = module_1.Decimal()
        number_0 = module_0.Number(minimum=decimal_0, maximum=decimal_0, multiple_of=decimal_0)
        str_0 = '^,lFxY'
        field_0 = module_0.Field(default=number_0)
        dict_0 = {str_0: field_0}
        object_0 = module_0.Object(properties=dict_0, pattern_properties=dict_0, property_names=field_0, max_properties=int_0)
        object_1 = module_0.Object(properties=dict_0, additional_properties=field_0, property_names=object_0, max_properties=int_0)
        any_0 = object_1.validate(dict_0)
    except BaseException:
        pass

def test_case_55():
    try:
        bool_0 = True
        field_0 = module_0.Field(allow_null=bool_0)
        str_0 = '(-?(?:0|[1-9]\\d*))(\\.\\d+)?([eE][-+]?\\d+)?'
        field_1 = module_0.Field(description=str_0)
        bytes_0 = b'\xa4F\x9cX_\x8c\x08!-c\x9d\x15\xc9QZI\x0e\xa0\xb5'
        int_0 = -3725
        array_0 = module_0.Array(field_1, bytes_0, int_0)
    except BaseException:
        pass

def test_case_56():
    try:
        int_0 = 1882
        number_0 = module_0.Number(minimum=int_0, maximum=int_0, exclusive_minimum=int_0, exclusive_maximum=int_0)
        any_0 = number_0.validate(int_0)
    except BaseException:
        pass

def test_case_57():
    try:
        int_0 = 6148
        decimal_0 = module_1.Decimal()
        number_0 = module_0.Number(exclusive_minimum=int_0)
        any_0 = number_0.validate(decimal_0)
    except BaseException:
        pass

def test_case_58():
    try:
        string_0 = module_0.String()
        integer_0 = module_0.Integer()
        var_0 = [string_0, string_0, integer_0, integer_0]
        array_0 = module_0.Array(var_0)
        field_0 = module_0.Field()
        const_0 = module_0.Const(string_0)
        str_0 = '/G7)(As\t?Ee'
        field_1 = module_0.Field(default=array_0)
        dict_0 = {str_0: field_1}
        int_0 = -4189
        set_0 = {string_0, string_0, field_1}
        object_0 = module_0.Object(properties=const_0, pattern_properties=dict_0, min_properties=int_0, max_properties=int_0, required=set_0)
    except BaseException:
        pass

def test_case_59():
    try:
        float_0 = None
        number_0 = module_0.Number(exclusive_minimum=float_0)
        str_0 = ' y\tqY'
        string_0 = module_0.String(format=str_0)
        any_0 = string_0.validate(float_0)
    except BaseException:
        pass

def test_case_60():
    try:
        number_0 = module_0.Number()
        bool_0 = True
        any_0 = number_0.validate(number_0, strict=bool_0)
    except BaseException:
        pass

def test_case_61():
    try:
        dict_0 = {}
        decimal_0 = module_1.Decimal(**dict_0)
        number_0 = module_0.Number(minimum=decimal_0, exclusive_minimum=decimal_0)
        bool_0 = False
        set_0 = {bool_0, number_0}
        int_0 = -1212
        array_0 = module_0.Array(number_0, bool_0, set_0, int_0)
    except BaseException:
        pass

def test_case_62():
    try:
        dict_0 = {}
        object_0 = module_0.Object(**dict_0)
        str_0 = '`)tjS)\t`'
        float_0 = 3341.700147
        number_0 = module_0.Number(exclusive_minimum=str_0, exclusive_maximum=dict_0, precision=str_0, multiple_of=float_0)
    except BaseException:
        pass

def test_case_63():
    try:
        dict_0 = {}
        object_0 = module_0.Object(**dict_0)
        bool_0 = True
        boolean_0 = module_0.Boolean(default=object_0, allow_null=bool_0)
        text_0 = module_0.Text()
        float_0 = 797.92025
        number_0 = module_0.Number(maximum=float_0, exclusive_maximum=float_0, **dict_0)
        bool_1 = False
        int_0 = 2543
        string_0 = module_0.String(allow_blank=bool_1, max_length=int_0, min_length=int_0, **dict_0)
        field_0 = module_0.Field()
        tuple_0 = (object_0, field_0)
        object_1 = module_0.Object(min_properties=int_0, required=tuple_0)
    except BaseException:
        pass

def test_case_64():
    try:
        str_0 = 'K/]=3Qb'
        int_0 = 1875
        number_0 = module_0.Number(maximum=int_0, exclusive_minimum=int_0, multiple_of=int_0)
        bool_0 = True
        string_0 = module_0.String(trim_whitespace=bool_0, min_length=int_0)
        any_0 = string_0.validate(str_0)
    except BaseException:
        pass

def test_case_65():
    try:
        dict_0 = {}
        str_0 = '*\r=)'
        field_0 = None
        dict_1 = {str_0: field_0}
        object_0 = module_0.Object(pattern_properties=dict_1, additional_properties=field_0, min_properties=dict_0, max_properties=field_0)
    except BaseException:
        pass

def test_case_66():
    try:
        str_0 = ''
        dict_0 = {}
        number_0 = module_0.Number(**dict_0)
        any_0 = number_0.validate(str_0)
    except BaseException:
        pass

def test_case_67():
    try:
        field_0 = module_0.Field()
        any_0 = field_0.get_default_value()
        integer_0 = module_0.Integer()
        text_0 = module_0.Text()
        var_0 = [text_0, text_0, integer_0, integer_0, integer_0, integer_0]
        array_0 = module_0.Array(var_0)
        int_0 = -244
        any_1 = array_0.serialize(any_0)
        const_0 = module_0.Const(int_0)
        any_2 = array_0.validate(any_0)
    except BaseException:
        pass

def test_case_68():
    try:
        int_0 = 219
        number_0 = module_0.Number(maximum=int_0)
        float_0 = 446.0377
        any_0 = number_0.validate(float_0)
    except BaseException:
        pass

def test_case_69():
    try:
        array_0 = module_0.Array()
        bool_0 = None
        any_0 = array_0.validate(bool_0, strict=bool_0)
    except BaseException:
        pass

def test_case_70():
    try:
        dict_0 = {}
        int_0 = 590
        bytes_0 = b''
        list_0 = [int_0, bytes_0, int_0, dict_0]
        str_0 = 's+>\x0bd`'
        bool_0 = False
        field_0 = module_0.Field(description=str_0, default=list_0, allow_null=bool_0)
        object_0 = module_0.Object(pattern_properties=dict_0, additional_properties=list_0, property_names=field_0, min_properties=int_0, max_properties=int_0)
    except BaseException:
        pass

def test_case_71():
    try:
        int_0 = 590
        int_1 = 1875
        number_0 = module_0.Number(multiple_of=int_0)
        any_0 = number_0.validate(int_1)
    except BaseException:
        pass

def test_case_72():
    try:
        dict_0 = {}
        int_0 = -522
        none_type_0 = None
        object_0 = module_0.Object(pattern_properties=none_type_0, max_properties=int_0, **dict_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_73():
    try:
        str_0 = 'bJ'
        decimal_0 = None
        integer_0 = module_0.Integer(maximum=decimal_0, exclusive_maximum=decimal_0, precision=str_0)
        boolean_0 = module_0.Boolean()
        str_1 = 'allOf'
        string_0 = module_0.String()
        int_0 = -1359
        string_1 = module_0.String(max_length=int_0, min_length=int_0, pattern=str_1)
        any_0 = string_1.validate(str_0)
    except BaseException:
        pass

def test_case_74():
    try:
        dict_0 = {}
        bool_0 = True
        int_0 = 878
        list_0 = [bool_0, bool_0, int_0, bool_0, dict_0, dict_0]
        array_0 = module_0.Array(list_0, bool_0, int_0, int_0, int_0)
    except BaseException:
        pass

def test_case_75():
    try:
        dict_0 = {}
        int_0 = 1268
        object_0 = module_0.Object(min_properties=int_0)
        list_0 = None
        const_0 = module_0.Const(list_0)
        any_0 = const_0.validate(dict_0)
    except BaseException:
        pass

def test_case_76():
    try:
        int_0 = 1869
        str_0 = '0'
        number_0 = module_0.Number(minimum=int_0, exclusive_minimum=int_0, precision=str_0)
        bool_0 = False
        any_0 = number_0.validate(int_0, strict=bool_0)
    except BaseException:
        pass

def test_case_77():
    try:
        dict_0 = {}
        boolean_0 = module_0.Boolean()
        decimal_0 = module_1.Decimal()
        number_0 = module_0.Number(multiple_of=decimal_0, **dict_0)
        bool_0 = False
        any_0 = number_0.validate(decimal_0, strict=bool_0)
    except BaseException:
        pass

def test_case_78():
    try:
        float_0 = None
        str_0 = 'Pn\nV*OA{,9Yo5Yt/YsP'
        bool_0 = True
        field_0 = module_0.Field(description=str_0, default=float_0, allow_null=bool_0)
        bool_1 = False
        field_1 = module_0.Field(allow_null=bool_1)
        union_0 = field_1.__or__(field_0)
        any_0 = union_0.validate(float_0)
        decimal_0 = module_0.Decimal(exclusive_minimum=float_0)
        field_2 = None
        any_1 = decimal_0.serialize(float_0)
        list_0 = [field_2, field_2]
        any_2 = decimal_0.serialize(any_1)
        union_1 = module_0.Union(list_0)
    except BaseException:
        pass

def test_case_79():
    try:
        int_0 = 1906
        number_0 = module_0.Number(minimum=int_0, multiple_of=int_0)
        dict_0 = {}
        choice_0 = module_0.Choice(**dict_0)
        int_1 = 882
        any_0 = number_0.validate(int_1)
    except BaseException:
        pass

def test_case_80():
    try:
        str_0 = 'KS'
        field_0 = module_0.Field(default=str_0)
        float_0 = -539.1
        integer_0 = module_0.Integer(maximum=float_0)
        union_0 = integer_0.__or__(field_0)
        any_0 = union_0.validate(float_0)
    except BaseException:
        pass

def test_case_81():
    try:
        string_0 = module_0.String()
        integer_0 = module_0.Integer()
        var_0 = [string_0, integer_0]
        array_0 = module_0.Array(var_0)
        var_1 = []
        any_0 = array_0.validate(var_1)
    except BaseException:
        pass

def test_case_82():
    try:
        int_0 = 66
        int_1 = [int_0, int_0, int_0, int_0, int_0, int_0, int_0]
        list_0 = [int_1, int_1]
        choice_0 = module_0.Choice(choices=list_0)
    except BaseException:
        pass

def test_case_83():
    try:
        str_0 = 'date'
        string_0 = module_0.String(format=str_0)
        var_0 = None
        any_0 = string_0.serialize(var_0)
        string_1 = module_0.String(format=str_0)
        str_1 = '2019-09-05'
        any_1 = string_1.serialize(str_1)
    except BaseException:
        pass

def test_case_84():
    try:
        float_0 = 781.7
        number_0 = module_0.Number(minimum=float_0, multiple_of=float_0)
        any_0 = number_0.validate(float_0)
    except BaseException:
        pass

def test_case_85():
    try:
        sequence_0 = None
        float_0 = 759.2715303125847
        number_0 = module_0.Number(minimum=float_0, multiple_of=float_0)
        any_0 = number_0.validate(float_0)
        decimal_0 = None
        str_0 = ''
        str_1 = "'\x0b\tG+I^c;"
        str_2 = None
        dict_0 = {str_0: sequence_0, str_1: str_0, str_1: decimal_0, str_2: str_1}
        decimal_1 = module_0.Decimal(minimum=decimal_0, maximum=float_0, exclusive_maximum=decimal_0, **dict_0)
    except BaseException:
        pass

def test_case_86():
    try:
        integer_0 = module_0.Integer()
        array_0 = module_0.Array(integer_0)
        int_0 = -1321
        float_0 = -1418.0
        var_0 = [int_0, float_0, int_0, int_0, integer_0]
        any_0 = array_0.validate(var_0)
    except BaseException:
        pass

def test_case_87():
    try:
        integer_0 = module_0.Integer()
        var_0 = [integer_0, integer_0, integer_0]
        array_0 = module_0.Array(var_0)
        bool_0 = True
        field_0 = module_0.Field()
        bool_1 = True
        array_1 = module_0.Array(field_0, field_0, bool_1)
        any_0 = array_1.validate(var_0, strict=bool_0)
    except BaseException:
        pass

def test_case_88():
    try:
        int_0 = 65
        int_1 = [int_0, int_0, int_0, int_0, int_0, int_0, int_0]
        none_type_0 = None
        bool_0 = False
        none_type_1 = None
        array_0 = module_0.Array(none_type_0, bool_0, none_type_1, int_1)
    except BaseException:
        pass

def test_case_89():
    try:
        float_0 = None
        dict_0 = {}
        float_1 = module_0.Float(exclusive_minimum=float_0, exclusive_maximum=float_0, **dict_0)
        const_0 = module_0.Const(float_1)
        str_0 = ''
        bool_0 = True
        boolean_0 = module_0.Boolean(allow_null=bool_0)
        any_0 = boolean_0.validate(str_0)
        choice_0 = module_0.Choice()
        any_1 = choice_0.validate(any_0)
    except BaseException:
        pass

def test_case_90():
    try:
        bool_0 = True
        string_0 = module_0.String()
        str_0 = 'p1'
        str_1 = 'p2'
        string_1 = {str_0: string_0, str_1: string_0}
        object_0 = module_0.Object(properties=string_1)
        str_2 = 'a('
        str_3 = ''
        str_4 = {str_0: str_2, str_1: str_3}
        any_0 = object_0.validate(str_4)
    except BaseException:
        pass

def test_case_91():
    try:
        bool_0 = False
        bool_1 = True
        string_0 = module_0.String()
        str_0 = 'p1'
        str_1 = 'p2'
        string_1 = None
        object_0 = module_0.Object(properties=string_1, additional_properties=bool_0)
        str_2 = 'a('
        str_3 = ''
        str_4 = {str_0: str_2, str_1: str_3}
        any_0 = object_0.validate(str_4)
    except BaseException:
        pass

def test_case_92():
    try:
        field_0 = module_0.Field()
        int_0 = 264
        integer_0 = module_0.Integer(exclusive_minimum=int_0)
        union_0 = integer_0.__or__(field_0)
        any_0 = union_0.validate(int_0)
    except BaseException:
        pass

def test_case_93():
    try:
        dict_0 = {}
        bool_0 = False
        str_0 = '/g;.)'
        int_0 = -2975
        integer_0 = module_0.Integer(exclusive_maximum=bool_0, precision=str_0, multiple_of=int_0, **dict_0)
        field_0 = module_0.Field(default=str_0, allow_null=bool_0)
        union_0 = integer_0.__or__(field_0)
        any_0 = union_0.validate(int_0)
    except BaseException:
        pass

def test_case_94():
    try:
        str_0 = 'Test'
        field_0 = module_0.Field(default=str_0)
        any_0 = field_0.get_default_value()
        field_1 = module_0.Field()
        any_1 = field_1.get_default_value()
        var_0 = None
        field_2 = module_0.Field(default=var_0)
        any_2 = field_2.get_default_value()
        var_1 = lambda : str_0
        field_3 = module_0.Field(default=var_1)
        any_3 = field_3.get_default_value()
    except BaseException:
        pass

def test_case_95():
    try:
        integer_0 = module_0.Integer()
        text_0 = module_0.Text()
        var_0 = [text_0, integer_0, text_0, integer_0, integer_0, integer_0, integer_0]
        date_0 = module_0.Date()
        array_0 = module_0.Array(date_0)
        any_0 = array_0.validate(var_0)
    except BaseException:
        pass

def test_case_96():
    try:
        int_0 = 66
        int_1 = [int_0, int_0, int_0, int_0, int_0, int_0, int_0]
        str_0 = 'Oxx\t%,t\nqX6nAijs'
        bool_0 = False
        field_0 = module_0.Field(title=str_0, allow_null=bool_0)
        any_0 = field_0.get_default_value()
        array_0 = module_0.Array(field_0, bool_0, int_0)
        any_1 = array_0.validate(int_1)
    except BaseException:
        pass

def test_case_97():
    try:
        bool_0 = True
        string_0 = module_0.String()
        str_0 = 'value'
        object_0 = module_0.Object(properties=string_0)
        str_1 = 'a('
        str_2 = ''
        str_3 = {str_0: str_1, str_0: str_2}
        any_0 = object_0.validate(str_3)
    except BaseException:
        pass