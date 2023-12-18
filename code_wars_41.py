def wrap(value):
    object = value['value'] == "my_wrapped_string"
    return object

x = input()
print(wrap(x))