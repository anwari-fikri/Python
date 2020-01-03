class Product:
	def __init__(self,id_num,name,price,quantity):
		self.id_num = id_num
		self.name = name
		self.price = price
		self.quantity = quantity

	def __str__(self):
		return (self.name).capitalize()

class Inventory:
	def __init__(self,id_num,name):
		self.id_num = id_num
		self.name = name
		self.products = []

	def __str__(self):
		return f'Inventory name: {self.name}'

	def add_product(self, Product):
		self.products.append(Product)

	def show_products(self):
		print(f"Product(s) in '{self.name}' Inventory")
		for x in self.products:
			print(x)

	def total_value(self):
		tot = 0
		for x in self.products:
			tot = x.price*x.quantity
		print("Total value of items: $",tot)

banana = Product(123,"banana",0.99,5)
print(banana)
strawberry = Product(345,"strawberry",3.49,15)
print(strawberry)

storage1 = Inventory(1,"Fruits")
print(storage1)
storage1.add_product(banana)
storage1.add_product(strawberry)
storage1.show_products()
storage1.total_value()

