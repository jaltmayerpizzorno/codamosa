# Automatically generated by Pynguin.
import ansible.playbook.base as module_0

def test_case_0():
    try:
        base_0 = module_0.Base()
        var_0 = base_0.get_dep_chain()
        field_attribute_base_0 = module_0.FieldAttributeBase()
        set_0 = None
        var_1 = field_attribute_base_0.get_variable_manager()
        dict_0 = None
        var_2 = field_attribute_base_0.get_variable_manager()
        var_3 = field_attribute_base_0.load_data(set_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        list_0 = [field_attribute_base_0, field_attribute_base_0, field_attribute_base_0, field_attribute_base_0]
        float_0 = 517.88085
        field_attribute_base_1 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_1.load_data(field_attribute_base_0, list_0, float_0)
    except BaseException:
        pass

def test_case_2():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        set_0 = {field_attribute_base_0, field_attribute_base_0}
        var_0 = field_attribute_base_0.load_data(set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.squash()
        var_1 = field_attribute_base_0.get_variable_manager()
        var_2 = field_attribute_base_0.dump_me()
        base_0 = module_0.Base()
        var_3 = base_0.get_search_path()
        str_0 = 'xNV>^h#>*SAx1#cb3p'
        var_4 = field_attribute_base_0.validate()
        var_5 = field_attribute_base_0.get_loader()
        var_6 = field_attribute_base_0.serialize()
        var_7 = base_0.get_dep_chain()
        var_8 = field_attribute_base_0.copy()
        int_0 = -2307
        str_1 = '6Ms5#'
        dict_0 = {str_0: var_5, str_1: str_0, str_1: var_1}
        str_2 = 'P0U[j)tM(@C<'
        var_9 = field_attribute_base_0.get_validated_value(dict_0, str_2, int_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.serialize()
        dict_0 = {}
        str_0 = 'ok: [%s]'
        base_0 = module_0.Base()
        var_1 = base_0.get_search_path()
        var_2 = field_attribute_base_0.load_data(dict_0, str_0)
        var_3 = field_attribute_base_0.dump_me()
        var_4 = field_attribute_base_0.copy()
        base_1 = module_0.Base()
        str_1 = 'xNV>^h#>*SAx1#cb3p'
        var_5 = field_attribute_base_0.validate()
        dict_1 = {field_attribute_base_0: field_attribute_base_0}
        var_6 = field_attribute_base_0.from_attrs(dict_1)
        var_7 = field_attribute_base_0.copy()
        list_0 = [field_attribute_base_0, str_1]
        str_2 = 'v;Gl#w6;$\x0cB=Q-*H'
        dict_2 = {str_1: list_0, str_2: str_1}
        var_8 = field_attribute_base_0.deserialize(dict_2)
        base_2 = module_0.Base()
        bool_0 = False
        var_9 = field_attribute_base_0.post_validate(bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.dump_attrs()
        field_attribute_base_1 = module_0.FieldAttributeBase()
        var_1 = field_attribute_base_0.from_attrs(field_attribute_base_1)
    except BaseException:
        pass

def test_case_6():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.get_ds()
        str_0 = '/sys/devices/virtual/dmi/id/product_serial'
        var_1 = field_attribute_base_0.get_loader()
        list_0 = [str_0]
        field_attribute_base_1 = module_0.FieldAttributeBase()
        var_2 = field_attribute_base_1.deserialize(list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        field_attribute_base_1 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_1.dump_me(field_attribute_base_0)
    except BaseException:
        pass

def test_case_8():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.squash()
        base_0 = module_0.Base()
        var_1 = base_0.get_dep_chain()
        var_2 = field_attribute_base_0.dump_attrs()
        var_3 = field_attribute_base_0.squash()
        var_4 = field_attribute_base_0.validate()
        var_5 = field_attribute_base_0.get_loader()
        var_6 = field_attribute_base_0.serialize()
        var_7 = field_attribute_base_0.copy()
        list_0 = [base_0]
        base_meta_0 = module_0.BaseMeta(*list_0)
    except BaseException:
        pass

def test_case_9():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.copy()
        field_attribute_base_1 = module_0.FieldAttributeBase()
        var_1 = field_attribute_base_1.serialize()
        var_2 = field_attribute_base_1.squash()
        dict_0 = {}
        var_3 = field_attribute_base_0.deserialize(dict_0)
        field_attribute_base_2 = module_0.FieldAttributeBase()
        dict_1 = {}
        str_0 = 'ok: [%s]'
        var_4 = field_attribute_base_2.load_data(dict_1, str_0)
        var_5 = field_attribute_base_2.dump_me()
        base_0 = module_0.Base()
        var_6 = field_attribute_base_2.copy()
        str_1 = 'xNV>^h#>*SAx1#cb3p'
        var_7 = field_attribute_base_2.dump_attrs()
        var_8 = field_attribute_base_2.validate()
        field_attribute_base_3 = module_0.FieldAttributeBase()
        var_9 = field_attribute_base_3.from_attrs(dict_1)
        var_10 = field_attribute_base_3.serialize()
        var_11 = field_attribute_base_0.copy()
        dict_2 = {base_0: str_1}
        list_0 = [dict_2, field_attribute_base_2]
        str_2 = 'v;Gl#w6;$\x0cB=Q-*H'
        var_12 = base_0.get_search_path()
        dict_3 = {str_1: list_0, str_2: str_1}
        var_13 = field_attribute_base_2.deserialize(dict_3)
        list_1 = [var_7, var_1, var_7]
        base_meta_0 = module_0.BaseMeta(*list_1)
    except BaseException:
        pass