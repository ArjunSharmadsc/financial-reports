import pandas as pd
import numpy as np
import math

class lquidityratio:

    def current_ratio(self,current_asset, current_liability):
        self.current_asset = current_asset
        self.current_liability = current_liability

        if current_liability == 0:
            raise ValueError("Current liability cannot be zero.\n")
        
        result = self.current_asset/self.current_liability

        if result < 1:
            print( f"current ratio is {result:.2f} which is way to very low and there are liquidity concerns \n" )

        elif 1 <= result < 2:
            print( f"current ratio is {result:.2f} which is high and and healthy \n" )

        elif 2 <= result < 3:
            print( f"current ratio is {result:.2f} which is high and strong but feisible to sustain long term \n" )

        else:
            print( f"current ratio is {result:.2f} which is very high indicating idle assets or inefficient use of working capital \n" )

        return result
    
    def quick_ratio(self, quick_asset, current_liability):
        self.quick_asset = quick_asset
        self.current_liability = current_liability
       
        if current_liability == 0:
             raise ValueError("Current liability cannot be zero. \n")

        qr_result = self.quick_asset/ self.current_liability

        if qr_result >= 2:
            print( f"quick ratio is {qr_result:.2f}, meaning there is excess cash or receivables  \n " )

        elif 1 <= qr_result < 2:
            print( f"quick ratio is {qr_result:.2f} which is high and strong but feasible to sustain long term \n" )

        else:
            print( f"quick ratio is {qr_result:.2f} which is low and concerning \n" )

        return qr_result
    
    
    



