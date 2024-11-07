# TODO Найдите количество книг, которое можно разместить на дискете
V = 1.44
Pages = 100
Str = 50
Symbols = 25
One_symbol = 4
Weight = (One_symbol * Symbols * Str * Pages) / (1024 * 1024)

Col = round(V // Weight)
print("Количество книг, помещающихся на дискету:", Col)
