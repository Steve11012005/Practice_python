class Recipe:
    def __init__(self, name, ingredients, prep_time):
        self.name = name
        self.ingredients = ingredients
        self.prep_time = prep_time
        self.is_prepared = False

    def list_ingredients(self):
        print(f"Ingredients for {self.name}:")
        for ingredients in self.ingredients:
            print(f"-{ingredients}")

    def prepare(self):
        print(f"Preparing{self.name}...")
        # Here self is used to call another method
        self.list_ingredients()
        print(f"Preparation wwill take {self.prep_time} minutes.")
        self.is_prepared = True

    def serve(self):
        if self.is_prepared:
            print(f"{self.name} is ready to be served. Enjoy your meal!")
        else:
            print(f"You need to prepare {self.name} first.")
            # Here self is used to call another method self.prepared()
            print(f"{self.name} is now ready to be served. Enjoy your meal!")


    # Creating a recipe
jollof_rice = Recipe(
    "Jollof_Rice",
    ["RIce", "Tomatoes", "Peppers", "Onions",
             "Vegetable oil", "Curry", "Thyme", "Bay leaves"],
    45
)
# Calling methods
jollof_rice.serve()
