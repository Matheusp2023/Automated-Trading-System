# Risk Management Tools: Tools to assess and manage the risk exposure of investments
# author: Matheus Pedro

import main
import portifolioManagement
import numpy as np
import time

class RiskManagementTools:
    def __init__(self, investment_amount):
        self.investment_amount = investment_amount

    def calculate_risk(self, volatility):
        risk = volatility * self.investment_amount
        return risk

    def manage_risk(self, risk_tolerance, volatility):
        main.clearPrompt()
        if self.calculate_risk(volatility) > risk_tolerance:
            print("Warning: Risk exposure exceeds tolerance. Consider adjusting your investment strategy.")
        else:
            print("Risk exposure within tolerance.")
        time.sleep(3)

def calculate_volatility(returns):
    if len(returns) < 2:
        raise ValueError("The list of returns must have at least two elements to calculate volatility.")

    # Calculate daily logarithmic returns
    log_returns = np.log(1 + np.array(returns))

    # Calculates volatility as the standard deviation of logarithmic returns
    volatility = np.std(log_returns, axis=0)

    return volatility

def riskManagementToolsFuctionality():
    investment_amount = portifolioManagement.Portfolio().calculate_portfolio_value()
    volatility = portifolioManagement.Portfolio().calculate_portfolio_volatility()
    risk_tolerance = float(input("Enter the risk tolerance: "))

    risk_manager = RiskManagementTools(investment_amount)
    risk_manager.manage_risk(risk_tolerance, volatility)