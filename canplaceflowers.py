class Solution:
    def canPlaceFlowers(self, flowerbed: [int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]

        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i+1] == flowerbed[i] == 0:
                flowerbed[i] = 1
                if n > 0:
                    n -= 1

        if n == 0:
            return True
        return False