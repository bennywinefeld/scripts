class Foo:
  def __init__(self, name):
    self.name = name
    print "\nCreated object ", self.name 
  def run(self, a):
    print "We're in function run() of class Foo"    
    return a+5
  def take(self, a):
    print "We're in function take() of class Foo"
    return self.run(a)
      
     
class Goo(Foo):
    def run(self, a):
        print "We're in function run() of class Goo"
        return a+8
      

a = Goo("inst_of_Goo")
print a.take(4)
            
b = Foo("inst_of_Foo")
print b.take(4)

Foo = Goo
c = Foo("new_inst_of_Foo")
print c.take(4)