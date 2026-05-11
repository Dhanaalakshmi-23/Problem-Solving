#1. Group products by category and find the costliest product in each category.
# sample input :
# [
#  ("Laptop", "Electronics", 70000),
#  ("Phone", "Electronics", 50000),
#  ("Shirt", "Clothing", 2000),
#  ("Jacket", "Clothing", 5000),
#  ("Sofa", "Furniture", 25000)
# ]

# output :
# {
#  'Electronics': ['Laptop', 'Phone'],
#  'Clothing': ['Shirt', 'Jacket'],
#  'Furniture': ['Sofa']
# }

# costliest product in Electronics : Laptop
# costliest product in Clothing : Jacket
# costliest product in Furniture : Sofa

def productDetails(data):
    groups = {}
    highest = {}
    
    for product, category, price in data:
        
        groups.setdefault(category, []).append(product)
        
        if category not in highest or price > highest[category][1]:
            highest[category] = (product, price)
    
    print(groups)
    
    for category in highest:
        print("costliest product in", category, ":", highest[category][0])


products = [
    ("Laptop", "Electronics", 70000),
    ("Phone", "Electronics", 50000),
    ("Shirt", "Clothing", 2000),
    ("Jacket", "Clothing", 5000),
    ("Sofa", "Furniture", 25000)
]

productDetails(products)