class PhoneNumber:
    def __init__(self, number):
        self.number=self.clean_number(number)
        self.numbercheck()
    def numbercheck(self):
        if len(self.number)<10:
            raise ValueError("must not be fewer than 10 digits")
        if len(self.number)==11 and self.number[0]!="1":
            raise ValueError("11 digits must start with 1")
        if len(self.number)>11:
            raise ValueError("must not be greater than 11 digits")
        if self.number[0]=="0":
            raise ValueError("area code cannot start with zero")
        if self.number[0]=="1":
            raise ValueError("area code cannot start with one")
        if self.number[3]=="0":
            raise ValueError("exchange code cannot start with zero")
        if self.number[3]=="1":
            raise ValueError("exchange code cannot start with one")
        
  
    def clean_number(self,number):
        cleared_number="".join(char for char in number if char.isdigit())
        if len(cleared_number)==11 and cleared_number[0]=="1":
            cleared_number=cleared_number[1:]
        else:
            for i in number:
                if i in ("@:!"):
                    raise ValueError("punctuations not permitted")
                if i.isalpha():
                    raise ValueError("letters not permitted")
        return cleared_number
    @property
    def area_code(self):
        return self.number[:3]
    def pretty(self):
        return "("+self.number[:3]+")-"+self.number[3:6]+"-"+self.number[6:]