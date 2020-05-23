from logic.model import Recipe
from logic.store import InMemoryStore

def test_in_memory_store():
    store = InMemoryStore()

    assert [] == store.get_recipes()

    recipe = Recipe("gnocchi", "gnocchi\ncherry tomatoes\nmozzarella")

    store.add_recipe(recipe)

    assert [recipe] == store.get_recipes()