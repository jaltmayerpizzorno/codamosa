# Automatically generated by Pynguin.
import tornado.concurrent as module_0
import concurrent.futures._base as module_1
import builtins as module_2

def test_case_0():
    try:
        bool_0 = True
        list_0 = [bool_0, bool_0, bool_0]
        callable_0 = module_0.run_on_executor(*list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        future_0 = module_1.Future()
        bool_0 = False
        dict_0 = {future_0: bool_0, future_0: future_0}
        optional_0 = None
        dict_1 = {}
        tuple_0 = (dict_0, optional_0, dict_1)
        module_0.future_set_exc_info(future_0, tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        dummy_executor_0 = module_0.DummyExecutor()
        future_0 = module_1.Future()
        var_0 = None
        callable_0 = module_0.run_on_executor()
        module_0.future_set_result_unless_cancelled(future_0, var_0)
        set_0 = {future_0, future_0}
        module_0.future_add_done_callback(future_0, set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        future_0 = module_1.Future()
        set_0 = {future_0, future_0}
        module_0.future_add_done_callback(future_0, set_0)
        future_1 = None
        module_0.chain_future(future_1, future_1)
    except BaseException:
        pass

def test_case_4():
    try:
        future_0 = None
        module_0.chain_future(future_0, future_0)
    except BaseException:
        pass

def test_case_5():
    try:
        list_0 = None
        bool_0 = module_0.is_future(list_0)
        bool_1 = True
        future_0 = module_1.Future()
        base_exception_0 = module_2.BaseException()
        module_0.future_set_exception_unless_cancelled(future_0, base_exception_0)
        dummy_executor_0 = module_0.DummyExecutor()
        dummy_executor_0.shutdown(bool_1)
        callable_0 = None
        dummy_executor_0.shutdown()
        dummy_executor_0.shutdown(bool_1)
        dummy_executor_1 = module_0.DummyExecutor()
        future_1 = dummy_executor_1.submit(callable_0)
        list_1 = [list_0]
        callable_1 = module_0.run_on_executor(*list_1)
        base_exception_1 = module_2.BaseException()
        future_2 = module_1.Future()
        callable_2 = module_0.run_on_executor(*list_1)
        set_0 = {dummy_executor_1, bool_0, future_1, dummy_executor_1}
        module_0.future_add_done_callback(future_2, callable_2)
        module_0.future_set_result_unless_cancelled(future_2, set_0)
        dummy_executor_2 = module_0.DummyExecutor()
        future_3 = None
        module_0.chain_future(future_3, future_3)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '3ve\t*BGzEF'
        str_1 = '*ecGV%NQ9WHLi\r>'
        str_2 = 'NkI\\Gy9r'
        callable_0 = module_0.run_on_executor()
        list_0 = [str_0, str_2]
        dummy_executor_0 = module_0.DummyExecutor()
        str_3 = '/etc/resolv.conf'
        dict_0 = {str_2: str_1, str_1: list_0, str_1: str_0, str_3: str_0}
        bool_0 = module_0.is_future(str_3)
        callable_1 = module_0.run_on_executor(*list_0, **dict_0)
    except BaseException:
        pass