# Automatically generated by Pynguin.
import ansible.plugins.loader as module_0
import ansible.utils.display as module_1

def test_case_0():
    pass

def test_case_1():
    plugin_load_context_0 = module_0.PluginLoadContext()
    var_0 = module_0.get_all_plugin_loaders()
    bool_0 = False
    str_0 = '-'
    var_1 = module_0.get_shell_plugin(bool_0, str_0)

def test_case_2():
    str_0 = '/pynguin/shell_plugins/windows'
    var_0 = module_0.add_all_plugin_dirs(str_0)

def test_case_3():
    list_0 = []
    plugin_load_context_0 = module_0.PluginLoadContext()
    var_0 = plugin_load_context_0.redirect(list_0)
    str_0 = 'ExscM::'
    dict_0 = {}
    var_1 = module_0.get_shell_plugin(dict_0, str_0)

def test_case_4():
    float_0 = 1696.38
    list_0 = [float_0, float_0]
    get_with_context_result_0 = module_0.get_with_context_result(*list_0)
    int_0 = -645
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_0 = ' D5[.l?C6E~?'
    dict_0 = {str_0: plugin_load_context_0}
    plugin_path_context_0 = module_0.PluginPathContext(plugin_load_context_0, dict_0)
    float_1 = 811.136
    var_0 = module_0.get_all_plugin_loaders()
    plugin_loader_0 = module_0.PluginLoader(int_0, plugin_path_context_0, plugin_path_context_0, float_1)
    var_1 = plugin_loader_0.has_plugin(plugin_load_context_0)
    str_1 = '.\x0b"'
    dict_1 = {str_0: plugin_load_context_0, plugin_path_context_0: float_1, plugin_path_context_0: var_0, str_1: float_1}
    var_2 = plugin_loader_0.__setstate__(dict_1)

def test_case_5():
    str_0 = 'fact_ccvVhe'
    dict_0 = {}
    var_0 = module_0.get_shell_plugin(dict_0, str_0)

def test_case_6():
    str_0 = 'action'
    var_0 = module_0.add_dirs_to_loader(str_0, str_0)

def test_case_7():
    int_0 = -1129
    list_0 = [int_0, int_0, int_0]
    bytes_0 = b'^2@D/\xa6[\xe7\xbf3\xad\xc3'
    str_0 = 'TaskInclude'
    bool_0 = True
    str_1 = 'K'
    plugin_loader_0 = module_0.PluginLoader(bytes_0, str_0, bool_0, str_1)
    var_0 = plugin_loader_0.has_plugin(list_0)

def test_case_8():
    str_0 = 'ansible.plugins.callback'
    str_1 = 'CallbackModule'
    plugin_loader_0 = module_0.PluginLoader(str_0, str_0, str_1, str_0)
    var_0 = plugin_loader_0.all()
    var_1 = list(var_0)

def test_case_9():
    str_0 = '#`u2L!'
    float_0 = 2487.0
    complex_0 = None
    int_0 = -5356
    jinja2_loader_0 = module_0.Jinja2Loader(float_0, complex_0, str_0, int_0)
    var_0 = jinja2_loader_0.all()

def test_case_10():
    str_0 = 'ansible.plugins.callback'
    str_1 = 'CallbackModule'
    str_2 = 'A7tbG.@ER2'
    plugin_loader_0 = module_0.PluginLoader(str_2, str_0, str_1, str_2)
    var_0 = plugin_loader_0.all()
    var_1 = plugin_loader_0.get(str_2)

def test_case_11():
    str_0 = 'ansible.plugins.callback'
    str_1 = 'CallbackModule'
    str_2 = 'A7tbG&(.@ER2'
    plugin_loader_0 = module_0.PluginLoader(str_2, str_0, str_1, str_2)
    var_0 = plugin_loader_0.all()
    var_1 = plugin_loader_0.get(str_2)

def test_case_12():
    str_0 = '5c0o *jDsx'
    set_0 = set()
    bytes_0 = b'\xc7\x84\xfa\xc4@\xc0'
    plugin_load_context_0 = module_0.PluginLoadContext()
    var_0 = plugin_load_context_0.record_deprecation(str_0, set_0, bytes_0)

def test_case_13():
    str_0 = 'cmd'
    var_0 = module_0.get_shell_plugin(str_0)

def test_case_14():
    str_0 = 'callback'
    str_1 = 'ansible.plugins.callback'
    str_2 = 'CallbackModule'
    str_3 = 'announce'
    plugin_loader_0 = module_0.PluginLoader(str_0, str_1, str_2, str_3)
    var_0 = plugin_loader_0.all()
    var_1 = list(var_0)

def test_case_15():
    float_0 = 1696.3834
    list_0 = [float_0, float_0]
    get_with_context_result_0 = module_0.get_with_context_result(*list_0)
    int_0 = -640
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_0 = ' D5[.l?C6E~?'
    dict_0 = {str_0: plugin_load_context_0}
    plugin_path_context_0 = module_0.PluginPathContext(plugin_load_context_0, dict_0)
    float_1 = 811.136
    plugin_loader_0 = module_0.PluginLoader(int_0, plugin_path_context_0, plugin_path_context_0, float_1)
    var_0 = plugin_loader_0.has_plugin(plugin_load_context_0)
    str_1 = None
    str_2 = "w^uJ'84F!CseChNt"
    bytes_0 = b'\x07A\xc7P\xc4\xb6G\xce'
    jinja2_loader_0 = module_0.Jinja2Loader(str_2, bytes_0, bytes_0, list_0, dict_0, list_0)
    var_1 = module_0.get_shell_plugin(str_1, jinja2_loader_0)

def test_case_16():
    bytes_0 = None
    display_0 = module_1.Display()
    var_0 = module_0.get_shell_plugin(bytes_0, display_0)

def test_case_17():
    float_0 = 1199.63642
    set_0 = None
    var_0 = module_0.add_all_plugin_dirs(set_0)
    str_0 = 'a\n#"6EciE'
    var_1 = module_0.get_all_plugin_loaders()
    bool_0 = False
    dict_0 = {float_0: bool_0, str_0: var_1}
    plugin_load_context_0 = module_0.PluginLoadContext()
    list_0 = [var_0]
    var_2 = plugin_load_context_0.record_deprecation(set_0, dict_0, list_0)

def test_case_18():
    str_0 = 'caltZiback'
    str_1 = 'ansible.plugins.callback'
    str_2 = 'CallbackModule'
    str_3 = 'announce'
    plugin_loader_0 = module_0.PluginLoader(str_0, str_1, str_2, str_3)
    var_0 = plugin_loader_0.all()
    str_4 = 'GDIJx=01'
    var_1 = plugin_loader_0.get(str_4)
    var_2 = list(var_0)
    tuple_0 = ()
    plugin_load_context_0 = module_0.PluginLoadContext()
    var_3 = plugin_loader_0.print_paths()
    plugin_path_context_0 = module_0.PluginPathContext(plugin_load_context_0, plugin_load_context_0)
    var_4 = module_0.get_shell_plugin(tuple_0, plugin_path_context_0)

def test_case_19():
    str_0 = 'action'
    var_0 = module_0.add_dirs_to_loader(str_0, str_0)

def test_case_20():
    str_0 = 'warning_text'
    str_1 = 'removal_date'
    str_2 = 'removal_version'
    str_3 = 'This module is going to be removed in a future release, use xyz instead.'
    str_4 = '2020-01-01'
    str_5 = '2.1.0'
    str_6 = {str_0: str_3, str_1: str_4, str_2: str_5}
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_7 = 'foo'
    str_8 = 'bar'
    var_0 = plugin_load_context_0.record_deprecation(str_7, str_6, str_8)