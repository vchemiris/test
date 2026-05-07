def calculate_discount(price, percent):
    return price - (price * percent / 100)

def test_calculate_discount():
    assert calculate_discount(100, 20) == 80