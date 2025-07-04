def function():
    global message
    message = "local variable"
    print(message)

function()
# message = "hello"
print(message)