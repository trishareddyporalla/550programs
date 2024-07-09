class A:
    def method(self):
        print("A class is defined")

class B:
    def method(self):
        print("B class is defined")

class C(A, B):
    def method(self):
        print("C class")
        super().method()

obj = C()
obj.method()
