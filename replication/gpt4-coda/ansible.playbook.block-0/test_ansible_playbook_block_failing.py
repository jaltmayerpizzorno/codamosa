# Automatically generated by Pynguin.
import ansible.playbook.block as module_0
import ansible.playbook.role as module_1

def test_case_0():
    try:
        float_0 = 512.0
        block_0 = module_0.Block(float_0, float_0)
        var_0 = block_0.serialize()
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = ()
        bytes_0 = b'iC\xee#\xd6>\xa2z\x1e\xa1;\x17\xddH3\x03,E\xb8l'
        block_0 = module_0.Block(bytes_0, tuple_0, tuple_0)
        var_0 = block_0.get_first_parent_include()
        str_0 = 'a`J\nz\tY~,lsAM,)X4@$'
        block_1 = module_0.Block()
        var_1 = block_1.__eq__(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "F3\tvc\r.mMf;O;Yis|AO'"
        bytes_0 = b'7\xe0d@X&&\xb8"j\x80>7\xb0\xb5'
        str_1 = '%d'
        float_0 = 1195.85
        block_0 = module_0.Block(bytes_0, str_1, float_0)
        var_0 = block_0.__ne__(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        tuple_0 = ()
        block_0 = module_0.Block(tuple_0)
        float_0 = -1836.926106
        list_0 = [block_0, float_0, float_0, float_0]
        var_0 = block_0.load(float_0, list_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '%(w!#N`k-x0p,-e'
        int_0 = -912
        block_0 = module_0.Block(str_0, int_0)
        dict_0 = {}
        dict_1 = {int_0: dict_0, int_0: int_0}
        var_0 = block_0.deserialize(dict_1)
        var_1 = block_0.has_tasks()
        var_2 = block_0.all_parents_static()
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\xce'
        float_0 = 955.7
        bool_0 = True
        block_0 = module_0.Block(bytes_0, float_0, bool_0)
        var_0 = block_0.has_tasks()
        block_1 = module_0.Block()
        var_1 = block_0.deserialize(block_1)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = None
        str_0 = 'geturl'
        block_0 = module_0.Block(str_0)
        int_0 = None
        int_1 = -251
        role_0 = module_1.Role()
        bool_0 = True
        block_1 = module_0.Block(int_1, role_0, bool_0)
        var_0 = block_1.set_loader(int_0)
        block_2 = module_0.Block(block_0, str_0)
        var_1 = block_2.filter_tagged_tasks(float_0)
        var_2 = block_2.all_parents_static()
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'NoE;3(tuw3JOak*$'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        block_0 = module_0.Block(str_0, dict_0)
        var_0 = block_0.get_include_params()
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = True
        str_0 = 'aPR(?Z%1]jjOiAbOC5\\'
        block_0 = module_0.Block(bool_0, str_0)
        var_0 = block_0.all_parents_static()
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = 512.0
        block_0 = module_0.Block(float_0, float_0)
        var_0 = block_0.get_first_parent_include()
    except BaseException:
        pass

def test_case_10():
    try:
        set_0 = set()
        dict_0 = {}
        str_0 = "\\f#06;'p'\r "
        block_0 = module_0.Block(dict_0, str_0)
        list_0 = [set_0, block_0, set_0]
        block_1 = module_0.Block(block_0, list_0)
        var_0 = block_1.get_vars()
    except BaseException:
        pass

def test_case_11():
    try:
        dict_0 = {}
        role_0 = module_1.Role(dict_0, dict_0)
        bytes_0 = b'\xf9'
        bool_0 = True
        block_0 = module_0.Block(bytes_0, role_0, bool_0)
        var_0 = block_0.serialize()
    except BaseException:
        pass

def test_case_12():
    try:
        bool_0 = False
        set_0 = set()
        str_0 = 'oWe'
        block_0 = module_0.Block(set_0, str_0, bool_0)
        dict_0 = {}
        bytes_0 = b'H-\x1f\x17\x81'
        var_0 = block_0.load(dict_0, bool_0, bytes_0)
    except BaseException:
        pass

def test_case_13():
    try:
        dict_0 = {}
        str_0 = '!E:~bE\x0c-0Rd=;Jiia'
        block_0 = module_0.Block(dict_0, str_0)
        var_0 = block_0.has_tasks()
        block_1 = module_0.Block()
        str_1 = '\n- name: give users access to multiple databases\n  mysql_user:\n    name: "{{ item[0] }}"\n    priv: "{{ item[1] }}.*:ALL"\n    append_privs: yes\n    password: "foo"\n  with_nested:\n    - [ \'alice\', \'bob\' ]\n    - [ \'clientdb\', \'employeedb\', \'providerdb\' ]\n# As with the case of \'with_items\' above, you can use previously defined variables.:\n\n- name: here, \'users\' contains the above list of employees\n  mysql_user:\n    name: "{{ item[0] }}"\n    priv: "{{ item[1] }}.*:ALL"\n    append_privs: yes\n    password: "foo"\n  with_nested:\n    - "{{ users }}"\n    - [ \'clientdb\', \'employeedb\', \'providerdb\' ]\n'
        var_1 = block_1.copy()
        var_2 = block_1.preprocess_data(block_0)
        var_3 = block_1.get_dep_chain()
        var_4 = block_1.deserialize(str_1)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'RG={~F~G Nx6q b#yW='
        float_0 = -1125.0
        tuple_0 = (float_0,)
        bytes_0 = b'+\x02\x05\xbb\xd2e\x06\x0el\x01\xe2\xb4\xbf\xf6\xccT'
        int_0 = -4946
        block_0 = module_0.Block(bytes_0, int_0)
        set_0 = set()
        block_1 = module_0.Block(str_0, tuple_0, block_0, bytes_0, set_0)
        var_0 = block_1.serialize()
    except BaseException:
        pass

def test_case_15():
    try:
        block_0 = module_0.Block()
        str_0 = 'name'
        str_1 = 'role'
        str_2 = 'parent_type'
        str_3 = 'parent'
        str_4 = 'dep1'
        str_5 = 'dep2'
        str_6 = [str_4, str_5]
        str_7 = 'vars'
        str_8 = 'test_role'
        str_9 = 'role_var'
        str_10 = 'value'
        str_11 = {str_9: str_10}
        str_12 = {str_0: str_8, str_7: str_11}
        str_13 = 'Block'
        str_14 = {str_0: str_4, str_4: str_6, str_1: str_12, str_2: str_13, str_3: str_4}
        var_0 = block_0.deserialize(str_14)
    except BaseException:
        pass

def test_case_16():
    try:
        block_0 = module_0.Block()
        str_0 = '9F;iJygj=.7RH_'
        str_1 = 'parent_type'
        str_2 = 'parent'
        str_3 = 'dep1'
        str_4 = [str_3, str_2]
        str_5 = 'vars'
        str_6 = 'test_role'
        str_7 = 'value'
        str_8 = {str_2: str_7}
        str_9 = {str_1: str_6, str_5: str_8}
        str_10 = {str_5: str_3, str_3: str_4, str_0: str_9, str_1: str_5, str_2: str_3}
        var_0 = block_0.deserialize(str_10)
    except BaseException:
        pass