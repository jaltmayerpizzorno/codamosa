# Automatically generated by Pynguin.
import typesystem.fields as module_0
import decimal as module_1
import re as module_2

def test_case_0():
    try:
        field_0 = module_0.Field()
        union_0 = field_0.__or__(field_0)
        any_0 = field_0.validate(field_0)
    except BaseException:
        pass

def test_case_1():
    try:
        field_0 = module_0.Field()
        union_0 = field_0.__or__(field_0)
        any_0 = union_0.validate(field_0)
    except BaseException:
        pass

def test_case_2():
    try:
        field_0 = module_0.Field()
        union_0 = field_0.__or__(field_0)
        any_0 = field_0.serialize(field_0)
        any_1 = union_0.validate(union_0)
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
        float_0 = 2496.61
        number_0 = module_0.Number(maximum=float_0, exclusive_minimum=float_0)
        any_0 = number_0.validate(float_0)
    except BaseException:
        pass

def test_case_5():
    try:
        field_0 = module_0.Field()
        int_0 = -1093
        decimal_0 = module_0.Decimal(exclusive_maximum=int_0)
        any_0 = decimal_0.serialize(field_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'ozt'
        boolean_0 = module_0.Boolean(description=str_0)
        any_0 = boolean_0.validate(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        date_0 = module_0.Date()
        str_0 = ')qt>>!2xu'
        field_0 = module_0.Field(title=str_0)
        str_1 = 'url'
        bool_0 = False
        boolean_0 = module_0.Boolean(description=str_1, default=str_1, allow_null=bool_0)
        bool_1 = True
        any_0 = boolean_0.validate(bool_0, strict=bool_1)
        str_2 = '(text='
        bool_2 = False
        field_1 = module_0.Field(title=str_1, description=str_2, allow_null=bool_2)
        field_2 = module_0.Field(allow_null=bool_1)
        union_0 = field_2.__or__(field_1)
        optional_0 = None
        array_0 = module_0.Array(field_2, bool_2, optional_0)
        any_1 = boolean_0.validate(date_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'not'
        bool_0 = None
        choice_0 = module_0.Choice(choices=str_0)
        any_0 = choice_0.validate(bool_0)
    except BaseException:
        pass

def test_case_9():
    try:
        array_0 = module_0.Array()
        choice_0 = module_0.Choice()
        any_0 = choice_0.validate(array_0)
    except BaseException:
        pass

def test_case_10():
    try:
        object_0 = module_0.Object()
        bool_0 = True
        string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_0)
        any_0 = object_0.validate(bool_0)
    except BaseException:
        pass

def test_case_11():
    try:
        object_0 = module_0.Object()
        field_0 = None
        any_0 = object_0.validate(field_0)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = -149
        array_0 = module_0.Array(int_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'ozt'
        any_0 = module_0.Any()
        any_1 = any_0.validate(str_0)
        bool_0 = None
        field_0 = module_0.Field(allow_null=bool_0)
        dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
        object_0 = module_0.Object(properties=dict_0, additional_properties=field_0)
        any_2 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_14():
    try:
        decimal_0 = module_0.Decimal()
        array_0 = module_0.Array()
        const_0 = module_0.Const(array_0)
        any_0 = array_0.validate(const_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'iw'
        bool_0 = True
        string_0 = module_0.String(trim_whitespace=bool_0, format=str_0)
        any_0 = string_0.serialize(bool_0)
        const_0 = module_0.Const(string_0)
        any_1 = const_0.validate(str_0, bool_0)
    except BaseException:
        pass

def test_case_16():
    try:
        date_time_0 = module_0.DateTime()
        str_0 = None
        field_0 = module_0.Field(description=str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        int_0 = 2276
        object_0 = module_0.Object(max_properties=int_0)
        bool_0 = True
        field_0 = module_0.Field(default=int_0, allow_null=bool_0)
        array_0 = module_0.Array(int_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = None
        any_0 = module_0.Any(title=str_0)
    except BaseException:
        pass

def test_case_19():
    try:
        bool_0 = True
        const_0 = module_0.Const(bool_0)
        string_0 = module_0.String(trim_whitespace=bool_0, max_length=const_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = 'AZDeZS*3A;qD~/KaO4r,'
        float_0 = 584.918
        decimal_0 = module_0.Decimal(multiple_of=float_0)
        number_0 = module_0.Number(precision=decimal_0, multiple_of=float_0)
        choice_0 = module_0.Choice()
        dict_0 = {}
        time_0 = module_0.Time(**dict_0)
        string_0 = module_0.String(min_length=time_0, pattern=str_0, **dict_0)
    except BaseException:
        pass

def test_case_21():
    try:
        int_0 = 4
        integer_0 = module_0.Integer()
        array_0 = module_0.Array(integer_0)
        int_1 = [int_0, int_0, int_0, int_0, int_0]
        date_time_0 = module_0.DateTime()
        any_0 = array_0.validate(int_1)
        dict_0 = {}
        number_0 = module_0.Number(minimum=int_1, maximum=int_1, **dict_0)
    except BaseException:
        pass

def test_case_22():
    try:
        date_time_0 = module_0.DateTime()
        boolean_0 = module_0.Boolean()
        any_0 = boolean_0.validate(date_time_0)
    except BaseException:
        pass

def test_case_23():
    try:
        number_0 = module_0.Number()
        any_0 = number_0.validate(number_0)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = ''
        float_0 = None
        number_0 = module_0.Number(multiple_of=float_0)
        any_0 = number_0.validate(str_0)
    except BaseException:
        pass

def test_case_25():
    try:
        choice_0 = module_0.Choice()
        dict_0 = {}
        array_0 = module_0.Array(**dict_0)
        set_0 = {choice_0, choice_0, array_0, array_0}
        bool_0 = True
        date_time_0 = module_0.DateTime()
        str_0 = '%~>3Z"F\rn\\mWJ|T'
        field_0 = module_0.Field(title=str_0, default=set_0)
        any_0 = field_0.get_default_value()
        string_0 = module_0.String(allow_blank=bool_0, format=date_time_0)
    except BaseException:
        pass

def test_case_26():
    try:
        str_0 = 'kg$l5ys9R9,\\Z#'
        bool_0 = True
        string_0 = module_0.String(trim_whitespace=bool_0, format=str_0)
        any_0 = string_0.validate(str_0)
        bool_1 = False
        any_1 = string_0.validate(bool_0, strict=bool_1)
    except BaseException:
        pass

def test_case_27():
    try:
        str_0 = 'nJ"5;U\\'
        tuple_0 = (str_0,)
        str_1 = 'E8gJEm'
        bool_0 = True
        list_0 = [str_0, str_1, bool_0, str_0]
        str_2 = 'mhq4,AF t,$ S'
        array_0 = module_0.Array()
        any_0 = array_0.serialize(list_0)
        str_3 = None
        dict_0 = {str_1: tuple_0, str_2: str_1, str_3: str_2, str_1: bool_0}
        object_0 = module_0.Object()
        any_1 = array_0.serialize(str_3)
        decimal_0 = module_1.Decimal(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_28():
    try:
        date_0 = module_0.Date()
        tuple_0 = (date_0,)
        int_0 = -1668
        array_0 = module_0.Array(tuple_0, int_0)
    except BaseException:
        pass

def test_case_29():
    try:
        field_0 = None
        string_0 = module_0.String()
        any_0 = string_0.validate(field_0)
    except BaseException:
        pass

def test_case_30():
    try:
        str_0 = 'k'
        int_0 = 3
        string_0 = module_0.String(min_length=int_0, pattern=str_0)
        bool_0 = True
        any_0 = module_0.Any(allow_null=bool_0)
        any_1 = string_0.serialize(string_0)
        field_0 = None
        const_0 = module_0.Const(field_0)
        any_2 = const_0.validate(string_0)
    except BaseException:
        pass

def test_case_31():
    try:
        str_0 = 'not'
        bool_0 = None
        field_0 = module_0.Field(allow_null=bool_0)
        dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
        object_0 = module_0.Object(properties=dict_0, additional_properties=field_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_32():
    try:
        str_0 = 'not'
        bool_0 = None
        field_0 = module_0.Field(allow_null=bool_0)
        dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
        object_0 = module_0.Object(pattern_properties=dict_0, additional_properties=bool_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_33():
    try:
        object_0 = module_0.Object()
        bool_0 = False
        int_0 = 0
        string_0 = module_0.String(allow_blank=bool_0, min_length=int_0)
        any_0 = string_0.serialize(object_0)
        field_0 = module_0.Field()
        union_0 = field_0.__or__(field_0)
        number_0 = module_0.Number(exclusive_minimum=int_0, precision=union_0)
        any_1 = number_0.validate(bool_0)
    except BaseException:
        pass

def test_case_34():
    try:
        array_0 = module_0.Array()
        bool_0 = True
        str_0 = '\\S'
        bool_1 = True
        boolean_0 = module_0.Boolean(title=str_0, allow_null=bool_1)
        any_0 = boolean_0.validate(array_0, strict=bool_0)
    except BaseException:
        pass

def test_case_35():
    try:
        str_0 = '|JXbF(\\j_\x0b:D)9'
        string_0 = module_0.String(pattern=str_0, format=str_0)
    except BaseException:
        pass

def test_case_36():
    try:
        str_0 = 'nJ"5;U\\'
        str_1 = 'E8gJEm'
        bool_0 = True
        list_0 = [str_0, str_1, bool_0]
        str_2 = 'mhq4,F $ S'
        array_0 = module_0.Array()
        any_0 = array_0.serialize(list_0)
        str_3 = None
        field_0 = module_0.Field()
        str_4 = '[9c?MwSTq \x0bS:qOWy'
        dict_0 = {str_2: field_0, str_4: field_0, str_3: field_0, str_0: field_0}
        any_1 = module_0.Any()
        date_0 = module_0.Date()
        object_0 = module_0.Object(pattern_properties=dict_0, min_properties=any_1, max_properties=date_0)
    except BaseException:
        pass

def test_case_37():
    try:
        bool_0 = None
        string_0 = module_0.String(trim_whitespace=bool_0)
        any_0 = module_0.Any()
        any_1 = any_0.validate(string_0)
        any_2 = string_0.serialize(string_0)
        field_0 = module_0.Field()
        any_3 = field_0.serialize(string_0)
        text_0 = module_0.Text()
        integer_0 = module_0.Integer(exclusive_minimum=text_0)
    except BaseException:
        pass

def test_case_38():
    try:
        float_0 = None
        float_1 = None
        str_0 = ''
        string_0 = module_0.String(pattern=str_0)
        any_0 = string_0.serialize(float_0)
        int_0 = -745
        int_1 = 1526
        field_0 = module_0.Field(default=float_0)
        bool_0 = True
        array_0 = module_0.Array(float_1, field_0, int_0, int_1, bool_0)
        str_1 = '3%4RWz'
        str_2 = 'xZWjuR3kSI'
        str_3 = None
        dict_0 = {str_1: field_0, str_1: field_0, str_2: field_0, str_3: field_0}
        object_0 = module_0.Object(properties=dict_0, min_properties=int_1)
    except BaseException:
        pass

def test_case_39():
    try:
        dict_0 = {}
        int_0 = 0
        str_0 = '$Pwd1)'
        object_0 = module_0.Object(min_properties=int_0, max_properties=int_0, required=str_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_40():
    try:
        str_0 = 'nJ"5;U\\'
        str_1 = 'E8gJEm'
        bool_0 = True
        list_0 = [str_0, str_1, bool_0]
        array_0 = module_0.Array()
        any_0 = array_0.serialize(list_0)
        object_0 = module_0.Object()
        date_0 = module_0.Date()
        object_1 = module_0.Object(additional_properties=bool_0, max_properties=date_0)
    except BaseException:
        pass

def test_case_41():
    try:
        int_0 = 2276
        object_0 = module_0.Object(max_properties=int_0)
        bool_0 = False
        field_0 = None
        any_0 = object_0.validate(field_0, strict=bool_0)
    except BaseException:
        pass

def test_case_42():
    try:
        bool_0 = True
        str_0 = 'mhq4,AF t,$ S'
        array_0 = module_0.Array()
        float_0 = module_0.Float()
        float_1 = 2947.2748
        any_0 = module_0.Any(title=str_0, default=str_0, allow_null=bool_0)
        object_0 = module_0.Object(min_properties=any_0, required=float_1)
    except BaseException:
        pass

def test_case_43():
    try:
        str_0 = 'Op'
        bool_0 = True
        str_1 = 'I2>R\\-NbN~)$ms=Xu4f'
        string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_0, pattern=str_0, format=str_1)
        any_0 = string_0.serialize(bool_0)
        str_2 = 'k'
        field_0 = None
        str_3 = ''
        dict_0 = {str_2: field_0, str_3: field_0, str_1: field_0}
        object_0 = module_0.Object(pattern_properties=dict_0)
    except BaseException:
        pass

def test_case_44():
    try:
        str_0 = 'QW'
        boolean_0 = module_0.Boolean(title=str_0)
        int_0 = None
        any_0 = boolean_0.validate(int_0)
    except BaseException:
        pass

def test_case_45():
    try:
        float_0 = 2496.101658762347
        bool_0 = False
        field_0 = module_0.Field()
        str_0 = 'max_items'
        field_1 = module_0.Field(description=str_0, default=float_0, allow_null=bool_0)
        union_0 = field_1.__or__(field_0)
        string_0 = module_0.String(pattern=union_0)
    except BaseException:
        pass

def test_case_46():
    try:
        text_0 = module_0.Text()
        bool_0 = True
        field_0 = module_0.Field(allow_null=bool_0)
        bytes_0 = b'4\xf6'
        int_0 = -962
        array_0 = module_0.Array(text_0, field_0, bytes_0, int_0, int_0)
    except BaseException:
        pass

def test_case_47():
    try:
        str_0 = '\n`+\x0cR\x0b9(QW|@T'
        dict_0 = {str_0: str_0}
        int_0 = 3
        object_0 = module_0.Object(min_properties=int_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_48():
    try:
        str_0 = '+=~o:lySQU:'
        dict_0 = {str_0: str_0}
        int_0 = -30
        object_0 = module_0.Object(min_properties=int_0)
        any_0 = object_0.validate(dict_0)
        any_1 = object_0.validate(str_0)
    except BaseException:
        pass

def test_case_49():
    try:
        str_0 = 'field_id'
        tuple_0 = (str_0,)
        bool_0 = False
        list_0 = [str_0, str_0, bool_0, str_0]
        object_0 = module_0.Object()
        dict_0 = {}
        dict_1 = {object_0: list_0, bool_0: dict_0, str_0: object_0, tuple_0: dict_0, tuple_0: dict_0, str_0: bool_0}
        any_0 = object_0.validate(dict_1, strict=bool_0)
    except BaseException:
        pass

def test_case_50():
    try:
        str_0 = '\n`+\x0cR\x0b9(QW|@T'
        dict_0 = {str_0: str_0}
        int_0 = -13
        object_0 = module_0.Object(min_properties=int_0)
        object_1 = module_0.Object(property_names=object_0, min_properties=int_0)
        any_0 = object_1.validate(dict_0)
    except BaseException:
        pass

def test_case_51():
    try:
        str_0 = 'tag:yaml.org,2002:float'
        int_0 = -1034
        string_0 = module_0.String(max_length=int_0, format=str_0)
        any_0 = string_0.validate(str_0)
    except BaseException:
        pass

def test_case_52():
    try:
        float_0 = -2418.0
        number_0 = module_0.Number(minimum=float_0, exclusive_maximum=float_0)
        any_0 = number_0.validate(float_0)
    except BaseException:
        pass

def test_case_53():
    try:
        float_0 = 4004.734
        str_0 = '_=q{A |A6q6C'
        field_0 = module_0.Field(title=str_0)
        bool_0 = False
        field_1 = module_0.Field(allow_null=bool_0)
        int_0 = -608
        object_0 = module_0.Object(additional_properties=field_1, min_properties=int_0)
        array_0 = module_0.Array(field_0, object_0, bool_0)
        any_0 = array_0.serialize(float_0)
    except BaseException:
        pass

def test_case_54():
    try:
        float_0 = 2488.996751565038
        number_0 = module_0.Number(maximum=float_0, exclusive_maximum=float_0)
        any_0 = number_0.validate(float_0)
    except BaseException:
        pass

def test_case_55():
    try:
        str_0 = 'not'
        bool_0 = None
        float_0 = 478.632
        float_1 = module_0.Float(minimum=float_0, maximum=float_0, exclusive_maximum=float_0, precision=str_0, multiple_of=float_0)
        field_0 = module_0.Field(allow_null=bool_0)
        dict_0 = {}
        array_0 = module_0.Array(float_1, field_0, **dict_0)
        any_0 = array_0.serialize(str_0)
        field_1 = module_0.Field(allow_null=bool_0)
        union_0 = field_1.__or__(field_1)
        dict_1 = {str_0: field_1, str_0: field_1, str_0: field_1, str_0: field_1, str_0: field_1}
        object_0 = module_0.Object(pattern_properties=dict_1)
        any_1 = object_0.validate(bool_0)
    except BaseException:
        pass

def test_case_56():
    try:
        str_0 = ''
        bool_0 = True
        number_0 = module_0.Number()
        any_0 = number_0.validate(str_0, strict=bool_0)
    except BaseException:
        pass

def test_case_57():
    try:
        float_0 = None
        field_0 = module_0.Field()
        list_0 = [field_0, field_0, field_0]
        union_0 = module_0.Union(list_0)
        any_0 = union_0.validate(float_0)
    except BaseException:
        pass

def test_case_58():
    try:
        list_0 = []
        union_0 = module_0.Union(list_0)
        any_0 = union_0.validate(union_0)
    except BaseException:
        pass

def test_case_59():
    try:
        str_0 = 'E8gJEm'
        str_1 = '"w'
        int_0 = 2
        string_0 = module_0.String(max_length=int_0, pattern=str_0)
        any_0 = string_0.validate(str_1)
    except BaseException:
        pass

def test_case_60():
    try:
        float_0 = -3988.7366362041043
        float_1 = -3990.693484215178
        number_0 = module_0.Number(minimum=float_0, maximum=float_1, exclusive_minimum=float_1)
        any_0 = number_0.validate(float_0)
    except BaseException:
        pass

def test_case_61():
    try:
        str_0 = '"'
        bool_0 = True
        int_0 = 2
        string_0 = module_0.String(max_length=int_0, min_length=int_0)
        any_0 = string_0.validate(str_0, strict=bool_0)
    except BaseException:
        pass

def test_case_62():
    try:
        object_0 = module_0.Object()
        bool_0 = True
        boolean_0 = module_0.Boolean(allow_null=bool_0)
        any_0 = boolean_0.validate(boolean_0)
    except BaseException:
        pass

def test_case_63():
    try:
        str_0 = "\nJ\x0c+x9q!'w7\x0ci!)W"
        field_0 = module_0.Field(description=str_0)
        const_0 = module_0.Const(field_0)
        tuple_0 = ()
        number_0 = module_0.Number(exclusive_maximum=tuple_0, precision=str_0)
    except BaseException:
        pass

def test_case_64():
    try:
        object_0 = module_0.Object()
        list_0 = []
        array_0 = module_0.Array(list_0)
        decimal_0 = module_1.Decimal()
        optional_0 = None
        decimal_1 = module_0.Decimal(maximum=array_0, exclusive_maximum=decimal_0, precision=optional_0, multiple_of=decimal_0)
    except BaseException:
        pass

def test_case_65():
    try:
        decimal_0 = module_0.Decimal()
        str_0 = None
        object_0 = module_0.Object()
        any_0 = decimal_0.serialize(str_0)
        field_0 = module_0.Field()
        bool_0 = True
        string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_0)
        any_1 = string_0.validate(field_0)
    except BaseException:
        pass

def test_case_66():
    try:
        float_0 = 2496.101658762347
        str_0 = '@l(<.\\y6(/,_Z'
        number_0 = module_0.Number(minimum=float_0, exclusive_maximum=float_0, precision=str_0, multiple_of=float_0)
        any_0 = number_0.validate(float_0)
    except BaseException:
        pass

def test_case_67():
    try:
        int_0 = -446
        number_0 = module_0.Number(exclusive_minimum=int_0, precision=int_0, multiple_of=int_0)
        any_0 = number_0.validate(int_0)
    except BaseException:
        pass

def test_case_68():
    try:
        float_0 = None
        number_0 = module_0.Number(minimum=float_0, maximum=float_0, exclusive_minimum=float_0)
        any_0 = number_0.validate(float_0)
    except BaseException:
        pass

def test_case_69():
    try:
        dict_0 = {}
        str_0 = 'ajZY'
        str_1 = 'LpL 9O6A_Mtf-2'
        dict_1 = {str_0: dict_0, str_1: dict_0}
        field_0 = None
        int_0 = -3269
        object_0 = module_0.Object(properties=dict_0, pattern_properties=dict_0, additional_properties=field_0, max_properties=int_0)
        object_1 = module_0.Object(properties=dict_0, additional_properties=dict_1, property_names=field_0, required=object_0)
    except BaseException:
        pass

def test_case_70():
    try:
        float_0 = -3988.482204391818
        float_1 = None
        bool_0 = True
        number_0 = module_0.Number(exclusive_minimum=float_1, multiple_of=float_0)
        int_0 = -1331
        any_0 = number_0.validate(int_0, strict=bool_0)
    except BaseException:
        pass

def test_case_71():
    try:
        bool_0 = None
        array_0 = module_0.Array()
        any_0 = array_0.validate(bool_0, strict=bool_0)
    except BaseException:
        pass

def test_case_72():
    try:
        int_0 = 2276
        object_0 = module_0.Object(max_properties=int_0)
        int_1 = 1134
        number_0 = module_0.Number(multiple_of=int_0)
        any_0 = number_0.validate(int_1)
    except BaseException:
        pass

def test_case_73():
    try:
        float_0 = -3988.482204391818
        int_0 = 1134
        number_0 = module_0.Number(minimum=int_0)
        any_0 = number_0.validate(float_0)
    except BaseException:
        pass

def test_case_74():
    try:
        str_0 = '\n`+\x0cR\x0b9(QW|@T'
        dict_0 = {str_0: str_0}
        int_0 = 3
        object_0 = module_0.Object(min_properties=int_0)
        object_1 = module_0.Object(property_names=object_0, min_properties=int_0)
        any_0 = object_1.validate(dict_0)
    except BaseException:
        pass

def test_case_75():
    try:
        float_0 = -3987.3265781120163
        dict_0 = {}
        str_0 = 'z_lqt&4iR6BODmr'
        bool_0 = False
        field_0 = module_0.Field(description=str_0, allow_null=bool_0)
        dict_1 = {}
        decimal_0 = module_1.Decimal(**dict_1)
        number_0 = module_0.Number(maximum=float_0, exclusive_minimum=float_0, exclusive_maximum=decimal_0)
        integer_0 = module_0.Integer()
        text_0 = module_0.Text()
        tuple_0 = (number_0, integer_0, float_0, text_0)
        object_0 = module_0.Object(properties=dict_0, additional_properties=field_0, property_names=field_0, required=tuple_0)
    except BaseException:
        pass

def test_case_76():
    try:
        str_0 = '\n`+\x0cR\x0b9(QW|@T'
        bool_0 = True
        string_0 = module_0.String(allow_blank=bool_0)
        any_0 = string_0.validate(str_0)
        bool_1 = False
        any_1 = string_0.validate(bool_1, strict=bool_1)
    except BaseException:
        pass

def test_case_77():
    try:
        str_0 = 'ZUy}#R@h-%dK['
        int_0 = -30
        object_0 = module_0.Object(min_properties=int_0)
        field_0 = None
        dict_0 = {str_0: field_0, str_0: field_0}
        object_1 = module_0.Object(properties=dict_0, pattern_properties=dict_0, min_properties=int_0)
    except BaseException:
        pass

def test_case_78():
    try:
        str_0 = ''
        float_0 = None
        number_0 = module_0.Number(multiple_of=float_0)
        str_1 = 'Must be a string.'
        list_0 = [str_1, str_0, number_0, float_0]
        int_0 = 1700
        bool_0 = True
        array_0 = module_0.Array(list_0, int_0, bool_0)
    except BaseException:
        pass

def test_case_79():
    try:
        str_0 = '/!:;7gx{=0VX3YJ2U1'
        bool_0 = True
        field_0 = module_0.Field(title=str_0, allow_null=bool_0)
        any_0 = field_0.get_default_value()
        time_0 = module_0.Time()
        str_1 = 'Vlat0NcUpv$nm=\r1'
        str_2 = 'Rar!nQ'
        float_0 = module_0.Float(precision=str_1, multiple_of=str_2)
    except BaseException:
        pass

def test_case_80():
    try:
        str_0 = ''
        int_0 = -1034
        string_0 = module_0.String(max_length=int_0, format=str_0)
        any_0 = string_0.validate(str_0)
    except BaseException:
        pass

def test_case_81():
    try:
        float_0 = 2512.3514060511725
        number_0 = module_0.Number(exclusive_maximum=float_0)
        float_1 = 2419.7
        bool_0 = True
        any_0 = number_0.validate(float_1, strict=bool_0)
        any_1 = number_0.validate(number_0)
    except BaseException:
        pass

def test_case_82():
    try:
        object_0 = module_0.Object()
        list_0 = [object_0]
        array_0 = module_0.Array(list_0)
        str_0 = '@l(<.y\\y6(/,_Z'
        int_0 = -2236
        number_0 = module_0.Number(minimum=int_0, maximum=int_0, precision=str_0, multiple_of=int_0)
        any_0 = array_0.serialize(object_0)
    except BaseException:
        pass

def test_case_83():
    try:
        str_0 = 'nXot'
        bool_0 = None
        field_0 = module_0.Field(allow_null=bool_0)
        dict_0 = {str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0, str_0: field_0}
        dict_1 = None
        object_0 = module_0.Object(properties=dict_1, additional_properties=field_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_84():
    try:
        dict_0 = {}
        bool_0 = False
        int_0 = -39
        string_0 = module_0.String(allow_blank=bool_0, min_length=int_0)
        str_0 = '{DU)~.%h'
        object_0 = module_0.Object(min_properties=int_0, max_properties=int_0, required=str_0)
        any_0 = object_0.validate(dict_0, strict=bool_0)
    except BaseException:
        pass

def test_case_85():
    try:
        time_0 = module_0.Time()
        str_0 = 'BI/h~`d"FzdB=s'
        bool_0 = False
        field_0 = module_0.Field(title=str_0, default=str_0, allow_null=bool_0)
        any_0 = field_0.serialize(time_0)
        str_1 = "B%5'ul\x0c~c"
        bool_1 = None
        field_1 = module_0.Field(allow_null=bool_1)
        dict_0 = {str_1: field_1, str_1: field_1, str_1: field_1, str_1: field_1, str_1: field_1}
        str_2 = '7pN+x|ZV'
        dict_1 = {str_1: dict_0, str_2: dict_0}
        validation_error_0 = None
        tuple_0 = ()
        tuple_1 = (dict_1, validation_error_0, tuple_0)
        choice_0 = module_0.Choice(choices=tuple_1)
    except BaseException:
        pass

def test_case_86():
    try:
        str_0 = 'kuV@[O\t!W}F{>G.'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        int_0 = -1212
        bool_0 = False
        string_0 = module_0.String(allow_blank=bool_0, trim_whitespace=bool_0, min_length=int_0)
        any_0 = string_0.serialize(str_0)
        dict_1 = None
        float_0 = None
        object_0 = module_0.Object(properties=dict_1, pattern_properties=dict_1, additional_properties=bool_0, min_properties=int_0, required=float_0)
        any_1 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_87():
    try:
        str_0 = 'jO`e9t~B'
        dict_0 = {str_0: str_0, str_0: str_0}
        int_0 = -6
        dict_1 = None
        number_0 = module_0.Number(multiple_of=int_0)
        object_0 = module_0.Object(properties=dict_1, additional_properties=number_0)
        any_0 = object_0.validate(dict_0)
    except BaseException:
        pass

def test_case_88():
    try:
        str_0 = 'name'
        string_0 = module_0.String()
        string_1 = {str_0: string_0}
        object_0 = module_0.Object(properties=string_1)
        str_1 = 'John Doe'
        var_0 = dict(name=str_1)
        any_0 = object_0.validate(var_0)
        var_1 = dict(name=str_1)
        str_2 = {str_0: str_1}
        any_1 = object_0.validate(str_2)
        var_2 = dict(name=str_1)
        str_3 = 'developer'
        var_3 = dict(name=str_1, job=str_3)
        any_2 = object_0.validate(var_3)
        var_4 = dict(name=str_1, job=str_3)
        str_4 = 'job'
        str_5 = {str_0: str_1, str_4: str_3}
        any_3 = object_0.validate(str_5)
        var_5 = dict(name=str_1, job=str_3)
        int_0 = 1
        var_6 = dict(name=int_0)
        any_4 = object_0.validate(var_6)
    except BaseException:
        pass

def test_case_89():
    try:
        str_0 = '^[0-9a-zA-Z_-]{2,9}$'
        var_0 = module_2.compile(str_0)
        string_0 = module_0.String(pattern=var_0)
        string_1 = [string_0]
        int_0 = 4
        array_0 = module_0.Array(string_1, int_0, int_0)
    except BaseException:
        pass

def test_case_90():
    try:
        int_0 = 4
        integer_0 = module_0.Integer()
        array_0 = module_0.Array(integer_0)
        int_1 = [int_0, int_0, int_0, int_0, int_0]
        date_time_0 = module_0.DateTime()
        int_2 = [int_1, int_0, int_0, int_0, int_0]
        any_0 = array_0.validate(int_2)
    except BaseException:
        pass

def test_case_91():
    try:
        integer_0 = module_0.Integer()
        string_0 = module_0.String()
        var_0 = [integer_0, string_0]
        str_0 = 'et'
        union_0 = module_0.Union(var_0)
        any_0 = union_0.validate(integer_0)
    except BaseException:
        pass

def test_case_92():
    try:
        field_0 = module_0.Field()
        any_0 = field_0.get_default_value()
        int_0 = 42
        field_1 = module_0.Field(default=int_0)
        any_1 = field_1.get_default_value()
        var_0 = lambda : int_0
        field_2 = module_0.Field(default=var_0)
        any_2 = field_2.get_default_value()
    except BaseException:
        pass