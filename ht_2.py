class new_str(str):
    def is_repeatance(self, s):
        if type(s) != str:
            return False
        else:
            lin = len(s)
            lout = len(self)
            if lin == 0 or lout == 0:
                am = 1
            else:
                am = int(lout/lin)
            if self == s*am:
                return True
            else:
                return False

    def is_palindrom(self):
        if len(self) == 0:
            return True
        else:
            if self.lower() == self[::-1].lower():
                return True
            else:
                return False


a = new_str('abba')
print(a.is_repeatance('ab'))
print(a.is_palindrom())
