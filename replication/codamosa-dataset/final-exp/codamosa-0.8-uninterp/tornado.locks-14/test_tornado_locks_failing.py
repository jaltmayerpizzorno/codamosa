# Automatically generated by Pynguin.
import tornado.locks as module_0
import builtins as module_1
import tornado.ioloop as module_2
import datetime as module_3

def test_case_0():
    try:
        lock_0 = module_0.Lock()
        lock_0.__aenter__()
        condition_0 = module_0.Condition()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -76
        semaphore_0 = module_0.Semaphore(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        lock_0 = module_0.Lock()
        str_0 = lock_0.__repr__()
        awaitable_0 = lock_0.acquire()
    except BaseException:
        pass

def test_case_3():
    try:
        semaphore_0 = module_0.Semaphore()
        semaphore_0.__enter__()
    except BaseException:
        pass

def test_case_4():
    try:
        lock_0 = module_0.Lock()
        lock_0.release()
    except BaseException:
        pass

def test_case_5():
    try:
        lock_0 = module_0.Lock()
        float_0 = 2537.0
        list_0 = [lock_0]
        base_exception_0 = module_1.BaseException(*list_0)
        lock_0.__aexit__(float_0, base_exception_0, lock_0)
        lock_0.__enter__()
    except BaseException:
        pass

def test_case_6():
    try:
        lock_0 = module_0.Lock()
        lock_0.__aenter__()
        semaphore_0 = module_0.Semaphore()
        semaphore_0.__aenter__()
        lock_1 = module_0.Lock()
        lock_1.__aenter__()
        optional_0 = None
        base_exception_0 = module_1.BaseException()
        bytes_0 = b'\xd5J\xf1Km\x91\xd2\xa8\xf3H\xdc;\xa19i}\x16(_\xf1'
        releasing_context_manager_0 = module_0._ReleasingContextManager(lock_1)
        releasing_context_manager_0.__exit__(optional_0, base_exception_0, bytes_0)
    except BaseException:
        pass

def test_case_7():
    try:
        event_0 = module_0.Event()
        event_0.set()
        lock_0 = module_0.Lock()
        str_0 = event_0.__repr__()
        event_1 = module_0.Event()
        event_1.clear()
        event_1.set()
        bool_0 = event_1.is_set()
        event_0.set()
        condition_0 = module_0.Condition()
    except BaseException:
        pass

def test_case_8():
    try:
        lock_0 = module_0.Lock()
        traceback_0 = None
        str_0 = lock_0.__repr__()
        bounded_semaphore_0 = module_0.BoundedSemaphore()
        lock_1 = module_0.Lock()
        event_0 = module_0.Event()
        none_type_0 = None
        lock_0.__exit__(none_type_0, event_0, traceback_0)
    except BaseException:
        pass

def test_case_9():
    try:
        event_0 = module_0.Event()
        bool_0 = event_0.is_set()
        semaphore_0 = module_0.Semaphore()
        str_0 = semaphore_0.__repr__()
        event_1 = module_0.Event()
        int_0 = -1554
        optional_0 = None
        condition_0 = None
        semaphore_0.__exit__(int_0, optional_0, condition_0)
    except BaseException:
        pass

def test_case_10():
    try:
        event_0 = module_0.Event()
        bool_0 = event_0.is_set()
        semaphore_0 = module_0.Semaphore()
        str_0 = semaphore_0.__repr__()
        semaphore_0.__aenter__()
        event_1 = module_0.Event()
        semaphore_0.release()
        event_1.set()
        releasing_context_manager_0 = module_0._ReleasingContextManager(event_1)
        i_o_loop_0 = module_2.IOLoop()
        dict_0 = {}
        base_exception_0 = module_1.BaseException(**dict_0)
        semaphore_0.__aexit__(i_o_loop_0, base_exception_0, bool_0)
        releasing_context_manager_0.__enter__()
        event_1.set()
        bytes_0 = b't'
        str_1 = 't'
        awaitable_0 = event_1.wait()
        list_0 = [bytes_0]
        str_2 = 'i|(ivYP.K4^AK~Y)[c!'
        dict_1 = {str_1: awaitable_0, str_1: list_0, str_2: event_1}
        timedelta_0 = module_3.timedelta(**dict_1)
    except BaseException:
        pass

def test_case_11():
    try:
        i_o_loop_0 = module_2.IOLoop()
        i_o_loop_1 = i_o_loop_0.instance()
        condition_0 = module_0.Condition()
        awaitable_0 = condition_0.wait()
        condition_0.notify_all()
        semaphore_0 = module_0.Semaphore()
        event_0 = module_0.Event()
        str_0 = semaphore_0.__repr__()
        semaphore_1 = module_0.Semaphore()
        semaphore_2 = module_0.Semaphore()
        timedelta_0 = module_3.timedelta()
        awaitable_1 = semaphore_2.acquire(timedelta_0)
        awaitable_2 = semaphore_2.acquire()
        bounded_semaphore_0 = module_0.BoundedSemaphore()
        lock_0 = module_0.Lock()
        condition_1 = module_0.Condition()
        event_1 = module_0.Event()
        dict_0 = None
        timedelta_1 = module_3.timedelta(**dict_0)
    except BaseException:
        pass

def test_case_12():
    try:
        optional_0 = None
        int_0 = 4267
        i_o_loop_0 = module_2.IOLoop()
        i_o_loop_1 = i_o_loop_0.instance()
        awaitable_0 = i_o_loop_1.run_in_executor(optional_0, int_0)
        list_0 = [awaitable_0, int_0, awaitable_0]
        releasing_context_manager_0 = module_0._ReleasingContextManager(list_0)
        condition_0 = module_0.Condition()
        awaitable_1 = condition_0.wait()
        condition_0.notify(int_0)
        condition_0.notify_all()
        semaphore_0 = module_0.Semaphore()
        event_0 = module_0.Event()
        float_0 = -5666.796477
        str_0 = semaphore_0.__repr__()
        semaphore_1 = module_0.Semaphore()
        semaphore_2 = module_0.Semaphore()
        awaitable_2 = semaphore_2.acquire()
        awaitable_3 = semaphore_2.acquire(float_0)
        bounded_semaphore_0 = module_0.BoundedSemaphore()
        condition_1 = module_0.Condition()
        condition_1.notify()
        lock_0 = module_0.Lock()
        condition_2 = module_0.Condition()
        event_1 = module_0.Event()
        awaitable_4 = event_0.wait()
        lock_1 = module_0.Lock()
        event_0.set()
        bounded_semaphore_0.release()
    except BaseException:
        pass

def test_case_13():
    try:
        optional_0 = None
        int_0 = 4267
        i_o_loop_0 = module_2.IOLoop()
        i_o_loop_1 = i_o_loop_0.instance()
        awaitable_0 = i_o_loop_1.run_in_executor(optional_0, int_0)
        list_0 = [awaitable_0, int_0, awaitable_0]
        releasing_context_manager_0 = module_0._ReleasingContextManager(list_0)
        condition_0 = module_0.Condition()
        awaitable_1 = condition_0.wait()
        condition_0.notify_all()
        semaphore_0 = module_0.Semaphore()
        event_0 = module_0.Event()
        float_0 = -5666.8
        str_0 = semaphore_0.__repr__()
        semaphore_1 = module_0.Semaphore()
        event_1 = module_0.Event()
        semaphore_2 = module_0.Semaphore()
        awaitable_2 = semaphore_2.acquire()
        awaitable_3 = semaphore_2.acquire(float_0)
        str_1 = semaphore_2.__repr__()
        bounded_semaphore_0 = module_0.BoundedSemaphore()
        semaphore_2.release()
        lock_0 = module_0.Lock()
        condition_1 = module_0.Condition()
        event_2 = module_0.Event()
        releasing_context_manager_1 = module_0._ReleasingContextManager(awaitable_2)
        awaitable_4 = event_0.wait()
        lock_1 = module_0.Lock()
        event_0.set()
        bounded_semaphore_0.release()
    except BaseException:
        pass

def test_case_14():
    try:
        optional_0 = None
        int_0 = 4267
        i_o_loop_0 = module_2.IOLoop()
        i_o_loop_1 = i_o_loop_0.instance()
        awaitable_0 = i_o_loop_1.run_in_executor(optional_0, int_0)
        list_0 = [awaitable_0, int_0, awaitable_0]
        releasing_context_manager_0 = module_0._ReleasingContextManager(list_0)
        condition_0 = module_0.Condition()
        awaitable_1 = condition_0.wait()
        condition_0.notify_all()
        semaphore_0 = module_0.Semaphore()
        event_0 = module_0.Event()
        float_0 = -5666.8
        str_0 = semaphore_0.__repr__()
        semaphore_1 = module_0.Semaphore()
        event_1 = module_0.Event()
        semaphore_2 = module_0.Semaphore()
        awaitable_2 = semaphore_2.acquire()
        awaitable_3 = semaphore_2.acquire(float_0)
        str_1 = semaphore_2.__repr__()
        bounded_semaphore_0 = module_0.BoundedSemaphore()
        semaphore_2.release()
        lock_0 = module_0.Lock()
        condition_1 = module_0.Condition()
        any_0 = i_o_loop_0.run_sync(condition_0)
    except BaseException:
        pass