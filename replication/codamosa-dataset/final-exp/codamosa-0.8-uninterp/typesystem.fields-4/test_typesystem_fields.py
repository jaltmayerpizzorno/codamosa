# Automatically generated by Pynguin.
import typesystem.fields as module_0
import decimal as module_1

def test_case_0():
    pass

def test_case_1():
    string_0 = module_0.String()

def test_case_2():
    decimal_0 = module_1.Decimal()
    str_0 = 'ua\x0bB'
    bool_0 = True
    boolean_0 = module_0.Boolean(description=str_0, allow_null=bool_0)
    any_0 = boolean_0.validate(decimal_0)

def test_case_3():
    str_0 = 'S{i$wTj!6R|FH3'
    field_0 = module_0.Field(description=str_0, default=str_0)
    union_0 = field_0.__or__(field_0)

def test_case_4():
    bool_0 = True
    string_0 = module_0.String(allow_blank=bool_0)

def test_case_5():
    field_0 = module_0.Field()
    any_0 = field_0.get_default_value()

def test_case_6():
    field_0 = module_0.Field()
    union_0 = field_0.__or__(field_0)

def test_case_7():
    str_0 = '3\no\t|nc'
    bool_0 = True
    string_0 = module_0.String(trim_whitespace=bool_0, pattern=str_0)
    any_0 = string_0.validate(str_0)

def test_case_8():
    integer_0 = module_0.Integer()

def test_case_9():
    int_0 = -7
    integer_0 = module_0.Integer(minimum=int_0, maximum=int_0, exclusive_minimum=int_0, exclusive_maximum=int_0, multiple_of=int_0)

def test_case_10():
    int_0 = 172
    integer_0 = module_0.Integer(multiple_of=int_0)
    any_0 = integer_0.validate(int_0)
    str_0 = '&2(7#&\x0bc'
    decimal_0 = module_0.Decimal(exclusive_maximum=int_0)
    any_1 = decimal_0.serialize(int_0)
    any_2 = module_0.Any(description=str_0)

def test_case_11():
    choice_0 = module_0.Choice()

def test_case_12():
    object_0 = module_0.Object()

def test_case_13():
    object_0 = module_0.Object()
    str_0 = 'abc'
    str_1 = {str_0: str_0}
    any_0 = object_0.validate(str_1)

def test_case_14():
    array_0 = module_0.Array()

def test_case_15():
    array_0 = module_0.Array()
    var_0 = [array_0, array_0, array_0]
    any_0 = array_0.validate(var_0)

def test_case_16():
    text_0 = module_0.Text()

def test_case_17():
    date_0 = module_0.Date()

def test_case_18():
    text_0 = module_0.Text()
    float_0 = -1420.846852
    number_0 = module_0.Number(minimum=float_0, maximum=float_0, exclusive_maximum=float_0)
    time_0 = module_0.Time()

def test_case_19():
    date_time_0 = module_0.DateTime()

def test_case_20():
    int_0 = 27
    integer_0 = module_0.Integer()
    str_0 = "'y+j\r)9.&p"
    bool_0 = True
    field_0 = module_0.Field(description=str_0, default=str_0, allow_null=bool_0)
    field_1 = module_0.Field()
    union_0 = field_1.__or__(field_0)
    any_0 = integer_0.validate(int_0)

def test_case_21():
    int_0 = 34
    any_0 = module_0.Any(default=int_0)
    any_1 = any_0.validate(int_0)
    integer_0 = module_0.Integer(multiple_of=int_0)
    any_2 = integer_0.validate(int_0)

def test_case_22():
    float_0 = 442.40112
    number_0 = module_0.Number(exclusive_minimum=float_0, multiple_of=float_0)
    field_0 = module_0.Field()
    const_0 = module_0.Const(field_0)

def test_case_23():
    text_0 = module_0.Text()
    str_0 = 'uEu"L=)'
    bool_0 = True
    field_0 = module_0.Field(description=str_0, default=text_0, allow_null=bool_0)
    any_0 = field_0.get_default_value()

def test_case_24():
    validation_error_0 = None
    bool_0 = True
    int_0 = 1285
    str_0 = "6'u0Nt_.$Lq"
    string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_0, max_length=int_0, min_length=int_0, format=str_0)
    any_0 = string_0.validate(validation_error_0)

def test_case_25():
    int_0 = 5
    string_0 = module_0.String(max_length=int_0)
    str_0 = 'abcd'
    any_0 = string_0.validate(str_0)

def test_case_26():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0]
    choice_0 = module_0.Choice(choices=list_0)
    field_0 = module_0.Field()

def test_case_27():
    bool_0 = False
    int_0 = -2216
    integer_0 = module_0.Integer(minimum=int_0)
    string_0 = module_0.String(max_length=int_0)
    var_0 = [integer_0]
    array_0 = module_0.Array(var_0, string_0, int_0, int_0, bool_0)

def test_case_28():
    int_0 = 1068
    field_0 = module_0.Field()
    array_0 = module_0.Array()
    bool_0 = True
    array_1 = module_0.Array(field_0, bool_0, int_0, bool_0)

def test_case_29():
    str_0 = '_}I@Q+MmeGqhGu'
    decimal_0 = None
    dict_0 = {}
    date_time_0 = module_0.DateTime(**dict_0)
    decimal_1 = module_0.Decimal(maximum=decimal_0, precision=str_0)
    time_0 = module_0.Time()
    str_1 = 'gec1'
    object_0 = module_0.Object(properties=time_0, required=str_1)
    field_0 = module_0.Field()
    dict_1 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
    object_1 = module_0.Object(pattern_properties=dict_1)
    any_0 = object_1.validate(dict_1)

def test_case_30():
    str_0 = '3\no\t|nc'
    bool_0 = False
    string_0 = module_0.String(trim_whitespace=bool_0, pattern=str_0)
    any_0 = string_0.serialize(str_0)

def test_case_31():
    str_0 = 'Nql~#XiN\n5W&HyT;D\x0b'
    string_0 = module_0.String(pattern=str_0)

def test_case_32():
    any_0 = module_0.Any()
    array_0 = module_0.Array()
    any_1 = array_0.serialize(any_0)

def test_case_33():
    int_0 = -3403
    field_0 = module_0.Field()
    object_0 = module_0.Object(max_properties=int_0)

def test_case_34():
    bool_0 = True
    int_0 = -2229
    integer_0 = module_0.Integer(minimum=int_0)
    string_0 = module_0.String(max_length=int_0)
    array_0 = module_0.Array(integer_0, string_0, int_0, int_0, bool_0)

def test_case_35():
    var_0 = None
    bool_0 = False
    array_0 = module_0.Array(var_0, bool_0, bool_0)

def test_case_36():
    float_0 = -511.449
    const_0 = module_0.Const(float_0)
    dict_0 = {}
    any_0 = const_0.validate(float_0)
    str_0 = 'C@H'
    field_0 = module_0.Field()
    dict_1 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
    object_0 = module_0.Object(properties=dict_1, additional_properties=field_0)
    any_1 = object_0.validate(dict_0)

def test_case_37():
    float_0 = None
    str_0 = 'JlQiA+nEd'
    float_1 = 442.40112
    number_0 = module_0.Number(exclusive_minimum=float_1, multiple_of=float_1)
    int_0 = 572
    int_1 = -1529
    list_0 = [int_1]
    field_0 = module_0.Field()
    const_0 = module_0.Const(field_0)
    string_0 = module_0.String()
    any_0 = string_0.serialize(list_0)
    array_0 = module_0.Array(field_0)
    dict_0 = {float_0: float_0, int_0: field_0, int_1: int_0, array_0: str_0}
    any_1 = array_0.serialize(dict_0)

def test_case_38():
    int_0 = 34
    integer_0 = module_0.Integer(multiple_of=int_0)
    any_0 = integer_0.validate(int_0)

def test_case_39():
    int_0 = 27
    integer_0 = module_0.Integer(maximum=int_0, precision=int_0)
    any_0 = integer_0.validate(int_0)

def test_case_40():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0]
    choice_0 = module_0.Choice(choices=list_0)
    any_0 = choice_0.validate(dict_0)
    field_0 = module_0.Field()

def test_case_41():
    int_0 = -3403
    str_0 = 'S{i$wTj!6R|FH3'
    integer_0 = module_0.Integer(exclusive_minimum=int_0, precision=str_0, multiple_of=int_0)
    field_0 = module_0.Field(default=integer_0)
    field_1 = module_0.Field()
    list_0 = [field_0, field_0, field_1, field_0]
    union_0 = module_0.Union(list_0)
    array_0 = module_0.Array(union_0)
    str_1 = 'EOkB'
    str_2 = 'VuRa>/M/qcJ@6'
    dict_0 = {str_1: field_1, str_2: field_0, str_0: field_1}
    int_1 = None
    object_0 = module_0.Object(properties=union_0, pattern_properties=dict_0, required=int_1)
    bool_0 = True
    boolean_0 = module_0.Boolean(allow_null=bool_0)
    any_0 = boolean_0.validate(int_1)

def test_case_42():
    dict_0 = {}
    str_0 = '3\no\t|nc'
    field_0 = module_0.Field()
    dict_1 = {str_0: field_0, str_0: field_0}
    object_0 = module_0.Object(properties=dict_1, additional_properties=field_0)
    any_0 = object_0.validate(dict_0)

def test_case_43():
    str_0 = 'q@Tn.o.er/u97<9^'
    field_0 = module_0.Field()
    dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
    object_0 = module_0.Object(pattern_properties=dict_0)
    any_0 = object_0.validate(dict_0)

def test_case_44():
    int_0 = 133
    const_0 = None
    dict_0 = {}
    int_1 = None
    object_0 = module_0.Object(properties=const_0, min_properties=int_1, max_properties=int_0, required=dict_0)
    any_0 = object_0.validate(dict_0)

def test_case_45():
    string_0 = module_0.String()
    integer_0 = module_0.Integer()
    var_0 = [string_0, integer_0]
    union_0 = module_0.Union(var_0)
    str_0 = 'test'
    any_0 = union_0.validate(str_0)
    int_0 = 3
    any_1 = union_0.validate(int_0)

def test_case_46():
    dict_0 = {}
    str_0 = '('
    field_0 = module_0.Field()
    dict_1 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
    field_1 = None
    object_0 = module_0.Object(properties=dict_1, pattern_properties=dict_1, additional_properties=field_1, **dict_0)
    any_0 = object_0.validate(dict_0)

def test_case_47():
    bool_0 = True
    int_0 = -3
    integer_0 = module_0.Integer(minimum=int_0)
    int_1 = -3210
    string_0 = module_0.String(max_length=int_1)
    var_0 = [integer_0]
    array_0 = module_0.Array(var_0, string_0, int_0, int_1, bool_0)
    any_0 = array_0.serialize(var_0)