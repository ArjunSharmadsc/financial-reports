import pandas as pd
import numpy as np
import math

class lquidity_ratio:

    def current_ratio(self,current_asset, current_liability):
        self.current_asset = current_asset
        self.current_liability = current_liability
        
        result = self.current_asset/self.current_liability

        if result >= 3:
            print( f"current ratio is {result} which is way to high and strong" )

        elif result < 3 and result > 2:
            print( f"current ratio is {result} which is high and strong but feisible to sustain long term" )

        else:
            print( f"current ratio is {result} which is low and concerning" )

        return result
    
    def quick_ratio(self, quick_asset, current_liability):
        self.quick_asset = quick_asset
        self.current_liability = current_liability

        qr_result = self.quick_asset/ self.current_liability

        if qr_result >= 1:
            print( f"current ratio is {qr_result} which is way to high and strong" )

        elif qr_result < 1 and qr_result > 0 :
            print( f"current ratio is {qr_result} which is high and strong but feisible to sustain long term" )

        else:
            print( f"current ratio is {qr_result} which is low and concerning" )

        return qr_result
    
    
    



