# Automatically generated by Pynguin.
import apimd.parser as module_0
import ast as module_1

def test_case_0():
    str_0 = 'TaDwA!23?%T3o`_'
    bool_0 = module_0.is_public_family(str_0)

def test_case_1():
    str_0 = '9t\\'
    str_1 = module_0.parent(str_0)

def test_case_2():
    str_0 = 'lne0z48#:\x0bdHAA2d*ux\n'
    str_1 = module_0.code(str_0)

def test_case_3():
    str_0 = "6S>oR'zB][YkjH``{y\rr"
    str_1 = module_0.esc_underscore(str_0)

def test_case_4():
    str_0 = '()\n\n'
    str_1 = module_0.doctest(str_0)

def test_case_5():
    str_0 = 'D`gs]|`p#d"{a6B'
    list_0 = []
    arguments_0 = module_1.arguments(*list_0)
    list_1 = [arguments_0, str_0]
    constant_0 = module_1.Constant(*list_1)
    str_1 = 'typing.Reversible'
    dict_0 = {}
    resolver_0 = module_0.Resolver(str_1, dict_0)
    a_s_t_0 = resolver_0.visit_Constant(constant_0)
    parser_0 = module_0.Parser()

def test_case_6():
    str_0 = 'Pg'
    str_1 = 'L'
    str_2 = 'b\t)Max'
    set_0 = {str_1, str_2}
    str_3 = 'tT~>'
    dict_0 = {str_0: set_0, str_0: set_0, str_3: set_0}
    list_0 = [dict_0, set_0]
    attribute_0 = module_1.Attribute(*list_0)
    str_4 = 'IL'
    str_5 = '\\(ziE'
    dict_1 = {str_4: str_5, str_5: str_4}
    resolver_0 = module_0.Resolver(str_4, dict_1)
    a_s_t_0 = resolver_0.visit_Attribute(attribute_0)

def test_case_7():
    int_0 = -1276
    dict_0 = {}
    parser_0 = module_0.Parser(int_0, dict_0, dict_0, dict_0)
    str_0 = parser_0.compile()

def test_case_8():
    str_0 = 'u(g'
    str_1 = None
    str_2 = 'k3|#\\-D8hm_K]VTG\x0c\\c'
    dict_0 = {str_1: str_1, str_1: str_0, str_1: str_1, str_0: str_2}
    parser_0 = module_0.Parser(dict_0, dict_0, dict_0)
    str_3 = parser_0.compile()

def test_case_9():
    str_0 = 'Ah\\Y}'
    str_1 = 'Any'
    bool_0 = True
    parser_0 = module_0.Parser(bool_0)
    parser_0.parse(str_0, str_1)

def test_case_10():
    str_0 = '\tstn"+@`6w#*%'
    int_0 = 89
    bool_0 = False
    parser_0 = module_0.Parser(int_0, bool_0)
    bool_1 = module_0.is_public_family(str_0)
    list_0 = [bool_1]
    dict_0 = {str_0: bool_0}
    ann_assign_0 = module_1.AnnAssign(*list_0, **dict_0)
    parser_0.globals(str_0, ann_assign_0)

def test_case_11():
    str_0 = 'Ah\\Y}'
    bool_0 = True
    parser_0 = module_0.Parser(bool_0)
    list_0 = []
    stmt_0 = None
    list_1 = [stmt_0, stmt_0, stmt_0, stmt_0, stmt_0, stmt_0]
    parser_0.class_api(str_0, str_0, list_0, list_1)

def test_case_12():
    bool_0 = True
    int_0 = 1071
    dict_0 = {}
    str_0 = '0Yr'
    dict_1 = {str_0: str_0, str_0: str_0}
    parser_0 = module_0.Parser(bool_0, int_0, dict_0, dict_1, dict_1)
    expr_0 = module_1.expr()
    list_0 = [expr_0, expr_0]
    name_0 = module_1.Name()
    list_1 = [name_0]
    parser_0.class_api(str_0, str_0, list_0, list_1)

def test_case_13():
    module_x_var_0 = None
    bool_0 = True
    str_0 = ''
    str_1 = 'JbNu5F^:z,X-m'
    dict_0 = {str_0: str_1, str_0: str_0, str_1: str_0}
    parser_0 = module_0.Parser(bool_0, dict_0, dict_0)
    parser_0.load_docstring(str_0, module_x_var_0)

def test_case_14():
    str_0 = 'a'
    bool_0 = True
    int_0 = 1108
    dict_0 = {}
    dict_1 = {}
    parser_0 = module_0.Parser(bool_0, int_0, dict_0, dict_1, dict_1)
    parser_0.parse(str_0, str_0)
    str_1 = parser_0.compile()
    bool_1 = parser_0.is_public(str_0)

def test_case_15():
    str_0 = 'Ah\\Y}'
    str_1 = 'Any'
    bool_0 = False
    parser_0 = module_0.Parser(bool_0)
    parser_0.parse(str_0, str_1)

def test_case_16():
    str_0 = 'D`gs]|`p#d"{a6B'
    str_1 = module_0.code(str_0)
    list_0 = []
    arguments_0 = module_1.arguments(*list_0)
    list_1 = [arguments_0, str_1]
    constant_0 = module_1.Constant(*list_1)
    str_2 = 'typing.Reversible'
    dict_0 = {}
    resolver_0 = module_0.Resolver(str_2, dict_0)
    a_s_t_0 = resolver_0.visit_Constant(constant_0)
    ann_assign_0 = module_1.AnnAssign()
    str_3 = 'y-j@@B'
    str_4 = module_0.code(str_3)
    parser_0 = module_0.Parser()
    ann_assign_1 = None
    parser_0.globals(str_0, ann_assign_1)

def test_case_17():
    str_0 = 'm9'
    bool_0 = module_0.is_magic(str_0)

def test_case_18():
    str_0 = 'Astn?2@`6w#s%'
    assign_0 = module_1.Assign()
    int_0 = 128
    bool_0 = True
    parser_0 = module_0.Parser(int_0, bool_0)
    dict_0 = {}
    parser_1 = module_0.Parser(bool_0, dict_0, dict_0)
    assign_1 = None
    parser_1.globals(str_0, assign_1)

def test_case_19():
    expr_0 = module_1.expr()
    str_0 = module_0.const_type(expr_0)

def test_case_20():
    import_from_0 = None
    int_0 = -2390
    str_0 = '?j@@s}`G6N\x0bn8CuifM'
    str_1 = ''
    set_0 = {str_0, str_1}
    dict_0 = {str_0: set_0, str_1: set_0}
    parser_0 = module_0.Parser()
    list_0 = [set_0, parser_0, parser_0]
    str_2 = '1t+'
    dict_1 = {str_2: dict_0, str_1: str_1, str_2: int_0, str_1: str_1, str_0: parser_0, str_1: import_from_0}
    assign_0 = module_1.Assign(*list_0, **dict_1)
    parser_0.globals(str_0, assign_0)

def test_case_21():
    str_0 = 'lkT"n&\'}j@R'
    str_1 = module_0.esc_underscore(str_0)
    list_0 = [str_1, str_0]
    constant_0 = module_1.Constant(*list_0)
    str_2 = 'typing.MutableSequence'
    str_3 = 'K['
    dict_0 = {str_2: str_2, str_2: str_1, str_3: str_0, str_3: str_0}
    resolver_0 = module_0.Resolver(str_1, dict_0)
    a_s_t_0 = resolver_0.visit_Constant(constant_0)
    str_4 = ')n'
    str_5 = 'kJ6'
    dict_1 = {str_4: str_5, str_4: str_1}
    resolver_1 = module_0.Resolver(str_1, dict_1)
    a_s_t_1 = resolver_1.visit_Constant(constant_0)

def test_case_22():
    subscript_0 = None
    list_0 = [subscript_0]
    name_0 = module_1.Name(*list_0)
    str_0 = '}&m\tRmCwe>'
    str_1 = 't(=i(3z)hWQ'
    str_2 = '?ru*MCKH%Qne\tx'
    dict_0 = {str_0: str_1, str_2: str_2, str_0: str_0, str_2: str_1}
    str_3 = '='
    resolver_0 = module_0.Resolver(str_0, dict_0, str_3)
    a_s_t_0 = resolver_0.visit_Name(name_0)
    assign_0 = module_1.Assign()

def test_case_23():
    str_0 = '4*tq,I"8pQr'
    list_0 = [str_0, str_0, str_0]
    subscript_0 = module_1.Subscript(*list_0)
    dict_0 = {}
    resolver_0 = module_0.Resolver(str_0, dict_0)
    a_s_t_0 = resolver_0.visit_Subscript(subscript_0)

def test_case_24():
    str_0 = 'P'
    bool_0 = False
    int_0 = 1088
    dict_0 = {}
    dict_1 = {str_0: str_0, str_0: str_0}
    parser_0 = module_0.Parser(bool_0, int_0, dict_0, dict_1, dict_1)
    list_0 = [str_0]
    str_1 = ''
    assign_0 = module_1.Assign(*list_0)
    parser_0.globals(str_1, assign_0)

def test_case_25():
    str_0 = '>>> '
    str_1 = module_0.doctest(str_0)
    expr_0 = module_1.expr()
    str_2 = module_0.const_type(expr_0)
    assign_0 = module_1.Assign()

def test_case_26():
    str_0 = '\nif True:\n    a = 1\nelse:\n    b = 2\n    try:\n        print(1)\n    except:\n        print(2)\n    finally:\n        print(3)\n    '
    var_0 = module_1.parse(str_0)
    var_1 = var_0.body
    iterator_0 = module_0.walk_body(var_1)
    var_2 = list(iterator_0)
    var_3 = len(var_2)

def test_case_27():
    str_0 = 'test'
    var_0 = {}
    resolver_0 = module_0.Resolver(str_0, var_0)
    int_0 = 0
    str_1 = 'Union[1, 2, 3, 4]'
    var_1 = module_1.parse(str_1)
    var_2 = var_1.body[int_0]
    var_3 = var_2.value
    var_4 = resolver_0.visit(var_3)
    var_5 = module_1.unparse(var_4)
    str_2 = 'Optional[1]'
    var_6 = module_1.parse(str_2)
    var_7 = var_6.body[int_0]
    var_8 = var_7.value
    var_9 = resolver_0.visit(var_8)
    var_10 = module_1.unparse(var_9)
    str_3 = 'List[int]'
    var_11 = module_1.parse(str_3)
    var_12 = var_11.body[int_0]
    var_13 = var_12.value
    var_14 = resolver_0.visit(var_13)
    var_15 = module_1.unparse(var_14)
    str_4 = 'test.a'
    str_5 = '0'
    str_6 = {str_4: str_5}
    resolver_1 = module_0.Resolver(str_0, str_6)
    str_7 = 'a'
    var_16 = module_1.parse(str_7)
    var_17 = var_16.body[int_0]
    var_18 = var_17.value
    var_19 = resolver_1.visit(var_18)
    var_20 = module_1.unparse(var_19)