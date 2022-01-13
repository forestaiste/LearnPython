dial_codes = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (81, 'Japan')
]

country_code = {country: code for code, country in dial_codes}
print(country_code)

codes = {code: country.upper() for country, code in country_code.items() if code < 66}
print(codes)
