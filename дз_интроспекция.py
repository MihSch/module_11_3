import inspect


def introspection_info(obj):
    return (f'\ntype: {type(obj).__name__}, '
            f'\nattributes and methods: {dir(obj)},'
            f' \nmodule: {inspect.getmodule(obj)}')


number_info = introspection_info(42)
print(number_info)
