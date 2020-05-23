from logic.model import Recipe
from logic.store import InMemoryStore
from logic.shoppinglist import create_list

def test_main():
    store = InMemoryStore()

    store.add_recipe(Recipe(
        "ham sandwich", 
        "ham\nbread"
    ))

    store.add_recipe(Recipe(
        "cheese sandwich",
        "cheese\nbread"
    ))

    expected = [
        "bread",
        "bread",
        "cheese",
        "ham"
    ]

    assert expected == create_list(store.get_recipes())