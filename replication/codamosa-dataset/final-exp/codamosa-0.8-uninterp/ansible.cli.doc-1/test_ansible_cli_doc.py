# Automatically generated by Pynguin.
import ansible.cli.doc as module_0
import ansible.utils.display as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'n|s%X_24nz'
    doc_c_l_i_0 = module_0.DocCLI(str_0)
    var_0 = doc_c_l_i_0.run()

def test_case_2():
    bool_0 = True
    tuple_0 = ()
    list_0 = []
    display_0 = module_1.Display(list_0)
    float_0 = -1248.58257
    dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
    doc_c_l_i_0 = module_0.DocCLI(dict_0)
    var_0 = doc_c_l_i_0.find_plugins(bool_0, tuple_0, display_0)

def test_case_3():
    str_0 = 'n|s%X_24nz'
    doc_c_l_i_0 = module_0.DocCLI(str_0)
    var_0 = doc_c_l_i_0.run()
    list_0 = []
    plugin_not_found_0 = module_0.PluginNotFound(*list_0)
    tuple_0 = (plugin_not_found_0, list_0)
    var_1 = doc_c_l_i_0.find_plugins(str_0, tuple_0, list_0)

def test_case_4():
    str_0 = '\rzfRaA"'
    int_0 = 70
    var_0 = module_0.add_collection_plugins(str_0, int_0)

def test_case_5():
    int_0 = -2072
    set_0 = set()
    doc_c_l_i_0 = module_0.DocCLI(int_0)
    bool_0 = False
    tuple_0 = (doc_c_l_i_0, bool_0)
    float_0 = -286.227807
    list_0 = [int_0, bool_0, doc_c_l_i_0, tuple_0]
    list_1 = [float_0, list_0, bool_0, doc_c_l_i_0]
    list_2 = None
    list_3 = [list_2]
    doc_c_l_i_1 = module_0.DocCLI(list_3)
    var_0 = doc_c_l_i_1.add_fields(int_0, set_0, tuple_0, float_0, list_1)