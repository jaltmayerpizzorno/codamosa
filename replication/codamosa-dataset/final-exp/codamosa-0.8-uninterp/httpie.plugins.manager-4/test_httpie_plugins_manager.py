# Automatically generated by Pynguin.
import httpie.plugins.manager as module_0

def test_case_0():
    plugin_manager_0 = module_0.PluginManager()

def test_case_1():
    plugin_manager_0 = module_0.PluginManager()
    dict_0 = plugin_manager_0.get_auth_plugin_mapping()

def test_case_2():
    plugin_manager_0 = module_0.PluginManager()
    var_0 = plugin_manager_0.load_installed_plugins()

def test_case_3():
    plugin_manager_0 = module_0.PluginManager()
    dict_0 = plugin_manager_0.get_formatters_grouped()