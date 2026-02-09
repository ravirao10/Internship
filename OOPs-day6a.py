# Parent class
class Payment:
    def pay(self):
        print("Processing payment...")

# Child class GooglePay
class GooglePay(Payment):
    def pay(self):
        print("Payment completed using Google Pay")

# Child class PhonePe
class PhonePe(Payment):
    def pay(self):
        print("Payment completed using PhonePe")

# Child class CreditCard
class CreditCard(Payment):
    def pay(self):
        print("Payment completed using Credit Card")

# Creating objects
payment = Payment()
gpay = GooglePay()
phonepe = PhonePe()
card = CreditCard()

# Calling pay() method
payment.pay()
gpay.pay()
phonepe.pay()
card.pay()
