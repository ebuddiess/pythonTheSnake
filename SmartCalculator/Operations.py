intent   =  ""
operator =  ""
operands = []
error  = 0 ;

addition = {
    "intent": ["addition", "add", "plus", "+","sum"]
}

subtract = {
    "intent": ["subtract", "minus", "reduce", "-"]
}

multiply = {
    "intent": ["multiply", "multiple", "*"]
}

division = {
    "intent": ["divide", "division", "/","by"]
}

class Operation:
    def scan(self,question):
     self.question = question
     self.calculate()

    def add(self):
        intent = addition.get("intent")
        for values in intent:
            if(str(self.question).__contains__(values)):
             return True;

    def multiply(self):
        intent = multiply.get("intent")
        for values in intent:
            if (str(self.question).__contains__(values)):
                return True;

    def subtract(self):
        intent = subtract.get("intent")
        for values in intent:
            if (str(self.question).__contains__(values)):
                return True;

    def divison(self):
        intent = division.get("intent")
        for values in intent:
            if (str(self.question).__contains__(values)):
                return True;

    def calculate(self):
        if(self.add()):
         self.string = str(self.question).split(" ")
         self.verify(self.string)
         self.sum = 0;
         for numbers in operands:
             self.sum +=numbers
         print(self.sum)  ; self.sum=0 ; operands.clear()

        elif(self.multiply()):
            self.string = str(self.question).split(" ")
            self.verify(self.string)
            self.multiple = 1;
            for numbers in operands:
                self.multiple *= numbers
            print(self.multiple) ;  self.multiple=0; operands.clear()

        elif (self.subtract()):
            self.string = str(self.question).split(" ")
            self.verify(self.string)
            if(len(operands)>2):
                print("More Than Two Operand Cannot Perform A Subtraction")
            else :
                print(operands[0]-operands[1]) ; operands.clear()
        elif(self.divison()):
            self.string = str(self.question).split(" ")
            self.verify(self.string)
            if (len(operands) > 2):
                print("More Than Two Operand Cannot Perform A Division")
            else:
                print(operands[0] / operands[1]) ; operands.clear()

    def verify(self,data):
        for values in data:
            if (values.isdigit()):
                operands.append(int(values))
            else:
                try:
                    if ((values.isdigit() == False) and (int(values))):
                        operands.append(int(values))
                except:
                    error = 1;