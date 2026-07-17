import pandas as pd
import numpy as np
import math

class lquidity_ratio:

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
    
    def cash_ratio(cash,bank,marketable_securities,current_liability):
       cash_and_securities = cash +bank + marketable_securities
       current_liability = current_liability
       
       if current_liability == 0:
           raise ValueError("Current liability cannot be zero. \n")
       
       cr_result = round(cash_and_securities/current_liability,2)

       if cr_result < 0.5:
          print(f"Cash ratio is {cr_result:.2f}, indicating poor liquidity and potential difficulty meeting short-term obligations.")

       elif 0.5 <= cr_result < 1:
         print(f"Cash ratio is {cr_result:.2f}, indicating an acceptable liquidity position.")

       elif 1 <= cr_result <= 2:
         print(f"Cash ratio is {cr_result:.2f}, indicating a healthy and strong liquidity position.")

       else:
         print(f"Cash ratio is {cr_result:.2f}, indicating excess idle cash that could potentially be invested more efficiently.")
        
    
       return cr_result
    
class Solvency_ratio:

    def debt_to_equity_ratio(long_term_debt, shareholders_equity):

        if long_term_debt == 0:
           raise ValueError("Current liability cannot be zero. \n")
        
        if shareholders_equity == 0:
           raise ValueError("Shareholders' equity cannot be zero.")
        
        debt_to_equity = long_term_debt / shareholders_equity

        if debt_to_equity < 0.5:
            print(f"Debt-to-Equity ratio is {debt_to_equity:.2f}, indicating very low financial leverage. The company is financially conservative but may not be fully utilizing debt for growth.")

        elif 0.5 <= debt_to_equity < 1:
            print(f"Debt-to-Equity ratio is {debt_to_equity:.2f}, indicating a healthy and well-balanced capital structure.")

        elif 1 <= debt_to_equity <= 2:
            print(f"Debt-to-Equity ratio is {debt_to_equity:.2f}, indicating moderate financial leverage. The company should monitor its debt levels.")

        else:
            print(f"Debt-to-Equity ratio is {debt_to_equity:.2f}, indicating high financial leverage and increased financial risk.")

        return debt_to_equity

    def debt_ratio(total_debt, total_assets):
        debt_ratio = total_debt/total_assets
        if debt_ratio < 0.3:
         print(f"Debt ratio is {debt_ratio:.2f}, indicating low financial risk and a conservative financing strategy.")

        elif 0.3 <= debt_ratio < 0.6:
          print(f"Debt ratio is {debt_ratio:.2f}, indicating a healthy and balanced use of debt financing.")

        elif 0.6 <= debt_ratio <= 0.8:
          print(f"Debt ratio is {debt_ratio:.2f}, indicating moderately high debt. The company should monitor its leverage carefully.")

        else:
          print(f"Debt ratio is {debt_ratio:.2f}, indicating very high financial risk as a large proportion of assets are financed by debt.")
        
        return debt_ratio
    
    def interest_coverage_ratio(ebit,interest_expense):
       if interest_expense == 0:
        raise ValueError("Interest expense cannot be zero.")
       if interest_expense < 0:
         raise ValueError("Interest expense cannot be negative.")
       interest_coverage = ebit/interest_expense

       if interest_coverage < 1.5:
          print(f"Interest Coverage Ratio is {interest_coverage:.2f}, indicating poor debt-servicing ability. The company may struggle to meet its interest obligations.")

       elif 1.5 <= interest_coverage < 3:
         print(f"Interest Coverage Ratio is {interest_coverage:.2f}, indicating an acceptable ability to cover interest expenses, but with a limited margin of safety.")

       elif 3 <= interest_coverage <= 5:
        print(f"Interest Coverage Ratio is {interest_coverage:.2f}, indicating a healthy ability to comfortably meet interest obligations.")

       else:
        print(f"Interest Coverage Ratio is {interest_coverage:.2f}, indicating a very strong debt-servicing capacity with a substantial margin of safety.")

        
