class MyClass (object):
    class_attribute ='world'
    def my_method (self, paraml):
        print('\nhello {}'.format(paraml))
        print ( ' The object: that called this method is : {}'.\
                format(str(self)))
        self. instance_attribute = paraml
           
my_instance = MyClass()
print ( "output of dir (my_instance):")
print (dir(my_instance))
my_instance.my_method( ' world' )	# adds the instance _attribute
print("Instance has new attribute with value:	{}".\
    format(my_instance.instance_attribute))
print("output of dir(my_instance):")
print (dir(my_instance))