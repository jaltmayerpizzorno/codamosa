# Automatically generated by Pynguin.
import ansible.plugins.action.copy as module_0

def test_case_0():
    try:
        int_0 = 3107
        set_0 = {int_0}
        str_0 = 'Ig=<%d+`'
        bool_0 = True
        action_module_0 = module_0.ActionModule(int_0, set_0, str_0, set_0, bool_0, str_0)
        var_0 = action_module_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ',cOy]p;\x0bhi'
        list_0 = [str_0, str_0]
        bytes_0 = None
        str_1 = '/k!GV+'
        tuple_0 = (bytes_0, str_1)
        str_2 = 'yZRQ5\x0cj\x0b\nA\\c[,k#'
        int_0 = -1207
        set_0 = {str_2, str_2, int_0, int_0}
        action_module_0 = module_0.ActionModule(bytes_0, tuple_0, list_0, bytes_0, list_0, set_0)
        int_1 = 888
        str_3 = '\x0buMU'
        dict_0 = None
        str_4 = 'Download and save a file via HTTP(S) or FTP (needs the module as parameter).\n    This is basically a wrapper around fetch_url().\n\n    :arg module: The AnsibleModule (used to get username, password etc. (s.b.).\n    :arg url:             The url to use.\n\n    :kwarg data:          The data to be sent (in case of POST/PUT).\n    :kwarg headers:       A dict with the request headers.\n    :kwarg method:        "POST", "PUT", etc.\n    :kwarg boolean use_proxy:     Default: True\n    :kwarg boolean force: If True: Do not get a cached copy (Default: False)\n    :kwarg last_mod_time: Default: None\n    :kwarg int timeout:   Default: 10\n    :kwarg unredirected_headers: (optional) A list of headers to not attach on a redirected request\n\n    :returns: A string, the path to the downloaded file.\n    '
        action_module_1 = module_0.ActionModule(list_0, action_module_0, int_1, str_3, dict_0, str_4)
        float_0 = -80.23
        action_module_2 = module_0.ActionModule(set_0, action_module_1, dict_0, float_0, list_0, set_0)
        list_1 = [str_0, str_1, int_0]
        float_1 = -1863.25474
        action_module_3 = module_0.ActionModule(float_1, float_1, set_0, list_0, float_0, list_1)
        action_module_4 = module_0.ActionModule(list_0, list_0, list_1, action_module_2, set_0, action_module_3)
        str_5 = 'One or more worker processes are still running and will be terminated.'
        var_0 = action_module_4.run(str_0, str_5)
    except BaseException:
        pass