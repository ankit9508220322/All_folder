import pandas as pd

data = pd.read_csv('simple.csv', encoding='latin-1')
Api_data = list(set(list(data['City'].drop_duplicates())))

final={
    'Api_data':Api_data
}
print(final)


# def city_api():
#     city_name = list(set(list(data['City'])))
#     city_dict = {
#         'city_name': city_name,
#     }
#     return city_dict