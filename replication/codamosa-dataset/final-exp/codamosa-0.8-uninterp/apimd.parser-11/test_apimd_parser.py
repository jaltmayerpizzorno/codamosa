# Automatically generated by Pynguin.
import apimd.parser as module_0
import ast as module_1

def test_case_0():
    str_0 = 'typing.Generator'
    str_1 = module_0.esc_underscore(str_0)
    str_2 = 'Z'
    str_3 = module_0.parent(str_2)

def test_case_1():
    str_0 = 'Z'
    bool_0 = module_0.is_magic(str_0)

def test_case_2():
    str_0 = '!kRCG/&CIH'
    bool_0 = module_0.is_public_family(str_0)

def test_case_3():
    str_0 = 'PT"~I0\x0b&6w'
    str_1 = 'fB'
    bool_0 = False
    dict_0 = {}
    parser_0 = module_0.Parser(bool_0, bool_0, dict_0)
    parser_0.parse(str_0, str_1)

def test_case_4():
    str_0 = "e<rfL$'s?)ygTyg2"
    str_1 = module_0.code(str_0)

def test_case_5():
    str_0 = '`'
    str_1 = module_0.doctest(str_0)

def test_case_6():
    expr_0 = module_1.expr()
    str_0 = module_0.const_type(expr_0)
    str_1 = '# Module `{}`'
    str_2 = "5Q=^'\\H"
    dict_0 = {str_0: str_1, str_0: str_2}
    parser_0 = module_0.Parser(dict_0, dict_0)
    var_0 = parser_0.__post_init__()

def test_case_7():
    module_x_var_0 = None
    str_0 = None
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    parser_0 = module_0.Parser(dict_0)
    parser_0.load_docstring(str_0, module_x_var_0)

def test_case_8():
    bool_0 = False
    dict_0 = {}
    str_0 = 'ns'
    str_1 = '8Y1\to\n$0/a'
    dict_1 = {str_1: str_0, str_0: str_1}
    parser_0 = module_0.Parser(bool_0, dict_0, dict_1)
    str_2 = parser_0.compile()

def test_case_9():
    str_0 = '__'
    expr_0 = module_1.expr()
    bool_0 = True
    str_1 = '~6'
    int_0 = 12
    parser_0 = module_0.Parser(bool_0, int_0)
    parser_0.parse(str_0, str_1)
    str_2 = parser_0.compile()

def test_case_10():
    str_0 = '?i;`iT?1L3K^!'
    dict_0 = {str_0: str_0}
    list_0 = [str_0]
    ann_assign_0 = module_1.AnnAssign(*list_0)
    bool_0 = True
    parser_0 = module_0.Parser(bool_0, dict_0)
    parser_0.globals(str_0, ann_assign_0)
    resolver_0 = module_0.Resolver(str_0, dict_0, str_0)

def test_case_11():
    expr_0 = module_1.expr()
    dict_0 = None
    parser_0 = module_0.Parser(dict_0)
    import_from_0 = module_1.ImportFrom()
    str_0 = parser_0.compile()
    list_0 = []
    list_1 = []
    parser_0.class_api(str_0, str_0, list_0, list_1)
    str_1 = ''
    resolver_0 = module_0.Resolver(str_1, dict_0, str_0)

def test_case_12():
    expr_0 = module_1.expr()
    str_0 = module_0.const_type(expr_0)
    str_1 = ' async '
    str_2 = '# Module `{}`'
    str_3 = '?n@D,\t$fOc'
    str_4 = "5Q=^'\\H"
    dict_0 = {str_0: str_2, str_3: str_4}
    parser_0 = module_0.Parser(dict_0, dict_0)
    str_5 = parser_0.resolve(str_0, expr_0, str_1)
    var_0 = parser_0.__post_init__()

def test_case_13():
    dict_0 = {}
    assign_0 = module_1.Assign()
    parser_0 = module_0.Parser(dict_0, dict_0, dict_0)
    str_0 = parser_0.compile()

def test_case_14():
    str_0 = '__'
    expr_0 = module_1.expr()
    bool_0 = False
    str_1 = 'b0'
    int_0 = 12
    parser_0 = module_0.Parser(bool_0, int_0)
    parser_0.parse(str_0, str_1)
    str_2 = parser_0.compile()

def test_case_15():
    str_0 = 'S'
    dict_0 = {}
    import_from_0 = module_1.ImportFrom(**dict_0)
    str_1 = 'i->0IqFAOvDY{1z:'
    list_0 = [str_0, import_from_0]
    name_0 = module_1.Name(*list_0)
    str_2 = None
    dict_1 = {str_0: str_0, str_1: str_2, str_2: str_2}
    resolver_0 = module_0.Resolver(str_1, dict_1)
    a_s_t_0 = resolver_0.visit_Name(name_0)

def test_case_16():
    dict_0 = {}
    import_from_0 = module_1.ImportFrom(**dict_0)
    int_0 = -1482
    str_0 = 'SQggh\x0b t/QY)qv=#'
    dict_1 = {str_0: str_0, str_0: str_0}
    parser_0 = module_0.Parser(int_0, dict_1, dict_1)
    parser_0.imports(str_0, import_from_0)
    list_0 = [str_0, import_from_0]
    name_0 = module_1.Name(*list_0)
    str_1 = None
    dict_2 = {str_1: str_1, str_1: str_0, str_1: str_1}
    resolver_0 = module_0.Resolver(str_1, dict_2)
    a_s_t_0 = resolver_0.visit_Name(name_0)

def test_case_17():
    str_0 = None
    set_0 = set()
    str_1 = 'lrArFTB?_$'
    dict_0 = {str_0: set_0, str_0: set_0, str_1: set_0}
    list_0 = [dict_0, dict_0, str_1]
    subscript_0 = module_1.Subscript(*list_0)
    str_2 = 'F["eKgiH!~hZ7!0D&ye'
    str_3 = '3C`t\n(o%S'
    str_4 = '-'
    dict_1 = {str_3: str_4, str_3: str_2}
    resolver_0 = module_0.Resolver(str_2, dict_1, str_2)
    a_s_t_0 = resolver_0.visit_Subscript(subscript_0)
    str_5 = 'typing.re.Pattern'
    str_6 = module_0.code(str_5)

def test_case_18():
    str_0 = 'k'
    dict_0 = {}
    import_from_0 = module_1.ImportFrom(**dict_0)
    int_0 = -1482
    str_1 = ''
    str_2 = 'il->0IqFAOvDY[{1z:'
    dict_1 = {str_1: str_1, str_2: str_1}
    parser_0 = module_0.Parser(int_0, dict_1, dict_1)
    parser_0.imports(str_0, import_from_0)
    list_0 = [str_1, import_from_0]
    name_0 = module_1.Name(*list_0)
    str_3 = '\tD'
    str_4 = None
    dict_2 = {str_0: str_0, str_3: str_1, str_4: str_4}
    str_5 = parser_0.compile()
    resolver_0 = module_0.Resolver(str_2, dict_2)
    a_s_t_0 = resolver_0.visit_Name(name_0)