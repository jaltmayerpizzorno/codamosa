# Automatically generated by Pynguin.
import ansible.playbook.base as module_0

def test_case_0():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        list_0 = [field_attribute_base_0]
        var_0 = field_attribute_base_0.load_data(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        str_0 = ',fwm-[9Bv6\t5'
        dict_0 = {str_0: field_attribute_base_0, str_0: str_0, str_0: field_attribute_base_0}
        var_0 = field_attribute_base_0.deserialize(dict_0)
        var_1 = field_attribute_base_0.post_validate(field_attribute_base_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\x02\x9fo \x80]'
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.from_attrs(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        set_0 = {field_attribute_base_0, field_attribute_base_0}
        str_0 = ',fwm-[9Bv6\t5'
        dict_0 = {str_0: field_attribute_base_0, str_0: str_0, str_0: field_attribute_base_0}
        var_0 = field_attribute_base_0.deserialize(dict_0)
        list_0 = [set_0]
        base_meta_0 = module_0.BaseMeta(*list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.dump_me()
        str_0 = '\\:Q#-'
        dict_0 = {field_attribute_base_0: field_attribute_base_0, field_attribute_base_0: var_0, var_0: str_0, str_0: var_0}
        tuple_0 = (dict_0, dict_0)
        var_1 = field_attribute_base_0.deserialize(tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.copy()
        var_1 = field_attribute_base_0.dump_me()
        str_0 = '\\:Q#-'
        var_2 = field_attribute_base_0.dump_me(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        base_0 = module_0.Base()
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = base_0.get_dep_chain()
        base_1 = module_0.Base()
        var_1 = field_attribute_base_0.copy()
        var_2 = base_1.get_path()
        var_3 = field_attribute_base_0.squash()
        var_4 = base_1.get_dep_chain()
        var_5 = base_1.get_search_path()
        base_2 = module_0.Base()
        var_6 = field_attribute_base_0.squash()
        field_attribute_base_1 = module_0.FieldAttributeBase()
        var_7 = field_attribute_base_1.copy()
        var_8 = field_attribute_base_1.dump_attrs()
        var_9 = field_attribute_base_0.dump_me()
        base_3 = module_0.Base()
        field_attribute_base_2 = module_0.FieldAttributeBase()
        field_attribute_base_3 = module_0.FieldAttributeBase()
        field_attribute_base_4 = module_0.FieldAttributeBase()
        var_10 = field_attribute_base_0.get_variable_manager()
        bytes_0 = b''
        var_11 = field_attribute_base_4.deserialize(bytes_0)
    except BaseException:
        pass

def test_case_7():
    try:
        base_0 = module_0.Base()
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = base_0.get_dep_chain()
        base_1 = module_0.Base()
        var_1 = base_1.get_path()
        var_2 = base_1.get_dep_chain()
        var_3 = base_1.get_search_path()
        base_2 = module_0.Base()
        field_attribute_base_1 = module_0.FieldAttributeBase()
        var_4 = field_attribute_base_1.copy()
        var_5 = field_attribute_base_1.dump_attrs()
        var_6 = field_attribute_base_0.dump_me()
        str_0 = 'i'
        dict_0 = {str_0: field_attribute_base_1}
        field_attribute_base_2 = module_0.FieldAttributeBase()
        var_7 = field_attribute_base_2.from_attrs(dict_0)
        list_0 = None
        var_8 = field_attribute_base_1.load_data(list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bytes_0 = b'\xfc\x9e'
        str_0 = None
        list_0 = [bytes_0]
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.load_data(bytes_0, str_0, list_0)
    except BaseException:
        pass

def test_case_9():
    try:
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.serialize()
        var_1 = field_attribute_base_0.copy()
        var_2 = field_attribute_base_0.squash()
        var_3 = field_attribute_base_0.get_ds()
        var_4 = field_attribute_base_0.get_loader()
        field_attribute_base_1 = module_0.FieldAttributeBase()
        tuple_0 = ()
        set_0 = {var_1, var_3}
        var_5 = field_attribute_base_1.load_data(tuple_0, set_0)
        var_6 = field_attribute_base_1.copy()
        var_7 = field_attribute_base_1.validate()
        base_meta_0 = module_0.BaseMeta()
    except BaseException:
        pass