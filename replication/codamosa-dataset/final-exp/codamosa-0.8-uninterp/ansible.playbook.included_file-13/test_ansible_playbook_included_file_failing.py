# Automatically generated by Pynguin.
import ansible.playbook.included_file as module_0
import ansible.playbook.task_include as module_1

def test_case_0():
    try:
        bytes_0 = b'\xef\x12\xc3(8\x99\xfd\x1cc\x7f~\t1'
        int_0 = 1678
        list_0 = [bytes_0, int_0]
        float_0 = 1.0
        included_file_0 = module_0.IncludedFile(bytes_0, int_0, list_0, float_0)
        var_0 = included_file_0.__eq__(included_file_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'show_task_path_on_failure'
        tuple_0 = ()
        float_0 = 2217.207615
        bool_0 = False
        bytes_0 = None
        set_0 = {tuple_0, float_0}
        included_file_0 = module_0.IncludedFile(set_0, str_0, bool_0, tuple_0)
        var_0 = included_file_0.process_include_results(tuple_0, bytes_0, float_0, included_file_0)
        var_1 = included_file_0.__repr__()
        var_2 = included_file_0.__eq__(included_file_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        tuple_0 = (bool_0,)
        task_include_0 = None
        str_0 = None
        str_1 = '!%#NC10D\tgMPxNiIG'
        bytes_0 = b'I\x01\xcbr\xe8%7\x9f'
        float_0 = None
        str_2 = 'VK-r\\M]g0Ynx*H+'
        included_file_0 = module_0.IncludedFile(str_1, bytes_0, float_0, str_2)
        int_0 = 86400
        bytes_1 = b'\xd3\x13\xbc~T\xeb'
        str_3 = 'VK-r\\M]g0Ynx*H+'
        float_1 = 1522.05
        tuple_1 = ()
        list_0 = [bytes_1, tuple_1, str_3]
        included_file_1 = module_0.IncludedFile(int_0, bytes_1, str_3, float_1, list_0)
        var_0 = included_file_1.process_include_results(tuple_0, task_include_0, str_0, included_file_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = None
        bytes_0 = b'\x17@}\xcc\xce'
        tuple_0 = (list_0, bytes_0)
        int_0 = -1499
        included_file_0 = module_0.IncludedFile(tuple_0, int_0, bytes_0, list_0)
        var_0 = included_file_0.__repr__()
        list_1 = []
        var_1 = included_file_0.add_host(included_file_0)
        str_0 = ''
        dict_0 = {}
        int_1 = 438
        included_file_1 = module_0.IncludedFile(dict_0, str_0, int_1, list_1)
        var_2 = included_file_0.add_host(included_file_0)
    except BaseException:
        pass

def test_case_4():
    try:
        var_0 = None
        var_1 = None
        str_0 = 'A'
        var_2 = dict(a=var_0)
        bool_0 = False
        task_include_0 = module_1.TaskInclude(str_0, str_0, bool_0)
        included_file_0 = module_0.IncludedFile(str_0, var_1, var_2, task_include_0, bool_0)
        var_3 = dict(b=bool_0)
        var_4 = dict(b=task_include_0)
        included_file_1 = module_0.IncludedFile(str_0, var_4, var_2, task_include_0, bool_0)
        var_5 = included_file_0 == included_file_1
        var_6 = included_file_0 == included_file_0
    except BaseException:
        pass