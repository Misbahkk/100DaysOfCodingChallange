import pandas as pd 


car_df = pd.read_csv(r"practice on youtube vedio\cars.csv",encoding="latin-1")
print(car_df.head())

print(car_df.columns)
#  ##perfoerm the operation on Brand column
print(car_df['brand'])
#find the top brand
selling_propotional = car_df["brand"].value_counts(normalize=True)
# #filter the brand that sell grater than 0.05%
selling_bol = selling_propotional > 0.05
top_brand = selling_propotional[selling_bol]
brand_name = top_brand.index
top_selling_brand = car_df[car_df['brand'].isin(brand_name)].copy()

print(top_selling_brand)

# #clean the price column
top_selling_brand['price']=top_selling_brand['price'].str.replace('$','').str.replace(',','').astype(int)
print(top_selling_brand['price'])

# clean the odometer column
top_selling_brand['odometer'] = top_selling_brand['odometer'].str.replace(",","").str.replace("km",'').astype(int)
print(top_selling_brand['odometer'])

top_selling_brand.rename({'odometer':'odometer (km)','price':'price ($)'},axis=1,inplace=True)
print(top_selling_brand.columns)

# Gropping the brand
groupping = top_selling_brand.groupby('brand')
brand_mean = groupping[['price ($)','odometer (km)']].mean().sort_values('price ($)')

# In data we have very abnormal values in prive like $0 sell the 900 cars thst is imposible 
# and very hight amoint to buy the car so we filter it maximum and minimum
# top_selling_brand['price ($)'].sort_values()
print(top_selling_brand['price ($)'].value_counts().sort_index())
normal_bol = top_selling_brand['price ($)'].between(1,350000)
normal_data = top_selling_brand[normal_bol]
print(normal_data['price ($)'])

# Gropping the brand
groupping = normal_data.groupby('brand')
brand_mean = groupping[['price ($)','odometer (km)']].mean().sort_values('price ($)')
print(brand_mean)


# clean and filter the year of registration
# In our data we have those car that register on 10000 but in this year cars no com
# and the data is also futers years so we fikter it 2016 data 
print(top_selling_brand['yearOfRegistration'].value_counts().sort_index())
year_bol = top_selling_brand['yearOfRegistration'].between(1910,2017)
top_selling_brand=top_selling_brand[year_bol]
print(top_selling_brand['yearOfRegistration'].value_counts().sort_index())

brand_mean = groupping[['price ($)','odometer (km)','yearOfRegistration']].mean().sort_values('price ($)')
print(brand_mean)
