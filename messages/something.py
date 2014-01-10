

class A(object):

    def __init__(self):
        self.lala = 'cake'



class B(A):
    pass


class C(B):

    def hello(self):
        print self.lala