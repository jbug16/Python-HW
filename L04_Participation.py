
def get_inputs():
    return str.upper(input(f'Enter Q for quit or any other key to compute tax '))

def calculate_price_with_tax():
    price = float(input('What is the price '))
    tax = float(input('What is the tax rate? '))
    return price * (100 + tax) / 100

def add_mult(x, y):
    return x + y and x * y

done = False
while not done:
    sentinel = get_inputs()
    if sentinel == 'Q':
        done = True
        print(sentinel,done)
        continue
    else:
        print("Compute tax")
    print(f'The calculated price is {calculate_price_with_tax()}')
    print(add_mult(10, 20))