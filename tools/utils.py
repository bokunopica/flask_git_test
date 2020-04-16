def printWrapper(func):
    def wrapper():
        print("a")
        return wrapper()