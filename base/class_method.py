

class A:
    class_name = "a"

    def __init__(self, name):
        # self.class_name = name
        pass

    @staticmethod
    def stat():
        return "From static_method"

    @classmethod
    def class_method(cls, name):
        cls.class_name = name
        return f"Class name from classmethod = {cls.class_name}"

a = A("b")

print(A.class_name)

print(A.class_method("b"))

print(A.class_name)

