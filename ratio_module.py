
class LiquidityRatio:
    @staticmethod
    def current_ratio(current_asset, current_liability):
        current_asset = current_asset
        current_liability = current_liability

        if current_liability == 0:
            raise ValueError("Current liability cannot be zero.\n")
        
        result = current_asset/current_liability

        if result < 1:
            print( f"current ratio is {result:.2f} which is way to very low and there are liquidity concerns \n" )

        elif 1 <= result < 2:
            print( f"current ratio is {result:.2f} which is high and and healthy \n" )

        elif 2 <= result < 3:
            print( f"current ratio is {result:.2f} which is high and strong but feisible to sustain long term \n" )

        else:
            print( f"current ratio is {result:.2f} which is very high indicating idle assets or inefficient use of working capital \n" )

        return result
    
    @staticmethod
    def quick_ratio(quick_asset, current_liability):
        quick_asset = quick_asset
        current_liability = current_liability
       
        if current_liability == 0:
             raise ValueError("Current liability cannot be zero. \n")

        qr_result = quick_asset/current_liability

        if qr_result >= 2:
            print( f"quick ratio is {qr_result:.2f}, meaning there is excess cash or receivables  \n " )

        elif 1 <= qr_result < 2:
            print( f"quick ratio is {qr_result:.2f} which is high and strong but feasible to sustain long term \n" )

        else:
            print( f"quick ratio is {qr_result:.2f} which is low and concerning \n" )

        return qr_result
    
    @staticmethod
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
    
class SolvencyRatio:
    
    @staticmethod
    def debt_to_equity_ratio(long_term_debt, shareholders_equity):
        
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

    @staticmethod
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
    
    @staticmethod
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
      
       return interest_coverage
    
    @staticmethod
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
    
    @staticmethod
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
    
class ProfitabilityRatio:
   
   @staticmethod
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
      
   @staticmethod
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
   
   @staticmethod
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
   
   @staticmethod
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
   
   @staticmethod
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
   
   @staticmethod 
   def return_on_asset(net_profit, total_assets):
     if total_assets == 0:
       raise ValueError("Total assets cannot be zero.")

     result = (net_profit / total_assets) * 100

     if result < 5:
       print(f"Return on Assets (ROA) is {result:.2f}%, indicating poor asset utilization. The company is generating relatively low profits from its assets.")

     elif 5 <= result < 10:
       print(f"Return on Assets (ROA) is {result:.2f}%, indicating satisfactory asset utilization with scope for improvement.")

     elif 10 <= result < 15:
       print(f"Return on Assets (ROA) is {result:.2f}%, indicating healthy profitability and efficient utilization of assets.")

     else:
       print(f"Return on Assets (ROA) is {result:.2f}%, indicating excellent asset utilization and strong profitability.")

     return result

class ActivityRatio:
  
  @staticmethod
  def inventory_turnover_ratio( cost_of_goods_sold, average_inventory):

    if average_inventory == 0:
        raise ValueError("Average inventory cannot be zero.")

    if average_inventory < 0:
        raise ValueError("Average inventory cannot be negative.")

    if cost_of_goods_sold < 0:
        raise ValueError("Cost of goods sold cannot be negative.")

    result = cost_of_goods_sold / average_inventory

    if result < 3:
        print(f"Inventory Turnover Ratio is {result:.2f}, indicating slow inventory movement. The company may be overstocking or experiencing weak sales.")

    elif 3 <= result < 6:
        print(f"Inventory Turnover Ratio is {result:.2f}, indicating satisfactory inventory management with a balanced turnover rate.")

    elif 6 <= result < 10:
        print(f"Inventory Turnover Ratio is {result:.2f}, indicating efficient inventory management and strong sales performance.")

    else:
        print(f"Inventory Turnover Ratio is {result:.2f}, indicating very high inventory turnover. While this reflects excellent sales efficiency, it may also suggest the risk of stock shortages if inventory levels are too low.")

    return result
  
  @staticmethod
  def debtors_turnover_ratio(net_credit_sales, average_trade_receivables):

    if average_trade_receivables == 0:
        raise ValueError("Average trade receivables cannot be zero.")

    if average_trade_receivables < 0:
        raise ValueError("Average trade receivables cannot be negative.")

    if net_credit_sales < 0:
        raise ValueError("Net credit sales cannot be negative.")

    result = net_credit_sales / average_trade_receivables

    if result < 5:
        print(f"Debtors Turnover Ratio is {result:.2f}, indicating slow collection of receivables. The company may have inefficient credit collection policies.")

    elif 5 <= result < 10:
        print(f"Debtors Turnover Ratio is {result:.2f}, indicating satisfactory collection efficiency and a healthy credit policy.")

    elif 10 <= result < 15:
        print(f"Debtors Turnover Ratio is {result:.2f}, indicating efficient collection of receivables and effective credit management.")

    else:
        print(f"Debtors Turnover Ratio is {result:.2f}, indicating excellent receivables management. However, an excessively high ratio may suggest overly strict credit policies that could limit sales.")

    return result
  
  @staticmethod
  def creditors_turnover_ratio(net_credit_purchases, average_trade_payables):

    if average_trade_payables == 0:
        raise ValueError("Average trade payables cannot be zero.")

    if average_trade_payables < 0:
        raise ValueError("Average trade payables cannot be negative.")

    if net_credit_purchases < 0:
        raise ValueError("Net credit purchases cannot be negative.")

    result = net_credit_purchases / average_trade_payables

    if result < 4:
        print(f"Creditors Turnover Ratio is {result:.2f}, indicating slow payment to suppliers. While this may improve short-term liquidity, consistently delayed payments could affect supplier relationships.")

    elif 4 <= result < 8:
        print(f"Creditors Turnover Ratio is {result:.2f}, indicating a balanced payment policy and healthy management of trade payables.")

    elif 8 <= result < 12:
        print(f"Creditors Turnover Ratio is {result:.2f}, indicating prompt payments to suppliers and efficient management of trade payables.")

    else:
        print(f"Creditors Turnover Ratio is {result:.2f}, indicating very rapid payment to suppliers. Although this reflects strong financial discipline, it may reduce the benefits of available trade credit.")

    return result
  
  @staticmethod
  def working_capital_turnover_ratio(net_sales, working_capital):

    if working_capital == 0:
        raise ValueError("Working capital cannot be zero.")

    if working_capital < 0:
        raise ValueError("Working capital cannot be negative.")

    if net_sales < 0:
        raise ValueError("Net sales cannot be negative.")

    result = net_sales / working_capital

    if result < 3:
        print(f"Working Capital Turnover Ratio is {result:.2f}, indicating inefficient utilization of working capital. The company may not be generating sufficient sales from its working capital.")

    elif 3 <= result < 6:
        print(f"Working Capital Turnover Ratio is {result:.2f}, indicating satisfactory utilization of working capital and a balanced operating performance.")

    elif 6 <= result < 10:
        print(f"Working Capital Turnover Ratio is {result:.2f}, indicating efficient utilization of working capital and strong operational efficiency.")

    else:
        print(f"Working Capital Turnover Ratio is {result:.2f}, indicating excellent utilization of working capital. However, an excessively high ratio may suggest insufficient working capital to support future operations.")

    return result
  
  @staticmethod
  def fixed_asset_turnover_ratio(net_sales, average_net_fixed_assets):

    if average_net_fixed_assets == 0:
        raise ValueError("Average net fixed assets cannot be zero.")

    if average_net_fixed_assets < 0:
        raise ValueError("Average net fixed assets cannot be negative.")

    if net_sales < 0:
        raise ValueError("Net sales cannot be negative.")

    result = net_sales / average_net_fixed_assets

    if result < 2:
        print(f"Fixed Asset Turnover Ratio is {result:.2f}, indicating poor utilization of fixed assets. The company may not be generating sufficient revenue from its investments in fixed assets.")

    elif 2 <= result < 5:
        print(f"Fixed Asset Turnover Ratio is {result:.2f}, indicating satisfactory utilization of fixed assets and efficient revenue generation.")

    elif 5 <= result < 8:
        print(f"Fixed Asset Turnover Ratio is {result:.2f}, indicating strong utilization of fixed assets and excellent operational efficiency.")

    else:
        print(f"Fixed Asset Turnover Ratio is {result:.2f}, indicating exceptional utilization of fixed assets. However, such a high ratio may indicate that the company is operating close to full capacity or may require additional capital investment.")

    return result
  
  @staticmethod
  def total_asset_turnover_ratio(net_sales, average_total_assets):

    if average_total_assets == 0:
        raise ValueError("Average total assets cannot be zero.")

    if average_total_assets < 0:
        raise ValueError("Average total assets cannot be negative.")

    if net_sales < 0:
        raise ValueError("Net sales cannot be negative.")

    result = net_sales / average_total_assets

    if result < 0.5:
        print(f"Total Asset Turnover Ratio is {result:.2f}, indicating poor asset utilization. The company is generating relatively low sales from its total assets.")

    elif 0.5 <= result < 1:
        print(f"Total Asset Turnover Ratio is {result:.2f}, indicating satisfactory asset utilization with room for improvement.")

    elif 1 <= result < 2:
        print(f"Total Asset Turnover Ratio is {result:.2f}, indicating efficient utilization of total assets and strong operational performance.")

    else:
        print(f"Total Asset Turnover Ratio is {result:.2f}, indicating excellent asset utilization. The company is generating a high level of sales from its asset base.")

    return result

class MarketCapitalisationRatio:
   
   @staticmethod
   def price_to_earnings_ratio(market_price_per_share, earnings_per_share):

    if earnings_per_share == 0:
        raise ValueError("Earnings per share cannot be zero.")

    if earnings_per_share < 0:
        raise ValueError("Earnings per share cannot be negative.")

    if market_price_per_share < 0:
        raise ValueError("Market price per share cannot be negative.")

    result = market_price_per_share / earnings_per_share

    if result < 10:
        print(f"Price-to-Earnings Ratio is {result:.2f}, indicating the stock may be undervalued or the market has low growth expectations.")

    elif 10 <= result < 20:
        print(f"Price-to-Earnings Ratio is {result:.2f}, indicating a fairly valued stock with healthy growth expectations.")

    elif 20 <= result < 30:
        print(f"Price-to-Earnings Ratio is {result:.2f}, indicating high investor confidence and strong future growth expectations.")

    else:
        print(f"Price-to-Earnings Ratio is {result:.2f}, indicating a very highly valued stock. Investors have strong growth expectations, but the stock may also be overvalued.")

    return result
   
   @staticmethod
   def price_to_book_ratio(market_price_per_share, book_value_per_share):

    if book_value_per_share == 0:
        raise ValueError("Book value per share cannot be zero.")

    if book_value_per_share < 0:
        raise ValueError("Book value per share cannot be negative.")

    if market_price_per_share < 0:
        raise ValueError("Market price per share cannot be negative.")

    result = market_price_per_share / book_value_per_share

    if result < 1:
        print(f"Price-to-Book Ratio is {result:.2f}, indicating the stock may be undervalued or that the market has concerns about the company's future prospects.")

    elif 1 <= result < 3:
        print(f"Price-to-Book Ratio is {result:.2f}, indicating a fairly valued stock with a healthy market valuation.")

    elif 3 <= result < 5:
        print(f"Price-to-Book Ratio is {result:.2f}, indicating a premium valuation. Investors expect strong future growth.")

    else:
        print(f"Price-to-Book Ratio is {result:.2f}, indicating a very high valuation. The stock may be significantly overvalued relative to its book value.")

    return result
   
   @staticmethod
   def dividend_yield_ratio(dividend_per_share, market_price_per_share):

    if market_price_per_share == 0:
        raise ValueError("Market price per share cannot be zero.")

    if dividend_per_share < 0:
        raise ValueError("Dividend per share cannot be negative.")

    if market_price_per_share < 0:
        raise ValueError("Market price per share cannot be negative.")

    result = (dividend_per_share / market_price_per_share) * 100

    if result < 2:
        print(f"Dividend Yield is {result:.2f}%, indicating a low dividend return. The company may be focusing on growth rather than distributing profits.")

    elif 2 <= result < 4:
        print(f"Dividend Yield is {result:.2f}%, indicating a healthy dividend return and a balanced dividend policy.")

    elif 4 <= result < 6:
        print(f"Dividend Yield is {result:.2f}%, indicating a strong dividend return, making the stock attractive for income-focused investors.")

    else:
        print(f"Dividend Yield is {result:.2f}%, indicating a very high dividend return. Investors should assess whether such dividends are sustainable over the long term.")

    return result
   
   @staticmethod
   def dividend_payout_ratio(dividend_per_share, earnings_per_share):

    if earnings_per_share == 0:
        raise ValueError("Earnings per share cannot be zero.")

    if dividend_per_share < 0:
        raise ValueError("Dividend per share cannot be negative.")

    if earnings_per_share < 0:
        raise ValueError("Earnings per share cannot be negative.")

    result = (dividend_per_share / earnings_per_share) * 100

    if result < 30:
        print(f"Dividend Payout Ratio is {result:.2f}%, indicating a conservative dividend policy. The company retains a large portion of its earnings for future growth.")

    elif 30 <= result < 60:
        print(f"Dividend Payout Ratio is {result:.2f}%, indicating a balanced dividend policy between rewarding shareholders and retaining earnings.")

    elif 60 <= result < 80:
        print(f"Dividend Payout Ratio is {result:.2f}%, indicating a generous dividend policy. The company distributes a significant portion of its earnings.")

    else:
        print(f"Dividend Payout Ratio is {result:.2f}%, indicating a very high payout ratio. The sustainability of future dividend payments should be evaluated carefully.")

    return result
   
   @staticmethod
   def earnings_per_share(net_profit, preference_dividends, weighted_average_equity_shares):

    if weighted_average_equity_shares == 0:
        raise ValueError("Weighted average number of equity shares cannot be zero.")

    if preference_dividends < 0:
        raise ValueError("Preference dividends cannot be negative.")

    if weighted_average_equity_shares < 0:
        raise ValueError("Weighted average number of equity shares cannot be negative.")

    result = (net_profit - preference_dividends) / weighted_average_equity_shares

    if result < 2:
        print(f"Earnings Per Share (EPS) is {result:.2f}, indicating relatively low earnings generated for each equity share.")

    elif 2 <= result < 5:
        print(f"Earnings Per Share (EPS) is {result:.2f}, indicating satisfactory earnings and stable profitability.")

    elif 5 <= result < 10:
        print(f"Earnings Per Share (EPS) is {result:.2f}, indicating strong profitability and healthy returns for shareholders.")

    else:
        print(f"Earnings Per Share (EPS) is {result:.2f}, indicating excellent earnings performance and significant value creation for shareholders.")

    return result
   
   @staticmethod
   def market_capitalization_to_sales_ratio(market_capitalization, annual_revenue):

    if annual_revenue == 0:
        raise ValueError("Annual revenue cannot be zero.")

    if market_capitalization < 0:
        raise ValueError("Market capitalization cannot be negative.")

    if annual_revenue < 0:
        raise ValueError("Annual revenue cannot be negative.")

    result = market_capitalization / annual_revenue

    if result < 1:
        print(f"Market Capitalization-to-Sales Ratio is {result:.2f}, indicating the company may be undervalued relative to its revenue.")

    elif 1 <= result < 3:
        print(f"Market Capitalization-to-Sales Ratio is {result:.2f}, indicating a fair market valuation relative to sales.")

    elif 3 <= result < 5:
        print(f"Market Capitalization-to-Sales Ratio is {result:.2f}, indicating a premium valuation with strong investor growth expectations.")

    else:
        print(f"Market Capitalization-to-Sales Ratio is {result:.2f}, indicating a very high market valuation relative to sales. Investors should assess whether the valuation is justified by future growth prospects.")

    return result
   



      