# Automatically generated by Pynguin.
import tornado.concurrent as module_0
import builtins as module_1
import concurrent.futures._base as module_2
import _asyncio as module_3

def test_case_0():
    try:
        callable_0 = None
        list_0 = [callable_0, callable_0]
        bool_0 = module_0.is_future(callable_0)
        dummy_executor_0 = module_0.DummyExecutor()
        future_0 = dummy_executor_0.submit(callable_0, *list_0)
        bytes_0 = b'\x1b\x03\xc8\x8b\xdf\xd5\xaf\x9a\xf4\xbe'
        return_value_ignored_error_0 = module_0.ReturnValueIgnoredError()
        base_exception_0 = module_1.BaseException()
        bytes_1 = b'\x94\x01\x86\x8b'
        tuple_0 = (bytes_0, return_value_ignored_error_0, base_exception_0, bytes_1)
        module_0.future_set_result_unless_cancelled(future_0, tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        dummy_executor_0 = module_0.DummyExecutor()
        bool_0 = False
        dummy_executor_0.shutdown(bool_0)
        callable_0 = module_0.run_on_executor(**dict_0)
        str_0 = 'JWCCk\rdZG\t\x0b'
        tuple_0 = (str_0,)
        future_0 = dummy_executor_0.submit(tuple_0)
        future_1 = None
        module_0.chain_future(future_1, future_1)
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
        future_0 = module_2.Future()
        type_0 = None
        none_type_0 = None
        tuple_0 = None
        tuple_1 = (type_0, none_type_0, tuple_0)
        module_0.future_set_exc_info(future_0, tuple_1)
    except BaseException:
        pass

def test_case_4():
    try:
        future_0 = module_2.Future()
        str_0 = 'Returns the time that ``self.absolute_path`` was last modified.\n\n        May be overridden in subclasses.  Should return a `~datetime.datetime`\n        object or None.\n\n        .. versionadded:: 3.1\n        '
        module_0.future_add_done_callback(future_0, str_0)
        var_0 = None
        module_0.future_set_result_unless_cancelled(future_0, var_0)
        str_1 = '6j\rQ'
        module_0.future_add_done_callback(future_0, str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        callable_0 = None
        dummy_executor_0 = module_0.DummyExecutor()
        future_0 = dummy_executor_0.submit(callable_0)
        tuple_0 = ()
        module_0.future_add_done_callback(future_0, tuple_0)
    except BaseException:
        pass

def test_case_6():
    try:
        future_0 = module_2.Future()
        bool_0 = True
        bytes_0 = b'\x9eZqO.\x84\xd1y\xa3\x03'
        list_0 = [future_0, bytes_0, future_0]
        dict_0 = {}
        dummy_executor_0 = module_0.DummyExecutor()
        future_1 = dummy_executor_0.submit(bytes_0, *list_0, **dict_0)
        module_0.future_set_result_unless_cancelled(future_0, bool_0)
        callable_0 = module_0.run_on_executor(*list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        future_0 = module_2.Future()
        tuple_0 = ()
        int_0 = -102
        module_0.future_set_result_unless_cancelled(future_0, int_0)
        str_0 = 'w'
        dict_0 = {str_0: tuple_0}
        list_0 = [dict_0, future_0]
        callable_0 = module_0.run_on_executor(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        future_0 = module_2.Future()
        list_0 = [future_0]
        callable_0 = module_0.run_on_executor(*list_0)
        dummy_executor_0 = module_0.DummyExecutor()
        future_1 = dummy_executor_0.submit(callable_0, *list_0)
        dummy_executor_1 = module_0.DummyExecutor()
        module_0.future_add_done_callback(future_0, dummy_executor_1)
        future_2 = module_3.Future()
    except BaseException:
        pass