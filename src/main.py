# Automaded Trading System
# author: Matheus Pedro

import os
import time
import marketDataAnalysis
import tradingStrategyImplementation
import buySellOrderExecution
import portifolioManagement

def clearPrompt():
    operation_system = os.name

    if operation_system == 'posix': # Unix/Linux/MacOS
        os.system('clear')
    elif operation_system == 'nt': # Windows
        os.system('cls')
    else:
        print("Unable to determine operating system to clear prompt")

def main():
    while True:
        clearPrompt()

        print("------ Automated Trading System ------")
        print("1 - Real-time analysis of financial market data")
        print("2 - Implement and test trading strategies")
        print("3 - Buy/Sell Order Execution")
        print("4 - Portfolio Management")
        print("5 - Quit")

        option = input("Choose a feature: ")

        if option == '1':
            clearPrompt()
            marketDataAnalysis.realTimeAnalyis()
        elif option == '2':
            clearPrompt()
            tradingStrategyImplementation.implementTestTradingStrategies()
        elif option == '3':
            clearPrompt()
            buySellOrderExecution.buySellOrderExecutionFunctionality()
        elif option == '4':
            clearPrompt()
            portifolioManagement.portfolioManagementFunctionality()
        elif option == '5':
            clearPrompt()
            quit()
        else:
            clearPrompt()
            print("Just enter your option number!")
            time.sleep(3)

if __name__ == '__main__':
    main()