class Payment:
    def __init__(self, amount):
        self.amount = amount

    def valid(self):
        return self.amount > 0

class Coupon(Payment):
    def __init__(self, amount, expiration):
        super().__init__(amount)
        self.expiration = expiration

    def valid(self):
        return super().valid() and not self.expiration

class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number
    def valid(self):
        return super().valid() and len(str(self.card_number)) == 16

class OnlinePayment(Payment):



print(payment.amount)
coupon = Coupon(10,False)
print(coupon.valid())
credit_card = CardPayment(10, 1234567891236549)
print(credit_card.valid())