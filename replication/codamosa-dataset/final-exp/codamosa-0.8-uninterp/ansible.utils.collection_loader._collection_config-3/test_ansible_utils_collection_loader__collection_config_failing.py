# Automatically generated by Pynguin.
import ansible.utils.collection_loader._collection_config as module_0

def test_case_0():
    try:
        bytes_0 = b'<\xb7'
        event_source_0 = module_0._EventSource()
        var_0 = event_source_0.__iadd__(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        bool_1 = True
        list_0 = [bool_0, bool_0, bool_1]
        event_source_0 = module_0._EventSource()
        var_0 = event_source_0.__isub__(list_0)
    except BaseException:
        pass