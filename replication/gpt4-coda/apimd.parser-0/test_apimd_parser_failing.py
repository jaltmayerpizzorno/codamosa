# Automatically generated by Pynguin.
import apimd.parser as module_0
import ast as module_1

def test_case_0():
    try:
        parser_0 = module_0.Parser()
        str_0 = ''
        str_1 = module_0.doctest(str_0)
        parser_0.parse(str_0, str_0)
        str_2 = '\x0bN</\nPs$#wvfk!6itRb&'
        str_3 = module_0.esc_underscore(str_1)
        str_4 = module_0.code(str_2)
        str_5 = parser_0.compile()
        bool_0 = parser_0.is_public(str_5)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'U2'
        import_0 = None
        str_1 = 'Z \r_S\x0bSI2%L{"} hwI~\x0b'
        dict_0 = {str_1: str_1}
        parser_0 = module_0.Parser(dict_0)
        parser_0.imports(str_0, import_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'i2R_U1'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        assign_0 = module_1.Assign(**dict_0)
        parser_0 = module_0.Parser()
        parser_0.globals(str_0, assign_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '^XaR'
        list_0 = [str_0, str_0, str_0]
        dict_0 = {str_0: str_0}
        assign_0 = module_1.Assign(*list_0, **dict_0)
        int_0 = 1539
        str_1 = None
        dict_1 = {str_1: str_1}
        dict_2 = {}
        parser_0 = module_0.Parser(int_0, dict_1, dict_2)
        parser_0.globals(str_0, assign_0)
        str_2 = '\tZ28QH(h_xv3qif\x0c'
        function_def_0 = module_1.FunctionDef()
        parser_0.api(str_2, function_def_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '6~CZk&4'
        str_1 = ''
        str_2 = 'x0#'
        str_3 = "gm,e'aqQgkcWEY"
        dict_0 = {str_2: str_2, str_3: str_3}
        function_def_0 = module_1.FunctionDef(**dict_0)
        str_4 = '`v"TH 2Rb'
        bool_0 = True
        int_0 = -755
        str_5 = None
        str_6 = 'j<G\x0cb+qS;GzgtL$'
        str_7 = 'vp=F@f\\k'
        dict_1 = {str_5: str_6, str_6: str_0, str_0: str_7}
        parser_0 = module_0.Parser(bool_0, int_0, dict_1)
        parser_0.api(str_1, function_def_0, prefix=str_4)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = None
        list_0 = [str_0]
        arguments_0 = module_1.arguments(*list_0)
        expr_0 = module_1.expr()
        bool_0 = False
        int_0 = 839
        str_1 = 'P0x#R``p:'
        set_0 = set()
        str_2 = ';:k[ JeG'
        str_3 = 'uGbycU3|k2OeqCmP'
        str_4 = '|UXs'
        set_1 = {str_2, str_3, str_2, str_4}
        str_5 = 'k_LqcT</2~L.++P\nW'
        str_6 = None
        dict_0 = {str_1: set_0, str_1: set_1, str_5: set_0, str_6: set_0}
        parser_0 = module_0.Parser(int_0, dict_0)
        parser_0.func_api(str_0, str_0, arguments_0, expr_0, has_self=bool_0, cls_method=bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'contextlib.AsyncContextManager'
        list_0 = [str_0]
        arguments_0 = module_1.arguments(*list_0)
        str_1 = 'Any'
        str_2 = 'Any'
        dict_0 = {str_1: str_0, str_2: str_2, str_0: str_1}
        expr_0 = module_1.expr(**dict_0)
        bool_0 = None
        bool_1 = True
        bool_2 = False
        str_3 = 'N|\n^Qy) @7g)hlXNt\\\t'
        int_0 = -247
        str_4 = 'L\x0c*q9EsK:_^u\tL'
        str_5 = 'cG<'
        int_1 = -5137
        dict_1 = {str_3: int_0, str_4: int_0, str_5: int_1}
        dict_2 = {str_5: str_4}
        parser_0 = module_0.Parser(bool_2, dict_1, dict_2, dict_2)
        parser_0.func_api(str_0, str_0, arguments_0, expr_0, has_self=bool_0, cls_method=bool_1)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'U)ijHKq{T'
        str_1 = 'RNuKIr;H<dF'
        expr_0 = module_1.expr()
        list_0 = [expr_0]
        constant_0 = module_1.Constant()
        set_0 = {constant_0}
        str_2 = 'mA'
        dict_0 = {str_2: str_0, str_0: str_1}
        subscript_0 = module_1.Subscript(**dict_0)
        list_1 = [constant_0, set_0, subscript_0]
        bool_0 = False
        int_0 = 3080
        dict_1 = {}
        parser_0 = module_0.Parser(bool_0, int_0, dict_1)
        parser_0.class_api(str_0, str_1, list_0, list_1)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '7O'
        bool_0 = True
        parser_0 = module_0.Parser(bool_0, bool_0)
        bool_1 = parser_0.is_public(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'mA'
        import_0 = module_1.Import()
        bool_0 = True
        int_0 = 0
        str_1 = 'collections.abc.Generator'
        str_2 = '&"Xz@md$\x0cTH20-i'
        dict_0 = {str_1: str_1, str_1: str_1, str_2: str_2}
        parser_0 = module_0.Parser(bool_0, int_0, dict_0, dict_0, dict_0)
        parser_0.imports(str_0, import_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '=L2CPv81a0#C k'
        list_0 = [str_0]
        iterable_0 = None
        str_1 = module_0.table(*list_0, items=iterable_0)
    except BaseException:
        pass

def test_case_11():
    try:
        bool_0 = False
        int_0 = 1
        str_0 = '^M$O|t#Sqo*i:<rk4EL_'
        str_1 = 'd '
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_1}
        parser_0 = module_0.Parser(bool_0, int_0, bool_0, dict_0, dict_0, dict_0)
        str_2 = parser_0.compile()
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'singl^e_underscore'
        list_0 = [str_0, str_0]
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        import_from_0 = module_1.ImportFrom(*list_0)
        bool_0 = True
        parser_0 = module_0.Parser(bool_0, dict_0, dict_0)
        parser_0.imports(str_0, import_from_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'h@'
        str_1 = 'a\rv-DkDZHwKRM}c3gp'
        list_0 = [str_0, str_1, str_1]
        str_2 = '$Y '
        dict_0 = {str_1: str_0, str_1: str_1, str_2: str_2}
        arguments_0 = module_1.arguments(*list_0, **dict_0)
        expr_0 = module_1.expr()
        bool_0 = False
        bool_1 = None
        bool_2 = False
        bool_3 = module_0.is_magic(str_1)
        dict_1 = {}
        str_3 = '1X&~'
        str_4 = 'es&k'
        dict_2 = {str_3: str_4, str_4: str_3, str_4: str_4}
        parser_0 = module_0.Parser(bool_2, dict_1, dict_2)
        parser_0.func_api(str_0, str_1, arguments_0, expr_0, has_self=bool_0, cls_method=bool_1)
    except BaseException:
        pass

def test_case_14():
    try:
        list_0 = []
        list_1 = [list_0]
        name_0 = module_1.Name(*list_1)
        str_0 = 'store_true'
        str_1 = '^/5qr'
        str_2 = '!7lv'
        str_3 = None
        dict_0 = {str_0: str_1, str_2: str_3, str_3: str_2}
        resolver_0 = module_0.Resolver(str_0, dict_0)
        a_s_t_0 = resolver_0.visit_Name(name_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'Cq'
        bool_0 = True
        int_0 = 1
        str_1 = 'py)'
        str_2 = '{3%NB`*"Yvo6T'
        str_3 = 'd '
        dict_0 = {str_2: str_0, str_1: str_1, str_2: str_3}
        parser_0 = module_0.Parser(bool_0, int_0, bool_0, dict_0, dict_0, dict_0)
        iterable_0 = None
        str_4 = 'm&\nS=Lm'
        list_0 = [str_2, str_4, str_3]
        str_5 = module_0.table(*list_0, items=iterable_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'O(0},W_*>'
        list_0 = []
        stmt_0 = None
        dict_0 = {}
        dict_1 = None
        parser_0 = module_0.Parser(dict_1, dict_0, dict_0)
        list_1 = [dict_0, list_0]
        str_1 = '/d&vh'
        dict_2 = {str_1: stmt_0}
        import_from_0 = module_1.ImportFrom(*list_1, **dict_2)
        parser_0.imports(str_0, import_from_0)
        expr_0 = module_1.expr(*list_1)
    except BaseException:
        pass

def test_case_17():
    try:
        dict_0 = {}
        parser_0 = module_0.Parser(dict_0, dict_0, dict_0)
        str_0 = '99wo\x0b+A/caUS'
        bool_0 = module_0.is_public_family(str_0)
        list_0 = [str_0]
        import_0 = module_1.Import(*list_0)
        parser_0.imports(str_0, import_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = "Ji6RsFr;nbnC:YQ6^{'"
        str_1 = 'D)oN:?4k2Q'
        bool_0 = module_0.is_magic(str_1)
        list_0 = [str_0]
        function_def_0 = module_1.FunctionDef(*list_0)
        str_2 = 'd^$PM?"\tmFr^.8|1%I'
        str_3 = 'j#HL^-XfMpu-+4w>?L_?'
        str_4 = module_0.esc_underscore(str_3)
        str_5 = '@'
        dict_0 = {str_2: str_2, str_2: str_5}
        parser_0 = module_0.Parser(dict_0)
        parser_0.api(str_0, function_def_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '^XaR'
        list_0 = [str_0, str_0, str_0]
        dict_0 = {str_0: str_0}
        assign_0 = module_1.Assign(*list_0, **dict_0)
        bool_0 = True
        str_1 = 'DDK-9g97Qs6'
        int_0 = 3
        str_2 = '<H&+0Lup~?'
        int_1 = 0
        dict_1 = {str_1: int_0, str_2: int_0, str_1: int_1}
        str_3 = '\n)FP'
        str_4 = 'mI`'
        str_5 = 'XZT6^($g'
        str_6 = '\x0c:; XHQ/Q{'
        dict_2 = {str_3: str_4, str_5: str_6, str_0: str_1, str_0: str_1}
        str_7 = '!?n\x0cL\\+48b :|GUQ'
        set_0 = {str_7, str_6}
        str_8 = 'M2r~'
        str_9 = '>Tq!0\t[Tp\x0b_1\\'
        dict_3 = {str_0: set_0, str_8: set_0, str_5: set_0, str_9: set_0}
        parser_0 = module_0.Parser(bool_0, dict_1, dict_2, dict_3, dict_2, dict_2)
        var_0 = parser_0.__repr__()
        int_2 = 1539
        str_10 = None
        dict_4 = {str_10: str_10}
        str_11 = '%%s#8jVWk5n;}^"|?Z'
        set_1 = {str_10, str_11, str_10, str_11}
        dict_5 = {str_10: set_1}
        parser_1 = module_0.Parser(int_2, dict_4, dict_5)
        str_12 = module_0.esc_underscore(str_0)
        parser_1.globals(str_0, assign_0)
        import_from_0 = module_1.ImportFrom(*list_0)
        parser_1.imports(str_0, import_from_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = 'example'
        str_1 = 'example.Union'
        str_2 = 'iv'
        str_3 = 'example.Dict'
        str_4 = 'example.Set'
        str_5 = 'example.Tuple'
        str_6 = 'typing.Union'
        str_7 = 'typing.Optional'
        str_8 = 'typin.List'
        str_9 = 'typing.Dict'
        str_10 = 'typing.Set'
        str_11 = 'typing.Tuple'
        str_12 = {str_1: str_6, str_2: str_7, str_4: str_8, str_3: str_9, str_4: str_10, str_5: str_11}
        resolver_0 = module_0.Resolver(str_0, str_12)
        int_0 = 0
        str_13 = 'Union[int, str]'
        var_0 = module_1.parse(str_13)
        var_1 = var_0.body[int_0]
        var_2 = var_1.value
        a_s_t_0 = resolver_0.visit_Subscript(var_2)
        var_3 = a_s_t_0.left
        var_4 = a_s_t_0.right
        var_5 = str_3.value
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'example'
        str_1 = 'example.Union'
        str_2 = 'iv'
        str_3 = 'example.Dict'
        str_4 = 'example.Set'
        str_5 = 'typing.Union'
        str_6 = 'typing.Optional'
        str_7 = 'typin.List'
        str_8 = 'typing.Dict'
        str_9 = 'typing.Set'
        str_10 = 'typing.Tuple'
        str_11 = {str_1: str_5, str_2: str_6, str_6: str_9, str_4: str_7, str_1: str_8, str_3: str_10, str_0: str_9}
        resolver_0 = module_0.Resolver(str_0, str_11)
        int_0 = 0
        str_12 = 'Union[int, str]'
        var_0 = module_1.parse(str_12)
        var_1 = var_0.body[int_0]
        var_2 = var_1.value
        a_s_t_0 = resolver_0.visit_Subscript(var_2)
        var_3 = a_s_t_0.left
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = 'single_underscore'
        list_0 = [str_0, str_0]
        subscript_0 = module_1.Subscript(*list_0)
        str_1 = 'oUNfJ+P9'
        str_2 = ''
        str_3 = None
        str_4 = ' API\n\n'
        list_1 = []
        str_5 = 'fR'
        dict_0 = {str_1: str_2, str_5: list_0}
        try_0 = module_1.Try(*list_0, **dict_0)
        name_0 = module_1.Name(*list_0)
        list_2 = [try_0, name_0]
        bool_0 = False
        int_0 = None
        str_6 = 'le'
        int_1 = 671
        str_7 = 'Pn'
        dict_1 = {str_1: int_0, str_6: int_1, str_7: int_1}
        str_8 = ';K'
        str_9 = 'H-'
        str_10 = 'S>G\tGbsGj<Kk\tpj"\x0b'
        dict_2 = {str_7: str_8, str_7: str_9, str_10: str_9, str_1: str_2}
        parser_0 = module_0.Parser(bool_0, dict_1, dict_2)
        parser_0.class_api(str_3, str_4, list_1, list_2)
    except BaseException:
        pass