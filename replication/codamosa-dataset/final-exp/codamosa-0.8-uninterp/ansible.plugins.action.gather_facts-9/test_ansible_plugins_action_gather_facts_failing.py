# Automatically generated by Pynguin.
import ansible.plugins.action.gather_facts as module_0

def test_case_0():
    try:
        bytes_0 = b'\xc6\xb3\x16\xec\x8d\xa3\xa2\x13\xfey\x93`\x06'
        str_0 = 'Unable to make %s into to %s, failed final rename from %s: %s'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        set_0 = set()
        bytes_1 = b'\x81\xb7pDW\x14\x8c\xf7\xb3\xf0\x0c\x97\xd0#\xd7\x07\xab\xdb\xbdh'
        list_0 = [dict_0]
        str_1 = 'B=-<cDPD$4'
        action_module_0 = module_0.ActionModule(dict_0, set_0, bytes_1, list_0, str_1, list_0)
        var_0 = action_module_0.run(bytes_0)
    except BaseException:
        pass