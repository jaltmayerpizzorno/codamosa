# Automatically generated by Pynguin.
import ast as module_0
import apimd.parser as module_1

def test_case_0():
    try:
        str_0 = 'HC.0H|PC?/3'
        expr_0 = module_0.expr()
        int_0 = -3104
        str_1 = 'r'
        str_2 = None
        str_3 = '(X>NE4y|[\tFRN)L'
        dict_0 = {str_1: str_1, str_2: str_3}
        parser_0 = module_1.Parser(int_0, dict_0)
        str_4 = parser_0.resolve(str_0, expr_0)
        str_5 = module_1.code(str_0)
        str_6 = None
        str_7 = 'typing.Union'
        str_8 = '?U34CgEl}"@A:GBr'
        str_9 = 'dZN\x0c0}2}4xm]T'
        str_10 = None
        str_11 = '5( u\\\x0cc1'
        dict_1 = {str_0: str_9, str_10: str_11}
        resolver_0 = module_1.Resolver(str_7, dict_1)
        str_12 = 'fi%'
        dict_2 = {str_7: str_7, str_8: str_0, str_12: str_7}
        parser_1 = module_1.Parser(dict_2)
        bool_0 = parser_1.is_public(str_6)
    except BaseException:
        pass

def test_case_1():
    try:
        constant_0 = module_0.Constant()
        str_0 = 'w,'
        str_1 = "w'>L\r\x0bWNc%:XUz"
        str_2 = 'coJ'
        str_3 = '$H'
        str_4 = 'HvfxP'
        dict_0 = {str_1: str_1, str_1: str_1, str_1: str_2, str_3: str_4}
        resolver_0 = module_1.Resolver(str_0, dict_0)
        a_s_t_0 = resolver_0.visit_Constant(constant_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ':@9+IZkiB\x0bJ'
        dict_0 = {str_0: str_0}
        name_0 = module_0.Name(**dict_0)
        str_1 = 'Jv_# |iO%I-Wr'
        dict_1 = {}
        resolver_0 = module_1.Resolver(str_1, dict_1)
        a_s_t_0 = resolver_0.visit_Name(name_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'ddM'
        str_1 = ',u'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_1: str_1}
        subscript_0 = module_0.Subscript(**dict_0)
        str_2 = ''
        str_3 = '5gn2Hx>\tb#)}o.JO'
        dict_1 = {str_2: str_3}
        resolver_0 = module_1.Resolver(str_2, dict_1)
        a_s_t_0 = resolver_0.visit_Subscript(subscript_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '5{G-bw#G!a"`k'
        import_0 = module_0.Import()
        dict_0 = {}
        parser_0 = module_1.Parser(dict_0)
        parser_0.imports(str_0, import_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'l'
        parser_0 = module_1.Parser()
        parser_0.parse(str_0, str_0)
        assign_0 = module_0.Assign()
        parser_0.globals(str_0, assign_0)
    except BaseException:
        pass

def test_case_6():
    try:
        ann_assign_0 = module_0.AnnAssign()
        function_def_0 = module_0.FunctionDef()
        str_0 = '/\tcR{\x0b1x|"R\x0c['
        str_1 = 'xufV@XX8'
        dict_0 = {str_0: str_1}
        parser_0 = module_1.Parser(dict_0)
        parser_0.api(str_0, function_def_0, prefix=str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'w,[p@$g"O.$H#\rx'
        bool_0 = module_1.is_public_family(str_0)
        int_0 = 2203
        str_1 = ',uYSm}f\x0c'
        bool_1 = module_1.is_public_family(str_1)
        str_2 = None
        dict_0 = {}
        str_3 = '886H4k'
        list_0 = [str_2]
        arguments_0 = module_0.arguments(*list_0)
        expr_0 = module_0.expr()
        bool_2 = True
        bool_3 = True
        str_4 = ''
        str_5 = 'l'
        str_6 = 'M/[nEqg'
        str_7 = 'FrP;uRPm!p&w@GZ'
        dict_1 = {str_2: str_2, str_4: str_5, str_6: str_7}
        parser_0 = module_1.Parser(int_0, bool_3, dict_0, dict_1)
        parser_0.func_api(str_3, str_3, arguments_0, expr_0, has_self=bool_0, cls_method=bool_2)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'FJ!RG\\\rp'
        arguments_0 = None
        optional_0 = None
        bool_0 = False
        bool_1 = False
        bool_2 = False
        int_0 = -159
        str_1 = '23- &{+ozh'
        dict_0 = {str_1: str_1, str_1: str_1, str_1: str_1}
        parser_0 = module_1.Parser(bool_2, int_0, dict_0, dict_0, dict_0, dict_0)
        parser_0.func_api(str_0, str_0, arguments_0, optional_0, has_self=bool_0, cls_method=bool_1)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = -185
        dict_0 = {}
        parser_0 = module_1.Parser(int_0, dict_0)
        str_0 = parser_0.compile()
        str_1 = '\x0cGYk_sW\x0bU^xKG'
        list_0 = [str_1]
        list_1 = [list_0, str_1, parser_0]
        assign_0 = module_0.Assign(*list_1)
        parser_0.globals(str_0, assign_0)
        str_2 = '\rq`'
        dict_1 = {str_1: str_1, str_0: str_2}
        parser_1 = module_1.Parser(dict_1)
        expr_0 = module_0.expr()
        list_2 = [expr_0, expr_0]
        list_3 = None
        parser_0.class_api(str_0, str_1, list_2, list_3)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'L2c?'
        parser_0 = module_1.Parser()
        bool_0 = parser_0.is_public(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'bte.$9D'
        str_1 = '1b@71>J z'
        str_2 = '=L3d jHeeZd'
        assign_0 = None
        bool_0 = False
        int_0 = 4432
        str_3 = '3.74X,d/Gs'
        dict_0 = {str_3: int_0}
        parser_0 = module_1.Parser(bool_0, int_0, dict_0)
        parser_0.globals(str_1, assign_0)
        expr_0 = module_0.expr()
        str_4 = module_1.const_type(expr_0)
        str_5 = '2)\rTy4=\rIQ'
        str_6 = module_1.esc_underscore(str_5)
        dict_1 = {str_0: str_0, str_0: str_1, str_2: str_1}
        parser_1 = module_1.Parser(dict_1, dict_1)
        assign_1 = module_0.Assign()
        str_7 = ''
        async_function_def_0 = None
        parser_0.api(str_7, async_function_def_0)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = None
        str_0 = 'y6'
        str_1 = module_1.code(str_0)
        str_2 = "' can not be found"
        str_3 = None
        str_4 = '#H'
        list_0 = [str_1, str_1, str_3, str_4]
        arguments_0 = module_0.arguments(*list_0)
        str_5 = 'typing'
        dict_0 = {str_5: list_0, str_4: str_0, str_0: str_4, str_2: int_0}
        import_0 = module_0.Import(**dict_0)
        bool_0 = False
        str_6 = 'M<v}9\tR7E&=$;0^_AOz'
        str_7 = 'typing.ValuesView'
        dict_1 = {str_6: str_7}
        str_8 = "'9"
        str_9 = '+9\x0bGhs[]ZS'
        str_10 = '4\tSv^9[?d'
        str_11 = 'bD\t#[a%Q'
        str_12 = 'typing.Set'
        dict_2 = {str_8: str_9, str_1: str_2, str_8: str_10, str_11: str_12}
        str_13 = 'u'
        str_14 = "a]>e*)zoV:%^[{TDY'K"
        set_0 = {str_0, str_11, str_13, str_14}
        str_15 = 'u*8s4|'
        dict_3 = {str_7: set_0, str_6: set_0, str_15: set_0}
        parser_0 = module_1.Parser(dict_1, dict_2, dict_3)
        parser_0.func_api(str_3, str_4, arguments_0, import_0, has_self=bool_0, cls_method=bool_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'y6'
        str_1 = module_1.code(str_0)
        str_2 = "' can not be found"
        list_0 = [str_0, str_2, str_0]
        async_function_def_0 = module_0.AsyncFunctionDef(*list_0)
        bool_0 = False
        int_0 = 2185
        dict_0 = {}
        parser_0 = module_1.Parser(bool_0, int_0, dict_0)
        parser_0.api(str_2, async_function_def_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'Qfa|6s'
        list_0 = []
        dict_0 = {}
        resolver_0 = module_1.Resolver(str_0, dict_0)
        stmt_0 = None
        list_1 = [stmt_0, stmt_0]
        str_1 = module_1.esc_underscore(str_0)
        list_2 = [dict_0]
        name_0 = module_0.Name(*list_2)
        a_s_t_0 = resolver_0.visit_Name(name_0)
        bool_0 = False
        dict_1 = {}
        dict_2 = {}
        parser_0 = module_1.Parser(bool_0, bool_0, dict_1, dict_2)
        var_0 = parser_0.__repr__()
        bool_1 = False
        parser_1 = module_1.Parser(bool_1, dict_0, dict_0)
        parser_1.class_api(str_0, str_0, list_0, list_1)
        list_3 = [stmt_0]
        subscript_0 = module_0.Subscript(*list_3)
        a_s_t_1 = resolver_0.visit_Subscript(subscript_0)
        bool_2 = parser_0.is_public(str_1)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'y6'
        str_1 = "' can not be found"
        int_0 = -1216
        str_2 = 'wG^\x0bE?Xc&snD(px]'
        int_1 = 338
        dict_0 = {str_1: int_0, str_0: int_0, str_2: int_0, str_1: int_1}
        parser_0 = module_1.Parser(dict_0)
        list_0 = [str_1, str_1]
        import_from_0 = module_0.ImportFrom(*list_0)
        str_3 = '}b>B\t5~FX#\tPv-\r8\r'
        parser_0.imports(str_3, import_from_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'Qfa|6s'
        dict_0 = {}
        resolver_0 = module_1.Resolver(str_0, dict_0)
        iterable_0 = None
        str_1 = module_1.table(items=iterable_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '(Qa>$Gl'
        str_1 = module_1.esc_underscore(str_0)
        str_2 = "\n[9sFm4d*'Th#4L"
        str_3 = 'vqgvTq%x'
        dict_0 = {str_2: str_3}
        resolver_0 = module_1.Resolver(str_3, dict_0)
        str_4 = 'vk>9a(,E@:S%;5?o'
        list_0 = [dict_0, str_0, str_2]
        ann_assign_0 = module_0.AnnAssign(*list_0)
        int_0 = -590
        str_5 = '`\x0c[U@i};}O%oO['
        str_6 = 'phDxT\rvU"/R['
        int_1 = 103
        dict_1 = {str_1: int_0, str_5: int_1, str_1: int_0, str_6: int_1}
        str_7 = ';<[,GEW&ZW^xwxQ'
        str_8 = 'ei l.|&*>B'
        dict_2 = {str_7: str_8, str_8: str_6, str_2: str_7}
        str_9 = 'V@'
        str_10 = '::'
        str_11 = ' \x0crHW9\\L'
        set_0 = {str_9, str_10, str_0, str_11}
        dict_3 = {str_1: set_0}
        parser_0 = module_1.Parser(int_0, dict_1, dict_2, dict_3)
        parser_0.globals(str_4, ann_assign_0)
        str_12 = module_1.doctest(str_2)
        parser_1 = module_1.Parser()
        parser_1.parse(str_1, str_3)
        import_from_0 = module_0.ImportFrom(*list_0)
        str_13 = None
        parser_0.imports(str_13, import_from_0)
    except BaseException:
        pass

def test_case_18():
    try:
        int_0 = None
        str_0 = 'y6'
        str_1 = module_1.code(str_0)
        str_2 = 'wG^\x0bE?Xc&snD(px]'
        parser_0 = module_1.Parser(int_0)
        str_3 = None
        parser_0.parse(str_2, str_3)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'wlsi!)v\\XALHfD! P'
        list_0 = [str_0]
        import_0 = module_0.Import(*list_0)
        str_1 = 'Am`+0u'
        str_2 = 't[a`\x0c\\/DX.#KiLHY(VB5'
        str_3 = 'Z(>y[> F^{[\x0b8LGH\x0b!n'
        str_4 = 'ucdR!`'
        dict_0 = {str_1: str_2, str_4: str_4, str_3: str_1, str_4: str_4}
        dict_1 = {}
        parser_0 = module_1.Parser(dict_0, dict_1)
        parser_0.imports(str_0, import_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = '(Qa>$Gl'
        str_1 = module_1.esc_underscore(str_0)
        str_2 = "\n[9sFm4d*'Th#4L"
        str_3 = 'vqgvTq%x'
        str_4 = '`\x0c[U@i};}O%oO['
        str_5 = module_1.doctest(str_2)
        parser_0 = module_1.Parser()
        parser_0.parse(str_1, str_3)
        str_6 = module_1.doctest(str_1)
        module_x_var_0 = None
        parser_0.load_docstring(str_3, module_x_var_0)
        bool_0 = parser_0.is_public(str_1)
        bool_1 = parser_0.is_public(str_4)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = "be.$'L9D"
        str_1 = 'dC:u^!Am\n\rRv3r)Ht'
        str_2 = 'vqgvTq%x'
        dict_0 = {str_2: str_1, str_0: str_2}
        resolver_0 = module_1.Resolver(str_2, dict_0)
        list_0 = [dict_0, str_0, str_1]
        ann_assign_0 = module_0.AnnAssign(*list_0)
        bool_0 = True
        int_0 = 1564
        parser_0 = module_1.Parser(bool_0, int_0, bool_0, dict_0, dict_0)
        str_3 = None
        list_1 = [str_3]
        iterable_0 = None
        str_4 = module_1.table(*list_1, items=iterable_0)
    except BaseException:
        pass