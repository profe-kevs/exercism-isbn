def is_valid(isbn):
    new_isbn = isbn.replace('-', '')
    acum = 0
    if not len(new_isbn) == 10:
        return False
    for index, d in enumerate(new_isbn):
        d_int = 0
        if(d.isnumeric()):
            d_int = int(d)
            acum = acum + (d_int * (10 - index))
        elif d == 'X' and index == len(new_isbn) - 1:
            d_int = 10
            acum = acum + (d_int * (10 - index))
        else:
            return False
    return (acum % 11) == 0