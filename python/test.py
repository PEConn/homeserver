from logic.model import Recipe
from logic.store import InMemoryStore
from logic.shoppinglist import create_list

if __name__ == "__main__":
    store = InMemoryStore()

    store.add_recipe(Recipe(
        "gnocchi", 
        "gnocchi\ncherry tomatoes\nmozzarella"
    ))

    store.add_recipe(Recipe(
        "ham sandwich",
        "ham\nbread"
    ))
    
    print(create_list(store.get_recipes()))