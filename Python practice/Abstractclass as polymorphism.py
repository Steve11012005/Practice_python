from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund(self, transaction_id, amount):
        pass

    @abstractmethod
    def get_transaction_status(self, transaction_id):
        pass


class PaystackProcessor(PaymentProcessor):
    def __init__(self, api_key):
        self.api_key = api_key
        self.provider = "Paystack"

    def process_payment(self, amount):
        # Implementation would use Paystack API
        transaction_id = "PS-" + str(hash(f"{amount} - {self.api_key}"))[:8]
        return f"Processing #{amount:,} via {self.provider}, Transaction ID: {transaction_id}"

    def refund(self, transaction_id, amount):
        return f"Refunding #{amount:,} for transaction {transaction_id} via {self.provider}"

    def get_transaction_status(self, transaction_id):
        return f"Transaction {transaction_id} status: Completed"


class FlutterwaveProcessor(PaymentProcessor):
    def __init__(self, merchant_id):
        self.merchant_id = merchant_id
        self.provider = "Flutterwave"

    def process_payment(self, amount):
        # Implementation would use Flutterwave API
        transaction_id = "FW-" + \
            str(hash(f"{amount} - {self.merchant_id}"))[:8]
        return f"Processing #{amount:,} via {self.provider}.Transaction ID: {transaction_id}"

    def refund(self, transaction_id, amount):
        return f"Refunding #{amount:,} for transaction {transaction_id} via {self.provider}"

    def get_transaction_status(self, transaction_id):
        return f"Transaction {transaction_id} status: Successful"


class CashPaymentProcessor(PaymentProcessor):
    def __init__(self):
        self.provider = "Cash"

    def process_payment(self, amount):
        transaction_id = "CASH-" + str(hash(str(amount)))[:8]
        return f"Collecting #{amount:,}nin cash.Receipt ID: {transaction_id}"

    def refund(self, transaction_id, amount):
        return f"Returning #{amount:,} cash for receipt {transaction_id}"

    def get_transaction_status(self, transaction_id):
        return f"Cash transaction {transaction_id} status: Completed"
# Function that uses polymorphism via the abstract interface


def process_order(payment_processor, order_amount):
    print(f"Order Amount: #(order_amount:,)")
    transaction_result = payment_processor.process_payment(order_amount)
    print(transaction_result)

    # Extract transaction ID(this is a simplication)
    transaction_id = transaction_result.split("Transaction ID:")[-1]
    if "Receipt ID:" in transaction_id:
        transaction_id = transaction_id.split("Receipt ID:")[-1]

    # Check Status
    print(payment_processor.get_transaction_status(transaction_id))
    print("-" * 40)
    return transaction_id


# Create diiferent payment processors
paystack = PaystackProcessor("sk_test_123456789")
flutterwave = FlutterwaveProcessor("654321")
cash = CashPaymentProcessor()
# Process orders with different payment methods
transactions = [
    process_order(paystack, 25000),
    process_order(flutterwave, 37500),
    process_order(cash, 15000)
]
# Process a refund
print("Processing a refund:")
print(paystack.refund(transactions[0], 25000))
