class Student(object):
    def __init__(self, first= ' ' , last= '', id=0 ):

        self.first_name_str = first
        self.last_name_str = last
        self.id_int = id

    def update(self, first='', last='', id=0):
        if first:
            self.first_name_str = first
        if last:
            self.last_name_str = last
        if id:
            self.id_int =id
    def __str__(self):
#	print "In__str__method"
        return "{} {} ID:{}".\
            format (self.first_name_str, self. last_name_str, self.id_int)

name= Student('dahua', 'li',2)

print(name.__str__())