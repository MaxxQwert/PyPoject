class NonPositiveError(BaseException):
    pass
class  PositiveList(list):
    def append(self, x):
        if x > 0:
            return super().append(x)
        else:
            raise NonPositiveError(str(x) + ' - Non A Positiv Numer')
#a = []
a = PositiveList()
a.append(-5)
