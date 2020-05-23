from typing import List

from logic.model import Recipe

def create_list(recipes: List[Recipe]) -> List[str]:
    ingredients = "\n".join([r.ingredients for r in recipes])
    return sorted(ingredients.split("\n"))