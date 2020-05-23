from dataclasses import dataclass

@dataclass
class Recipe:
    name: str
    ingredients: str

PLAN = ([
    {
        "day": "Sunday",
        "meals": [
            {"time": "Dinner", "meal": "Sweet & Sour Pork", "cook": "Kim"}
        ]
    },
    {
        "day": "Monday",
        "meals": [
            {"time": "Lunch", "meal": "Gnocchi bake", "cook": "Peter"},
            {"time": "Dinner", "meal": "Pad Thai", "cook": "Kim"},
        ]
    },
    {
        "day": "Beyond",
        "meals": [
            {"time": "???", "meal": "Lentil & Sausage", "cook": "Peter"}
        ]
    }
])

def getPlan():
    return PLAN