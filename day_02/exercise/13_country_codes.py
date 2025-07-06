# Add more country codes
country_codes = {
    "PH": "Philippines",
    "US": "United States",
    "UK": "United Kingdom",
    "JP": "Japan",
    "RUS": "Russia"
}

country_code = input("Enter country code: ")
print(country_codes.get(country_code, "Unknown"))
# print(country_codes[country_code])
# print(country_codes)

for code in country_codes.keys():
    print(code)

for country in country_codes.values():
    print(country)

