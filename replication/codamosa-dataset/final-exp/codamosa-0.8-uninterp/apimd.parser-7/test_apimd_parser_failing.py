# Automatically generated by Pynguin.
import apimd.parser as module_0
import ast as module_1
import collections.abc as module_2

def test_case_0():
    try:
        str_0 = 'V'
        str_1 = module_0.code(str_0)
        str_2 = '\rMbU? y'
        str_3 = module_0.doctest(str_2)
        name_0 = module_1.Name()
        str_4 = '.__init__'
        str_5 = '&'
        str_6 = '\n:,^K^P8f'
        dict_0 = {str_1: str_1, str_4: str_3, str_5: str_6}
        resolver_0 = module_0.Resolver(str_0, dict_0)
        a_s_t_0 = resolver_0.visit_Name(name_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'k|j~klmP[Mm'
        str_1 = 'eR1\x0c~-(~N(i^]P HT'
        str_2 = '__main__'
        str_3 = module_0.esc_underscore(str_2)
        str_4 = module_0.code(str_1)
        expr_0 = None
        parser_0 = module_0.Parser()
        str_5 = parser_0.resolve(str_0, expr_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = []
        subscript_0 = module_1.Subscript(*list_0)
        str_0 = 'EMn@qRpR%B W]5'
        dict_0 = {}
        resolver_0 = module_0.Resolver(str_0, dict_0)
        a_s_t_0 = resolver_0.visit_Subscript(subscript_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '.j8 #)d^6m'
        bool_0 = module_0.is_magic(str_0)
        attribute_0 = module_1.Attribute()
        str_1 = "a5*'{7G8hn"
        str_2 = 'l^4T'
        str_3 = 'G6EpLpJp3u1&_a\n\t'
        str_4 = 'RbqM'
        str_5 = "{L%@w'-(aQ"
        dict_0 = {str_2: str_2, str_0: str_3, str_4: str_5, str_0: str_3}
        resolver_0 = module_0.Resolver(str_1, dict_0, str_5)
        a_s_t_0 = resolver_0.visit_Attribute(attribute_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'e(d\n\t^\\hp0GhwVa'
        dict_0 = {}
        parser_0 = module_0.Parser(dict_0, dict_0, dict_0)
        bool_0 = parser_0.is_public(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = "0'"
        bool_0 = module_0.is_public_family(str_0)
        import_0 = module_1.Import()
        bool_1 = False
        parser_0 = module_0.Parser(bool_1)
        parser_0.imports(str_0, import_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'g<FI'
        bool_0 = module_0.is_public_family(str_0)
        str_1 = '\x0ck'
        str_2 = module_0.doctest(str_1)
        str_3 = '4IKn8!'
        str_4 = 'Uz\x0ct.J:|\\l#ySrKSDt>'
        dict_0 = {str_3: str_4}
        int_0 = -3283
        parser_0 = module_0.Parser(int_0, dict_0)
        dict_1 = {}
        assign_0 = module_1.Assign(**dict_1)
        parser_0.globals(str_0, assign_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '{XnM02+g-KM7H'
        list_0 = [str_0, str_0]
        arguments_0 = module_1.arguments(*list_0)
        str_1 = 'AF ]I:\nb`=2Bc\x0bU6h ('
        async_function_def_0 = module_1.AsyncFunctionDef()
        int_0 = 1
        bool_0 = True
        dict_0 = {}
        parser_0 = module_0.Parser(int_0, bool_0, dict_0)
        parser_0.api(str_1, async_function_def_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '{XnM02+g-KM7H'
        list_0 = [str_0, str_0]
        arguments_0 = module_1.arguments(*list_0)
        str_1 = 'AF ]I:\nb`=2Bc\x0bU6h ('
        bool_0 = True
        dict_0 = {}
        str_2 = ']'
        dict_1 = {str_0: str_2}
        set_0 = None
        dict_2 = {str_0: set_0, str_2: set_0, str_0: set_0}
        parser_0 = module_0.Parser(dict_0, dict_1, dict_1, dict_2, dict_1)
        parser_0.func_api(str_0, str_0, arguments_0, str_1, has_self=bool_0, cls_method=bool_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'typing.Tuple'
        str_1 = '`'
        str_2 = 'V\x0bKgagLaQ'
        dict_0 = {str_1: str_1, str_0: str_0, str_2: str_1}
        parser_0 = module_0.Parser(dict_0, dict_0)
        str_3 = "Q'1z'HIos&0c=}M 4OoV"
        list_0 = [dict_0]
        import_from_0 = module_1.ImportFrom(*list_0)
        parser_0.imports(str_3, import_from_0)
    except BaseException:
        pass

def test_case_10():
    try:
        ann_assign_0 = module_1.AnnAssign()
        bool_0 = False
        str_0 = None
        set_0 = {str_0, str_0}
        dict_0 = {str_0: set_0, str_0: set_0}
        parser_0 = module_0.Parser(bool_0, dict_0)
        parser_0.globals(str_0, ann_assign_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'Pqpu"Ce'
        str_1 = 'bzA~&=TG8X;L^&re(:cc'
        str_2 = '{@L~@IJ~'
        str_3 = ' <= '
        str_4 = module_0.doctest(str_3)
        str_5 = module_0.esc_underscore(str_2)
        list_0 = []
        str_6 = "'a9\x0c=AdXPq\r"
        str_7 = '<\r'
        str_8 = '-@/.H-Z.2DU#S0X9o2Z'
        dict_0 = {str_6: str_5}
        arguments_0 = module_1.arguments(**dict_0)
        list_1 = [list_0, arguments_0, str_0, str_1]
        arguments_1 = module_1.arguments(*list_1, **dict_0)
        expr_0 = module_1.expr(**dict_0)
        bool_0 = True
        bool_1 = True
        str_9 = ';->P<>}['
        dict_1 = {str_1: str_9}
        str_10 = '?V%1[-O\r\t&x'
        set_0 = {str_9}
        str_11 = '>o`I-o:yjxe?H'
        dict_2 = {str_10: set_0, str_3: set_0, str_3: set_0, str_11: set_0}
        parser_0 = module_0.Parser(dict_1, dict_2, dict_1)
        parser_0.func_api(str_7, str_8, arguments_1, expr_0, has_self=bool_0, cls_method=bool_1)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '\\T\n\t?lX#z^o2ogq1KMAX'
        bool_0 = module_0.is_public_family(str_0)
        int_0 = 2126
        str_1 = module_0.doctest(str_0)
        sequence_0 = None
        iterator_0 = module_0.walk_body(sequence_0)
        dict_0 = {str_1: str_0}
        parser_0 = module_0.Parser(int_0, dict_0, dict_0)
        str_2 = parser_0.compile()
        sequence_1 = module_2.Sequence()
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '+h~2B`lze8j3}:.vTc'
        str_1 = '3[wadC&2#'
        str_2 = 'i'
        str_3 = 'e6'
        str_4 = '&&jr\t#hxlP'
        str_5 = 'o\r ;\rAQ\\'
        dict_0 = {str_0: str_1, str_2: str_0, str_3: str_1, str_4: str_5}
        set_0 = None
        str_6 = 'G/M\\Zf]JgE7s{g'
        str_7 = "N\\Z\\37(32$!X'QL36\\4x"
        dict_1 = {str_3: set_0, str_0: set_0, str_6: set_0, str_7: set_0}
        dict_2 = {}
        parser_0 = module_0.Parser(dict_0, dict_1, dict_0, dict_2, dict_0)
        str_8 = parser_0.compile()
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '$A-tI.$O('
        str_1 = 'e6'
        list_0 = [str_0, str_0]
        str_2 = '\rhL6erf'
        str_3 = 'SdHyJ0x}{\\.]7`]u'
        str_4 = "UG'DX|CH\x0cC;-\x0b"
        dict_0 = {str_2: str_0, str_3: list_0, str_4: str_4, str_0: list_0}
        import_from_0 = module_1.ImportFrom(*list_0, **dict_0)
        bool_0 = True
        str_5 = 'j8'
        dict_1 = {str_5: str_1}
        parser_0 = module_0.Parser(bool_0, dict_1, dict_1)
        parser_0.imports(str_1, import_from_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '_+<H|5,Z]P`ZT,#f'
        bool_0 = module_0.is_public_family(str_0)
        ann_assign_0 = None
        function_def_0 = module_1.FunctionDef()
        str_1 = '-#\x0c-\nBfDhjXt8n`~'
        str_2 = None
        str_3 = None
        dict_0 = {str_3: str_2, str_1: ann_assign_0}
        attribute_0 = module_1.Attribute(**dict_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'typing.Tuple'
        int_0 = 3
        bool_0 = True
        parser_0 = module_0.Parser(int_0, bool_0)
        parser_0.parse(str_0, str_0)
        str_1 = "aBByI.y`VqW'HzOFc"
        expr_0 = module_1.expr()
        list_0 = [expr_0, expr_0]
        str_2 = module_0.doctest(str_1)
        list_1 = []
        parser_0.class_api(str_1, str_0, list_0, list_1)
        list_2 = [bool_0]
        dict_0 = {str_1: list_1}
        name_0 = module_1.Name(*list_2, **dict_0)
        dict_1 = {}
        resolver_0 = module_0.Resolver(str_1, dict_1)
        a_s_t_0 = resolver_0.visit_Name(name_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = None
        str_1 = '0Vx<xt*@G[_'
        int_0 = -3794
        list_0 = [str_1, str_0]
        constant_0 = module_1.Constant(*list_0)
        str_2 = '_N"x~LFtO"C'
        dict_0 = {}
        resolver_0 = module_0.Resolver(str_2, dict_0)
        a_s_t_0 = resolver_0.visit_Constant(constant_0)
        str_3 = module_0.parent(str_0, level=int_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = None
        str_1 = 'Z;VFD'
        int_0 = -3794
        list_0 = [str_1, str_0]
        constant_0 = module_1.Constant(*list_0)
        str_2 = '_N"x~LFtO"C'
        dict_0 = {}
        resolver_0 = module_0.Resolver(str_2, dict_0)
        a_s_t_0 = resolver_0.visit_Constant(constant_0)
        str_3 = module_0.parent(str_0, level=int_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '^\tna66c'
        list_0 = [str_0]
        attribute_0 = module_1.Attribute(*list_0)
        bool_0 = module_0.is_public_family(str_0)
        dict_0 = {}
        str_1 = '#\x0b*'
        str_2 = 'b='
        bool_1 = False
        parser_0 = module_0.Parser(bool_1, dict_0, dict_0, dict_0, dict_0)
        str_3 = parser_0.compile()
        str_4 = module_0.doctest(str_2)
        resolver_0 = module_0.Resolver(str_0, dict_0, str_1)
        subscript_0 = module_1.Subscript(*list_0)
        a_s_t_0 = resolver_0.visit_Subscript(subscript_0)
        a_s_t_1 = resolver_0.visit_Attribute(attribute_0)
        bool_2 = False
        parser_1 = module_0.Parser(bool_2, bool_1)
        str_5 = '1=s@LSoyKqO^r_GSb=l['
        class_def_0 = module_1.ClassDef()
        str_6 = '`?z'
        parser_1.api(str_5, class_def_0, prefix=str_6)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = '$A-tI.$O('
        str_1 = 'e6'
        list_0 = [str_0, str_0]
        str_2 = '\rhL6erf'
        str_3 = 'SdHyJ0x}{\\.]7`]u'
        str_4 = "UG'DX|CH\x0cC;-\x0b"
        str_5 = 'xg'
        bool_0 = False
        int_0 = 238
        dict_0 = {str_3: int_0}
        parser_0 = module_0.Parser(bool_0, dict_0)
        str_6 = "`K'("
        assign_0 = module_1.Assign(*list_0)
        parser_0.globals(str_6, assign_0)
        dict_1 = {str_2: str_0, str_3: list_0, str_4: str_4, str_5: list_0}
        import_from_0 = module_1.ImportFrom(*list_0, **dict_1)
        str_7 = 'j8'
        dict_2 = {str_7: str_1}
        parser_1 = module_0.Parser(bool_0, dict_2, dict_2)
        parser_1.imports(str_1, import_from_0)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'Pqpu"Ce'
        str_1 = '3i\x0bp\\5_E!{r'
        str_2 = 'l6{:8or)h/" V!\t/-G,\\'
        dict_0 = {str_0: str_1, str_2: str_1, str_1: str_0, str_1: str_1, str_0: str_0}
        parser_0 = module_0.Parser(dict_0)
        dict_1 = {str_2: str_0}
        resolver_0 = module_0.Resolver(str_0, dict_1)
        list_0 = [dict_0]
        import_0 = module_1.Import(*list_0)
        parser_0.imports(str_0, import_0)
    except BaseException:
        pass

def test_case_22():
    try:
        parser_0 = module_0.Parser()
        str_0 = parser_0.compile()
        module_x_var_0 = None
        parser_0.load_docstring(str_0, module_x_var_0)
        bool_0 = parser_0.is_public(str_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 'typing.Tuple'
        int_0 = 3
        bool_0 = True
        parser_0 = module_0.Parser(int_0, bool_0)
        parser_0.parse(str_0, str_0)
        expr_0 = module_1.expr()
        str_1 = "/'zbf"
        str_2 = module_0.code(str_1)
        str_3 = parser_0.compile()
        str_4 = '<+K<XIn]u\r-%'
        bool_1 = parser_0.is_public(str_4)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = '` <= '
        list_0 = []
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        parser_0 = module_0.Parser(dict_0)
        str_1 = module_0.doctest(str_0)
        str_2 = 'I2M1f:wr__'
        parser_0.parse(str_0, str_2)
        import_from_0 = module_1.ImportFrom()
        parser_0.imports(str_2, import_from_0)
        str_3 = module_0.parent(str_0)
        str_4 = parser_0.compile()
        str_5 = 'v;2c(ZTW<oh~'
        list_1 = None
        parser_0.class_api(str_0, str_5, list_1, list_0)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = ' <= '
        list_0 = []
        str_1 = module_0.code(str_0)
        list_1 = []
        str_2 = '4gvE\n_eW)iSg\x0c\x0b'
        str_3 = "6%K&S\\i+'EIRxhm?r"
        dict_0 = {str_1: str_2, str_3: str_2, str_3: str_1, str_3: str_3, str_1: str_1}
        parser_0 = module_0.Parser(dict_0)
        str_4 = module_0.doctest(str_0)
        parser_0.class_api(str_0, str_0, list_0, list_1)
        str_5 = 'bwOT%'
        str_6 = 'hI{J\\0!>+'
        str_7 = '5|5'
        parser_0.parse(str_6, str_7)
        str_8 = module_0.esc_underscore(str_4)
        str_9 = 'Ta:'
        str_10 = module_0.parent(str_9)
        list_2 = [str_0]
        str_11 = 'phFHfr}'
        list_3 = [parser_0, str_1]
        str_12 = '@classmethod'
        resolver_0 = module_0.Resolver(str_12, dict_0)
        str_13 = 'lH\x0b/Z1'
        dict_1 = {str_11: list_3, str_13: str_5}
        function_def_0 = module_1.FunctionDef(*list_2, **dict_1)
        parser_0.api(str_10, function_def_0)
    except BaseException:
        pass