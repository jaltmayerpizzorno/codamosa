# Automatically generated by Pynguin.
import httpie.plugins.manager as module_0

def test_case_0():
    try:
        list_0 = []
        plugin_manager_0 = module_0.PluginManager(*list_0)
        dict_0 = {}
        plugin_manager_1 = module_0.PluginManager(*list_0, **dict_0)
        list_1 = plugin_manager_1.get_auth_plugins()
        dict_1 = plugin_manager_0.get_auth_plugin_mapping()
        str_0 = '='
        list_2 = plugin_manager_1.get_formatters()
        plugin_manager_2 = module_0.PluginManager()
        var_0 = plugin_manager_2.register()
        var_1 = plugin_manager_2.unregister(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "Ge':fP,lzCZOE(z<M=@"
        plugin_manager_0 = module_0.PluginManager()
        type_0 = plugin_manager_0.get_auth_plugin(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        plugin_manager_0 = module_0.PluginManager()
        list_0 = plugin_manager_0.get_converters()
        str_0 = '0 i9vo+\x0c3|e)T'
        type_0 = plugin_manager_0.get_auth_plugin(str_0)
    except BaseException:
        pass