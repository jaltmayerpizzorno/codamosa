# Automatically generated by Pynguin.
import pytutils.lazy.lazy_import as module_0

def test_case_0():
    try:
        import_processor_0 = module_0.ImportProcessor()
        list_0 = []
        illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(import_processor_0, list_0)
        var_0 = illegal_use_of_scope_replacer_0.__str__()
    except BaseException:
        pass

def test_case_1():
    try:
        import_processor_0 = module_0.ImportProcessor()
        str_0 = '%2<1$VHA%Sr#\nA ;lU.'
        illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(import_processor_0, str_0, str_0)
        var_0 = illegal_use_of_scope_replacer_0.__str__()
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -626
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
        illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(int_0, dict_0)
        var_0 = illegal_use_of_scope_replacer_0.__unicode__()
    except BaseException:
        pass

def test_case_3():
    try:
        import_processor_0 = module_0.ImportProcessor()
        set_0 = {import_processor_0}
        illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(import_processor_0, set_0)
        var_0 = illegal_use_of_scope_replacer_0.__repr__()
    except BaseException:
        pass

def test_case_4():
    try:
        var_0 = {}
        str_0 = 'test'
        scope_replacer_0 = module_0.ScopeReplacer(var_0, var_0, str_0)
        str_1 = 'test'
        var_1 = var_0[str_1]
        var_2 = var_1.test_attr
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = None
        import_processor_0 = module_0.ImportProcessor()
        tuple_0 = ()
        str_1 = None
        str_2 = "\n    Parses env file content.\n\n    From honcho.\n\n    >>> lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']\n    >>> load_env_file(lines, write_environ=dict())\n    OrderedDict([('TEST', '.../yeee'),\n             ('THISIS', '.../a/test'),\n             ('YOLO',\n              '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])\n\n    "
        import_replacer_0 = module_0.ImportReplacer(str_1, tuple_0, str_0, import_processor_0, str_2)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'l#RQe\rL+wIjeBm)qH9*'
        int_0 = -634
        bool_0 = False
        list_0 = [bool_0, str_0]
        import_replacer_0 = module_0.ImportReplacer(int_0, bool_0, list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'T\rE4=SD?N7c5nbVx'
        import_processor_0 = module_0.ImportProcessor(str_0)
        dict_0 = {str_0: import_processor_0, str_0: str_0, str_0: import_processor_0}
        var_0 = import_processor_0.lazy_import(dict_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '2\x0b6r( rc0'
        import_processor_0 = module_0.ImportProcessor()
        var_0 = import_processor_0.lazy_import(str_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 9
        str_0 = 'Lazily compiled regex objects.\n\nThis module defines a class which creates proxy objects for regex\ncompilation.  This allows overriding re.compile() to return lazily compiled\nobjects.\n\nWe do this rather than just providing a new interface so that it will also\nbe used by existing Python modules that create regexs.\n'
        var_0 = module_0.lazy_import(int_0, str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        import_processor_0 = module_0.ImportProcessor()
        list_0 = [import_processor_0, import_processor_0, import_processor_0, import_processor_0]
        str_0 = None
        scope_replacer_0 = None
        bytes_0 = b"\x96k\xa3\x15\xa9'5\x0c\xe3"
        tuple_0 = (str_0, bytes_0)
        import_replacer_0 = module_0.ImportReplacer(list_0, str_0, scope_replacer_0, tuple_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '\n    Iterate over running totals, ie [a,b,c,d] -> func( func( func(a, b), c), d) with each func result yielded.\n    Func is operator.add by default.\n\n    >>> list(accumulate([1,2,3,4,5]))\n    [1, 3, 6, 10, 15]\n    >>> list(accumulate([1,2,3,4,5], operator.mul))\n    [1, 2, 6, 24, 120]\n\n    :param iterable: Iterable\n    :param func: method (default=operator.add) to call for each pair of (last call result or first item, next item)\n    :return generator: Generator\n    '
        import_processor_0 = module_0.ImportProcessor()
        var_0 = import_processor_0.lazy_import(str_0, str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '\n    from bzrlib import branch\n    '
        var_0 = module_0.lazy_import(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'fKa)2'
        int_0 = -4
        illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(str_0, int_0)
        str_1 = '8?g3qk%nG\x0c#) '
        import_processor_0 = module_0.ImportProcessor()
        var_0 = import_processor_0.lazy_import(illegal_use_of_scope_replacer_0, str_1)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'T\rE4=SD?N7c5nbVx'
        tuple_0 = ()
        list_0 = [tuple_0, tuple_0, str_0]
        import_processor_0 = None
        list_1 = [import_processor_0, str_0, import_processor_0]
        tuple_1 = (import_processor_0, list_1)
        str_1 = ''
        str_2 = 'wEt^x(`cS#I7'
        str_3 = 'K $mcRU0Jd%`=D\x0cA0'
        dict_0 = {str_0: import_processor_0, str_1: str_2, str_3: list_1}
        var_0 = module_0.disallow_proxying()
        illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(tuple_1, dict_0)
        var_1 = illegal_use_of_scope_replacer_0.__eq__(list_0)
        var_2 = module_0.disallow_proxying()
        var_3 = illegal_use_of_scope_replacer_0.__eq__(illegal_use_of_scope_replacer_0)
        import_processor_1 = module_0.ImportProcessor(import_processor_0)
        illegal_use_of_scope_replacer_1 = module_0.IllegalUseOfScopeReplacer(import_processor_1, import_processor_1)
        var_4 = illegal_use_of_scope_replacer_1.__str__()
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '2v\x0b6( r\n0'
        import_processor_0 = module_0.ImportProcessor()
        var_0 = import_processor_0.lazy_import(str_0, str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        var_0 = {}
        var_1 = lambda x, y, z: y[z]
        str_0 = 'w'
        scope_replacer_0 = module_0.ScopeReplacer(var_0, var_1, str_0)
        var_2 = lambda x, y, z: y[z]
        str_1 = 'WHW'
        var_3 = scope_replacer_0.__getattribute__(str_1)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = "Restore the original function to re.compile().\n\n    It is safe to call reset_compile() multiple times, it will always\n    restore re.compile() to the value that existed at import time.\n    Though the first call will reset back to the original (it doesn't\n    track nesting level)\n    "
        var_0 = module_0.lazy_import(str_0, str_0, str_0)
    except BaseException:
        pass