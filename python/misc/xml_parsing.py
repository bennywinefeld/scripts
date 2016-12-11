# XML parsing and storing to SQL
import xml.etree.ElementTree as ET

def simple_test():
  tree = ET.parse('/home/benny/testing/grpc/top.xml')
  root = tree.getroot()
  print root.tag
  for step in root:
    print step.tag, step.attrib
    for param in step:
      unit = ""
      param_name = param.tag
      for val_or_unit in param:      
        if val_or_unit.tag == 'value':
          value = val_or_unit.text
        elif val_or_unit.tag == 'unit':
          unit = val_or_unit.text
      print " ",param_name,"=",value,unit
      

if __name__ == '__main__':
  simple_test() 