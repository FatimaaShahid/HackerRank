class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self) :
        self.maximumDifference = 0
        for i in range(len(self.__elements)) :
            for j in range(i+1,len(self.__elements)) :
                a=self.__elements[i]
                b=self.__elements[j]
                self.maximumDifference = max(self.maximumDifference,abs(a-b))
        return self.maximumDifference


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)