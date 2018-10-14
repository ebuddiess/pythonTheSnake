from Operations import Operation
class SmartCalculator:

    def __init__(self,question):
        self.question = question;

    def show(self):
        print(self.question)

    def convert(self):
        self.question = str(self.question.lower())

    def operate(self):
        op = Operation();
        op.scan(self.question)




# main started
while(True):
    query = input("WHAT IS YOUR QUERY ?")
    if(query=='close') : print("Good Bye"); break ;
    sc = SmartCalculator(query);
    sc.convert()
    sc.operate()