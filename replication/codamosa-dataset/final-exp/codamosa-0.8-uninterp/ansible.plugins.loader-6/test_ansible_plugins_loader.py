# Automatically generated by Pynguin.
import ansible.plugins.loader as module_0

def test_case_0():
    pass

def test_case_1():
    var_0 = module_0.get_all_plugin_loaders()

def test_case_2():
    bool_0 = True
    var_0 = module_0.add_all_plugin_dirs(bool_0)

def test_case_3():
    str_0 = '4s'
    str_1 = None
    var_0 = module_0.get_shell_plugin(str_1, str_0)

def test_case_4():
    str_0 = '4s'
    str_1 = None
    var_0 = module_0.get_shell_plugin(str_1, str_0)

def test_case_5():
    plugin_load_context_0 = module_0.PluginLoadContext()
    bool_0 = None
    int_0 = 3572
    list_0 = [plugin_load_context_0, plugin_load_context_0, plugin_load_context_0]
    str_0 = '/pynguin/shell_plugins/windows'
    plugin_loader_0 = module_0.PluginLoader(plugin_load_context_0, int_0, list_0, str_0)
    dict_0 = {str_0: int_0, str_0: bool_0}
    var_0 = plugin_loader_0.add_directory(str_0, dict_0)

def test_case_6():
    plugin_load_context_0 = module_0.PluginLoadContext()
    bool_0 = False
    int_0 = -38
    str_0 = '!=qq@%i8"la'
    plugin_loader_0 = module_0.PluginLoader(bool_0, int_0, str_0, str_0)
    var_0 = plugin_loader_0.has_plugin(plugin_load_context_0)

def test_case_7():
    str_0 = 'T6-r#_h"AXEPP=w'
    jinja2_loader_0 = None
    str_1 = '*j5'
    plugin_load_context_0 = module_0.PluginLoadContext()
    var_0 = plugin_load_context_0.record_deprecation(str_0, jinja2_loader_0, str_1)

def test_case_8():
    plugin_load_context_0 = module_0.PluginLoadContext()
    plugin_load_context_1 = module_0.PluginLoadContext()
    dict_0 = None
    var_0 = module_0.get_shell_plugin(dict_0, plugin_load_context_0)

def test_case_9():
    bool_0 = False
    plugin_load_context_0 = module_0.PluginLoadContext()
    var_0 = module_0.get_shell_plugin(bool_0, plugin_load_context_0)

def test_case_10():
    str_0 = 'powershell'
    var_0 = module_0.get_shell_plugin(str_0, str_0)

def test_case_11():
    str_0 = 's'
    plugin_load_context_0 = module_0.PluginLoadContext()
    int_0 = -37
    str_1 = '!=qq@%i8"la'
    dict_0 = None
    jinja2_loader_0 = None
    bool_0 = True
    plugin_loader_0 = module_0.PluginLoader(str_1, dict_0, jinja2_loader_0, bool_0)
    plugin_path_context_0 = None
    plugin_loader_1 = module_0.PluginLoader(str_0, plugin_loader_0, int_0, plugin_path_context_0)
    var_0 = plugin_loader_0.has_plugin(dict_0)

def test_case_12():
    str_0 = 'shell'
    str_1 = '/'
    var_0 = module_0.add_dirs_to_loader(str_0, str_1)
    str_2 = 'module'
    str_3 = '/module'
    str_4 = [str_1, str_3]
    var_1 = module_0.add_dirs_to_loader(str_2, str_4)
    str_5 = 'cache'
    str_6 = [str_1, str_3]
    var_2 = module_0.add_dirs_to_loader(str_5, str_6)
    str_7 = 'action'
    str_8 = '/item'
    str_9 = [str_1, str_8]
    var_3 = module_0.add_dirs_to_loader(str_7, str_9)
    str_10 = 'lookup'
    str_11 = '/var'
    str_12 = [str_1, str_11]
    var_4 = module_0.add_dirs_to_loader(str_10, str_12)

def test_case_13():
    str_0 = 'shell'
    str_1 = '/'
    var_0 = module_0.add_dirs_to_loader(str_0, str_1)
    str_2 = 'module'
    str_3 = '/module'
    str_4 = [str_1, str_3]
    var_1 = module_0.add_dirs_to_loader(str_2, str_4)
    str_5 = 'cache'
    str_6 = [str_1, str_3]
    var_2 = module_0.add_dirs_to_loader(str_5, str_6)
    str_7 = 'action'
    str_8 = '/item'
    str_9 = [str_1, str_8]
    var_3 = module_0.add_dirs_to_loader(str_7, str_9)
    str_10 = 'lookup'
    str_11 = '/var'
    str_12 = [str_1, str_11]
    var_4 = module_0.add_dirs_to_loader(str_10, str_12)

def test_case_14():
    str_0 = '__init__'
    str_1 = None
    var_0 = module_0.get_shell_plugin(str_1, str_0)

def test_case_15():
    int_0 = 131072
    var_0 = module_0.add_all_plugin_dirs(int_0)
    str_0 = None
    tuple_0 = ()
    list_0 = []
    str_1 = 'iH6k<Sqv\x0c'
    plugin_load_context_0 = module_0.PluginLoadContext()
    float_0 = 1397.495867
    str_2 = 'B'
    plugin_loader_0 = module_0.PluginLoader(str_1, int_0, int_0, plugin_load_context_0, float_0, str_2)
    plugin_loader_1 = module_0.PluginLoader(tuple_0, tuple_0, list_0, plugin_loader_0)
    var_1 = module_0.get_shell_plugin(str_0, str_2)
    tuple_1 = (str_2, int_0, int_0)
    str_3 = '[lHE?b6\n+1_xpU`IM'
    bool_0 = False
    list_1 = []
    set_0 = {tuple_1, str_3}
    var_2 = plugin_loader_1.find_plugin_with_context(str_3, plugin_loader_1, bool_0, list_1, set_0)

def test_case_16():
    int_0 = 131072
    var_0 = module_0.add_all_plugin_dirs(int_0)
    str_0 = None
    tuple_0 = ()
    list_0 = []
    str_1 = '/pynguin/shell_plugins/windows'
    plugin_load_context_0 = module_0.PluginLoadContext()
    float_0 = 1397.495867
    str_2 = 'powershell'
    plugin_loader_0 = module_0.PluginLoader(str_1, int_0, int_0, plugin_load_context_0, float_0, str_2)
    plugin_loader_1 = module_0.PluginLoader(tuple_0, tuple_0, list_0, plugin_loader_0)
    var_1 = module_0.get_shell_plugin(str_0, str_2)
    var_2 = plugin_loader_1.print_paths()
    bool_0 = False
    plugin_loader_2 = None
    dict_0 = None
    plugin_load_context_1 = module_0.PluginLoadContext()
    var_3 = plugin_load_context_1.resolve(plugin_loader_2, dict_0, int_0, plugin_loader_2)
    tuple_1 = (str_2, int_0, int_0)
    bytes_0 = b'\x9cS[WS\x81\xfc\xf5D\xfe'
    str_3 = '[lHE?b6\n+1_xpU`IM'
    dict_1 = {tuple_0: var_0}
    plugin_loader_3 = module_0.PluginLoader(bytes_0, str_3, dict_1, dict_1, plugin_load_context_1)
    str_4 = 'NMaMnq"l=s*!p'
    list_1 = []
    set_0 = {tuple_1, str_3}
    var_4 = plugin_loader_1.find_plugin_with_context(str_4, plugin_loader_3, bool_0, list_1, set_0)