import requests  
import json  

# --Variables--  
old_user_id = 																						                                    # User ID of the "limited" user that controls the orders. No quotes.  
api_key = "" 																						                                      # API key  
user_id = 																							                                      # User ID of the "limited" user you want to give access to. No quotes.  


headers = { 																						                                      # usual header info for call to DigiCert  
  'X-DC-DEVKEY': f'{api_key}',  
  'Content-Type': "application/json"  
  }  

url = f'https://www.digicert.com/services/v2/order/certificate?user_id%5D={old_user_id}' 			# URL of the current users orders (old_user_id)   
response = requests.request("GET", url, headers=headers) 											                # This response is grabbing all the orders for the URL variable specified on line 6  
data = response.text  
json_data = json.loads(data)  



for orders in json_data["orders"]: 																	                          # This "for" loop is grabbing every order number in the provided data.  
  order_id = orders["id"]  
  url = f'https://www.digicert.com/services/v2/order/certificate/{order_id}/user-access' 			# A new URL is created for each order. This is the endpoint for managing user access.  
  print(order_id, " ", url) 			# Some output of each order and it's URL.  
  payload = f'{{"user_id_assignments":["{user_id}"]}}' 												                # This is body of the PUT request. It includes the "user_id" of the limited user you are looking to add. 
  
  
  
   ## If you would like to see what orders are being referenced before commiting to any changes, comment out lines 33 and 34.
   
   
  response = requests.request("PUT", url, data=payload, headers=headers) 							        # New response (PUT request) to DigiCert that sets our user  
  print(response.text)
  
 
