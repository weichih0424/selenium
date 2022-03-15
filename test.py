

class tvbs:
    def __init__(self,name):
        self.cname='tvbs'
        self.pname=name

    def printname(self):
        print(self.cname,self.pname)

eric = tvbs("eric")
eric.printname()
