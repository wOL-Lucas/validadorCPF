

def verifierDigitCalculator(cpf,secondDigit):

        if len(cpf) != 11 and secondDigit == False:
            raise Exception('CPF não é válido')
        
        elif len(cpf) != 11 and secondDigit == True or len(cpf) == 11:
            
            if secondDigit == True:
                 cpf = cpf[0:10]
            else:
                 cpf = cpf[0:9]

            i = 2
            validint = 0
            nums = []
            for number in cpf:
                nums.append(number)
            
            nums.reverse()
            for num in nums:
                validint += int(num) * i
                i+=1

            divisionRest = validint % 11
            dr = divisionRest
            if dr >= 2:
                dr = 11 - divisionRest
            else:
                dr = 0

            return cpf + str(dr)
        else:
             raise Exception('CPF não é válido')


def cpfvalidator(cpf):
    rcpf = cpf.replace('.','').replace('-','')
    cpf = rcpf
    
    cpfWFDigit = verifierDigitCalculator(cpf,False)
    cpfWSDigit = verifierDigitCalculator(cpfWFDigit,True)

    if cpf == cpfWSDigit:
        return True
    
if cpfvalidator('11502981971') == True:     
     print('CPF VÁLIDO')

else:
     print('CPF INVÁLIDO')
