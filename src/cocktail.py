from typing import Dict, List


class Cocktail:
    name: str
    image: str
    instructions: str
    ingredients: List[str]

    def __init__(self, data: Dict) -> None:
        self.name = data.get("strDrink")
        self.image = data.get("strDrinkThumb")
        self.instructions = data.get("strInstructions")
        self.ingredients = [
            value for key, value in data.items() if "strIngredient" in key and value
        ]

    def __str__(self) -> str:
        return self.name