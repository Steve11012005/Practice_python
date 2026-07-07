from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    def verify_payment(self, payment_id):
        return f"Verifying payment {payment_id}"


class Paystack(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing #{amount} payment via Paystack"

    def refund(self, amount):
        return f"Refunding #{amount} via Paystack"


class Flutterwave(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing #{amount} payment via Flutterwave"

    def refund(self, amount):
        return f"Refunding #{amount} via Flutterwave"


paystack = Paystack()
flutterwave = Flutterwave()
print(paystack.process_payment(5000))
print(flutterwave.process_payment(7500))
print(paystack.verify_payment("TXN123456"))
print(flutterwave.verify_payment("TXN789012"))
