# Automatically generated by Pynguin.
import typesystem.fields as module_0
import decimal as module_1

def test_case_0():
    try:
        dict_0 = {}
        str_0 = 'wFr3DuJm@\nBF:&i\tOk'
        bool_0 = True
        boolean_0 = module_0.Boolean(title=str_0, allow_null=bool_0)
        any_0 = boolean_0.validate(dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        field_0 = module_0.Field()
        bool_0 = True
        validation_result_0 = field_0.validate_or_error(field_0, strict=bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        array_0 = module_0.Array()
        any_0 = array_0.validate(array_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ''
        bool_0 = False
        string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_0, pattern=str_0, format=str_0)
        any_0 = string_0.serialize(string_0)
        bool_1 = True
        any_1 = string_0.validate(string_0, strict=bool_1)
    except BaseException:
        pass

def test_case_4():
    try:
        number_0 = module_0.Number()
        any_0 = number_0.validate(number_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = None
        number_0 = module_0.Number(maximum=int_0)
        any_0 = number_0.validate(int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'o\t.#6Tj62{#l61'
        number_0 = module_0.Number()
        any_0 = number_0.validate(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'o\t.#6Tj82{#l61'
        int_0 = 861
        number_0 = module_0.Number(maximum=int_0, precision=str_0)
        bool_0 = True
        any_0 = number_0.validate(str_0, strict=bool_0)
    except BaseException:
        pass

def test_case_8():
    try:
        boolean_0 = module_0.Boolean()
        any_0 = boolean_0.validate(boolean_0)
    except BaseException:
        pass

def test_case_9():
    try:
        boolean_0 = module_0.Boolean()
        boolean_1 = None
        any_0 = boolean_0.validate(boolean_1)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = None
        choice_0 = module_0.Choice()
        bool_0 = True
        any_0 = choice_0.validate(int_0, strict=bool_0)
    except BaseException:
        pass

def test_case_11():
    try:
        choice_0 = module_0.Choice()
        any_0 = choice_0.validate(choice_0)
    except BaseException:
        pass

def test_case_12():
    try:
        number_0 = None
        array_0 = module_0.Array(number_0)
        str_0 = 'C]|h`?x<,M,I#@!FWhP'
        field_0 = module_0.Field(title=str_0)
        union_0 = field_0.__or__(field_0)
        any_0 = union_0.validate(array_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'elo'
        bool_0 = True
        any_0 = module_0.Any()
        any_1 = any_0.validate(str_0, bool_0)
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        const_0 = module_0.Const(str_0, **dict_0)
    except BaseException:
        pass

def test_case_14():
    try:
        float_0 = 113.0919
        bool_0 = True
        const_0 = module_0.Const(float_0)
        any_0 = const_0.validate(float_0, bool_0)
        number_0 = module_0.Number(exclusive_maximum=float_0)
        any_1 = number_0.validate(float_0)
    except BaseException:
        pass

def test_case_15():
    try:
        field_0 = module_0.Field()
        float_0 = 4512.0
        number_0 = module_0.Number(multiple_of=float_0)
        any_0 = field_0.get_default_value()
        const_0 = module_0.Const(float_0)
        any_1 = const_0.validate(any_0)
    except BaseException:
        pass

def test_case_16():
    try:
        date_time_0 = module_0.DateTime()
        bool_0 = False
        none_type_0 = None
        decimal_0 = module_1.Decimal()
        float_0 = module_0.Float(exclusive_minimum=none_type_0, exclusive_maximum=decimal_0)
        field_0 = module_0.Field()
        any_0 = field_0.serialize(date_time_0)
        string_0 = module_0.String(max_length=date_time_0, format=bool_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'lo'
        str_1 = 'kONzx>hOJ6!'
        bool_0 = True
        boolean_0 = module_0.Boolean(title=str_1, allow_null=bool_0)
        any_0 = boolean_0.validate(str_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'L(\\N%\x0ce(r{C|Lh=X'
        field_0 = module_0.Field(title=str_0, description=str_0)
        dict_0 = {str_0: field_0}
        object_0 = module_0.Object(properties=dict_0, pattern_properties=dict_0, property_names=field_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = ''
        int_0 = 842
        field_0 = module_0.Field(title=str_0)
        array_0 = module_0.Array(field_0, field_0, int_0)
        number_0 = module_0.Number(minimum=int_0)
        any_0 = number_0.validate(array_0)
    except BaseException:
        pass

def test_case_20():
    try:
        field_0 = module_0.Field()
        list_0 = [field_0]
        none_type_0 = None
        array_0 = module_0.Array(list_0, none_type_0)
    except BaseException:
        pass

def test_case_21():
    try:
        dict_0 = {}
        dict_1 = None
        field_0 = module_0.Field(default=dict_1)
        array_0 = module_0.Array(field_0, **dict_0)
        any_0 = array_0.validate(dict_1)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = ''
        bool_0 = False
        string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_0, pattern=str_0, format=str_0)
        any_0 = string_0.validate(str_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = '^i$gulCe\x0cIZk42C&'
        bool_0 = True
        string_0 = module_0.String(pattern=str_0)
        any_0 = string_0.validate(str_0, strict=bool_0)
    except BaseException:
        pass

def test_case_24():
    try:
        dict_0 = None
        int_0 = -1365
        object_0 = module_0.Object(min_properties=int_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_25():
    try:
        dict_0 = {}
        dict_1 = None
        field_0 = module_0.Field(default=dict_1)
        union_0 = field_0.__or__(field_0)
        str_0 = 'j\x0b'
        object_0 = module_0.Object(property_names=union_0, required=str_0, **dict_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_26():
    try:
        bool_0 = True
        array_0 = module_0.Array(bool_0)
    except BaseException:
        pass

def test_case_27():
    try:
        list_0 = []
        union_0 = module_0.Union(list_0)
        date_0 = module_0.Date()
        bool_0 = True
        any_0 = union_0.validate(bool_0, bool_0)
    except BaseException:
        pass

def test_case_28():
    try:
        str_0 = 'kL(\\N%\x0ce(r{C|Lh=#X'
        field_0 = module_0.Field(title=str_0, description=str_0)
        dict_0 = {str_0: field_0}
        object_0 = module_0.Object(pattern_properties=dict_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_29():
    try:
        array_0 = module_0.Array()
        object_0 = module_0.Object()
        any_0 = object_0.validate(object_0)
    except BaseException:
        pass

def test_case_30():
    try:
        field_0 = None
        object_0 = module_0.Object(property_names=field_0)
        any_0 = object_0.validate(field_0)
    except BaseException:
        pass

def test_case_31():
    try:
        dict_0 = {}
        field_0 = None
        int_0 = -220
        object_0 = module_0.Object(property_names=field_0, max_properties=int_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_32():
    try:
        date_time_0 = module_0.DateTime()
        bool_0 = True
        bool_1 = True
        float_0 = 481.7833
        number_0 = module_0.Number(precision=bool_1, multiple_of=float_0)
        bool_2 = False
        any_0 = number_0.validate(bool_0, strict=bool_2)
    except BaseException:
        pass

def test_case_33():
    try:
        boolean_0 = module_0.Boolean()
        bool_0 = True
        field_0 = module_0.Field(default=boolean_0, allow_null=bool_0)
        field_1 = module_0.Field(default=boolean_0)
        union_0 = field_1.__or__(field_0)
        any_0 = boolean_0.validate(union_0)
    except BaseException:
        pass

def test_case_34():
    try:
        str_0 = 'L(\\N%\x0c*(r{C|L9=X'
        boolean_0 = module_0.Boolean()
        any_0 = boolean_0.validate(str_0)
    except BaseException:
        pass

def test_case_35():
    try:
        str_0 = ''
        int_0 = 842
        field_0 = module_0.Field(title=str_0)
        array_0 = module_0.Array(field_0, field_0, int_0)
        number_0 = module_0.Number(minimum=int_0)
        any_0 = array_0.serialize(int_0)
    except BaseException:
        pass

def test_case_36():
    try:
        str_0 = '\tMNtL!H#d1D9+b\tr`u'
        field_0 = module_0.Field()
        dict_0 = {}
        const_0 = module_0.Const(str_0, **dict_0)
        float_0 = 84.19372
        integer_0 = module_0.Integer(exclusive_minimum=const_0, precision=str_0, multiple_of=float_0)
    except BaseException:
        pass

def test_case_37():
    try:
        str_0 = '\tMNtL!H#Nd1D9+Jk\tr`u'
        int_0 = 821
        number_0 = module_0.Number(exclusive_minimum=int_0, precision=str_0, multiple_of=int_0)
        any_0 = number_0.validate(int_0)
    except BaseException:
        pass

def test_case_38():
    try:
        int_0 = 821
        number_0 = module_0.Number(maximum=int_0, exclusive_maximum=int_0)
        any_0 = number_0.validate(int_0)
    except BaseException:
        pass

def test_case_39():
    try:
        int_0 = None
        string_0 = module_0.String(min_length=int_0)
        any_0 = string_0.validate(int_0)
    except BaseException:
        pass

def test_case_40():
    try:
        date_time_0 = module_0.DateTime()
        any_0 = module_0.Any()
        bool_0 = False
        object_0 = module_0.Object(properties=date_time_0, additional_properties=bool_0)
        any_1 = object_0.validate(bool_0)
    except BaseException:
        pass

def test_case_41():
    try:
        str_0 = '\tMNtL!H#Nd1D9+Jk\tr`u'
        field_0 = module_0.Field()
        dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0}
        any_0 = module_0.Any(title=str_0)
        date_time_0 = module_0.DateTime()
        none_type_0 = None
        object_0 = module_0.Object(properties=dict_0, property_names=field_0, max_properties=date_time_0, required=none_type_0)
    except BaseException:
        pass

def test_case_42():
    try:
        date_time_0 = module_0.DateTime()
        bool_0 = True
        str_0 = "`'SEATv4SZpC.8QwK*"
        field_0 = module_0.Field(title=str_0)
        str_1 = "lQI'3_M1iH??APObLj"
        dict_0 = {str_0: field_0, str_1: field_0}
        object_0 = module_0.Object(properties=dict_0, pattern_properties=dict_0)
        bool_1 = False
        string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_1, min_length=field_0, pattern=str_0)
    except BaseException:
        pass

def test_case_43():
    try:
        date_time_0 = module_0.DateTime()
        date_0 = module_0.Date()
        str_0 = '\x0cNw1#Fg[7T\\r'
        field_0 = module_0.Field()
        str_1 = None
        str_2 = ')D]*4J\r#c]7&yO'
        field_1 = module_0.Field(description=str_2, default=str_1)
        str_3 = '/ug)4'
        dict_0 = {str_0: field_0, str_1: field_1, str_3: field_1}
        int_0 = None
        object_0 = module_0.Object(properties=dict_0, property_names=field_0, min_properties=int_0, max_properties=int_0)
    except BaseException:
        pass

def test_case_44():
    try:
        date_time_0 = module_0.DateTime()
        str_0 = 'dependencies'
        field_0 = None
        str_1 = 'qL1r##g"L.d)'
        dict_0 = {str_0: field_0, str_0: field_0, str_1: field_0}
        dict_1 = {field_0: dict_0}
        object_0 = module_0.Object(pattern_properties=dict_0, max_properties=dict_1)
    except BaseException:
        pass

def test_case_45():
    try:
        float_0 = 481.783
        number_0 = module_0.Number(exclusive_minimum=float_0, multiple_of=float_0)
        any_0 = number_0.validate(float_0)
    except BaseException:
        pass

def test_case_46():
    try:
        field_0 = module_0.Field()
        list_0 = []
        union_0 = module_0.Union(list_0)
        number_0 = module_0.Number()
        date_0 = module_0.Date()
        str_0 = ':7:'
        bool_0 = True
        boolean_0 = module_0.Boolean(title=str_0, default=list_0, allow_null=bool_0)
        number_1 = module_0.Number(minimum=boolean_0)
    except BaseException:
        pass

def test_case_47():
    try:
        text_0 = module_0.Text()
        dict_0 = {}
        time_0 = module_0.Time()
        str_0 = 'ZJe+0Ye\rPI@C]~4?ih?\t'
        field_0 = module_0.Field(description=str_0)
        decimal_0 = module_1.Decimal(**dict_0)
        float_0 = module_0.Float(exclusive_maximum=decimal_0, **dict_0)
        union_0 = field_0.__or__(field_0)
        optional_0 = None
        bool_0 = True
        dict_1 = {float_0: dict_0, bool_0: optional_0}
        object_0 = module_0.Object(properties=optional_0, pattern_properties=dict_1)
    except BaseException:
        pass

def test_case_48():
    try:
        field_0 = module_0.Field()
        number_0 = module_0.Number()
        str_0 = 'i\x0b?'
        dict_0 = {}
        object_0 = module_0.Object(min_properties=str_0, **dict_0)
    except BaseException:
        pass

def test_case_49():
    try:
        boolean_0 = module_0.Boolean()
        time_0 = module_0.Time()
        bool_0 = True
        any_0 = boolean_0.validate(time_0, strict=bool_0)
    except BaseException:
        pass

def test_case_50():
    try:
        str_0 = None
        boolean_0 = module_0.Boolean(description=str_0)
    except BaseException:
        pass

def test_case_51():
    try:
        bool_0 = False
        field_0 = module_0.Field(allow_null=bool_0)
        bool_1 = field_0.has_default()
        bool_2 = False
        text_0 = module_0.Text()
        union_0 = field_0.__or__(field_0)
        int_0 = -1138
        array_0 = module_0.Array(field_0, bool_1, int_0)
        date_time_0 = module_0.DateTime()
        str_0 = None
        any_0 = module_0.Any(title=str_0, allow_null=bool_2)
    except BaseException:
        pass

def test_case_52():
    try:
        int_0 = 821
        str_0 = ''
        number_0 = module_0.Number(exclusive_maximum=int_0, precision=str_0)
        any_0 = number_0.validate(str_0)
    except BaseException:
        pass

def test_case_53():
    try:
        str_0 = '`((Abr4\\<!ZN!\x0bi=?'
        bool_0 = False
        bool_1 = True
        int_0 = -2690
        string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_1, max_length=int_0)
        any_0 = string_0.validate(str_0, strict=bool_0)
    except BaseException:
        pass

def test_case_54():
    try:
        text_0 = module_0.Text()
        dict_0 = {}
        time_0 = module_0.Time()
        optional_0 = None
        object_0 = module_0.Object(pattern_properties=optional_0, **dict_0)
        str_0 = '\x0b'
        float_0 = -1092.0
        number_0 = module_0.Number(maximum=time_0, precision=str_0, multiple_of=float_0, **dict_0)
    except BaseException:
        pass

def test_case_55():
    try:
        field_0 = module_0.Field()
        object_0 = module_0.Object(property_names=field_0)
        dict_0 = {}
        text_0 = module_0.Text(**dict_0)
        number_0 = module_0.Number(exclusive_maximum=text_0, **dict_0)
    except BaseException:
        pass

def test_case_56():
    try:
        field_0 = module_0.Field()
        time_0 = module_0.Time()
        number_0 = module_0.Number(multiple_of=time_0)
    except BaseException:
        pass

def test_case_57():
    try:
        int_0 = None
        list_0 = None
        object_0 = module_0.Object(properties=list_0)
        bool_0 = True
        dict_0 = {}
        const_0 = module_0.Const(list_0, **dict_0)
        string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_0, max_length=int_0, pattern=const_0)
    except BaseException:
        pass

def test_case_58():
    try:
        field_0 = module_0.Field()
        float_0 = 4103.5
        str_0 = ':7:'
        number_0 = module_0.Number(precision=str_0, multiple_of=float_0)
        list_0 = [str_0, float_0, field_0]
        object_0 = module_0.Object(properties=number_0, required=list_0)
    except BaseException:
        pass

def test_case_59():
    try:
        float_0 = 2240.97
        int_0 = -120
        number_0 = module_0.Number(minimum=float_0, exclusive_minimum=float_0, multiple_of=int_0)
        bool_0 = False
        any_0 = number_0.validate(int_0, strict=bool_0)
    except BaseException:
        pass

def test_case_60():
    try:
        str_0 = 'qZ<\n7;%+B]fi@'
        field_0 = module_0.Field(title=str_0, description=str_0)
        dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0}
        object_0 = module_0.Object(properties=dict_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_61():
    try:
        dict_0 = {}
        optional_0 = None
        decimal_0 = module_0.Decimal()
        any_0 = decimal_0.serialize(optional_0)
        field_0 = None
        object_0 = module_0.Object(property_names=field_0)
        int_0 = 821
        str_0 = '1"\nbXF\x0bNjr'
        number_0 = module_0.Number(minimum=int_0, maximum=int_0, precision=str_0, **dict_0)
        bool_0 = False
        array_0 = module_0.Array(field_0, field_0, bool_0)
    except BaseException:
        pass

def test_case_62():
    try:
        str_0 = 'kL(\\N%\x0ce(r{C|Lh=#X'
        field_0 = module_0.Field(title=str_0, description=str_0)
        dict_0 = {str_0: field_0}
        int_0 = 236
        object_0 = module_0.Object(min_properties=int_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_63():
    try:
        str_0 = 'o\t.#6Tj62{#l61'
        float_0 = 482.29181581566127
        str_1 = ':7:'
        number_0 = module_0.Number(precision=str_1, multiple_of=float_0)
        field_0 = None
        str_2 = '<Bj'
        dict_0 = {str_1: field_0, str_0: field_0, str_2: field_0, str_2: field_0}
        object_0 = module_0.Object(properties=dict_0)
    except BaseException:
        pass

def test_case_64():
    try:
        boolean_0 = module_0.Boolean()
        bool_0 = False
        dict_0 = {}
        choice_0 = module_0.Choice(**dict_0)
        dict_1 = {boolean_0: bool_0}
        dict_2 = {}
        string_0 = module_0.String(allow_blank=bool_0, format=dict_1, **dict_2)
    except BaseException:
        pass

def test_case_65():
    try:
        dict_0 = {}
        optional_0 = None
        object_0 = module_0.Object(pattern_properties=optional_0, **dict_0)
        tuple_0 = ()
        object_1 = module_0.Object(additional_properties=tuple_0)
    except BaseException:
        pass

def test_case_66():
    try:
        str_0 = ''
        bool_0 = True
        string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_0, pattern=str_0, format=str_0)
        any_0 = string_0.validate(str_0)
        any_1 = string_0.validate(string_0, strict=bool_0)
    except BaseException:
        pass

def test_case_67():
    try:
        dict_0 = None
        int_0 = -1365
        str_0 = ''
        number_0 = module_0.Number(minimum=int_0, exclusive_minimum=int_0, exclusive_maximum=int_0, precision=str_0)
        bool_0 = None
        field_0 = module_0.Field()
        list_0 = [field_0, field_0]
        union_0 = module_0.Union(list_0)
        any_0 = union_0.validate(dict_0, bool_0)
    except BaseException:
        pass

def test_case_68():
    try:
        dict_0 = {}
        object_0 = module_0.Object()
        bool_0 = False
        any_0 = object_0.validate(dict_0, strict=bool_0)
        str_0 = 'kgFe|rB}\\'
        dict_1 = {bool_0: object_0}
        list_0 = [object_0, str_0]
        list_1 = [dict_1, list_0, any_0]
        date_time_0 = module_0.DateTime()
        array_0 = module_0.Array(list_1, date_time_0)
    except BaseException:
        pass

def test_case_69():
    try:
        int_0 = 1293
        bool_0 = True
        field_0 = module_0.Field(default=int_0, allow_null=bool_0)
        dict_0 = {}
        number_0 = module_0.Number(maximum=int_0, exclusive_minimum=int_0, **dict_0)
        int_1 = 2810
        str_0 = 'w\x0cF9Okj(LJ<$'
        bool_1 = False
        field_1 = module_0.Field(title=str_0, default=str_0, allow_null=bool_1)
        any_0 = field_1.serialize(int_0)
        bool_2 = True
        any_1 = number_0.validate(int_1, strict=bool_2)
    except BaseException:
        pass

def test_case_70():
    try:
        date_time_0 = module_0.DateTime()
        bool_0 = False
        str_0 = 'kL(\\N%\x0ce(r{C|Lh=#X'
        field_0 = module_0.Field(title=str_0, description=str_0)
        int_0 = 236
        string_0 = module_0.String(trim_whitespace=bool_0, max_length=int_0, min_length=int_0)
        any_0 = string_0.validate(str_0)
    except BaseException:
        pass

def test_case_71():
    try:
        int_0 = None
        array_0 = module_0.Array(int_0)
        any_0 = array_0.validate(int_0)
    except BaseException:
        pass

def test_case_72():
    try:
        dict_0 = None
        bool_0 = True
        string_0 = module_0.String(allow_blank=bool_0)
        any_0 = string_0.validate(dict_0, strict=bool_0)
    except BaseException:
        pass

def test_case_73():
    try:
        int_0 = None
        number_0 = module_0.Number(maximum=int_0)
        const_0 = module_0.Const(int_0)
        any_0 = const_0.validate(number_0)
    except BaseException:
        pass

def test_case_74():
    try:
        dict_0 = {}
        bool_0 = False
        choice_0 = module_0.Choice()
        optional_0 = None
        none_type_0 = None
        object_0 = module_0.Object(properties=choice_0, pattern_properties=optional_0, max_properties=none_type_0)
        field_0 = module_0.Field(default=bool_0, allow_null=bool_0)
        str_0 = '>N%bsmKA;t"*#3'
        array_0 = module_0.Array(field_0, field_0, str_0, **dict_0)
    except BaseException:
        pass

def test_case_75():
    try:
        int_0 = 824
        number_0 = module_0.Number(multiple_of=int_0)
        any_0 = number_0.validate(int_0)
        any_1 = number_0.validate(any_0)
        bool_0 = True
        date_time_0 = None
        str_0 = 'v1/bP'
        bool_1 = True
        field_0 = module_0.Field(title=str_0, description=str_0, allow_null=bool_1)
        str_1 = ':o}SY8<a<g@A'
        field_1 = module_0.Field(title=str_1, default=number_0, allow_null=bool_0)
        union_0 = field_1.__or__(field_0)
        any_2 = union_0.validate(date_time_0, bool_0)
        str_2 = 'pUS\x0by**`H0'
        string_0 = module_0.String(trim_whitespace=bool_0, format=str_2)
        any_3 = string_0.validate(int_0)
    except BaseException:
        pass

def test_case_76():
    try:
        int_0 = 824
        number_0 = module_0.Number(multiple_of=int_0)
        any_0 = number_0.validate(int_0)
        any_1 = number_0.validate(any_0)
        bool_0 = True
        str_0 = 'v1/bP'
        bool_1 = True
        field_0 = module_0.Field(title=str_0, description=str_0, allow_null=bool_1)
        str_1 = ':o}SY8<a<g@A'
        field_1 = module_0.Field(title=str_1, default=number_0, allow_null=bool_0)
        int_1 = 697
        any_2 = number_0.validate(int_1)
    except BaseException:
        pass

def test_case_77():
    try:
        str_0 = 'kL(\\N%\x0ce(r{C|Lh=#X'
        field_0 = module_0.Field(title=str_0, description=str_0)
        dict_0 = {}
        object_0 = module_0.Object(pattern_properties=dict_0)
        bytes_0 = b'\xe9\x90J\x97\xb1S\xc2\x80`^\x94\xe5,M\xf3\xad'
        dict_1 = {object_0: field_0, object_0: bytes_0, bytes_0: object_0}
        any_0 = object_0.validate(dict_1)
    except BaseException:
        pass

def test_case_78():
    try:
        text_0 = None
        bool_0 = True
        bool_1 = False
        str_0 = 'SW}D'
        string_0 = module_0.String(allow_blank=bool_0, pattern=str_0, format=str_0)
        any_0 = string_0.validate(text_0)
        str_1 = None
        date_time_0 = module_0.DateTime()
        str_2 = 'tX=+u(`p84J,>Nm-Uq'
        dict_0 = {str_1: date_time_0, str_2: date_time_0}
        string_1 = module_0.String(trim_whitespace=bool_1, **dict_0)
    except BaseException:
        pass

def test_case_79():
    try:
        str_0 = '=Wd+$GM'
        field_0 = module_0.Field(title=str_0, description=str_0)
        dict_0 = {str_0: field_0, str_0: field_0}
        object_0 = module_0.Object(additional_properties=field_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_80():
    try:
        bytes_0 = b'H^\xb6\xe4X,\xe3\x82\xf6s9\x9c\x1cy'
        str_0 = 'max_properties'
        bool_0 = True
        boolean_0 = module_0.Boolean(description=str_0, allow_null=bool_0)
        array_0 = module_0.Array(boolean_0)
        any_0 = array_0.serialize(bytes_0)
        bool_1 = False
        field_0 = module_0.Field(allow_null=bool_1)
        bool_2 = True
        field_1 = module_0.Field(default=bytes_0, allow_null=bool_2)
        union_0 = field_1.__or__(field_0)
        decimal_0 = module_1.Decimal()
        boolean_1 = module_0.Boolean(default=decimal_0)
        any_1 = boolean_1.validate(union_0)
    except BaseException:
        pass

def test_case_81():
    try:
        str_0 = 'pdTrs+'
        field_0 = module_0.Field(title=str_0, description=str_0)
        dict_0 = {str_0: field_0}
        object_0 = module_0.Object(pattern_properties=dict_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_82():
    try:
        int_0 = 821
        str_0 = '8'
        number_0 = module_0.Number(exclusive_maximum=int_0, precision=str_0)
        any_0 = number_0.validate(str_0)
    except BaseException:
        pass

def test_case_83():
    try:
        text_0 = module_0.Text()
        string_0 = module_0.String()
        number_0 = module_0.Number()
        var_0 = [string_0, text_0]
        bool_0 = True
        array_0 = module_0.Array(var_0, bool_0)
        var_1 = [var_0]
        any_0 = array_0.validate(var_1)
    except BaseException:
        pass

def test_case_84():
    try:
        var_0 = []
        bool_0 = False
        array_0 = module_0.Array(var_0, bool_0)
        int_0 = -1
        int_1 = 2
        int_2 = [int_0, int_1]
        any_0 = array_0.validate(int_2)
    except BaseException:
        pass

def test_case_85():
    try:
        text_0 = module_0.Text()
        var_0 = None
        string_0 = module_0.String()
        number_0 = module_0.Number()
        var_1 = [string_0, text_0]
        bool_0 = True
        array_0 = module_0.Array(var_1, bool_0)
        any_0 = array_0.validate(var_1)
    except BaseException:
        pass

def test_case_86():
    try:
        field_0 = module_0.Field()
        bool_0 = True
        array_0 = module_0.Array(field_0, bool_0)
        str_0 = '{kcv'
        var_0 = [str_0]
        any_0 = array_0.validate(var_0)
    except BaseException:
        pass

def test_case_87():
    try:
        str_0 = 'uuid'
        string_0 = module_0.String(format=str_0)
        array_0 = module_0.Array(string_0)
        str_1 = '.nKF9Vg|0v"lI[/Y'
        str_2 = 'test5'
        str_3 = [str_2, str_1, str_0, str_2, str_1, str_1, str_1, str_0]
        any_0 = array_0.validate(str_3)
    except BaseException:
        pass

def test_case_88():
    try:
        var_0 = None
        string_0 = module_0.String()
        number_0 = module_0.Number()
        var_1 = [string_0, number_0]
        bool_0 = False
        array_0 = module_0.Array(var_1, bool_0)
        str_0 = 'a'
        int_0 = 2
        any_0 = string_0.serialize(int_0)
        var_2 = [str_0, var_0]
        any_1 = array_0.validate(var_2)
    except BaseException:
        pass

def test_case_89():
    try:
        var_0 = []
        bool_0 = True
        array_0 = module_0.Array(var_0, bool_0)
        any_0 = array_0.serialize(bool_0)
    except BaseException:
        pass

def test_case_90():
    try:
        var_0 = None
        string_0 = module_0.String()
        number_0 = module_0.Number()
        var_1 = [string_0, number_0]
        bool_0 = True
        array_0 = module_0.Array(var_1, bool_0)
        str_0 = 'a'
        any_0 = array_0.serialize(str_0)
        var_2 = [var_0, var_0]
        any_1 = array_0.validate(var_2)
    except BaseException:
        pass

def test_case_91():
    try:
        var_0 = []
        bool_0 = True
        array_0 = module_0.Array(var_0, bool_0)
        any_0 = array_0.validate(var_0, strict=bool_0)
        var_1 = []
        any_1 = array_0.serialize(var_1)
        var_2 = array_0.valid
    except BaseException:
        pass

def test_case_92():
    try:
        float_0 = 100.75605991686099
        number_0 = module_0.Number(multiple_of=float_0)
        int_0 = 5379
        bool_0 = True
        any_0 = number_0.validate(int_0, strict=bool_0)
    except BaseException:
        pass

def test_case_93():
    try:
        int_0 = 7
        field_0 = module_0.Field(default=int_0)
        any_0 = field_0.get_default_value()
        var_0 = lambda : int_0
        field_1 = module_0.Field(default=var_0)
        any_1 = field_1.get_default_value()
    except BaseException:
        pass

def test_case_94():
    try:
        bool_0 = False
        integer_0 = module_0.Integer()
        var_0 = [integer_0]
        union_0 = module_0.Union(var_0)
        any_0 = union_0.validate(var_0, bool_0)
    except BaseException:
        pass

def test_case_95():
    try:
        string_0 = module_0.String()
        string_1 = [string_0]
        union_0 = module_0.Union(string_1)
        str_0 = 'Hello World!'
        int_0 = 5
        any_0 = union_0.validate(str_0)
        var_0 = print(any_0)
        any_1 = union_0.validate(int_0)
    except BaseException:
        pass

def test_case_96():
    try:
        integer_0 = module_0.Integer()
        string_0 = module_0.String()
        var_0 = [integer_0, string_0]
        union_0 = module_0.Union(var_0)
        int_0 = 10
        any_0 = union_0.validate(int_0)
        var_1 = any_0 == int_0
        str_0 = 's'
        any_1 = union_0.validate(str_0)
        var_2 = any_1 == str_0
        str_1 = ''
        any_2 = union_0.validate(str_1)
    except BaseException:
        pass