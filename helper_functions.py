def extract_date_to_decade(date_str):
    '''
    Extracts from a date string the decade
    '''
    date_split = date_str.split('-')
    year = ''
    for val in date_split:
        if(len(val) == 4):
            year = val
    year = int(year)
    return str(year - (year % 10))


def extract_date_to_year(date_str):
    '''
    Extracts from a date string the year
    '''
    date_split = date_str.split('-')
    year = ''
    for val in date_split:
        if(len(val) == 4):
            year = val
    return str(year)


data_dict = {   1942: {'England':4,'Wales':1,'France':3,'Spain':7},
                1944: {'England':5,'Wales':3,'France':3,'Spain':9},
                1945: {'England':8,'Wales':3,'France':9,'Spain':9},
            }
