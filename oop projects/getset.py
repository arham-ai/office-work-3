class myclass:
    def _init_(self,value):
        self._value=value

    def show(self):
        print(f"value is(self._value)")
    @property
    def value(self):
        return self.value 
obj= myclass(10)
print(obj._value)
obj.show()