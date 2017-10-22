class A:
    member = "this is a test."

    # def __init__(self):
    #     pass

    @classmethod
    def Print1(cls):
        print "print 1: ", cls.member

    def Print2(self):
        print "print 2: ", self.member

    @classmethod
    def Print3(paraTest):
        print "print 3: ", paraTest.member

    @classmethod
    def Print25(afa):
        print("afa",afa.member)

    @staticmethod
    def print4():
        print "hello"

    def Print5(a):
        print 'a'
a = A()
A.Print1()
a.Print1()
# A.Print2()
a.Print25()
a.Print2()
A.Print3()
a.Print3()
A.print4()
a.Print5()