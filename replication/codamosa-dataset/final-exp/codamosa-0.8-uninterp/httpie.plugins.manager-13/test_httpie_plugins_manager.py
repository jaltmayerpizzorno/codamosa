# Automatically generated by Pynguin.
import httpie.plugins.manager as module_0

def test_case_0():
    pass

def test_case_1():
    plugin_manager_0 = module_0.PluginManager()
    list_0 = plugin_manager_0.get_converters()
    str_0 = 'c)mQ3W:7#\n'
    list_1 = []
    var_0 = plugin_manager_0.register()
    str_1 = ''
    str_2 = '--proxy'
    dict_0 = {str_0: list_1, str_0: list_1, str_1: str_1, str_2: list_0}
    plugin_manager_1 = module_0.PluginManager(**dict_0)
    var_1 = plugin_manager_1.__repr__()
    plugin_manager_2 = module_0.PluginManager()

def test_case_2():
    plugin_manager_0 = module_0.PluginManager()
    list_0 = plugin_manager_0.get_converters()

def test_case_3():
    plugin_manager_0 = module_0.PluginManager()
    var_0 = plugin_manager_0.load_installed_plugins()

def test_case_4():
    plugin_manager_0 = module_0.PluginManager()
    list_0 = plugin_manager_0.get_auth_plugins()

def test_case_5():
    plugin_manager_0 = module_0.PluginManager()
    dict_0 = plugin_manager_0.get_auth_plugin_mapping()

def test_case_6():
    plugin_manager_0 = module_0.PluginManager()
    dict_0 = plugin_manager_0.get_formatters_grouped()

def test_case_7():
    str_0 = '.K`~5GjC+'
    str_1 = '\n    You can specify a local cert to use as client side SSL certificate.\n    This file may either contain both private key and certificate or you may\n    specify --cert-key separately.\n\n    '
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_1: str_0}
    plugin_manager_0 = module_0.PluginManager(**dict_0)
    list_0 = plugin_manager_0.get_transport_plugins()