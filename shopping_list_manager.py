class ShoppingList :
    def __init__(self):
        self.shopping_list = []
        # to make sure that this same list is shared across all instances of the class



    def add_items(self, item) :
        self.shopping_list.append(item)
        print(f"{item} added Sucessfully")
    


    def remove_items(self, item) :
        if self.shopping_list :
            if item in self.shopping_list :
                self.shopping_list.remove(item)
                print(f"{item} removed")
                self.view_list()
            else :
                print(f"{item} does not exist.")
        else :
            print("Shopping List is empty")



    def view_list(self) :
        if self.shopping_list :
            print("\nShopping List:")
            for i, item in enumerate(self.shopping_list, start=1):
                print(f"{i}. {item}")
        else :
            print("Shopping List is empty")



    def clear_list(self) :
        if self.shopping_list :
            self.shopping_list.clear()
            print("Shopping List is empty")
        else :
            print("Shopping List is already empty")



    def sort_items(self) :
        if self.shopping_list :
            print("\nSorted Shopping List:")
            self.shopping_list.sort()
            self.view_list()
        else :
            print("Shopping List is empty")
            



shop_list = ShoppingList()
shop_list.add_items("Butter")
shop_list.add_items("Cheese")
shop_list.add_items("Buy Shoes")
shop_list.add_items("Apples")

shop_list.view_list()
shop_list.sort_items()
shop_list.remove_items("Apples")
shop_list.clear_list()
shop_list.clear_list()
shop_list.remove_items("Butter")