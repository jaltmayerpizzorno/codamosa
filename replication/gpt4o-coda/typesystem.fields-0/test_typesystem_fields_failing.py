# Automatically generated by Pynguin.
import typesystem.fields as module_0
import decimal as module_1

def test_case_0():
    try:
        str_0 = ";O<'e"
        bool_0 = True
        boolean_0 = module_0.Boolean(allow_null=bool_0)
        any_0 = boolean_0.validate(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        field_0 = module_0.Field(default=dict_0)
        validation_result_0 = field_0.validate_or_error(field_0)
    except BaseException:
        pass

def test_case_2():
    try:
        dict_0 = {}
        field_0 = module_0.Field(default=dict_0)
        optional_0 = None
        str_0 = '|lMEnd4\r3'
        object_0 = module_0.Object(property_names=field_0, min_properties=optional_0, required=str_0, **dict_0)
        any_0 = field_0.serialize(field_0)
        any_1 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        array_0 = module_0.Array()
        any_0 = array_0.validate(array_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '^L$vY51\r'
        string_0 = module_0.String(pattern=str_0)
        any_0 = string_0.validate(string_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 2
        number_0 = module_0.Number(minimum=int_0, maximum=int_0, exclusive_minimum=int_0, multiple_of=int_0)
        any_0 = number_0.validate(int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        number_0 = module_0.Number()
        any_0 = number_0.validate(number_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 2
        choice_0 = module_0.Choice()
        number_0 = module_0.Number(exclusive_maximum=int_0)
        any_0 = number_0.validate(int_0)
    except BaseException:
        pass

def test_case_8():
    try:
        decimal_0 = module_1.Decimal()
        number_0 = module_0.Number(maximum=decimal_0, exclusive_maximum=decimal_0, multiple_of=decimal_0)
        any_0 = number_0.validate(decimal_0)
    except BaseException:
        pass

def test_case_9():
    try:
        boolean_0 = module_0.Boolean()
        any_0 = boolean_0.validate(boolean_0)
    except BaseException:
        pass

def test_case_10():
    try:
        text_0 = module_0.Text()
        bool_0 = True
        bool_1 = True
        boolean_0 = module_0.Boolean(default=text_0, allow_null=bool_1)
        any_0 = boolean_0.validate(text_0, strict=bool_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'N^L:BU5s\rb'
        boolean_0 = module_0.Boolean(title=str_0)
        any_0 = boolean_0.validate(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        choice_0 = module_0.Choice()
        any_0 = choice_0.validate(choice_0)
    except BaseException:
        pass

def test_case_13():
    try:
        time_0 = module_0.Time()
        int_0 = 1
        array_0 = module_0.Array(int_0, int_0)
    except BaseException:
        pass

def test_case_14():
    try:
        list_0 = []
        union_0 = module_0.Union(list_0)
        any_0 = union_0.validate(list_0)
    except BaseException:
        pass

def test_case_15():
    try:
        date_0 = module_0.Date()
        field_0 = module_0.Field()
        union_0 = field_0.__or__(field_0)
        any_0 = union_0.validate(date_0)
    except BaseException:
        pass

def test_case_16():
    try:
        tuple_0 = None
        str_0 = 'r/'
        any_0 = module_0.Any(title=str_0)
        any_1 = any_0.validate(tuple_0)
        object_0 = module_0.Object()
        any_2 = object_0.validate(tuple_0)
    except BaseException:
        pass

def test_case_17():
    try:
        dict_0 = {}
        const_0 = module_0.Const(dict_0)
        any_0 = const_0.validate(dict_0)
        any_1 = const_0.validate(const_0)
    except BaseException:
        pass

def test_case_18():
    try:
        date_time_0 = module_0.DateTime()
        const_0 = module_0.Const(date_time_0)
        set_0 = {date_time_0}
        int_0 = 661
        string_0 = module_0.String(max_length=set_0, min_length=int_0)
    except BaseException:
        pass

def test_case_19():
    try:
        decimal_0 = module_1.Decimal()
        number_0 = module_0.Number(maximum=decimal_0, exclusive_minimum=decimal_0, precision=decimal_0)
        any_0 = number_0.validate(decimal_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = ''
        date_time_0 = module_0.DateTime()
        str_1 = '+?+@AsnCjHqwxa-S'
        dict_0 = {str_0: str_0, str_1: str_0}
        array_0 = module_0.Array(date_time_0, dict_0)
    except BaseException:
        pass

def test_case_21():
    try:
        time_0 = module_0.Time()
        array_0 = module_0.Array(time_0)
        var_0 = [array_0, array_0]
        any_0 = array_0.validate(var_0)
    except BaseException:
        pass

def test_case_22():
    try:
        dict_0 = {}
        field_0 = module_0.Field(default=dict_0)
        object_0 = module_0.Object(additional_properties=field_0, property_names=field_0)
        str_0 = 'y1=7DsfV3 &g}Qr>6X'
        string_0 = module_0.String(pattern=str_0)
        bool_0 = True
        any_0 = module_0.Any(description=str_0, default=string_0, allow_null=bool_0)
        array_0 = module_0.Array(field_0, field_0, any_0)
    except BaseException:
        pass

def test_case_23():
    try:
        int_0 = -42
        decimal_0 = module_0.Decimal(exclusive_minimum=int_0, exclusive_maximum=int_0)
        choice_0 = module_0.Choice()
        any_0 = decimal_0.serialize(decimal_0)
    except BaseException:
        pass

def test_case_24():
    try:
        dict_0 = {}
        bool_0 = True
        field_0 = module_0.Field(default=dict_0, allow_null=bool_0)
        str_0 = '|lMEnd4\r3'
        str_1 = '<J~?"Pi7{{_\'Oee2b]Hz'
        dict_1 = {str_1: field_0, str_0: field_0}
        boolean_0 = module_0.Boolean(default=bool_0)
        any_0 = boolean_0.validate(bool_0)
        optional_0 = None
        object_0 = module_0.Object(pattern_properties=dict_1, required=optional_0, **dict_0)
        any_1 = object_0.validate(dict_1)
    except BaseException:
        pass

def test_case_25():
    try:
        date_0 = module_0.Date()
        array_0 = module_0.Array()
        field_0 = module_0.Field()
        str_0 = None
        bool_0 = False
        any_0 = module_0.Any(description=str_0, default=field_0, allow_null=bool_0)
    except BaseException:
        pass

def test_case_26():
    try:
        tuple_0 = None
        int_0 = 127
        string_0 = module_0.String(min_length=int_0)
        any_0 = string_0.validate(tuple_0)
    except BaseException:
        pass

def test_case_27():
    try:
        array_0 = module_0.Array()
        field_0 = module_0.Field()
        dict_0 = {}
        time_0 = module_0.Time(**dict_0)
        decimal_0 = module_1.Decimal(**dict_0)
        str_0 = 'pOi$ MN:j'
        string_0 = module_0.String(min_length=decimal_0, pattern=str_0, **dict_0)
    except BaseException:
        pass

def test_case_28():
    try:
        text_0 = None
        number_0 = module_0.Number()
        any_0 = number_0.validate(text_0)
    except BaseException:
        pass

def test_case_29():
    try:
        bool_0 = False
        none_type_0 = None
        string_0 = module_0.String(allow_blank=bool_0, max_length=none_type_0, pattern=bool_0)
    except BaseException:
        pass

def test_case_30():
    try:
        str_0 = '2PnD57'
        number_0 = module_0.Number(precision=str_0)
        any_0 = number_0.validate(str_0)
    except BaseException:
        pass

def test_case_31():
    try:
        any_0 = module_0.Any()
        string_0 = module_0.String(format=any_0)
    except BaseException:
        pass

def test_case_32():
    try:
        float_0 = -2598.96
        field_0 = module_0.Field()
        str_0 = 'l%28wus&J=&\x0c&U'
        bool_0 = True
        field_1 = module_0.Field(title=str_0, description=str_0, allow_null=bool_0)
        union_0 = field_1.__or__(field_0)
        any_0 = union_0.validate(float_0)
    except BaseException:
        pass

def test_case_33():
    try:
        str_0 = 'xztiol3'
        choice_0 = module_0.Choice(choices=str_0)
        any_0 = choice_0.validate(str_0)
    except BaseException:
        pass

def test_case_34():
    try:
        int_0 = 361
        str_0 = 'wYW(LkbpYU90&dl'
        string_0 = module_0.String(min_length=int_0)
        any_0 = string_0.validate(str_0)
    except BaseException:
        pass

def test_case_35():
    try:
        array_0 = module_0.Array()
        int_0 = 2895
        object_0 = module_0.Object(max_properties=int_0)
        float_0 = module_0.Float(exclusive_maximum=int_0)
        bool_0 = False
        any_0 = object_0.validate(float_0, strict=bool_0)
    except BaseException:
        pass

def test_case_36():
    try:
        str_0 = ''
        string_0 = module_0.String()
        object_0 = module_0.Object(properties=string_0, required=str_0)
        bool_0 = True
        any_0 = string_0.validate(str_0, strict=bool_0)
    except BaseException:
        pass

def test_case_37():
    try:
        bool_0 = True
        object_0 = module_0.Object()
        any_0 = object_0.validate(bool_0)
    except BaseException:
        pass

def test_case_38():
    try:
        str_0 = 'U/HWI0'
        bool_0 = True
        boolean_0 = module_0.Boolean(title=str_0, description=str_0, default=str_0, allow_null=bool_0)
        any_0 = boolean_0.validate(str_0)
    except BaseException:
        pass

def test_case_39():
    try:
        time_0 = module_0.Time()
        decimal_0 = None
        choice_0 = module_0.Choice()
        list_0 = [choice_0]
        object_0 = module_0.Object(property_names=time_0, max_properties=decimal_0, required=list_0)
    except BaseException:
        pass

def test_case_40():
    try:
        dict_0 = {}
        field_0 = module_0.Field(default=dict_0)
        str_0 = '`|r<<@KL~|.^+.v6>*'
        dict_1 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
        object_0 = module_0.Object(properties=dict_1)
        any_0 = object_0.validate(dict_1)
    except BaseException:
        pass

def test_case_41():
    try:
        dict_0 = {}
        field_0 = module_0.Field(default=dict_0)
        str_0 = 'p(Sh\x0b'
        dict_1 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
        object_0 = module_0.Object(pattern_properties=dict_1)
        any_0 = object_0.validate(dict_1)
    except BaseException:
        pass

def test_case_42():
    try:
        str_0 = '3'
        integer_0 = module_0.Integer()
        object_0 = module_0.Object(properties=integer_0, required=str_0)
        str_1 = {integer_0: str_0, str_0: str_0}
        any_0 = object_0.validate(str_1)
    except BaseException:
        pass

def test_case_43():
    try:
        dict_0 = {}
        text_0 = module_0.Text(**dict_0)
        bool_0 = False
        float_0 = 2959.17078
        number_0 = module_0.Number(multiple_of=float_0)
        any_0 = number_0.validate(bool_0)
    except BaseException:
        pass

def test_case_44():
    try:
        date_0 = module_0.Date()
        array_0 = module_0.Array()
        float_0 = 3548.7
        number_0 = module_0.Number(minimum=float_0, exclusive_minimum=float_0, multiple_of=float_0)
        bool_0 = True
        any_0 = number_0.validate(number_0, strict=bool_0)
    except BaseException:
        pass

def test_case_45():
    try:
        int_0 = 4
        number_0 = module_0.Number(minimum=int_0, maximum=int_0, exclusive_maximum=int_0)
        int_1 = 2961
        any_0 = number_0.validate(int_1)
    except BaseException:
        pass

def test_case_46():
    try:
        str_0 = ''
        number_0 = module_0.Number(precision=str_0)
        any_0 = number_0.validate(str_0)
    except BaseException:
        pass

def test_case_47():
    try:
        str_0 = 'KzoYi/.!]"RA~L\rOR0'
        array_0 = module_0.Array()
        boolean_0 = None
        dict_0 = {str_0: array_0, array_0: array_0, str_0: boolean_0, boolean_0: str_0}
        object_0 = module_0.Object(max_properties=dict_0)
    except BaseException:
        pass

def test_case_48():
    try:
        str_0 = 'Ni]WInY1+rHOD42'
        field_0 = module_0.Field()
        union_0 = field_0.__or__(field_0)
        any_0 = field_0.get_default_value()
        string_0 = module_0.String(pattern=str_0)
        decimal_0 = module_0.Decimal(precision=str_0, multiple_of=string_0)
    except BaseException:
        pass

def test_case_49():
    try:
        dict_0 = {}
        field_0 = module_0.Field(default=dict_0)
        date_time_0 = module_0.DateTime()
        tuple_0 = (date_time_0, date_time_0)
        array_0 = module_0.Array(tuple_0)
        str_0 = '|mMEnd^\r3'
        bool_0 = True
        field_1 = module_0.Field(default=dict_0, allow_null=bool_0)
        list_0 = [field_0, field_1]
        union_0 = module_0.Union(list_0)
        float_0 = module_0.Float(minimum=union_0, precision=str_0)
    except BaseException:
        pass

def test_case_50():
    try:
        dict_0 = {}
        list_0 = [dict_0]
        none_type_0 = None
        sequence_0 = None
        object_0 = module_0.Object(additional_properties=list_0, max_properties=none_type_0, required=sequence_0)
    except BaseException:
        pass

def test_case_51():
    try:
        dict_0 = {}
        object_0 = module_0.Object(**dict_0)
        number_0 = None
        decimal_0 = None
        list_0 = None
        tuple_0 = (number_0, decimal_0, list_0, dict_0)
        str_0 = '|OshY1eZq6Or(#= B\x0b0'
        number_1 = module_0.Number(maximum=tuple_0, exclusive_minimum=decimal_0, precision=str_0, multiple_of=decimal_0)
    except BaseException:
        pass

def test_case_52():
    try:
        tuple_0 = ()
        const_0 = module_0.Const(tuple_0)
        str_0 = '/{!{\nt"{F2G'
        number_0 = module_0.Number(exclusive_minimum=const_0, precision=str_0)
    except BaseException:
        pass

def test_case_53():
    try:
        object_0 = None
        str_0 = '7=>6PM:?;S'
        boolean_0 = module_0.Boolean(description=str_0)
        any_0 = boolean_0.validate(object_0)
    except BaseException:
        pass

def test_case_54():
    try:
        str_0 = None
        field_0 = module_0.Field(title=str_0)
    except BaseException:
        pass

def test_case_55():
    try:
        int_0 = 2
        float_0 = 1353.3019039832268
        dict_0 = {}
        date_time_0 = module_0.DateTime()
        object_0 = module_0.Object(property_names=int_0, min_properties=int_0, **dict_0)
        str_0 = ',tB_t8I]l'
        any_0 = module_0.Any(title=str_0, default=int_0)
        any_1 = any_0.validate(float_0)
        int_1 = 1704
        string_0 = module_0.String()
        bool_0 = True
        number_0 = module_0.Number(minimum=float_0, exclusive_minimum=int_1)
        any_2 = number_0.validate(int_0, strict=bool_0)
    except BaseException:
        pass

def test_case_56():
    try:
        int_0 = 2
        float_0 = 1388.9483356421106
        dict_0 = {}
        number_0 = module_0.Number(maximum=float_0, exclusive_maximum=float_0, multiple_of=float_0, **dict_0)
        any_0 = number_0.validate(int_0)
    except BaseException:
        pass

def test_case_57():
    try:
        int_0 = 2
        dict_0 = {}
        object_0 = module_0.Object(property_names=int_0, min_properties=int_0, **dict_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_58():
    try:
        array_0 = module_0.Array()
        int_0 = -15
        str_0 = 'XOTkp(Xj\x0c}u[U\x0bN'
        str_1 = "';n\x0br@q2bpIK>v&"
        field_0 = module_0.Field(default=int_0)
        dict_0 = {str_1: field_0, str_1: field_0, str_1: field_0, str_0: field_0}
        object_0 = module_0.Object(properties=dict_0, max_properties=int_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_59():
    try:
        tuple_0 = None
        object_0 = module_0.Object()
        bool_0 = True
        dict_0 = {tuple_0: bool_0, tuple_0: object_0}
        any_0 = object_0.validate(dict_0, strict=bool_0)
    except BaseException:
        pass

def test_case_60():
    try:
        str_0 = 'Y|+'
        integer_0 = module_0.Integer()
        object_0 = module_0.Object(properties=integer_0, required=str_0)
        str_1 = {integer_0: str_0, str_0: str_0}
        any_0 = object_0.validate(str_1)
    except BaseException:
        pass

def test_case_61():
    try:
        object_0 = module_0.Object()
        bool_0 = True
        field_0 = module_0.Field(allow_null=bool_0)
        number_0 = module_0.Number(exclusive_maximum=field_0)
    except BaseException:
        pass

def test_case_62():
    try:
        dict_0 = {}
        str_0 = None
        field_0 = module_0.Field(default=dict_0)
        str_1 = None
        dict_1 = {str_0: field_0, str_1: field_0}
        object_0 = module_0.Object(properties=dict_1, property_names=field_0)
    except BaseException:
        pass

def test_case_63():
    try:
        str_0 = 'K}*z,|v'
        field_0 = module_0.Field()
        dict_0 = {str_0: field_0}
        field_1 = module_0.Field(title=str_0)
        time_0 = module_0.Time()
        str_1 = 'G.Kmk|8Y'
        object_0 = module_0.Object(properties=dict_0, pattern_properties=dict_0, additional_properties=field_1, min_properties=time_0, required=str_1)
    except BaseException:
        pass

def test_case_64():
    try:
        array_0 = module_0.Array()
        int_0 = 18
        str_0 = 'XOTkp(Xj\x0c}u[U\x0bN'
        str_1 = 'b'
        field_0 = module_0.Field(default=int_0)
        dict_0 = {str_1: field_0, str_1: field_0, str_1: field_0, str_0: field_0}
        object_0 = module_0.Object(properties=dict_0, max_properties=int_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_65():
    try:
        dict_0 = {}
        field_0 = module_0.Field(default=dict_0)
        str_0 = '`|r<<@KL~|.^+.v6>*'
        dict_1 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
        none_type_0 = None
        object_0 = module_0.Object(pattern_properties=dict_1, max_properties=none_type_0, **dict_0)
        any_0 = object_0.validate(dict_0)
        any_1 = object_0.validate(dict_1)
    except BaseException:
        pass

def test_case_66():
    try:
        tuple_0 = None
        object_0 = module_0.Object()
        any_0 = object_0.validate(tuple_0)
    except BaseException:
        pass

def test_case_67():
    try:
        date_0 = module_0.Date()
        str_0 = ''
        tuple_0 = None
        dict_0 = {str_0: tuple_0}
        number_0 = module_0.Number(precision=dict_0)
        bool_0 = False
        field_0 = module_0.Field(title=str_0, allow_null=bool_0)
        object_0 = module_0.Object(properties=dict_0, property_names=field_0)
    except BaseException:
        pass

def test_case_68():
    try:
        array_0 = module_0.Array()
        optional_0 = None
        any_0 = array_0.validate(optional_0)
    except BaseException:
        pass

def test_case_69():
    try:
        str_0 = ''
        bool_0 = True
        int_0 = -1404
        date_time_0 = module_0.DateTime()
        object_0 = module_0.Object(additional_properties=bool_0, property_names=date_time_0, min_properties=int_0)
        dict_0 = {str_0: date_time_0, str_0: object_0}
        any_0 = object_0.validate(dict_0, strict=bool_0)
    except BaseException:
        pass

def test_case_70():
    try:
        str_0 = ''
        bool_0 = False
        int_0 = -1372
        date_time_0 = module_0.DateTime()
        object_0 = module_0.Object(additional_properties=bool_0, property_names=date_time_0, min_properties=int_0)
        dict_0 = {str_0: date_time_0, str_0: object_0}
        any_0 = object_0.validate(dict_0, strict=bool_0)
    except BaseException:
        pass

def test_case_71():
    try:
        dict_0 = {}
        str_0 = '0!g\tGtpF\x0c\\E'
        bool_0 = True
        field_0 = module_0.Field(title=str_0, default=dict_0, allow_null=bool_0)
        dict_1 = {str_0: field_0, str_0: field_0, str_0: field_0}
        object_0 = module_0.Object(properties=dict_1, additional_properties=field_0)
        bool_1 = False
        optional_0 = None
        object_1 = module_0.Object(additional_properties=bool_1, required=optional_0)
        bool_2 = False
        any_0 = object_1.validate(dict_1, strict=bool_2)
    except BaseException:
        pass

def test_case_72():
    try:
        str_0 = 't;-AyW2f1v4'
        int_0 = -231
        string_0 = module_0.String(max_length=int_0)
        any_0 = string_0.validate(str_0)
    except BaseException:
        pass

def test_case_73():
    try:
        str_0 = ''
        string_0 = module_0.String()
        integer_0 = module_0.Integer()
        str_1 = [str_0]
        int_0 = 30
        integer_1 = module_0.Integer()
        var_0 = {str_0: string_0, str_0: integer_1}
        object_0 = module_0.Object(properties=var_0, required=str_1)
        int_1 = {str_0: int_0}
        any_0 = object_0.validate(int_1)
        string_1 = module_0.String()
        integer_2 = module_0.Integer()
    except BaseException:
        pass

def test_case_74():
    try:
        dict_0 = {}
        field_0 = module_0.Field(default=dict_0)
        optional_0 = None
        str_0 = '|m%\x0bd^\r3'
        object_0 = module_0.Object(min_properties=optional_0, required=str_0, **dict_0)
        str_1 = '+T'
        str_2 = None
        field_1 = module_0.Field(default=str_0)
        dict_1 = {str_1: field_0, str_2: field_1}
        int_0 = -1754
        number_0 = module_0.Number(exclusive_minimum=int_0, precision=str_1, **dict_0)
        object_1 = module_0.Object(pattern_properties=dict_1, additional_properties=field_1, max_properties=int_0, required=number_0, **dict_0)
    except BaseException:
        pass

def test_case_75():
    try:
        int_0 = 1
        dict_0 = {}
        object_0 = module_0.Object(property_names=int_0, min_properties=int_0, **dict_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_76():
    try:
        integer_0 = None
        choice_0 = module_0.Choice(choices=integer_0)
        any_0 = choice_0.validate(integer_0)
    except BaseException:
        pass

def test_case_77():
    try:
        time_0 = module_0.Time()
        array_0 = module_0.Array(time_0)
        var_0 = [array_0, array_0]
        any_0 = array_0.serialize(var_0)
    except BaseException:
        pass

def test_case_78():
    try:
        dict_0 = None
        time_0 = module_0.Time()
        array_0 = module_0.Array(time_0)
        any_0 = array_0.serialize(dict_0)
        var_0 = [array_0, array_0]
        any_1 = array_0.validate(var_0)
    except BaseException:
        pass

def test_case_79():
    try:
        int_0 = 2
        str_0 = 'wYW(LkbpYU90&dl'
        string_0 = module_0.String(min_length=int_0)
        any_0 = string_0.validate(str_0)
        int_1 = -4
        array_0 = module_0.Array(int_1)
    except BaseException:
        pass

def test_case_80():
    try:
        dict_0 = {}
        field_0 = module_0.Field(default=dict_0)
        str_0 = ''
        dict_1 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
        object_0 = module_0.Object(pattern_properties=dict_1)
        any_0 = object_0.validate(dict_1)
    except BaseException:
        pass

def test_case_81():
    try:
        dict_0 = {}
        str_0 = 'pLZ'
        bool_0 = True
        int_0 = None
        string_0 = module_0.String(allow_blank=bool_0, max_length=int_0, min_length=int_0, pattern=str_0, **dict_0)
        any_0 = string_0.validate(int_0, strict=bool_0)
    except BaseException:
        pass

def test_case_82():
    try:
        text_0 = None
        list_0 = []
        union_0 = module_0.Union(list_0)
        any_0 = union_0.validate(text_0)
    except BaseException:
        pass

def test_case_83():
    try:
        int_0 = 1716
        number_0 = module_0.Number(multiple_of=int_0)
        int_1 = 139
        any_0 = number_0.validate(int_1)
    except BaseException:
        pass

def test_case_84():
    try:
        bool_0 = True
        str_0 = "R9Q\x0c'kc\x0c%z<?D Hqj9=8"
        string_0 = module_0.String(allow_blank=bool_0, pattern=str_0)
        any_0 = string_0.validate(str_0)
    except BaseException:
        pass

def test_case_85():
    try:
        str_0 = ''
        string_0 = module_0.String()
        any_0 = string_0.validate(str_0)
    except BaseException:
        pass

def test_case_86():
    try:
        object_0 = module_0.Object()
        str_0 = 'Q Lr6Fh:+GIe(\t/`'
        str_1 = '5&U%-Ux3'
        field_0 = module_0.Field(description=str_1, default=str_1)
        any_0 = field_0.get_default_value()
        field_1 = None
        dict_0 = {str_0: field_1}
        object_1 = module_0.Object(pattern_properties=dict_0, property_names=field_1)
    except BaseException:
        pass

def test_case_87():
    try:
        time_0 = module_0.Time()
        str_0 = ', start_positio\n='
        array_0 = module_0.Array(time_0)
        var_0 = [array_0, time_0, str_0]
        any_0 = array_0.validate(var_0)
    except BaseException:
        pass

def test_case_88():
    try:
        float_0 = 1803.6
        number_0 = module_0.Number(exclusive_minimum=float_0, exclusive_maximum=float_0)
        str_0 = ''
        int_0 = -1477
        bool_0 = None
        date_time_0 = module_0.DateTime()
        object_0 = module_0.Object(additional_properties=bool_0, property_names=date_time_0, min_properties=int_0)
        str_1 = 'L\'4Vh!R7Q_|hE\x0c"u\t|B_'
        dict_0 = {str_0: date_time_0, str_1: object_0}
        any_0 = object_0.validate(dict_0, strict=bool_0)
    except BaseException:
        pass

def test_case_89():
    try:
        tuple_0 = None
        object_0 = module_0.Object()
        const_0 = module_0.Const(tuple_0)
        any_0 = const_0.validate(object_0)
    except BaseException:
        pass

def test_case_90():
    try:
        date_time_0 = module_0.DateTime()
        tuple_0 = (date_time_0, date_time_0)
        array_0 = module_0.Array(tuple_0)
        decimal_0 = module_1.Decimal()
        number_0 = module_0.Number(exclusive_maximum=decimal_0)
        any_0 = array_0.serialize(decimal_0)
    except BaseException:
        pass

def test_case_91():
    try:
        array_0 = module_0.Array()
        int_0 = 1
        int_1 = [int_0]
        any_0 = array_0.validate(int_1)
        array_1 = module_0.Array(any_0)
    except BaseException:
        pass

def test_case_92():
    try:
        str_0 = ''
        string_0 = module_0.String()
        integer_0 = module_0.Integer()
        var_0 = {str_0: string_0, str_0: integer_0}
        object_0 = module_0.Object(properties=var_0, required=str_0)
        str_1 = {integer_0: str_0, str_0: str_0}
        any_0 = object_0.validate(str_1)
    except BaseException:
        pass

def test_case_93():
    try:
        str_0 = '3'
        string_0 = module_0.String()
        integer_0 = module_0.Integer()
        var_0 = {str_0: string_0, str_0: integer_0}
        object_0 = module_0.Object(properties=var_0, required=str_0)
        str_1 = {integer_0: str_0, str_0: str_0}
        any_0 = object_0.validate(str_1)
    except BaseException:
        pass

def test_case_94():
    try:
        array_0 = module_0.Array()
        int_0 = 1
        int_1 = []
        any_0 = array_0.serialize(array_0)
        array_1 = module_0.Array(any_0)
        var_0 = [int_0, int_1, any_0]
        any_1 = array_1.validate(var_0)
    except BaseException:
        pass

def test_case_95():
    try:
        var_0 = None
        bool_0 = True
        text_0 = None
        date_0 = module_0.Date()
        array_0 = module_0.Array(var_0, bool_0, text_0, date_0)
    except BaseException:
        pass

def test_case_96():
    try:
        var_0 = []
        field_0 = module_0.Field()
        int_0 = -149
        array_0 = module_0.Array(field_0, field_0, int_0, int_0)
        any_0 = array_0.validate(var_0)
    except BaseException:
        pass

def test_case_97():
    try:
        time_0 = module_0.Time()
        array_0 = module_0.Array(time_0)
        var_0 = [array_0, array_0]
        bool_0 = True
        field_0 = module_0.Field(default=array_0, allow_null=bool_0)
        int_0 = -3839
        array_1 = module_0.Array(field_0, bool_0, int_0, bool_0)
        any_0 = array_1.validate(var_0)
    except BaseException:
        pass

def test_case_98():
    try:
        var_0 = []
        field_0 = module_0.Field()
        bool_0 = True
        array_0 = module_0.Array(field_0, field_0, bool_0)
        any_0 = array_0.validate(var_0)
    except BaseException:
        pass

def test_case_99():
    try:
        str_0 = 'H):'
        bool_0 = False
        dict_0 = {str_0: str_0, str_0: bool_0, str_0: str_0}
        field_0 = module_0.Field(allow_null=bool_0)
        list_0 = [dict_0, field_0, field_0]
        int_0 = 245
        tuple_0 = (list_0, int_0)
        choice_0 = module_0.Choice(choices=tuple_0)
    except BaseException:
        pass

def test_case_100():
    try:
        date_0 = module_0.Date()
        array_0 = module_0.Array()
        int_0 = []
        array_1 = module_0.Array(int_0)
        any_0 = array_0.serialize(array_1)
        field_0 = module_0.Field()
        any_1 = array_1.serialize(int_0)
        bool_0 = False
        any_2 = array_0.validate(bool_0)
    except BaseException:
        pass