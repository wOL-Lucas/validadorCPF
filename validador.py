class Cpf:
    def __init__(self, number):
        self.number = str(number).replace('.','').replace('-','')
        if len(self.number) != 11:
            raise Exception ("Invalid Object CPF number. Len needs to be == 11")

    def asList(self) -> list:
        self.values = []
        for algarism in self.number:
            self.values.append(algarism)

        return self.values
    
    def Reversed(self) -> list:
        self.values = self.asList()
        self.values.reverse()
        return self.values

    def isValid(self) -> bool:
        digits = ""
        i = 0
        while i < 2:
            i+=1
            delimeter = 2
            if i == 1: delimeter = 1
            
            multiplier = 2
            total = 0
            for number in self.Reversed()[delimeter:11]:
                total += int(number) * multiplier
                multiplier += 1

            rest = total % 11
            if rest < 2: digit = 0
            else: digit = 11 - rest

            digits += str(digit)
            digits = digits[::-1]
        
        if digits == self.number[9:11]:
            return True

        return False




cpf = Cpf('11502981971')
print(cpf.isValid())
