import trader
import stock
import automatedTrading
import os
import time
import keyboard
import plotly.express as px

def clear_screen():
        # Verifica se o sistema operacional é Windows
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

def main():
    clear_screen()
    name = input("Bem-vindo! Por favor, digite seu nome: ")
    trader_user = trader.Trader(name)

    print(f"\nOlá, {trader_user.name}! Sua conta foi criada com sucesso.")
    time.sleep(3)

    while True:
        clear_screen()
        print("\nMenu Principal:")
        print("1. Visualizar Portfolio")
        print("2. Depositar Fundos")
        print("3. Retirar Fundos")
        print("4. Comprar Ações")
        print("5. Vender Ações")
        print("6. Exibir Histórico de Transações")
        print("7. Analisar Ação")
        print("8. Negociações Automaticas")
        print("9. Sair")

        choice = input("Por favor, selecione uma opção: ")

        if choice == '1':
            clear_screen()
            trader_user.displayPortfolio()
            trader_user.plotPortfolioPieChart()
        elif choice == '2':
            clear_screen()
            amount = float(input("Digite o valor que deseja depositar: "))
            trader_user.deposit(amount)
            print(f"Depósito de ${amount} realizado com sucesso.")
            time.sleep(3)
        elif choice == '3':
            clear_screen()
            amount = float(input("Digite o valor que deseja retirar: "))
            if  trader_user.withdraw(amount):
                print(f"Retirada de ${amount} realizada com sucesso.")
            time.sleep(3)
        elif choice == '4':
            clear_screen()
            symbol = input("Digite o símbolo da ação que deseja comprar: ")
            quantity = int(input("Digite a quantidade de ações que deseja comprar: "))
            if trader_user.buyStock(stock=stock.Stock(symbol=symbol), quantity=quantity):
                print("Ação comprada com sucesso.")
            time.sleep(3)
        elif choice == '5':
            clear_screen()
            symbol = input("Digite o símbolo da ação que deseja vender: ")
            quantity = int(input("Digite a quantidade de ações que deseja vender: "))
            if trader_user.sellStock(stock.Stock(symbol=symbol), quantity=quantity):
                print("Ação vendida com sucesso.")
            time.sleep(3)
        elif choice == '6':
            clear_screen()
            print(trader_user.transaction_log.display_transactions())
            time.sleep(3)
        elif choice == '7':
            clear_screen()
            symbol = input("Digite o símbolo da ação que deseja analisar: ")
            df = px.data.stocks()
            fig = px.line(df, x='date', y=symbol)
            fig.show()
            time.sleep(3)
        elif choice == '8':
            clear_screen()
            symbol = input("Digite o símbolo da ação que deseja implementar a sua estratégia: ")
            quantity = int(input("Digite a quantidade de ações que deseja negociar: "))
            stock_aapl = stock.Stock(symbol)

            clear_screen()
            print("\nEscolha qual estratégia implementar: ")
            print("1. Implementação Concreta para Média Móvel Simples (SMA)")
            print("2. Implementação Concreta para Índice de Força Relativa (RSI)")

            choice = input("Por favor, selecione uma opção: ")

            if choice == '1':
                while True:
                    if keyboard.is_pressed('q'):
                        print("Tecla 'q' pressionada. Encerrando o loop.")
                        break
                    strategy_a = automatedTrading.SimpleMovingAverageStrategy(stock_aapl, trader_user, quantity)
                    trading_strategy_a = automatedTrading.TradingStrategy(strategy_a)
                    trading_strategy_a.execute()
                    time.sleep(3)
            elif choice == '2':
                while True:
                    if keyboard.is_pressed('q'):
                        print("Tecla 'q' pressionada. Encerrando o loop.")
                        break
                    strategy_b = automatedTrading.RelativeStrengthIndexStrategy(stock_aapl, trader_user, quantity)
                    trading_strategy_b = automatedTrading.TradingStrategy(strategy_b)
                    trading_strategy_b.execute()
                    time.sleep(3)
            else:
                clear_screen()
                print("Opção inválida. Por favor, selecione novamente.")
                time.sleep(3)
            time.sleep(3)
        elif choice == '9':
            clear_screen()
            print("Obrigado por usar nosso sistema. Até mais!")
            time.sleep(3)
            clear_screen()
            break
        else:
            clear_screen()
            print("Opção inválida. Por favor, selecione novamente.")
            time.sleep(3)

if __name__ == "__main__":
    main()