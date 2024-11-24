budget = float(input())
season = input()

CONFIRM_TEXT = 'Somewhere in {} \r {Вид почивка} - {Похарчена сума}'

booking = {
    (0.00, 100.00) : {
        ('summer', 'winter', 'Bulgaria') : (('Camp',0.30), ('Hotel', 0.70))
    },
    (101.00, 1000.00): {
        ('summer', 'winter', 'Balkans'): (('Camp',0.40), ('Hotel', 0.80))
    },
    (1001.00, float('inf')) : {
        ('summer', 'winter', 'Europe'): (('Hotel',0.90), ('Hotel', 0.90))
    }
}


destination = ''
journey_type = ''
discount = 0
diff = 0

for x in booking.items():
    if x[0][0] < budget <= x[0][1]:
        for y in x[1].items():
            if season == y[0][0]:
                destination = y[0][2]
                journey_type = y[1][0][0]
                discount = y[1][0][1]
            elif season == y[0][1]:
                destination = y[0][2]
                journey_type = y[1][1][0]
                discount = y[1][1][1]









cost = budget * discount
print(f'Somewhere in {destination} \r\n{journey_type} - {cost:.2f}')