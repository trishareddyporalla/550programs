class A:

    def method(self):
        print("A class is defined")
        super().method()


class B:

    def method(self):
        print("B class is defined")
        super().method()


class C(A,B):

    def method(self):
        print("C class is defined")
        super().method()
obj=C()
obj.method()