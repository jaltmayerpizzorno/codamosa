# Automatically generated by Pynguin.
import tornado.concurrent as module_0
import _asyncio as module_1
import concurrent.futures._base as module_2
import builtins as module_3

def test_case_0():
    try:
        future_0 = None
        dummy_executor_0 = module_0.DummyExecutor()
        future_1 = dummy_executor_0.submit(future_0)
        future_2 = module_1.Future()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'm=\\\nD=Q+aZ<I\x0cB\r-V:v'
        bool_0 = module_0.is_future(str_0)
        bool_1 = module_0.is_future(bool_0)
        list_0 = [bool_0, bool_0]
        str_1 = 'Unrecognized command line option: %r'
        str_2 = '6r{1(Ns03h).'
        dict_0 = {str_1: bool_0, str_0: bool_0, str_1: bool_0, str_2: str_2}
        callable_0 = module_0.run_on_executor(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        future_0 = None
        module_0.chain_future(future_0, future_0)
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        callable_0 = module_0.run_on_executor(**dict_0)
        list_0 = [dict_0, callable_0]
        future_0 = module_2.Future()
        var_0 = None
        future_1 = module_2.Future()
        module_0.future_add_done_callback(future_1, callable_0)
        module_0.future_set_result_unless_cancelled(future_0, var_0)
        return_value_ignored_error_0 = module_0.ReturnValueIgnoredError(*list_0)
        bool_0 = module_0.is_future(return_value_ignored_error_0)
        callable_1 = module_0.run_on_executor(*list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        future_0 = module_2.Future()
        bool_0 = False
        dummy_executor_0 = module_0.DummyExecutor()
        callable_0 = module_0.run_on_executor()
        module_0.future_set_result_unless_cancelled(future_0, callable_0)
        dummy_executor_0.shutdown(bool_0)
        dummy_executor_1 = module_0.DummyExecutor()
        dummy_executor_0.shutdown()
        int_0 = -1633
        module_0.future_add_done_callback(future_0, int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        future_0 = module_2.Future()
        str_0 = '|r%KG'
        none_type_0 = None
        optional_0 = None
        var_0 = None
        module_0.future_set_result_unless_cancelled(future_0, var_0)
        tuple_0 = (str_0, none_type_0, optional_0)
        module_0.future_set_exc_info(future_0, tuple_0)
    except BaseException:
        pass

def test_case_6():
    try:
        future_0 = module_2.Future()
        base_exception_0 = module_3.BaseException()
        module_0.future_add_done_callback(future_0, base_exception_0)
        dummy_executor_0 = module_0.DummyExecutor()
        bool_0 = module_0.is_future(future_0)
        list_0 = [dummy_executor_0]
        callable_0 = module_0.run_on_executor(*list_0)
        callable_1 = module_0.run_on_executor()
        module_0.future_set_result_unless_cancelled(future_0, callable_1)
        dummy_executor_1 = module_0.DummyExecutor()
        dummy_executor_0.shutdown()
        return_value_ignored_error_0 = module_0.ReturnValueIgnoredError()
        callable_2 = None
        future_1 = dummy_executor_1.submit(callable_2)
        list_1 = []
        str_0 = '/\x0b.5VVStd'
        dict_0 = {str_0: str_0}
        dummy_executor_2 = module_0.DummyExecutor(*list_1, **dict_0)
    except BaseException:
        pass