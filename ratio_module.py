import pandas as pd
import numpy as np
import math

class lquidity_ratio:

    def current_ratio(self,current_asset, current_liability):
        self.current_asset = current_asset
        self.current_liability = current_liability
        
        result = current_asset/current_liability
        return result

