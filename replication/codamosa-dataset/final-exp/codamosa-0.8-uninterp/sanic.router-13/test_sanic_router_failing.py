# Automatically generated by Pynguin.
import sanic.router as module_0

def test_case_0():
    try:
        str_0 = ',DlW5t)#,eH?jL*e\t)'
        bytes_0 = b'\xb3]:'
        dict_0 = {str_0: str_0}
        bool_0 = False
        router_0 = module_0.Router()
        var_0 = router_0.add(str_0, bytes_0, dict_0, bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        router_0 = module_0.Router(bool_0)
        str_0 = '~Yuq\n?*'
        int_0 = -1850
        str_1 = 'DcDn<dn+y0&7'
        dict_0 = {str_1: bool_0}
        var_0 = router_0.add(str_0, int_0, dict_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'GRACEFUL_SHUTDOWN_TIMEOUT'
        callable_0 = None
        bool_0 = False
        router_0 = module_0.Router()
        str_1 = 'wsZq\r!tE0^o,EV>'
        list_0 = [str_0]
        bool_1 = True
        var_0 = router_0.add(str_1, list_0, callable_0, str_0, bool_0, bool_0, bool_0, bool_1)
    except BaseException:
        pass

def test_case_3():
    try:
        router_0 = module_0.Router()
        str_0 = '/test72/<__id>'
        str_1 = []
        var_0 = router_0.add(str_0, str_1, str_0)
        var_1 = router_0.finalize()
    except BaseException:
        pass