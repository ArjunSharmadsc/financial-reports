
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

    def proprietary_ratio(shareholders_equity, total_assets):
       
       if total_assets == 0:
        raise ValueError("Total assets cannot be zero.")
       if shareholders_equity < 0 or total_assets < 0:
        raise ValueError("Shareholders' funds and total assets cannot be negative.")
       
       proprietary_ratio = shareholders_equity/total_assets

       if proprietary_ratio < 0.30:
        print(f"Proprietary Ratio is {proprietary_ratio:.2f}, indicating a weak financial position with heavy dependence on external debt.")

       elif 0.30 <= proprietary_ratio < 0.50:
        print(f"Proprietary Ratio is {proprietary_ratio:.2f}, indicating a fair financial position with a balanced mix of debt and equity financing.")

       elif 0.50 <= proprietary_ratio <= 0.75:
        print(f"Proprietary Ratio is {proprietary_ratio:.2f}, indicating a healthy financial position with strong shareholders' support.")

       else:
        print(f"Proprietary Ratio is {proprietary_ratio:.2f}, indicating excellent financial stability and very low dependence on external debt.")

        return proprietary_ratio
    
    def capital_gearing_ratio(equity_shareholders_funds,fixed_interest_bearing_funds):
       if equity_shareholders_funds == 0:
          raise ValueError("Equity shareholders' funds cannot be zero.")
       if equity_shareholders_funds < 0:
           raise ValueError("Equity shareholders' funds cannot be negative.")
       
       capital_gearing = fixed_interest_bearing_funds/ equity_shareholders_funds
       
       if capital_gearing < 0.5:
         print(f"Capital Gearing Ratio is {capital_gearing:.2f}, indicating low gearing and a conservative capital structure with low financial risk.")

       elif 0.5 <= capital_gearing < 1:
         print(f"Capital Gearing Ratio is {capital_gearing:.2f}, indicating a balanced capital structure with moderate financial leverage.")

       elif 1 <= capital_gearing <= 2:
         print(f"Capital Gearing Ratio is {capital_gearing:.2f}, indicating high gearing. The company relies significantly on fixed-interest capital and should monitor its debt obligations.")

       else:
        print(f"Capital Gearing Ratio is {capital_gearing:.2f}, indicating very high gearing and increased financial risk due to heavy dependence on fixed-interest financing.")

        return capital_gearing
    
class profitability_ratio:
   
   def gross_profit_ratio(gross_profit,revenue):
      if revenue == 0:
        raise ValueError("Revenue cannot be zero.")
      
      result = (gross_profit / revenue) * 100

      if result < 20:
        print(f"Gross Profit Ratio is {result:.2f}%, indicating low profitability. The company may have high production or operating costs.")
      elif 20 <= result < 40:
       print(f"Gross Profit Ratio is {result:.2f}%, indicating a satisfactory profit margin and reasonable cost management.")
      elif 40 <= result < 60:
       print(f"Gross Profit Ratio is {result:.2f}%, indicating strong profitability and efficient cost control.")
      else:
       print(f"Gross Profit Ratio is {result:.2f}%, indicating excellent profitability. However, such a high margin should be evaluated in the context of the industry.")

       return result
      
   def net_profit_ratio(net_profit_after_tex, revenue):
      result = (net_profit_after_tex / revenue) * 100

      if revenue == 0:
       raise ValueError("Revenue cannot be zero.")

      if result < 5:
        print(f"Net Profit Ratio is {result:.2f}%, indicating low profitability. The company retains only a small portion of its revenue as profit.")

      elif 5 <= result < 10:
       print(f"Net Profit Ratio is {result:.2f}%, indicating satisfactory profitability with room for improvement.")

      elif 10 <= result < 20:
        print(f"Net Profit Ratio is {result:.2f}%, indicating healthy profitability and efficient overall business operations.")

      else:
        print(f"Net Profit Ratio is {result:.2f}%, indicating excellent profitability. The company is converting a significant portion of its revenue into net profit.")

      return result
   
   def operating_profit_ratio(operating_profit,revenue):
      if revenue == 0:
        raise ValueError("Revenue cannot be zero.")

      result = (operating_profit / revenue) * 100
 
      if result < 10:
       print(f"Operating Profit Ratio is {result:.2f}%, indicating low operating profitability. The company may have high operating expenses or inefficient cost management.")

      elif 10 <= result < 20:
       print(f"Operating Profit Ratio is {result:.2f}%, indicating satisfactory operating profitability with room for improvement.")

      elif 20 <= result < 30:
       print(f"Operating Profit Ratio is {result:.2f}%, indicating healthy operating profitability and efficient cost management.")

      else:
       print(f"Operating Profit Ratio is {result:.2f}%, indicating excellent operating profitability. The company is highly efficient in generating operating income from its revenue.")

      return result
   
   def return_on_captial_employeed(ebit,capital_employed):
      if capital_employed == 0:
        raise ValueError("Capital employed cannot be zero.")
      if capital_employed < 0:
        raise ValueError("Capital employed cannot be negative.")

      result = (ebit / capital_employed) * 100

      if result < 10:
        print(f"Return on Capital Employed (ROCE) is {result:.2f}%, indicating poor efficiency in generating profits from the capital employed.")

      elif 10 <= result < 15:
        print(f"Return on Capital Employed (ROCE) is {result:.2f}%, indicating satisfactory efficiency with room for improvement.")

      elif 15 <= result < 20:
        print(f"Return on Capital Employed (ROCE) is {result:.2f}%, indicating healthy profitability and efficient utilization of capital.")

      else:
        print(f"Return on Capital Employed (ROCE) is {result:.2f}%, indicating excellent capital efficiency and strong returns on invested capital.")

      return result
   
   def return_on_equity(net_profit,shareholders_equity):
     if shareholders_equity == 0:
        raise ValueError("Shareholders' equity cannot be zero.")
     if shareholders_equity < 0:
        raise ValueError("Shareholders' equity cannot be negative.")

     result = (net_profit / shareholders_equity) * 100

     if result < 10:
       print(f"Return on Equity (ROE) is {result:.2f}%, indicating low returns for shareholders. The company may not be utilizing shareholders' funds efficiently.")

     elif 10 <= result < 15:
       print(f"Return on Equity (ROE) is {result:.2f}%, indicating satisfactory returns with scope for improvement.")

     elif 15 <= result < 20:
       print(f"Return on Equity (ROE) is {result:.2f}%, indicating healthy returns and efficient utilization of shareholders' equity.")

     else:
       print(f"Return on Equity (ROE) is {result:.2f}%, indicating excellent returns for shareholders and strong financial performance.")

     return result
      

      



      