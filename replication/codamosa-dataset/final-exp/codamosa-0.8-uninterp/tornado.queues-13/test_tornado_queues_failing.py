# Automatically generated by Pynguin.
import tornado.queues as module_0
import datetime as module_1

def test_case_0():
    try:
        var_0 = None
        queue_iterator_0 = module_0._QueueIterator(var_0)
        awaitable_0 = queue_iterator_0.__anext__()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -2992
        queue_full_0 = module_0.QueueFull()
        queue_0 = module_0.Queue(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        queue_0 = module_0.Queue()
        var_0 = queue_0.get_nowait()
    except BaseException:
        pass

def test_case_3():
    try:
        queue_0 = module_0.Queue()
        awaitable_0 = queue_0.get()
    except BaseException:
        pass

def test_case_4():
    try:
        queue_0 = module_0.Queue()
        queue_0.task_done()
    except BaseException:
        pass

def test_case_5():
    try:
        queue_0 = module_0.Queue()
        str_0 = queue_0.__str__()
        awaitable_0 = queue_0.join()
    except BaseException:
        pass

def test_case_6():
    try:
        queue_0 = module_0.Queue()
        var_0 = queue_0.__aiter__()
        list_0 = [var_0]
        queue_empty_0 = module_0.QueueEmpty(*list_0)
        int_0 = None
        priority_queue_0 = module_0.PriorityQueue(int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        queue_0 = module_0.Queue()
        bool_0 = queue_0.full()
        lifo_queue_0 = module_0.LifoQueue()
        queue_1 = module_0.Queue()
        str_0 = queue_1.__repr__()
        queue_2 = module_0.Queue()
        timedelta_0 = None
        list_0 = [timedelta_0]
        dict_0 = {}
        queue_empty_0 = module_0.QueueEmpty(*list_0, **dict_0)
        var_0 = None
        future_0 = queue_0.put(var_0)
    except BaseException:
        pass

def test_case_8():
    try:
        queue_0 = module_0.Queue()
        str_0 = queue_0.__str__()
        bool_0 = queue_0.full()
        var_0 = None
        queue_0.put_nowait(var_0)
        str_1 = queue_0.__str__()
        var_1 = queue_0.__aiter__()
        var_2 = queue_0.get_nowait()
        awaitable_0 = queue_0.join()
    except BaseException:
        pass

def test_case_9():
    try:
        queue_0 = module_0.Queue()
        str_0 = queue_0.__str__()
        int_0 = 100
        var_0 = None
        queue_0.put_nowait(var_0)
        var_1 = queue_0.__aiter__()
        var_2 = queue_0.get_nowait()
        list_0 = []
        str_1 = 'NB|.hKX]2e~Y\r\x0cd8kl'
        timedelta_0 = module_1.timedelta(*list_0)
        lifo_queue_0 = module_0.LifoQueue()
        var_3 = None
        queue_iterator_0 = module_0._QueueIterator(var_3)
        bool_0 = queue_0.full()
        var_4 = queue_0.__aiter__()
        str_2 = queue_0.__repr__()
        dict_0 = {str_1: int_0, str_0: lifo_queue_0}
        queue_empty_0 = module_0.QueueEmpty(**dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        queue_0 = module_0.Queue()
        str_0 = queue_0.__str__()
        bool_0 = queue_0.full()
        bool_1 = queue_0.full()
        int_0 = 100
        var_0 = None
        queue_0.put_nowait(var_0)
        queue_0.put_nowait(var_0)
        queue_0.task_done()
        priority_queue_0 = module_0.PriorityQueue(int_0)
        queue_0.put_nowait(var_0)
        bool_2 = queue_0.empty()
        var_1 = queue_0.__aiter__()
        var_2 = queue_0.get_nowait()
        list_0 = []
        str_1 = '  \tgg4?(:5}H*NJP'
        str_2 = 'NB|.hKX]2e~Y\r\x0cd8kl'
        timedelta_0 = module_1.timedelta(*list_0)
        dict_0 = {str_1: bool_1, str_2: timedelta_0}
        queue_empty_0 = module_0.QueueEmpty(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = 2
        queue_0 = module_0.Queue(int_0)
        int_1 = 1
        queue_0.put_nowait(int_1)
        queue_0.put_nowait(int_0)
        int_2 = 3
        queue_0.put_nowait(int_2)
    except BaseException:
        pass