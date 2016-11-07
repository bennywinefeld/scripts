class Foo:
  def __init__(self, name):
    self.name = name
    print "\nCreated object ", self.name 
  def run(self, a):
    print "We're in function run() of class Foo"    
    return a+5
  def take(self, a):
    print "We're in function take() of class Foo"
    # Now launch function run. If it was an instance of Goo (subclass)
    # then we'll actually invoke run() of Goo  
    return self.run(a)
      
# Goo is a subclass of Foo     
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