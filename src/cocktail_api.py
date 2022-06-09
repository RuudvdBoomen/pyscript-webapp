from pyodide.http import pyfetch
import asyncio
from cocktail import Cocktail
from js import document, console


async def main():
    await get_cocktails()


async def get_cocktails(search_value=""):
    try:
        url = "https://thecocktaildb.com/api/json/v1/1/search.php"
        if search_value:
            url = f"{url}?s={search_value}"
        else:
            url = f"{url}?f=a"
        response = await pyfetch(url=url, method="GET")

        json = await response.json()
    except Exception as x:
        console.log("Error calling cocktail API: {}".format(x))

    cocktails = [Cocktail(data) for data in json.get("drinks")]

    # Build cocktails
    cocktails_list = document.getElementById("cocktails")
    cocktails_list.innerHTML = ""
    for cocktail in cocktails:
        cocktail_card = document.createElement("div")
        cocktail_card.classList.add("rounded", "overflow-hidden", "shadow-lg")

        # Image
        image = document.createElement("img")
        image.src = cocktail.image
        image.classList.add("w-full")
        cocktail_card.appendChild(image)

        # Name
        name = document.createElement("div")
        name.appendChild(document.createTextNode(cocktail.name))
        name.classList.add("font-bold", "text-xl", "mb-2")

        # Instructions
        instructions = document.createElement("div")
        instructions.appendChild(document.createTextNode(cocktail.instructions))
        instructions.classList.add("text-gray-700", "text-base")

        name_instructions_div = document.createElement("div")
        name_instructions_div.classList.add("px-6", "py-4")
        name_instructions_div.appendChild(name)
        name_instructions_div.appendChild(instructions)
        cocktail_card.append(name_instructions_div)

        # Ingredients
        ingredients = document.createElement("div")
        ingredients.classList.add("px-6", "pt-4", "pb-2")
        for ingredient in cocktail.ingredients:
            ingredients_list = document.createElement("span")
            ingredients_list.classList.add(
                "inline-block",
                "bg-gray-200",
                "rounded-full",
                "px-3",
                "py-1",
                "text-sm",
                "font-semibold",
                "text-gray-700",
                "mr-2",
                "mb-2",
            )
            ingredients_list.appendChild(document.createTextNode(ingredient))
            ingredients.appendChild(ingredients_list)
        cocktail_card.appendChild(ingredients)

        cocktails_list.appendChild(cocktail_card)


async def search_cocktails(*args):
    search_value = document.getElementById("search-input").value
    await get_cocktails(search_value)


async def clear_search(*args):
    await get_cocktails()


main()