def outer_function():
    x=5
    def inner_function():
        nonlocal x
        x+=2

    inner_function()
    print(x)

outer_function()