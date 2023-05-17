stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    list_of_items = inventory.items()
    total_items = 0
    
    print('Inventory:')
    for item, amount in list_of_items:
        print(amount, item)
        total_items += amount

    print(f'Total number of items: {total_items}')



if __name__ == "__main__":
    displayInventory(stuff)
