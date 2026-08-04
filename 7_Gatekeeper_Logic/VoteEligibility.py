# Implement vote_eligibility(age, country). Return Eligible if age is at least 18 and country is Nigeria. Otherwise return Not eligible. The country check should be case-insensitive and should ignore leading and trailing spaces.
def vote_eligibility(age, country):
    country = country.strip().lower()
    if age >= 18 and country == "nigeria":
        return "Eligible"
    else:
        return "Not eligible"
