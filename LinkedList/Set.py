def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False