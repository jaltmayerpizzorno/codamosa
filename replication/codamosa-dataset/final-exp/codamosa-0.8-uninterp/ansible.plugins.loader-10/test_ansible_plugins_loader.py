# Automatically generated by Pynguin.
import ansible.plugins.loader as module_0

def test_case_0():
    pass

def test_case_1():
    var_0 = module_0.get_all_plugin_loaders()

def test_case_2():
    str_0 = 'test'
    var_0 = module_0.add_dirs_to_loader(str_0, str_0)

def test_case_3():
    str_0 = '[V[IFqY'
    bool_0 = False
    dict_0 = {str_0: str_0, str_0: str_0, bool_0: str_0, bool_0: str_0}
    plugin_path_context_0 = module_0.PluginPathContext(str_0, dict_0)
    var_0 = module_0.get_all_plugin_loaders()

def test_case_4():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0]
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_0 = '/pynguin/shell_plugins/windows'
    plugin_path_context_0 = module_0.PluginPathContext(list_0, str_0)
    var_0 = plugin_load_context_0.record_deprecation(plugin_path_context_0, tuple_0, str_0)
    var_1 = module_0.get_all_plugin_loaders()

def test_case_5():
    str_0 = 'ansible.plugins.action'
    str_1 = 'ActionBase'
    plugin_load_context_0 = module_0.PluginLoadContext()
    var_0 = None
    var_1 = {}
    plugin_loader_0 = module_0.PluginLoader(str_1, str_0, var_0, var_1, var_0)
    var_2 = plugin_loader_0.find_plugin_with_context(str_0)
    var_3 = plugin_loader_0.__getstate__()
    bool_0 = True
    var_4 = plugin_loader_0.has_plugin(bool_0)

def test_case_6():
    str_0 = 'ansible.plugins.action'
    str_1 = 'ActionBase'
    plugin_loader_0 = module_0.PluginLoader(str_1, str_0, str_1, str_0, str_1)
    bool_0 = False
    var_0 = plugin_loader_0.has_plugin(bool_0)

def test_case_7():
    int_0 = 200000
    str_0 = '[/7c`j/\\i[z6@Z2+'
    list_0 = [str_0, str_0]
    plugin_load_context_0 = module_0.PluginLoadContext()
    plugin_loader_0 = module_0.PluginLoader(str_0, list_0, list_0, plugin_load_context_0)
    var_0 = plugin_loader_0.has_plugin(int_0)

def test_case_8():
    bool_0 = True
    tuple_0 = ()
    int_0 = 1736
    list_0 = [tuple_0, tuple_0]
    float_0 = 1000.0
    plugin_loader_0 = module_0.PluginLoader(tuple_0, int_0, list_0, float_0)
    var_0 = plugin_loader_0.has_plugin(bool_0)

def test_case_9():
    plugin_load_context_0 = module_0.PluginLoadContext()
    var_0 = module_0.add_all_plugin_dirs(plugin_load_context_0)

def test_case_10():
    str_0 = 'E'
    set_0 = {str_0, str_0}
    plugin_path_context_0 = module_0.PluginPathContext(str_0, set_0)
    plugin_load_context_0 = module_0.PluginLoadContext()
    plugin_load_context_1 = module_0.PluginLoadContext()
    get_with_context_result_0 = None
    var_0 = module_0.get_shell_plugin(get_with_context_result_0, plugin_path_context_0)

def test_case_11():
    str_0 = 'ansible.plugins.action'
    str_1 = 'ActionBase'
    var_0 = None
    var_1 = {}
    plugin_loader_0 = module_0.PluginLoader(str_1, str_0, var_0, var_1, var_0)
    var_2 = plugin_loader_0.print_paths()
    str_2 = 'debug'
    var_3 = plugin_loader_0.find_plugin_with_context(str_2)
    bool_0 = True
    var_4 = plugin_loader_0.has_plugin(bool_0)

def test_case_12():
    str_0 = 'c'
    plugin_path_context_0 = None
    var_0 = module_0.get_shell_plugin(plugin_path_context_0, str_0)

def test_case_13():
    str_0 = 'sh'
    var_0 = module_0.get_shell_plugin(str_0)

def test_case_14():
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_0 = 'qW'
    dict_0 = None
    list_0 = [plugin_load_context_0, str_0]
    var_0 = module_0.get_shell_plugin(dict_0, list_0)

def test_case_15():
    str_0 = 'E'
    bool_0 = False
    plugin_path_context_0 = None
    var_0 = module_0.get_shell_plugin(plugin_path_context_0, str_0)
    plugin_load_context_0 = module_0.PluginLoadContext()
    set_0 = {plugin_load_context_0, plugin_path_context_0}
    dict_0 = {str_0: bool_0, str_0: plugin_load_context_0, var_0: bool_0}
    bytes_0 = b'\x00\x8ee\xa4_j\xe3p\xfa\x9c\x8c\x02\xd8"mS\'R'
    str_1 = ''
    bool_1 = False
    float_0 = 1.5
    jinja2_loader_0 = module_0.Jinja2Loader(plugin_path_context_0, dict_0, bytes_0, bool_1, float_0)
    float_1 = -3776.6683705127953
    plugin_loader_0 = module_0.PluginLoader(plugin_load_context_0, jinja2_loader_0, plugin_path_context_0, float_1, bytes_0)
    tuple_0 = (dict_0, float_0)
    tuple_1 = (str_1, plugin_load_context_0, tuple_0, bytes_0)
    var_1 = plugin_loader_0.has_plugin(set_0, tuple_1)

def test_case_16():
    plugin_load_context_0 = module_0.PluginLoadContext()
    plugin_path_context_0 = None
    str_0 = '/input/ansible/plugins/shell/windows'
    var_0 = module_0.get_shell_plugin(plugin_path_context_0, str_0)

def test_case_17():
    str_0 = 'E'
    set_0 = {str_0, str_0, str_0}
    plugin_path_context_0 = module_0.PluginPathContext(str_0, set_0)
    tuple_0 = None
    bytes_0 = b'\xe2\x9c\xbb:\xdf\xc1c\x1f`\xfc'
    plugin_load_context_0 = module_0.PluginLoadContext()
    bool_0 = False
    jinja2_loader_0 = module_0.Jinja2Loader(tuple_0, plugin_path_context_0, bytes_0, str_0, set_0)
    dict_0 = {bytes_0: set_0, bool_0: jinja2_loader_0, jinja2_loader_0: bool_0, jinja2_loader_0: bytes_0}
    float_0 = 60.0
    var_0 = plugin_load_context_0.record_deprecation(plugin_path_context_0, dict_0, float_0)

def test_case_18():
    plugin_path_context_0 = None
    str_0 = 'powershell'
    var_0 = module_0.get_shell_plugin(plugin_path_context_0, str_0)

def test_case_19():
    str_0 = 'h'
    set_0 = {str_0, str_0}
    plugin_path_context_0 = module_0.PluginPathContext(str_0, set_0)
    tuple_0 = None
    str_1 = '/usr/share/ansible/plugins/doc_fragments/windows'
    float_0 = None
    list_0 = [plugin_path_context_0, set_0, tuple_0, float_0]
    plugin_loader_0 = module_0.PluginLoader(plugin_path_context_0, set_0, list_0, set_0, plugin_path_context_0)
    var_0 = plugin_loader_0.format_paths(str_1)
    bytes_0 = b'\xe2\x9c\xbb:\xdf\xc1c\x1f`\xfc'
    plugin_load_context_0 = module_0.PluginLoadContext()
    bool_0 = False
    jinja2_loader_0 = module_0.Jinja2Loader(tuple_0, plugin_path_context_0, bytes_0, str_0, set_0)
    dict_0 = {bytes_0: set_0, bool_0: jinja2_loader_0, jinja2_loader_0: bool_0, jinja2_loader_0: bytes_0}
    float_1 = 61.17590791332369
    var_1 = plugin_load_context_0.record_deprecation(plugin_path_context_0, dict_0, float_1)
    list_1 = [str_1]
    var_2 = module_0.get_shell_plugin(float_0, list_1)

def test_case_20():
    str_0 = 't'
    set_0 = {str_0}
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_1 = 'QBayu^ji4HhWrT'
    plugin_path_context_0 = module_0.PluginPathContext(plugin_load_context_0, str_1)
    float_0 = -1073.27
    str_2 = None
    str_3 = 'vz{F6>qz=LDNJ1 !O{i'
    dict_0 = {str_2: str_0, str_0: float_0, str_1: str_0, str_3: plugin_path_context_0}
    plugin_loader_0 = module_0.PluginLoader(str_0, plugin_path_context_0, float_0, float_0, dict_0)
    var_0 = plugin_loader_0.has_plugin(set_0)

def test_case_21():
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_0 = 'yum'
    str_1 = 'warning_text'
    str_2 = 'removal_versio'
    str_3 = 'deprecated'
    str_4 = '2.0'
    str_5 = {str_1: str_3, str_2: str_4}
    str_6 = ''
    var_0 = plugin_load_context_0.record_deprecation(str_0, str_5, str_6)
    str_7 = 'apt'
    str_8 = 'removal_date'
    str_9 = '2020-01-01'
    str_10 = {str_1: str_3, str_8: str_9}
    var_1 = plugin_load_context_0.record_deprecation(str_7, str_10, str_6)

def test_case_22():
    str_0 = 'ActionBase'
    var_0 = {str_0: str_0}
    plugin_loader_0 = module_0.PluginLoader(str_0, str_0, str_0, var_0, str_0)
    str_1 = 'debug'
    var_1 = plugin_loader_0.find_plugin_with_context(str_1)
    str_2 = 'ansible_collections.my_ns.my_coll.my_plugins.my_action'
    var_2 = plugin_loader_0.find_plugin_with_context(str_2)

def test_case_23():
    plugin_load_context_0 = module_0.PluginLoadContext()
    str_0 = 'yum'
    str_1 = 'warning_text'
    str_2 = 'removal_versio'
    str_3 = 'deprecated'
    str_4 = '2.0'
    str_5 = {str_1: str_3, str_2: str_4}
    str_6 = ''
    var_0 = plugin_load_context_0.record_deprecation(str_0, str_5, str_6)

def test_case_24():
    str_0 = 'ansible.plugins.action'
    str_1 = 'ActiconB=se'
    str_2 = "<5'"
    dict_0 = {str_1: str_0, str_2: str_0, str_2: str_0}
    bytes_0 = b'\xd9\x8c\x88\x17;\xef\xe6\x11S\xca\x0c!\xaa\x82\xe7'
    dict_1 = {str_1: str_0}
    plugin_path_context_0 = module_0.PluginPathContext(bytes_0, dict_1)
    float_0 = 550.8304877729083
    plugin_loader_0 = module_0.PluginLoader(bytes_0, dict_1, plugin_path_context_0, float_0)
    var_0 = plugin_loader_0.__setstate__(dict_0)
    var_1 = None
    var_2 = {}
    plugin_loader_1 = module_0.PluginLoader(str_1, str_0, var_1, var_2, var_1)
    str_3 = 'debug'
    var_3 = plugin_loader_1.find_plugin_with_context(str_3)
    var_4 = plugin_loader_1.__getstate__()
    str_4 = 'ansible_collections.my_ns.my_coll.my_plugins.my_action'
    var_5 = plugin_loader_1.find_plugin_with_context(str_4)
    var_6 = plugin_loader_1.has_plugin(str_0)