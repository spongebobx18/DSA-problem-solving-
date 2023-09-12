class DataStream:


    def __init__(self, value: int, k: int):
        self.k=k
        self.val=value
        self.n=0
        

        

    def consec(self, num: int) -> bool:
        if num==self.val:
            self.n+=1
        else:
            self.n=0
        if self.n>=self.k:
            return True
        else:
            return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)