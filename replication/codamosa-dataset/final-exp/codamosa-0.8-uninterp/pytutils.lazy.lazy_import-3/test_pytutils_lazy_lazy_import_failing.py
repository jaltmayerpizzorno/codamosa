# Automatically generated by Pynguin.
import pytutils.lazy.lazy_import as module_0

def test_case_0():
    try:
        str_0 = ''
        illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(str_0, str_0, str_0)
        var_0 = illegal_use_of_scope_replacer_0.__str__()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'ö'
        illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(str_0, str_0, str_0)
        var_0 = illegal_use_of_scope_replacer_0.__unicode__()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'g '
        illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(str_0, str_0, str_0)
        var_0 = illegal_use_of_scope_replacer_0.__str__()
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 1017.302
        import_processor_0 = module_0.ImportProcessor()
        illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(float_0, import_processor_0)
        var_0 = illegal_use_of_scope_replacer_0.__repr__()
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        bool_0 = False
        tuple_0 = (bool_0, dict_0)
        complex_0 = None
        list_0 = [bool_0, complex_0, bool_0]
        illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(tuple_0, list_0)
        var_0 = illegal_use_of_scope_replacer_0.__eq__(illegal_use_of_scope_replacer_0)
        import_processor_0 = None
        str_0 = "\n    Proxies mutable access to another mapping and allows for attribute-style access.\n\n    >>> a = dict(whoa=True, hello=[1,2,3], why='always')\n    >>> b = ProxyMutableAttrDict(a)\n\n    Nice reprs:\n\n    >>> b\n    <ProxyMutableAttrDict {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}>\n\n    Setting works as you'd expect:\n\n    >>> b['nice'] = False\n    >>> b['whoa'] = 'yeee'\n    >>> b\n    <ProxyMutableAttrDict {'whoa': 'yeee', 'hello': [1, 2, 3], 'why': 'always', 'nice': False}>\n\n    Checking that the changes are in fact being performed on the proxied object:\n\n    >>> a\n    {'whoa': 'yeee', 'hello': [1, 2, 3], 'why': 'always', 'nice': False}\n\n    Attribute style access:\n\n    >>> b.whoa\n    'yeee'\n    >>> b.state = 'new'\n    >>> b\n    <ProxyMutableAttrDict {'whoa': 'yeee', 'hello': [1, 2, 3], 'why': 'always', 'nice': False, 'state': 'new'}>\n\n    Recursion is handled:\n\n    >>> b.subdict = dict(test=True)\n    >>> b.subdict.test\n    True\n    >>> b\n    <ProxyMutableAttrDict {'whoa': 'yeee', 'hello': [1, 2, 3], 'why': 'always', 'nice': False, 'state': 'new',\n    'subdict': <ProxyMutableAttrDict {'test': True}>}>\n\n    "
        import_processor_1 = module_0.ImportProcessor()
        var_1 = import_processor_1.lazy_import(import_processor_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = "'"
        illegal_use_of_scope_replacer_0 = module_0.IllegalUseOfScopeReplacer(str_0, str_0, str_0)
        var_0 = illegal_use_of_scope_replacer_0.__eq__(str_0)
        var_1 = illegal_use_of_scope_replacer_0.__str__()
    except BaseException:
        pass

def test_case_6():
    try:
        var_0 = locals()
        str_0 = 'a_fAn?'
        scope_replacer_0 = module_0.ScopeReplacer(var_0, str_0, str_0)
        var_1 = scope_replacer_0.__setattr__(str_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        dict_0 = {}
        float_0 = -892.2
        float_1 = 3076.38424
        bool_0 = False
        bytes_0 = b'"\xb7\xca\xad\xfd\xc4\x93\x82f:B\xa1'
        import_replacer_0 = module_0.ImportReplacer(float_0, dict_0, float_1, bool_0, bytes_0)
    except BaseException:
        pass

def test_case_8():
    try:
        dict_0 = None
        scope_replacer_0 = None
        dict_1 = {}
        bool_0 = False
        str_0 = '__deepcopy__'
        import_replacer_0 = module_0.ImportReplacer(dict_1, bool_0, str_0, scope_replacer_0)
        import_replacer_1 = module_0.ImportReplacer(dict_0, scope_replacer_0, import_replacer_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '\n   import time\n    '
        var_0 = module_0.lazy_import(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '__setattr__ must work even after the object is resolved'
        var_0 = module_0.lazy_import(str_0, str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '#d4#).;S\x0co'
        str_1 = '$QpfEO&fV7zxQ8L+z#'
        dict_0 = {str_1: str_1, str_0: str_1, str_1: str_1}
        bool_0 = True
        bytes_0 = b'\xda<\xa1Q#d_t\x90\xa9\xf3\x18\xd6\xec\xbdF\xd7'
        import_replacer_0 = module_0.ImportReplacer(dict_0, bool_0, bytes_0, bool_0)
        import_processor_0 = module_0.ImportProcessor()
        var_0 = import_processor_0.lazy_import(dict_0, import_replacer_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '__setattr__ must work even after the object is resolved'
        str_1 = '\nfrom bzrlib import (\n    conflicts,\n    merge,\n    osutils,\n    )\n'
        var_0 = module_0.lazy_import(str_0, str_1)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '#V\ry\tSW\\6'
        import_processor_0 = module_0.ImportProcessor()
        var_0 = module_0.lazy_import(import_processor_0, str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        import_processor_0 = module_0.ImportProcessor()
        str_0 = "cb,:L7\x0cqja5'(r+.ZY"
        var_0 = module_0.lazy_import(import_processor_0, str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = "\n    Proxies mutable access to another mapping and allows for attribute-style access.\n\n    >>> a = dict(whoa=True, hello=[1,2,3], why='always')\n    >>> b = ProxyMutableAttrDict(a)\n\n    Nice reprs:\n\n    >>> b\n    <ProxyMutableAttrDict {'whoa': True, 'hello': [1, 2, 3], 'why': 'always'}>\n\n    Setting works as you'd expect:\n\n    >>> b['nice'] = False\n    >>> b['whoa'] = 'yeee'\n    >>> b\n    <ProxyMutableAttrDict {'whoa': 'yeee', 'hello': [1, 2, 3], 'why': 'always', 'nice': False}>\n\n    Checking that the changes are in fact being performed on the proxied object:\n\n    >>> a\n    {'whoa': 'yeee', 'hello': [1, 2, 3], 'why': 'always', 'nice': False}\n\n    Attribute style access:\n\n    >>> b.whoa\n    'yeee'\n    >>> b.state = 'new'\n    >>> b\n    <ProxyMutableAttrDict {'whoa': 'yeee', 'hello': [1, 2, 3], 'why': 'always', 'nice': False, 'state': 'new'}>\n\n    Recursion is handled:\n\n    >>> b.subdict = dict(test=True)\n    >>> b.subdict.test\n    True\n    >>> b\n    <ProxyMutableAttrDict {'whoa': 'yeee', 'hello': [1, 2, 3], 'why': 'always', 'nice': False, 'state': 'new',\n    'subdict': <ProxyMutableAttrDict {'test': True}>}>\n\n    "
        import_processor_0 = module_0.ImportProcessor()
        var_0 = import_processor_0.lazy_import(import_processor_0, str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '\n    import time\n    '
        var_0 = module_0.lazy_import(str_0, str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '\n   import time,   '
        var_0 = module_0.lazy_import(str_0, str_0)
    except BaseException:
        pass