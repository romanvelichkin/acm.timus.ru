# 1402. Коктейли
# https://acm.timus.ru/problem.aspx?space=1&num=1402
# solved

drinks = int(input())
cocktails = 0

"""
Amount of combinations is calculated by multiplication of amount of possible digits on each position.
So if 'x' = {0, 9} - 10 possible digits, then 'xx' can have 10*10 combinations.

In this problem each ingredient can be met just once. So previous example 'xx' in this situation will
have 10*9 combinations. 
If we also limited in amount of ingredients - like 2 ingredients. In this case 'xx' example will have
2*1 combination.

We also have to include shorter combinations - with 3 ingredients we still can do 2 ingredients cocktails.

Ex:
3 drinks, means can be make cocktails with 3 ingredients and with 2 ingredients.
For 3 ing cocktails formula is 3*2*1 = 6
For 2 ing cocktails formula is 3*2 = 6
So with 3 drinks we can make 12 cocktails.
"""

# Cocktails can be made only from at least 2 ingredients.
# With only 1 drink we can't make cocktails
if drinks > 1:
    # First loop is over all possible lengths for given amount of drinks (ex: 3 drinks means 3 ing and 2 ing cocktails)
    for length in range(2, drinks+1):
        temp_drinks = drinks
        j_cocktails = 1
        # Count how many cocktails can be made with selected length (amount of ingredients)
        for j in range(length, 0, -1):
            j_cocktails *= temp_drinks
            temp_drinks -= 1
        cocktails += j_cocktails
print(cocktails)
