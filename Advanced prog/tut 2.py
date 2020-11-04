class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.slots[carType - 1] >= 1:
            self.slots[carType - 1] -= 1
            return True
        else:
            return False


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.numList = []

    def addNum(self, num: int) -> None:
        self.numList.append(num)
        self.numList = sorted(self.numList)

    def findMedian(self) -> float:
        if len(self.numList) % 2 != 0:
            return float(self.numList[len(self.numList) // 2])
        elif len(self.numList) == 1:
            return self.numList[0]
        else:
            return (self.numList[(len(self.numList) // 2)-1]+self.numList[(len(self.numList) // 2)])/2
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

s = MedianFinder()


s.addNum(1)
# print(s.findMedian())
s.addNum(2)
print(s.findMedian())
s.addNum(3)
print(s.findMedian())