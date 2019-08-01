class H2O:
    def __init__(self):
        self.H = 0
        self.O = 0
        self.fx = {} 

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        
        self.H += 1
        if "H" not in self.fx:
            self.fx["H"] = releaseHydrogen
        self.sync()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.O += 1
        if "O" not in self.fx:
            self.fx["O"] = releaseOxygen
        self.sync()
        
    def sync(self):
        if self.H > 1 and self.O > 0:
            self.fx["H"]()
            self.fx["H"]()
            self.fx["O"]()
            self.H = 0 if self.H - 2 < 0 else self.H - 2
            self.O = 0 if self.O - 1 < 0 else self.O - 1
            
     # 52 ms, 95.65%
