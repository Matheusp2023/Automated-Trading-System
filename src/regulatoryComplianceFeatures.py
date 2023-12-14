# Regulatory Compliance Features: Ensuring compliance with financial regulations
# author: Matheus Pedro

import time

def check_compliance(transaction_value, compliance_limit):
    """
    Checks if a transaction complies with financial regulations.

    Parameters:
    - transaction_value (float): The value of the transaction.
    - compliance_limit (float): The maximum limit allowed by regulation.

    Returns:
    - compliance (bool): True if the transaction is compliant, False otherwise.
    """
    compliance = transaction_value <= compliance_limit
    return compliance

def regulatoryComplianceFeaturesFunctionalities():
    regulatory_compliance_limit = 1000000.00
    print("Transaction limit is US$1,000,000")

    # Transaction
    transaction_value = float(input("Enter the amount of your transaction: "))
    compliance = check_compliance(transaction_value, regulatory_compliance_limit)
    print(f"Is Transaction compliant? {compliance}")

    time.sleep(3)
