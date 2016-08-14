from adaptor.turkey_package.turkey import Turkey


class WildTurkey(Turkey):
    
    def gobble(self):
        print("ゴロゴロ")
    
    def fly(self):
        print("短い距離を飛んでいます")
        
if __name__ == "__main__":
    obj = WildTurkey()
    obj.gobble()
    obj.fly()