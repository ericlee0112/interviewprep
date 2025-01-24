'''
we are building a backend system used by a restaurant to manage recipes and inventory and display menus to customers


part 1 : admin api
the system stores a series of recipes with each specifying the ingredients and time required to prepare a dish. 
An ingredient can either be :
        - a raw ingredient (like oil and potato)
        - a dish made using a different recipe (like chips)
    
{
    "dish_name" : "fish_and_chips",
    "ingredients" : ["fried_fish", "chips", "salt"]
    "time" : 10
}

In this recipe, "salt" is a raw ingredient, whereas "fried fish" and "chips" are dishes that can be prepared by other recipes described as follows:

{
    "dish_name" : "fried_fish",
    "ingredients" : ["fish", "oil"]
    "time" : 20
}

{
    "dish_name" : "chips",
    "ingredients" : ["potato", "oil"]
    "time" : 15
}


implement the following apis

add_recipe( name, ingredients, time) : adds recipe to system, if recipe already exists, overwrite

add_supply( raw_ingredient, count) : supplies restaurant with count number of raw_ingredient

get_recipe(name) : 

raw ingredients() : returns/prints a list of raw ingredients and their avalablities in a format (that contains the name and avalably of each ingredient. 
    The returned ingredients should be sorted by wallablity in ascending order. If two ingredients have the same avallability, they should be sorted by the name of the ingredient in alphabetical order.
    you should not return raw ingredients with 0 availability

timehashmap 
dish name -> time    

recipe hashmap 
dish name -> list of ingredients

ingredients count hashmap 
dish name -> count

'''
import collections
import heapq

class Restaurant:
    def __init__(self):
        self.recipeTimeHashmap = collections.defaultdict(int)
        self.recipeIngredientsHashMap = collections.defaultdict(list)
        self.ingredientsCountHashMap = collections.defaultdict(int)
    
    def add_recipe(self, dishname, ingredients, time):
        self.recipeIngredientsHashMap[dishname] = ingredients
        self.recipeTimeHashmap[dishname] = time
    
    def add_supply(self, ingredient, count):
        self.ingredientsCountHashMap[ingredient] += count
    
    def get_recipe(self, dishname):
        return self.recipeIngredientsHashMap[dishname]
    
    def get_raw_ingredients(self):
        heap = []
        for ingredient, count in self.ingredientsCountHashMap.items():
            heapq.heappush(heap, (count, ingredient))
        
        res = []
        while len(heap) > 0:
            (count, ingredient) = heapq.heappop(heap)
            res.append((ingredient, count))
        
        return res

    def place_order(self, dishname):
        # check if dishname exists in recipeIngredientsHashMap

        # for ingredient in self.recipeIngredientsHashMap[dishname]
            # check if ingredient exists in self.ingredientsCountHashMap and self.ingredientsCountHashMap[ingredient] > 0
        
        # if true, then reduce counts by 1 for all ingredients

        # return true
    
    def get_appetizers(self):
        # an appetizer is a dish that takes less than 10 minutes



