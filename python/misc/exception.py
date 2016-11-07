file = "testfile"
try:    
    print "Trying to open " + file    
    fh = open(file, "w")    
    print "If you see this line, file opened correctly"
except IOError:    
    print "Executing exception"
finally:   
    print "Executing finally clause"