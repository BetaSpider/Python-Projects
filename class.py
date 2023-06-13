class strq:
    def __init__(self):
        self.uc=0
        self.lc=0
        self.sp=0
        self.vow=0
        self.cons=0
        self.string=""
    def getstr(self):
        self.string=str(input("Enter the string"))
    def cuc(self):
        for ch in self.string:
            if (ch.isupper()):
                self.uc+=1
        print("The given string has\n")
        print("Uppercase",self.uc)
   
    def clc(self):
        for ch in self.string:
            if (ch.islower()):
                self.lc+=1
        print("Lowercase",self.lc)
    def csp(self):
        for ch in self.string:
            if ch==" ":
                self.sp+=1
        print("Space",self.sp)
    def cvow(self):
        for ch in self.string:
            if (ch in ('A','a','E','e','I','i','O','o','U','u')):
                self.vow+=1
        print("Vowels",self.vow)
    def ccons(self):
        for ch in self.string:
            if (ch not in ('A','a','E','e','I','i','O','o','U','u')):
                self.cons+=1
        print("Consonants",self.cons)
    def execute(self):
        self.cuc()
        self.clc()
        self.csp()
        self.cvow()
        self.ccons()
    
S=strq()
S.getstr()
S.execute()

    
