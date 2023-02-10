import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            nonlocal path
            function_call_time = str(datetime.datetime.now())
            f = open(path, 'a')
            f.write(f'{function_call_time}\n{old_function.__name__}\n')
            f.close()
            for i in args:
                f = open(path, 'a')
                f.write(f'{i}\n')
                f.close()
            for i_1 in kwargs.values():
                f = open(path, 'a')
                f.write(f'{i_1}\n')
                f.close()
            result = old_function(*args, **kwargs)
            f = open(path, 'a')
            f.write(f'{result}\n')
            f.close()
            return result
        return new_function

    return __logger
