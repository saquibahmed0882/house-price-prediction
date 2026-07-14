countries = {
    "India": {
        "Uttar Pradesh": [
            "Ghazipur",
            "Varanasi",
            "Lucknow",
            "Prayagraj"
        ],
        "Delhi": [
            "New Delhi"
        ]
    },

    "USA": {
        "California": [
            "Los Angeles",
            "San Francisco"
        ],
        "New York": [
            "New York City"
        ]
    },

    "UK": {
        "England": [
            "London",
            "Manchester"
        ]
    }
}


def get_countries():

    return list(countries.keys())


def get_states(country):

    if country in countries:
        return list(countries[country].keys())

    return []


def get_cities(country, state):

    if country in countries and state in countries[country]:
        return countries[country][state]

    return []