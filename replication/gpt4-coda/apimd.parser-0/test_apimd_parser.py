# Automatically generated by Pynguin.
import apimd.parser as module_0
import ast as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'single_underscore'
    str_1 = 'wi|%0'
    str_2 = None
    str_3 = '#(zud]X}o4z{'
    dict_0 = {str_2: str_1, str_1: str_0, str_0: str_3}
    resolver_0 = module_0.Resolver(str_1, dict_0, str_2)
    str_4 = 'SomeType'
    list_0 = [str_4, str_0]
    constant_0 = module_1.Constant(*list_0)
    a_s_t_0 = resolver_0.visit_Constant(constant_0)

def test_case_2():
    str_0 = 'j?E;8c'
    str_1 = module_0.parent(str_0)

def test_case_3():
    str_0 = 'tp\x0b*!`fL=|#/U2$SA'
    bool_0 = module_0.is_public_family(str_0)

def test_case_4():
    str_0 = '!'
    str_1 = module_0.code(str_0)

def test_case_5():
    str_0 = '\tZ28QH(h_xv3qif\x0c'
    str_1 = module_0.esc_underscore(str_0)

def test_case_6():
    str_0 = '@N'
    str_1 = module_0.doctest(str_0)

def test_case_7():
    expr_0 = module_1.expr()
    str_0 = module_0.const_type(expr_0)

def test_case_8():
    dict_0 = None
    str_0 = None
    resolver_0 = module_0.Resolver(str_0, dict_0)
    list_0 = [resolver_0]
    subscript_0 = module_1.Subscript(*list_0)
    a_s_t_0 = resolver_0.visit_Subscript(subscript_0)

def test_case_9():
    str_0 = 'fdM\x0bA@T{y)O/6'
    str_1 = 'LxuKB\r>,`$noy\tQ'
    str_2 = '6r[DEk^sQN{E$'
    str_3 = None
    dict_0 = {str_0: str_0, str_1: str_1, str_0: str_0, str_2: str_3}
    resolver_0 = module_0.Resolver(str_0, dict_0, str_1)
    list_0 = [resolver_0]
    constant_0 = module_1.Constant(*list_0)
    str_4 = 'Y{'
    str_5 = '6/D)IB$V7n17MD:ee'
    str_6 = '0N4q{<i\t[l4F[O~H(aZ'
    str_7 = '5jlp#cgQ}\\pobUo\r'
    dict_1 = {str_4: str_5, str_6: str_4, str_7: str_4}
    str_8 = 'j'
    resolver_1 = module_0.Resolver(str_4, dict_1, str_8)
    a_s_t_0 = resolver_1.visit_Constant(constant_0)

def test_case_10():
    str_0 = 'tmfj!\t<P=5a]=cg_U?'
    list_0 = [str_0]
    constant_0 = module_1.Constant(*list_0)
    str_1 = 'YS'
    dict_0 = {str_0: str_1}
    resolver_0 = module_0.Resolver(str_0, dict_0)
    a_s_t_0 = resolver_0.visit_Constant(constant_0)
    bool_0 = module_0.is_magic(str_0)

def test_case_11():
    stmt_0 = None
    list_0 = [stmt_0]
    list_1 = [list_0]
    attribute_0 = module_1.Attribute(*list_1)
    dict_0 = {}
    str_0 = '*=UDDGg1HfH'
    resolver_0 = module_0.Resolver(str_0, dict_0, str_0)
    a_s_t_0 = resolver_0.visit_Attribute(attribute_0)

def test_case_12():
    parser_0 = module_0.Parser()

def test_case_13():
    str_0 = 'O(0},W_,N>gp'
    list_0 = []
    stmt_0 = None
    list_1 = [stmt_0]
    dict_0 = {str_0: str_0}
    parser_0 = module_0.Parser(dict_0, dict_0, dict_0)
    parser_0.class_api(str_0, str_0, list_0, list_1)

def test_case_14():
    parser_0 = module_0.Parser()
    str_0 = ''
    parser_0.parse(str_0, str_0)

def test_case_15():
    str_0 = 'O(0},W_,N>gp'
    list_0 = []
    stmt_0 = None
    list_1 = [stmt_0]
    dict_0 = {}
    parser_0 = module_0.Parser(dict_0, dict_0, dict_0)
    parser_0.class_api(str_0, str_0, list_0, list_1)

def test_case_16():
    bool_0 = False
    int_0 = 1
    str_0 = '^M$R|t#Sqo*i:<rk4E}_'
    str_1 = 'd '
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_1}
    parser_0 = module_0.Parser(bool_0, int_0, bool_0, dict_0, dict_0, dict_0)
    import_from_0 = module_1.ImportFrom()
    parser_0.imports(str_1, import_from_0)
    parser_0.parse(str_1, str_1)

def test_case_17():
    parser_0 = module_0.Parser()
    str_0 = parser_0.compile()

def test_case_18():
    str_0 = '(K|i2Zz\x0cB;'
    str_1 = 'Tp2 \x0bpg'
    str_2 = module_0.parent(str_1)
    str_3 = 'yv\niDm3AXIyLnx\x0b{<U{'
    bool_0 = module_0.is_public_family(str_1)
    int_0 = 22
    bool_1 = True
    dict_0 = {}
    str_4 = 'b'
    str_5 = '$^;z]AEDb=\t#bo&cEnc'
    dict_1 = {str_4: str_5, str_3: str_4, str_0: str_3}
    parser_0 = module_0.Parser(int_0, bool_1, dict_0, dict_1, dict_1)
    str_6 = '<g'
    module_x_var_0 = None
    parser_0.load_docstring(str_6, module_x_var_0)

def test_case_19():
    bool_0 = False
    int_0 = 1
    str_0 = '^M$O|t#Sqo*i:<rk4EL_'
    str_1 = 'd '
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_1}
    parser_0 = module_0.Parser(bool_0, int_0, bool_0, dict_0, dict_0, dict_0)
    parser_0.parse(str_1, str_1)

def test_case_20():
    bool_0 = False
    dict_0 = {}
    str_0 = 'GHWj\t4"3X[N,dR$'
    str_1 = "LjrT\r@'Mgmn"
    dict_1 = {str_0: str_1, str_1: str_0, str_0: str_0}
    parser_0 = module_0.Parser(bool_0, dict_0, dict_1, dict_1)
    str_2 = parser_0.compile()

def test_case_21():
    str_0 = 'ay'
    bool_0 = module_0.is_public_family(str_0)

def test_case_22():
    str_0 = '\tZ28QH(h_xv3qif\x0c'
    list_0 = [str_0]
    ann_assign_0 = module_1.AnnAssign(*list_0)
    set_0 = {str_0, str_0, str_0}
    str_1 = 'pqi(w\x0b\nb9"f'
    dict_0 = {str_0: set_0, str_1: set_0}
    parser_0 = module_0.Parser(dict_0)
    parser_0.globals(str_0, ann_assign_0)
    str_2 = module_0.esc_underscore(str_0)

def test_case_23():
    str_0 = ''
    str_1 = module_0.code(str_0)

def test_case_24():
    str_0 = '^XaR'
    list_0 = [str_0, str_0, str_0]
    dict_0 = {str_0: str_0}
    assign_0 = module_1.Assign(*list_0, **dict_0)
    int_0 = 1539
    str_1 = None
    dict_1 = {str_1: str_1}
    str_2 = '%%s#8jVWk5n;}^"|?Z'
    set_0 = {str_1, str_2, str_1, str_2}
    dict_2 = {str_1: set_0}
    parser_0 = module_0.Parser(int_0, dict_1, dict_2)
    parser_0.globals(str_0, assign_0)

def test_case_25():
    str_0 = '^XaR'
    list_0 = [str_0, str_0, str_0]
    bool_0 = True
    parser_0 = module_0.Parser(bool_0)
    var_0 = parser_0.__post_init__()
    dict_0 = {str_0: str_0}
    assign_0 = module_1.Assign(*list_0, **dict_0)
    parser_0.globals(str_0, assign_0)
    str_1 = ']NSkd'
    list_1 = []
    list_2 = [assign_0]
    parser_0.class_api(str_0, str_1, list_1, list_2)

def test_case_26():
    str_0 = 'single_underscore'
    list_0 = [str_0, str_0]
    subscript_0 = module_1.Subscript(*list_0)
    str_1 = 'oUNfJ+P9'
    str_2 = ''
    dict_0 = {str_1: str_1, str_0: str_0, str_2: str_1}
    str_3 = ''
    dict_1 = {str_0: str_0, str_2: str_2, str_0: str_0, str_2: str_2}
    expr_0 = module_1.expr(**dict_1)
    list_1 = [expr_0, expr_0, expr_0, expr_0]
    list_2 = [subscript_0]
    bool_0 = True
    int_0 = 1377
    dict_2 = {str_1: int_0, str_2: int_0, str_2: int_0, str_2: int_0}
    set_0 = set()
    dict_3 = {str_0: set_0, str_0: set_0}
    parser_0 = module_0.Parser(bool_0, dict_2, dict_0, dict_3, dict_0)
    parser_0.class_api(str_1, str_3, list_1, list_2)

def test_case_27():
    parser_0 = module_0.Parser()
    str_0 = ''
    parser_0.parse(str_0, str_0)
    str_1 = parser_0.compile()
    var_0 = parser_0.const

def test_case_28():
    str_0 = 'example'
    str_1 = 'example.Union'
    str_2 = 'example.Optional'
    str_3 = 'example.List'
    str_4 = 'example.Dict'
    str_5 = 'example.Set'
    str_6 = 'example.Tuple'
    str_7 = 'typing.Union'
    str_8 = 'typing.Optional'
    str_9 = 'typing.List'
    str_10 = 'typing.Dict'
    str_11 = 'typing.Set'
    str_12 = 'typing.Tuple'
    str_13 = {str_1: str_7, str_2: str_8, str_3: str_9, str_4: str_10, str_5: str_11, str_6: str_12}
    resolver_0 = module_0.Resolver(str_0, str_13)
    int_0 = 0
    str_14 = 'Union[int, str]'
    var_0 = module_1.parse(str_14)
    var_1 = var_0.body[int_0]
    var_2 = var_1.value
    a_s_t_0 = resolver_0.visit_Subscript(var_2)
    var_3 = a_s_t_0.left
    var_4 = a_s_t_0.right
    str_15 = 'Optional[str]'
    var_5 = module_1.parse(str_15)
    var_6 = var_5.body[int_0]
    var_7 = var_6.value
    a_s_t_1 = resolver_0.visit_Subscript(var_7)

def test_case_29():
    str_0 = 'example'
    str_1 = 'example.Union'
    str_2 = 'example.Optional'
    str_3 = 'example.List'
    str_4 = 'example.Dict'
    str_5 = 'example.SeA'
    str_6 = 'example.Tuple'
    str_7 = 'typing.Union'
    str_8 = 'typing.List'
    str_9 = 'typing.Dict'
    str_10 = 'typing.Set'
    str_11 = {str_1: str_7, str_2: str_9, str_3: str_8, str_4: str_9, str_5: str_10, str_6: str_5}
    resolver_0 = module_0.Resolver(str_0, str_11)
    int_0 = 0
    str_12 = 'Union[int, str]'
    var_0 = module_1.parse(str_12)
    var_1 = var_0.body[int_0]
    var_2 = var_1.value
    a_s_t_0 = resolver_0.visit_Subscript(var_2)
    var_3 = a_s_t_0.left
    var_4 = a_s_t_0.right
    str_13 = 'Optiongal[str]'
    var_5 = module_1.parse(str_13)
    var_6 = var_5.body[int_0]
    var_7 = var_6.value
    a_s_t_1 = resolver_0.visit_Subscript(var_7)