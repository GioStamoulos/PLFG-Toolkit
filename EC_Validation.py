class EC_Validation:

    def __init__(self, EC):  
        self.EC = EC 

    def EC_check(self):
        try:
            EC = (self.EC).split('.')
            if len(EC)==4:
                if (int(EC[0])<=7 and int(EC[0])>=1):
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False