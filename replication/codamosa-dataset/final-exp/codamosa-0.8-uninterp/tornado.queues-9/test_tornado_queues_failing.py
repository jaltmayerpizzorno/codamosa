# Automatically generated by Pynguin.
import tornado.queues as module_0
import datetime as module_1

def test_case_0():
    try:
        str_0 = '.|-\x0bXdL~@I<b\r9'
        dict_0 = {str_0: str_0}
        queue_iterator_0 = module_0._QueueIterator(dict_0)
        awaitable_0 = queue_iterator_0.__anext__()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -2098
        lifo_queue_0 = module_0.LifoQueue(int_0)
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
        awaitable_0 = queue_0.join()
    except BaseException:
        pass

def test_case_6():
    try:
        queue_empty_0 = module_0.QueueEmpty()
        queue_full_0 = module_0.QueueFull()
        timedelta_0 = module_1.timedelta()
        queue_0 = module_0.Queue()
        var_0 = queue_0.__aiter__()
        queue_iterator_0 = module_0._QueueIterator(queue_0)
        bool_0 = queue_0.full()
        var_1 = queue_0.get_nowait()
    except BaseException:
        pass

def test_case_7():
    try:
        priority_queue_0 = module_0.PriorityQueue()
        str_0 = 'Stops listening for new connections.\n\n        Requests currently in progress may still continue after the\n        server is stopped.\n        '
        str_1 = 'last_name'
        str_2 = 'Ff;0%s"zV?'
        dict_0 = {str_0: priority_queue_0, str_1: str_0, str_2: str_1}
        queue_full_0 = module_0.QueueFull(**dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        queue_0 = module_0.Queue()
        str_0 = queue_0.__str__()
        queue_1 = module_0.Queue()
        int_0 = queue_1.qsize()
        queue_1.put_nowait(int_0)
        int_1 = queue_1.qsize()
        var_0 = queue_1.get_nowait()
        queue_1.task_done()
        int_2 = queue_1.qsize()
        int_3 = 2
        list_0 = [int_0, int_2, int_3]
        queue_empty_0 = module_0.QueueEmpty(*list_0)
        queue_1.put_nowait(int_3)
        int_4 = queue_1.qsize()
        int_5 = None
        queue_2 = module_0.Queue(int_5)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 2
        queue_0 = module_0.Queue(int_0)
        var_0 = None
        queue_0.put_nowait(var_0)
        queue_0.task_done()
        int_1 = queue_0.qsize()
        future_0 = queue_0.put(var_0)
    except BaseException:
        pass

def test_case_10():
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

def test_case_11():
    try:
        queue_0 = module_0.Queue()
        int_0 = queue_0.qsize()
        bool_0 = queue_0.empty()
        bool_1 = queue_0.full()
        str_0 = queue_0.__str__()
        queue_full_0 = module_0.QueueFull()
        int_1 = 135
        queue_1 = module_0.Queue(int_1)
        var_0 = None
        queue_0.put_nowait(var_0)
        var_1 = queue_0.__aiter__()
        str_1 = queue_0.__str__()
        int_2 = -1885
        bool_2 = queue_0.full()
        queue_2 = module_0.Queue(int_2)
    except BaseException:
        pass

def test_case_12():
    try:
        queue_0 = module_0.Queue()
        str_0 = queue_0.__str__()
        queue_1 = module_0.Queue()
        int_0 = queue_1.qsize()
        int_1 = 1
        queue_1.put_nowait(int_1)
        int_2 = queue_1.qsize()
        queue_1.task_done()
        int_3 = queue_1.qsize()
        str_1 = queue_1.__str__()
        awaitable_0 = queue_0.join()
    except BaseException:
        pass