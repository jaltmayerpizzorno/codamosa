# Automatically generated by Pynguin.
import ansible.plugins.loader as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = './'
    var_0 = module_0.add_all_plugin_dirs(str_0)

def test_case_2():
    str_0 = '\r/\\X)W!I/'
    var_0 = module_0.add_all_plugin_dirs(str_0)

def test_case_3():
    str_0 = 'lookup'
    var_0 = module_0.add_dirs_to_loader(str_0, str_0)

def test_case_4():
    bool_0 = True
    str_0 = 'i'
    dict_0 = {}
    var_0 = module_0.get_shell_plugin(dict_0, str_0)
    list_0 = None
    float_0 = -1006.73311
    var_1 = module_0.get_shell_plugin(list_0, float_0)
    list_1 = [str_0]
    bytes_0 = b'\xb3\xc7\xc0\x08\xe8\xbf\x1b\x98'
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_1 = 'cmd'
    var_2 = module_0.add_all_plugin_dirs(str_1)
    var_3 = plugin_load_context_0.nope(bool_0)
    dict_1 = {str_0: bytes_0, str_0: bytes_0, str_0: str_0}
    get_with_context_result_0 = None
    plugin_load_context_1 = module_0.PluginLoadContext()
    plugin_load_context_2 = module_0.PluginLoadContext()
    var_4 = plugin_load_context_2.record_deprecation(list_1, dict_1, plugin_load_context_1)
    bool_1 = True
    plugin_loader_0 = module_0.PluginLoader(bytes_0, get_with_context_result_0, str_0, bool_1, dict_1)
    tuple_0 = ()
    var_5 = plugin_loader_0.has_plugin(tuple_0)
    bytes_1 = b'\x8c@\xe8\x14\xb29r\xc6\x1c\xe7CEo\xa8\xd7'
    var_6 = plugin_load_context_0.resolve(bytes_1, list_0, get_with_context_result_0, bytes_0)
    bool_2 = False
    int_0 = -4280
    var_7 = module_0.get_shell_plugin(bool_2, int_0)

def test_case_5():
    str_0 = None
    bool_0 = False
    plugin_load_context_0 = module_0.PluginLoadContext()
    plugin_loader_0 = module_0.PluginLoader(bool_0, plugin_load_context_0, bool_0, plugin_load_context_0)
    var_0 = plugin_loader_0.has_plugin(str_0)

def test_case_6():
    str_0 = 'i'
    dict_0 = {}
    var_0 = module_0.get_shell_plugin(dict_0, str_0)

def test_case_7():
    tuple_0 = ()
    bool_0 = True
    str_0 = '}H+-weinp'
    int_0 = 8192
    plugin_loader_0 = module_0.PluginLoader(tuple_0, bool_0, str_0, int_0, bool_0)
    var_0 = plugin_loader_0.__getstate__()

def test_case_8():
    bool_0 = True
    str_0 = ''
    var_0 = module_0.get_shell_plugin(str_0, bool_0)

def test_case_9():
    bool_0 = False
    str_0 = 'ssh_opts'
    float_0 = 0.0001
    plugin_loader_0 = None
    jinja2_loader_0 = module_0.Jinja2Loader(bool_0, str_0, float_0, plugin_loader_0)
    bytes_0 = b'yI\xf09\x14'
    var_0 = module_0.get_shell_plugin(plugin_loader_0, bytes_0)

def test_case_10():
    str_0 = 'i'
    dict_0 = {}
    var_0 = module_0.get_shell_plugin(dict_0, str_0)

def test_case_11():
    str_0 = 'lookup'
    var_0 = module_0.add_dirs_to_loader(str_0, str_0)

def test_case_12():
    str_0 = 'powershell'
    var_0 = module_0.get_shell_plugin(str_0)

def test_case_13():
    bool_0 = True
    str_0 = 'i'
    list_0 = None
    float_0 = -1006.73311
    var_0 = module_0.get_shell_plugin(list_0, float_0)
    bytes_0 = b'\xb3\xc7\xc0\x08\xe8\xbf\x1b\x98'
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_1 = 'cmd'
    var_1 = module_0.add_all_plugin_dirs(str_1)
    var_2 = plugin_load_context_0.nope(bool_0)
    dict_0 = {str_0: bytes_0, str_0: bytes_0, str_0: str_0}
    get_with_context_result_0 = None
    plugin_load_context_1 = module_0.PluginLoadContext()
    plugin_load_context_2 = module_0.PluginLoadContext()
    plugin_loader_0 = module_0.PluginLoader(bytes_0, get_with_context_result_0, str_0, bool_0, dict_0)
    str_2 = '*hS'
    var_3 = plugin_loader_0.has_plugin(str_2)
    var_4 = plugin_loader_0.has_plugin(str_1, bytes_0)
    var_5 = plugin_loader_0.add_directory(str_1)
    tuple_0 = (dict_0, str_2, plugin_load_context_2, get_with_context_result_0)
    var_6 = plugin_loader_0.has_plugin(tuple_0)

def test_case_14():
    bytes_0 = b'\xb3\xc7\xc0\x08\xe8\xbf\x1b\x98'
    str_0 = 'nvHB&h;)N'
    dict_0 = {str_0: bytes_0, str_0: bytes_0, str_0: str_0}
    get_with_context_result_0 = None
    bool_0 = True
    plugin_loader_0 = module_0.PluginLoader(bytes_0, get_with_context_result_0, str_0, bool_0, dict_0)
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_1 = 'a\x0cuv?;w\x0b%@)P7'
    var_0 = plugin_loader_0.has_plugin(str_1)

def test_case_15():
    bool_0 = True
    list_0 = None
    float_0 = -1006.73311
    var_0 = module_0.get_shell_plugin(list_0, float_0)
    bytes_0 = b'\xb3\xc7\xc0\x08\xe8\xbf\x1b\x98'
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_0 = 'cmd'
    var_1 = plugin_load_context_0.nope(bool_0)
    dict_0 = {str_0: bytes_0, str_0: bytes_0, str_0: str_0}
    get_with_context_result_0 = None
    plugin_load_context_1 = module_0.PluginLoadContext()
    bool_1 = True
    plugin_loader_0 = module_0.PluginLoader(bytes_0, get_with_context_result_0, str_0, bool_1, dict_0)
    str_1 = 'c]rY=WcXyTj\r'
    bytes_1 = b'\x1a|h%U\x85\xd5\xb1\xc8'
    var_2 = plugin_loader_0.has_plugin(str_1, bytes_1)

def test_case_16():
    bool_0 = False
    str_0 = 'i'
    dict_0 = {}
    var_0 = module_0.get_shell_plugin(dict_0, str_0)
    list_0 = None
    float_0 = -1006.73311
    var_1 = module_0.get_shell_plugin(list_0, float_0)
    list_1 = [str_0]
    tuple_0 = ()
    jinja2_loader_0 = module_0.Jinja2Loader(tuple_0, tuple_0, tuple_0, dict_0)
    bytes_0 = b'\xb3\xc7\xc0\x08\xe8\xbf\x1b\x98'
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_1 = 'cmd'
    var_2 = module_0.add_all_plugin_dirs(str_1)
    var_3 = plugin_load_context_0.nope(bool_0)
    dict_1 = {str_0: bytes_0, str_0: bytes_0, str_0: str_0}
    get_with_context_result_0 = None
    plugin_load_context_1 = module_0.PluginLoadContext()
    var_4 = plugin_load_context_1.record_deprecation(list_1, dict_1, plugin_load_context_1)
    plugin_loader_0 = module_0.PluginLoader(bytes_0, get_with_context_result_0, str_0, bool_0, dict_1)
    str_2 = '*hS'
    var_5 = plugin_loader_0.has_plugin(str_2)
    bytes_1 = b'\x1a|h%U\x85\xd5'
    var_6 = plugin_loader_0.has_plugin(str_1, bytes_1)
    var_7 = plugin_loader_0.add_directory(str_1)
    var_8 = plugin_loader_0.has_plugin(str_1)

def test_case_17():
    str_0 = 'i'
    dict_0 = {}
    var_0 = module_0.get_shell_plugin(dict_0, str_0)
    list_0 = None
    float_0 = -1006.73311
    var_1 = module_0.get_shell_plugin(list_0, float_0)
    list_1 = [str_0]
    bytes_0 = b'\xb3\xc7\xc0\x08\xe8\xbf\x1b\x98'
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_1 = 'cmd'
    var_2 = module_0.add_all_plugin_dirs(str_1)
    dict_1 = {str_0: bytes_0}
    get_with_context_result_0 = None
    plugin_load_context_1 = module_0.PluginLoadContext()
    plugin_load_context_2 = module_0.PluginLoadContext()
    var_3 = plugin_load_context_2.record_deprecation(list_1, dict_1, plugin_load_context_1)
    bool_0 = False
    plugin_loader_0 = module_0.PluginLoader(bytes_0, get_with_context_result_0, str_0, bool_0, dict_1)
    bytes_1 = b'\x1a|h%U\x85\xd5'
    var_4 = plugin_loader_0.has_plugin(str_1, bytes_1)
    var_5 = plugin_loader_0.add_directory(str_1)
    str_2 = 'IA9p7WqtEV'
    str_3 = 'zSf0^l1;V'
    str_4 = '5!Z}9,G)Xp*prp'
    jinja2_loader_0 = module_0.Jinja2Loader(str_2, str_1, str_3, str_4)
    jinja2_loader_1 = module_0.Jinja2Loader(float_0, list_0, list_1, bytes_1)
    var_6 = jinja2_loader_1.all(**dict_1)
    var_7 = plugin_loader_0.has_plugin(list_0)

def test_case_18():
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_0 = 'test_dep'
    str_1 = 'warning_text'
    str_2 = 'test_text'
    str_3 = {str_1: str_2}
    str_4 = 'test_coll'
    var_0 = plugin_load_context_0.record_deprecation(str_0, str_3, str_4)
    str_5 = 'test_dep_date'
    str_6 = 'removal_date'
    str_7 = 'test_date'
    str_8 = '1.1'
    str_9 = {str_1: str_7, str_6: str_8}
    var_1 = plugin_load_context_0.record_deprecation(str_5, str_9, str_4)

def test_case_19():
    list_0 = None
    float_0 = -1006.73311
    var_0 = module_0.get_shell_plugin(list_0, float_0)
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_0 = 'cmd'
    plugin_load_context_1 = module_0.PluginLoadContext()
    str_1 = '*|S'
    str_2 = 'zSf0^l1;V'
    jinja2_loader_0 = module_0.Jinja2Loader(str_1, str_0, str_2, str_1)
    var_1 = jinja2_loader_0.all()

def test_case_20():
    str_0 = 'i'
    dict_0 = {}
    var_0 = module_0.get_shell_plugin(dict_0, str_0)
    list_0 = None
    float_0 = -1006.73311
    var_1 = module_0.get_shell_plugin(list_0, float_0)
    list_1 = [str_0]
    bytes_0 = b'\xb3\xc7\xc0\x08\xe8\xbf\x1b\x98'
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_1 = 'cmd'
    var_2 = module_0.add_all_plugin_dirs(str_1)
    dict_1 = {str_0: bytes_0}
    get_with_context_result_0 = None
    plugin_load_context_1 = module_0.PluginLoadContext()
    plugin_load_context_2 = module_0.PluginLoadContext()
    var_3 = plugin_load_context_2.record_deprecation(list_1, dict_1, plugin_load_context_1)
    bool_0 = False
    plugin_loader_0 = module_0.PluginLoader(bytes_0, get_with_context_result_0, str_0, bool_0, dict_1)
    tuple_0 = ()
    bytes_1 = b'\x1a|h%U\x85\xd5'
    var_4 = plugin_loader_0.has_plugin(str_1, bytes_1)
    var_5 = plugin_loader_0.add_directory(str_1)
    str_2 = 'IA9p7WqtEV'
    str_3 = 'zSf0^l1;V'
    str_4 = '5!Z}9,G)Xp*prp'
    jinja2_loader_0 = module_0.Jinja2Loader(str_2, str_1, str_3, str_4)
    var_6 = jinja2_loader_0.all(*list_1, **dict_1)
    var_7 = plugin_loader_0.has_plugin(tuple_0, dict_1)