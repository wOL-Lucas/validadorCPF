class Cpf:
    def __init__(self, number: str)-> None:
        self.number = self._sanitize(number)


    def _sanitize(self,number: str):
        number = number.replace('.','').replace('/','').replace('-','')
        if len(number) != 11:
            raise Exception ("Invalid Object CPF number: Invalid CPF length")
        else:
            return number


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
            for num in self.Reversed()[delimeter:11]:
                total += int(num) * multiplier
                multiplier += 1

            rest = total % 11
            if rest < 2: digit = 0
            else: digit = 11 - rest

            digits += str(digit)
        
        return digits[::-1] == self.number[9:11]



class Cnpj:
    def __init__(self, number: str):
        self.number = self._sanitize(number)
        
    def _sanitize(self, number:str):
        number = number.replace('.','').replace('/','').replace('-','')
        if len(number) != 14:
            raise Exception('Invalid Object CNPJ number. Invalid CNPJ length')
        
        else:
            return number

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
        
        return digits == self.number[12:14]



def validate(numero: str) -> None:
    try:
        cpf = Cpf(numero)
        print(cpf.isValid())

    except Exception as e1:
        try:
            cnpj = Cnpj(numero)
            print(cnpj.isValid())

        except Exception as e2:
            print(e1,'\n\------------------- \n', e2)
