# Automatically generated by Pynguin.
import httpie.plugins.manager as module_0

def test_case_0():
    try:
        dict_0 = {}
        plugin_manager_0 = module_0.PluginManager(**dict_0)
        var_0 = plugin_manager_0.filter()
        plugin_manager_1 = module_0.PluginManager()
        var_1 = plugin_manager_1.load_installed_plugins()
        plugin_manager_2 = module_0.PluginManager()
        list_0 = plugin_manager_0.get_formatters()
        type_0 = None
        dict_1 = plugin_manager_2.get_formatters_grouped()
        plugin_manager_3 = module_0.PluginManager()
        dict_2 = plugin_manager_3.get_auth_plugin_mapping()
        var_2 = plugin_manager_3.filter()
        plugin_manager_4 = module_0.PluginManager()
        list_1 = plugin_manager_4.get_transport_plugins()
        plugin_manager_5 = module_0.PluginManager()
        dict_3 = plugin_manager_5.get_formatters_grouped()
        var_3 = plugin_manager_5.unregister(type_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = None
        plugin_manager_0 = module_0.PluginManager()
        type_0 = plugin_manager_0.get_auth_plugin(str_0)
    except BaseException:
        pass