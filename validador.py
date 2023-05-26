class Cpf:
    def __init__(self, number)-> None:
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
        if self.number == "00000000000":
            return False

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


class Cnpj:
    def __init__(self, number):
        self.number = str(number).replace('.','').replace('/','').replace('-','')
        if len(number) != 14:
            raise Exception('Invalid Object CNPJ number. Len needs to be == 14')

    def asList(self) -> list:
        self.values = []
        for algarism in self.number:
            self.values.append(algarism)
        
        return self.values

    def isValid(self)-> bool:
        if self.number == "00000000000000":
            return False
        
        digits = ""
        i = 0
        while i < 2:
            i +=1
            delimeter = 13
            multiplier = 6
            if i == 1:
                multiplier = 5
                delimeter = 12

            total = 0
            for number in self.number[0:delimeter]:
                total  += int(number) * multiplier
                multiplier -= 1
                if multiplier == 1:
                    multiplier = 9
            
            rest = total % 11
            if rest < 2: digit = 0
            else: digit = 11 - rest

            digits += str(digit)
        
        if digits == self.number[12:14]:
            return True
        
        return False


def validate(numero) -> None:
    length = len(numero)
    if length == 11 or length == 14:
        
        if length == 11:
            cpf = Cpf(numero)
            print(cpf.isValid())
            return
        
        cnpj = Cnpj(numero)
        print(cnpj.isValid())
        
    else:
        raise Exception('Comprimento invalido.')