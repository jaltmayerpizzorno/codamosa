# Automatically generated by Pynguin.
import httpie.plugins.base as module_0

def test_case_0():
    try:
        str_0 = 'format_options'
        str_1 = 'headers_only'
        bool_0 = False
        bool_1 = {str_1: bool_0}
        bool_2 = {str_0: bool_1}
        formatter_plugin_0 = module_0.FormatterPlugin(**bool_2)
        str_2 = 'Last-Modified: Tue, 22 Jan 2019 16:33:34 GMT\n    ETag: "5c467a7e-5b1"\n    Vary: Accept'
        str_3 = formatter_plugin_0.format_headers(str_2)
        auth_plugin_0 = module_0.AuthPlugin()
        var_0 = auth_plugin_0.get_auth()
    except BaseException:
        pass

def test_case_1():
    try:
        transport_plugin_0 = module_0.TransportPlugin()
        var_0 = transport_plugin_0.get_adapter()
    except BaseException:
        pass

def test_case_2():
    try:
        base_plugin_0 = module_0.BasePlugin()
        complex_0 = None
        list_0 = None
        tuple_0 = (list_0,)
        converter_plugin_0 = module_0.ConverterPlugin(tuple_0)
        var_0 = converter_plugin_0.convert(complex_0)
    except BaseException:
        pass

def test_case_3():
    try:
        formatter_plugin_0 = module_0.FormatterPlugin()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'format_options'
        str_1 = 'headers_only'
        bool_0 = False
        bool_1 = {str_1: bool_0}
        bool_2 = {str_0: bool_1}
        formatter_plugin_0 = module_0.FormatterPlugin(**bool_2)
        str_2 = 'Last-Modified: Tue, 22 Jan 2019 16:33:34 GMT\n    ETag: "5c467a7e-5b1"\n    Vary: Accept'
        str_3 = formatter_plugin_0.format_headers(str_2)
        str_4 = '%R,ed7A3qp2='
        str_5 = formatter_plugin_0.format_body(str_2, str_4)
        auth_plugin_0 = module_0.AuthPlugin()
        var_0 = auth_plugin_0.get_auth()
    except BaseException:
        pass