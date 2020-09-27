import requests  
import json  

# --Variables-- #

# User ID of the "limited" user that controls the orders. No quotes. 
old_user_id =

# API key
api_key = "" 

# User ID of the "limited" user you want to give access to. No quotes.  
user_id = 																							                                      




headers = { 																						                                        
  'X-DC-DEVKEY': f'{api_key}',  
  'Content-Type': "application/json"  
  }  


# URL of the current users orders (old_user_id) / Filtering options could be added here
url = f'https://www.digicert.com/services/v2/order/certificate?user_id%5D={old_user_id}' 			  
response = requests.request("GET", url, headers=headers) 											                 
data = response.text  
json_data = json.loads(data)  


# This loop is grabbing every order number in the provided data.
# A new URL and body for our request are created.
for orders in json_data["orders"]: 		
  
  order_id = orders["id"]  
  url = f'https://www.digicert.com/services/v2/order/certificate/{order_id}/user-access'
  
  # Some output of each order and it's URL.
  print(order_id, " ", url) 			  
  payload = f'{{"user_id_assignments":["{user_id}"]}}' 												                
  
  
  # If you would like to see what orders are being referenced before commiting to any changes, comment out the lines below.
  response = requests.request("PUT", url, data=payload, headers=headers) 							         
  print(response.text)
  
 
