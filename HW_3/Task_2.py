def print_user(name, surname, year_of_birth, city_of_residence, email, phone):
    print(f"User {name} {surname} born in year {year_of_birth}, who lives in the city of {city_of_residence}, "
          f"and uses Email {email} and phone {phone}")


user_template = {
    'name': 'Name',
    'surname': 'Surname',
    'year_of_birth': 'Year of birth',
    'city_of_residence': 'City of residence',
    'email': 'Email',
    'phone': 'Phone'
}
my_user = {}
for key, value in user_template.items():
    input_value = input(f'{value}: ')
    my_user.update({key: input_value})

print_user(**my_user)