# Automatically generated by Pynguin.
import pytutils.lazy.lazy_import as module_0

def test_case_0():
    try:
        dict_0 = {}
        illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(dict_0, dict_0)
        var_0 = illegal_use_of_scope_replacer_0.__unicode__()
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = -914.91
        dict_0 = {}
        illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(float_0, dict_0, float_0)
        var_0 = illegal_use_of_scope_replacer_0.__str__()
    except BaseException:
        pass

def test_case_2():
    try:
        tuple_0 = ()
        dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0}
        illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(tuple_0, dict_0)
        var_0 = illegal_use_of_scope_replacer_0.__str__()
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = []
        bool_0 = False
        illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(list_0, bool_0)
        var_0 = illegal_use_of_scope_replacer_0.__repr__()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\nimport sys\n'
        dict_0 = {}
        float_0 = 2074.601
        scope_replacer_0 = module_0.ScopeReplacer(dict_0, dict_0, float_0)
        var_0 = module_0.lazy_import(str_0, scope_replacer_0)
    except BaseException:
        pass

def test_case_5():
    try:
        var_0 = module_0.disallow_proxying()
        str_0 = '\nimport sys\n'
        var_1 = module_0.lazy_import(str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        illegal_use_of_scope_replacer_0 = None
        set_0 = {illegal_use_of_scope_replacer_0, illegal_use_of_scope_replacer_0}
        list_0 = []
        import_replacer_0 = module_0.ImportReplacer(illegal_use_of_scope_replacer_0, set_0, set_0, list_0, set_0)
    except BaseException:
        pass

def test_case_7():
    try:
        tuple_0 = ()
        dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0}
        list_0 = None
        import_replacer_0 = None
        dict_1 = {}
        import_replacer_1 = module_0.ImportReplacer(dict_0, import_replacer_0, dict_1)
        var_0 = module_0.lazy_import(list_0, import_replacer_1)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '\nimport sys\n'
        var_0 = module_0.lazy_import(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '\nimport sys\n'
        var_0 = module_0.lazy_import(str_0, str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        import_processor_0 = module_0.ImportProcessor()
        var_0 = globals()
        dict_0 = {}
        bytes_0 = b'\xf1\xda\xe0\x9c\xcfS|"Z\xe6\xbc\x93\x17'
        str_0 = '\tstA.c\x0byB8t'
        dict_1 = {}
        import_replacer_0 = module_0.ImportReplacer(dict_0, bytes_0, dict_1, dict_1)
        var_1 = module_0.lazy_import(str_0, import_replacer_0, dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = ',+'
        var_0 = module_0.lazy_import(str_0, str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        var_0 = globals()
        str_0 = '\nimport sys\n'
        dict_0 = {str_0: str_0, str_0: var_0, str_0: var_0, str_0: var_0}
        import_processor_0 = module_0.ImportProcessor(dict_0)
        str_1 = '%(bg_black)s%(log_color)s[%(asctime)s] [%(name)s/%(process)d] %(message)s %(blue)s@%(funcName)s:%(lineno)d #%(levelname)s%(reset)s'
        var_1 = module_0.lazy_import(import_processor_0, str_1)
    except BaseException:
        pass

def test_case_13():
    try:
        import_processor_0 = module_0.ImportProcessor()
        int_0 = None
        float_0 = 677.65925
        int_1 = -1364
        illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(float_0, int_1)
        var_0 = illegal_use_of_scope_replacer_0.__eq__(int_0)
        bytes_0 = b'\xbeVR\xfc#Q5\xe2\xd1X\x8a*'
        import_processor_1 = module_0.ImportProcessor()
        str_0 = '2uxP\rsr;zlY(4K\\9>'
        list_0 = None
        dict_0 = {bytes_0: import_processor_0, import_processor_0: import_processor_1, str_0: import_processor_0, bytes_0: list_0}
        var_1 = import_processor_0.lazy_import(dict_0, str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = "2'ha:%`_n2XH*"
        str_1 = '\\A([A-Za-z_0-9]+)=(.*)\\Z'
        var_0 = module_0.lazy_import(str_0, str_1)
    except BaseException:
        pass

def test_case_15():
    try:
        import_processor_0 = module_0.ImportProcessor()
        dict_0 = {import_processor_0: import_processor_0, import_processor_0: import_processor_0, import_processor_0: import_processor_0}
        tuple_0 = (dict_0,)
        str_0 = "Create lazy imports for all of the imports in text.\n\n    This is typically used as something like::\n\n        from bzrlib.lazy_import import lazy_import\n        lazy_import(globals(), '''\n        from bzrlib import (\n            foo,\n            bar,\n            baz,\n            )\n        import bzrlib.branch\n        import bzrlib.transport\n        ''')\n\n    Then 'foo, bar, baz' and 'bzrlib' will exist as lazy-loaded\n    objects which will be replaced with a real object on first use.\n\n    In general, it is best to only load modules in this way. This is\n    because other objects (functions/classes/variables) are frequently\n    used without accessing a member, which means we cannot tell they\n    have been used.\n    "
        var_0 = import_processor_0.lazy_import(tuple_0, str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        import_processor_0 = module_0.ImportProcessor()
        str_0 = '?7='
        illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(import_processor_0, str_0)
        list_0 = []
        float_0 = 1335.932712
        illegal_use_of_scope_replacer_1 = module_0.IllegalUseOfScopeReplacer(list_0, float_0)
        var_0 = illegal_use_of_scope_replacer_1.__eq__(illegal_use_of_scope_replacer_0)
        float_1 = 677.65925
        int_0 = -1364
        illegal_use_of_scope_replacer_2 = module_0.IllegalUseOfScopeReplacer(float_1, int_0)
        import_processor_1 = module_0.ImportProcessor()
        import_processor_2 = module_0.ImportProcessor()
        var_1 = illegal_use_of_scope_replacer_2.__str__()
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '\n  import bi.osu8^d  '
        var_0 = module_0.lazy_import(str_0, str_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'from bzrlib import errors'
        var_0 = module_0.lazy_import(str_0, str_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '\n  mpor $iosuDi\n^d  '
        str_1 = 'bad from/import %r'
        dict_0 = {}
        str_2 = '] ;,SC1<dE%.ux'
        str_3 = "*PBGq97.P8UG:'/,H6?"
        dict_1 = {str_2: str_1, str_0: str_0, str_3: str_2}
        import_processor_0 = None
        illegal_use_of_scope_replacer_0 = None
        import_replacer_0 = module_0.ImportReplacer(dict_1, import_processor_0, illegal_use_of_scope_replacer_0)
        tuple_0 = (import_replacer_0,)
        float_0 = 293.700021
        scope_replacer_0 = module_0.ScopeReplacer(dict_0, tuple_0, float_0)
        dict_2 = {str_1: scope_replacer_0}
        set_0 = {str_0, str_1, tuple_0, float_0}
        str_4 = 'WLS9Jvx6|U`[e'
        scope_replacer_1 = module_0.ScopeReplacer(dict_2, set_0, str_4)
        int_0 = 4680
        scope_replacer_2 = module_0.ScopeReplacer(dict_2, scope_replacer_1, int_0)
        var_0 = scope_replacer_2.__call__()
    except BaseException:
        pass