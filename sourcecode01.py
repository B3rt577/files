class Bitwise:
    '''
    Instantiation of Bitwise class is established. Note: '0' means FALSE and '1' is TRUE.
    I take only 2 parameters to just get the data from user. The 3 arrays are indvidually 
    used in the 3 functions: AND(), OR(), XOR().
    '''
    def __init__(self, param1, param2):
        self.param1= param1
        self.param2= param2
        self.arr1 = []
        self.arr2 = []
        self.arr3 = []
    '''
    AND function is established here. Its function is to make sure both bitwise string
    elements is equivalent to each other, otherwise default to string '0'.
    '''
    def AND(self):
        for i in range(len(self.param1)):
            if len(self.param1) == len(self.param2):
                if self.param1[i] == '0' and self.param2[i] == '0':
                    self.arr3.append('0')
                elif self.param1[i] == '1' and self.param2[i] == '1':
                    self.arr3.append('1')
                else:
                    self.arr3.append('0')
            else:
                return False
        return ' '.join(self.arr3)
    '''
    OR function is established here. Its function is to make both bitwise string elements
    that are TRUE or/and TRUE or FALSE or vice versa to equal the string '1'. If both 
    elements are FALSE, then it defaults to string '0'.
    '''
    def OR(self):
        for i in range(len(self.param1)):
            if len(self.param1) == len(self.param2):
                if self.param1[i] == '0' and self.param2[i] == '1':
                    self.arr1.append('1')
                elif self.param1[i] == '1' and self.param2[i] == '0':
                    self.arr1.append('1')
                elif self.param1[i] == '0' and self.param2[i] == '0':
                    self.arr1.append('0')
                elif self.param1[i] == '1' and self.param2[i] == '1':
                    self.arr1.append('1')
                else:
                    return False
            else:
                return False
        return ' '.join(self.arr1)
    '''
    XOR function is established here. Its function is to make both bitwise string elements
    that are TRUE or FALSE or vice versa to equal the string '1'. If both 
    elements are FALSE or TRUE, then it defaults to string '0'.      
    ''' 
    def XOR(self):
        for i in range(len(self.param1)):
            if len(self.param1) == len(self.param2):
                if self.param1[i] == '0' and self.param2[i] == '1':
                    self.arr2.append('1')
                elif self.param1[i] == '1' and self.param2[i] == '0':
                    self.arr2.append('1')
                elif self.param1[i] == '0' and self.param2[i] == '0':
                    self.arr2.append('0')
                elif self.param1[i] == '1' and self.param2[i] == '1':
                    self.arr2.append('0')
                else:
                    return False
            else:
                return False
        return ' '.join(self.arr2)
'''
As any python file that is made, we need a main function to get userinputs
and input parameters to the class, in this case we need to call the class Bitwise in main().   
''' 
def main():
    userin1 = list(input("Please input 1st bit string: "))
    userin2 = list(input("Please input 2st bit string: "))

    elems = Bitwise(userin1, userin2)

    print("the result of and:", elems.AND())
    print("the result of or:", elems.OR())
    print("the result of xor:", elems.XOR())

main()
