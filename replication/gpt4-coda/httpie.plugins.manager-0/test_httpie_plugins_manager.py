# Automatically generated by Pynguin.
import httpie.plugins.manager as module_0

def test_case_0():
    plugin_manager_0 = module_0.PluginManager()

def test_case_1():
    dict_0 = {}
    plugin_manager_0 = module_0.PluginManager(**dict_0)
    var_0 = plugin_manager_0.register()

def test_case_2():
    plugin_manager_0 = module_0.PluginManager()
    list_0 = plugin_manager_0.get_formatters()

def test_case_3():
    plugin_manager_0 = module_0.PluginManager()
    var_0 = plugin_manager_0.load_installed_plugins()

def test_case_4():
    plugin_manager_0 = module_0.PluginManager()
    dict_0 = plugin_manager_0.get_auth_plugin_mapping()

def test_case_5():
    plugin_manager_0 = module_0.PluginManager()
    dict_0 = plugin_manager_0.get_formatters_grouped()

def test_case_6():
    plugin_manager_0 = module_0.PluginManager()
    dict_0 = plugin_manager_0.get_formatters_grouped()
    list_0 = plugin_manager_0.get_formatters()
    plugin_manager_1 = module_0.PluginManager()
    dict_1 = plugin_manager_1.get_auth_plugin_mapping()
    dict_2 = plugin_manager_0.get_auth_plugin_mapping()
    var_0 = plugin_manager_0.register()
    list_1 = plugin_manager_0.get_converters()

def test_case_7():
    plugin_manager_0 = module_0.PluginManager()
    list_0 = plugin_manager_0.get_transport_plugins()
    plugin_manager_1 = module_0.PluginManager()
    list_1 = plugin_manager_1.get_formatters()
    list_2 = plugin_manager_1.get_formatters()
    list_3 = plugin_manager_1.get_auth_plugins()

def test_case_8():
    str_0 = 'MEF6i:.>-u'
    str_1 = "&@Zx$zH'65L>*"
    str_2 = 'httpie.plugins.transport.v1'
    dict_0 = {str_0: str_0, str_1: str_2}
    plugin_manager_0 = module_0.PluginManager(**dict_0)
    var_0 = plugin_manager_0.__repr__()