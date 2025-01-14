def introspection_info(obj):    
    type_of_object = type(obj) # Получение типа объекта.   
    attributes = dir(obj)  # Получение атрибутов объекта.    
    methods = [method for method in dir(obj) if callable(getattr(obj, method))] # Получение методов объекта.    
    module = getattr(obj, '__module__', None) # Получение модуля, к которому принадлежит объект.
    additional_info = {
        "str": lambda s: f"'{s}'",
        "int": lambda i: str(i),
        "float": lambda f: str(f)}

    return {
        "type": type_of_object.__name__,
        "attributes": attributes,
        "methods": methods,
        "module": module,
        **additional_info
    }

number_info = introspection_info(42)
print(number_info)
