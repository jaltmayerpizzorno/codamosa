# Automatically generated by Pynguin.
import ansible.plugins.loader as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '/etc'
    var_0 = module_0.add_all_plugin_dirs(str_0)

def test_case_2():
    dict_0 = None
    var_0 = module_0.add_all_plugin_dirs(dict_0)

def test_case_3():
    str_0 = 'filter'
    str_1 = '/root/ansible-new/lib/ansible/plugins/filter'
    var_0 = module_0.add_dirs_to_loader(str_0, str_1)
    str_2 = 'action'
    var_1 = module_0.add_dirs_to_loader(str_2, str_1)

def test_case_4():
    plugin_load_context_0 = None
    int_0 = 3202
    var_0 = module_0.get_shell_plugin(plugin_load_context_0, int_0)

def test_case_5():
    bool_0 = True
    int_0 = None
    tuple_0 = None
    plugin_loader_0 = module_0.PluginLoader(bool_0, int_0, tuple_0, tuple_0)
    var_0 = plugin_loader_0.has_plugin(plugin_loader_0)

def test_case_6():
    str_0 = 'a6X0`FFXEByA1 AWD\x0c'
    dict_0 = {str_0: str_0}
    bytes_0 = b'\x18\xe4\xc7\x9a\xd2\xc32iDs\xea\xd2'
    bool_0 = True
    bytes_1 = b'-v'
    str_1 = 'm9"H_=GS:uK6'
    str_2 = "$pg&%F'7P0;Hslx-"
    str_3 = None
    tuple_0 = (str_3,)
    plugin_load_context_0 = module_0.PluginLoadContext()
    plugin_path_context_0 = module_0.PluginPathContext(tuple_0, plugin_load_context_0)
    tuple_1 = (plugin_path_context_0,)
    str_4 = '$,2'
    dict_1 = {str_1: bytes_1, str_2: bytes_1, str_1: tuple_1, str_4: bytes_1}
    tuple_2 = (dict_1,)
    plugin_loader_0 = module_0.PluginLoader(bytes_0, bool_0, bytes_1, tuple_2)
    var_0 = plugin_loader_0.__setstate__(dict_0)

def test_case_7():
    str_0 = '>*%#t7)r@'
    bool_0 = True
    int_0 = None
    tuple_0 = None
    plugin_loader_0 = module_0.PluginLoader(bool_0, int_0, tuple_0, tuple_0)
    var_0 = plugin_loader_0.has_plugin(str_0)
    var_1 = plugin_loader_0.print_paths()

def test_case_8():
    str_0 = 'osLdg5w.1]/}B&\rc5m'
    float_0 = 1807.8
    bool_0 = False
    tuple_0 = ()
    bytes_0 = b'\xd0zK\xc7\x80'
    tuple_1 = (tuple_0, float_0, bytes_0)
    bytes_1 = b'\xc3\xb9s\x00\x07\xbf\x84\xc4\xc9\xe4\xe1_\xbe\x18\xe5\x14C\x04'
    dict_0 = {tuple_1: tuple_1}
    plugin_load_context_0 = module_0.PluginLoadContext()
    plugin_loader_0 = module_0.PluginLoader(bool_0, tuple_1, bytes_1, dict_0, plugin_load_context_0, tuple_1)
    str_1 = 'ad{&5`!'
    int_0 = 257
    plugin_loader_1 = module_0.PluginLoader(float_0, plugin_loader_0, str_1, int_0)
    var_0 = plugin_loader_1.format_paths(str_0)

def test_case_9():
    str_0 = 'csh'
    set_0 = None
    var_0 = module_0.get_shell_plugin(set_0, str_0)

def test_case_10():
    str_0 = 'D'
    float_0 = -1636.99
    bool_0 = False
    plugin_load_context_0 = module_0.PluginLoadContext()
    plugin_path_context_0 = module_0.PluginPathContext(bool_0, plugin_load_context_0)
    list_0 = [str_0]
    plugin_loader_0 = module_0.PluginLoader(bool_0, str_0, plugin_path_context_0, list_0)
    var_0 = plugin_loader_0.has_plugin(float_0)

def test_case_11():
    str_0 = 's'
    set_0 = None
    str_1 = 'Z2K0\t'
    list_0 = [str_0, str_1, str_0, set_0]
    bytes_0 = b'w\r'
    dict_0 = {set_0: set_0, set_0: str_0}
    plugin_load_context_0 = module_0.PluginLoadContext()
    list_1 = []
    plugin_path_context_0 = module_0.PluginPathContext(list_1, bytes_0)
    tuple_0 = (plugin_load_context_0, plugin_path_context_0, plugin_load_context_0, list_1)
    plugin_loader_0 = module_0.PluginLoader(set_0, bytes_0, dict_0, tuple_0)
    float_0 = 2467.0
    str_2 = '[S'
    var_0 = plugin_load_context_0.resolve(list_1, tuple_0, float_0, str_2)
    var_1 = plugin_loader_0.has_plugin(str_1, list_0)
    var_2 = module_0.get_shell_plugin(set_0, str_0)

def test_case_12():
    str_0 = 'csh'
    set_0 = None
    list_0 = [str_0, str_0, str_0, set_0]
    bytes_0 = b'w\r'
    dict_0 = {set_0: set_0, set_0: str_0}
    plugin_load_context_0 = module_0.PluginLoadContext()
    list_1 = [bytes_0]
    plugin_path_context_0 = module_0.PluginPathContext(list_1, bytes_0)
    tuple_0 = (plugin_load_context_0, plugin_path_context_0, plugin_load_context_0, list_1)
    plugin_loader_0 = module_0.PluginLoader(set_0, bytes_0, dict_0, tuple_0)
    var_0 = plugin_loader_0.has_plugin(str_0, list_0)

def test_case_13():
    str_0 = 'csh'
    set_0 = None
    list_0 = [str_0, str_0, str_0, set_0]
    bytes_0 = b'w\r'
    dict_0 = {set_0: set_0, set_0: str_0}
    plugin_load_context_0 = module_0.PluginLoadContext()
    list_1 = [bytes_0]
    plugin_path_context_0 = module_0.PluginPathContext(list_1, bytes_0)
    tuple_0 = (plugin_load_context_0, plugin_path_context_0, plugin_load_context_0, list_1)
    plugin_loader_0 = module_0.PluginLoader(set_0, bytes_0, dict_0, tuple_0)
    var_0 = plugin_loader_0.__getstate__()
    var_1 = plugin_loader_0.has_plugin(set_0, list_0)
    var_2 = module_0.get_shell_plugin(set_0, str_0)

def test_case_14():
    plugin_load_context_0 = None
    int_0 = 3202
    var_0 = module_0.get_shell_plugin(plugin_load_context_0, int_0)

def test_case_15():
    str_0 = '>*%#t7)r@'
    bool_0 = True
    int_0 = None
    tuple_0 = None
    plugin_loader_0 = module_0.PluginLoader(bool_0, int_0, tuple_0, tuple_0)
    var_0 = plugin_loader_0.has_plugin(str_0)
    var_1 = plugin_loader_0.has_plugin(plugin_loader_0)

def test_case_16():
    bytes_0 = b'g\xf5'
    str_0 = 'y$[u'
    list_0 = [str_0, str_0, str_0]
    bytes_1 = b'>|\x97u\x85d\x1f\x14WM\xcd\x92M\x18\xaf\x80@\xac'
    plugin_load_context_0 = module_0.PluginLoadContext()
    plugin_loader_0 = module_0.PluginLoader(str_0, list_0, bytes_1, plugin_load_context_0)
    var_0 = plugin_loader_0.add_directory(bytes_0)

def test_case_17():
    list_0 = []
    str_0 = ',/s]V#'
    plugin_load_context_0 = None
    int_0 = 3217
    var_0 = module_0.get_shell_plugin(plugin_load_context_0, int_0)
    str_1 = 'V~T/f=UDkz='
    bytes_0 = b'\xe89\x00\x8e\xef\xc21\x8e\xf6\xec\xfa\xfb\x10e'
    bool_0 = False
    complex_0 = None
    float_0 = 1000.0
    jinja2_loader_0 = module_0.Jinja2Loader(plugin_load_context_0, bool_0, str_1, bytes_0, complex_0, float_0)
    dict_0 = {str_0: plugin_load_context_0}
    var_1 = jinja2_loader_0.all(*list_0, **dict_0)

def test_case_18():
    str_0 = 'sh'
    set_0 = None
    var_0 = module_0.get_shell_plugin(set_0, str_0)

def test_case_19():
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_0 = 'daniel'
    str_1 = 'warning_text'
    str_2 = 'removal_date'
    str_3 = 'removal_version'
    str_4 = 'is awesome'
    str_5 = '01/01/01'
    str_6 = 'collection'
    str_7 = '3.0'
    str_8 = {str_1: str_4, str_2: str_5, str_3: str_7}
    var_0 = plugin_load_context_0.record_deprecation(str_0, str_8, str_6)
    str_9 = '01/01/02'
    str_10 = {str_1: str_4, str_2: str_9, str_3: str_7}
    var_1 = plugin_load_context_0.record_deprecation(str_0, str_10, str_6)