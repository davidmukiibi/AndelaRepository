class BinarySearch(list):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super(BinarySearch,self).__init__()
        for x in range(1, a+1):
            self.append(x*b)
        self.length = len(self)  

    def search(self, value):
        count = 0
        first = 0
        last = len(self)-1
        midpoint = 0
        found = False
       
        try:
            if value == self[first]:
                found = True
                midpoint = first  
            elif value == self[last]:
                found = True
                midpoint = last
            elif value not in self:
                found = True
                midpoint = -1


            while first <= last and not found:
                midpoint = (first + last)//2
                if self[midpoint] == value:
                    found = True
                else:
                    if self[midpoint] > value:
                        last = midpoint -1
                        count += 1
                    else:
                        first = midpoint + 1
                        count += 1
           
            return {'count': count, 'index': midpoint}
        except:
            raise ValueError