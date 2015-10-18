import requests


def decide_restaurant(payload):
	restaurant = payload['restaurant']
	return restaurant

def get_order_items(payload):
	'''
	Grab all order items and remove the empty ones
	Empty ones will be "Ninguno", "Ninguna", "No Escogi ______".
	'''
	order = {}
	order_items = payload['order_items']
	empty_responses = ["Ninguno", "Ninguna", "No Escogi"]
	for item in order_items:
		if order_items[item] in empty_responses:
			print "Not selected"
		else:
			order[item] = order_items[item]
	return order



# 1. decide restaurant
# 2. get order items and confirmaition number
# 3. create order template and confirmation template (database)
# 4. create custom link: (www.blablabla.com/confirmation=OrderID)
# 5. send email to mailgun with restaurant email
# 6. receive confirmation webhook (with order ID)
# 7. send confirmation email (with already created payload in database)

payload = {
			"restaurant":"Demo Restaurant",
			"order_items":{
							"Item1":"Ninguno", 
							"Item2":"Ninguna", 
							"Item3":"Pollo a la Carbonara Pasta ($9.00)",
							"Item4":"No Escogi Carnes",
							"Item5":"Carne Especial ($4)"
							},
			"customer_info":{
							"name":"Juan del Pueblo",
							"email":"juan@pueblo.com",
							"phone":"787-555-5555",
							"address":"Frente al parque de bombas, dejar con guardia"
							}		
			}
print decide_restaurant(payload)
order = get_order_items(payload)
for item in order:
	print '{0}: {1}'.format(item, order[item])