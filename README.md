<h1 id="digicert-user-access">DigiCert User-Access</h1>
<p>Here’s an example using DigiCert’s API and Python to manage limited user-access on a set of orders. Case usage was an employee leaving the company and they needed to give control to another user.</p>
<h3 id="pre-requisites">Pre-Requisites</h3>
<ul>
<li>DigiCert API Key</li>
<li>user_id of the current owner</li>
<li>user_id of the user you can to give access to</li>
</ul>
<h3 id="some-considerations">Some Considerations</h3>
<ul>
<li>
<p>The URL used to get the orders in this example grabs everything. This includes expired, rejected or renewed. If you are looking for a subset of orders there is some URL filtering that can be done. Here’s a few examples</p>
<pre><code>  filters%5Bstatus%5D%5B0%5D=issued
  filters%5Bstatus%5D%5B1%5D=pending
  filters%5Bstatus%5D%5B2%5D=reissue_pending
  filters%5Bsearch%5D%5B0%5D=%25{search_string}
</code></pre>
</li>
<li>
<p>User access with DigiCert orders is reserved for the “limited_user” role. The users that have access is just an array of user_id’s. I’ve found you can never remove the original requestor/owner but you can append to the array without needing to provide their user_id. Like any settings array with the DigiCert API any new one sent overwirtes the previous. So if you want to give multiple additional users access, you need to provide all their user_id’s in the same payload.</p>
<pre><code>  {"user_id_assignments":["111111"]}  # Adds a single user with  original requestor
  {"user_id_assignments":["222222", "33333"]} # Adds two users in addition to original requestor. Could potentially remove user "11111" if previously set. 
</code></pre>
</li>
</ul>
<h1 id="section"></h1>
<pre><code>    import requests  
	import json  
	  
	# --Variables--  
	old_user_id = 																						# User ID of the "limited" user that controls the orders. No quotes.  
	api_key = "" 																						# API key  
	user_id = 																							# User ID of the "limited" user you want to give access to. No quotes.  
	  
	  
	# --Good Stuff--  
	headers = { 																						# usual header info for call to DigiCert  
	  'X-DC-DEVKEY': f'{api_key}',  
	  'Content-Type': "application/json"  
	  }  
	  
	url = f'https://www.digicert.com/services/v2/order/certificate?user_id%5D={old_user_id}' 			# URL of the current users orders (old_user_id)   
	response = requests.request("GET", url, headers=headers) 											# This response is grabbing all the orders for the URL variable specified on line 6  
	data = response.text  
	json_data = json.loads(data)  
	  
	  
	  
	for orders in json_data["orders"]: 																	# This "for" loop is grabbing every order number in the provided data.  
	  order_id = orders["id"]  
	  url = f'https://www.digicert.com/services/v2/order/certificate/{order_id}/user-access' 			# A new URL is created for each order. This is the endpoint for managing user access.  
	  print(order_id, " ", url) 			# Some output of each order and it's URL.  
	  payload = f'{{"user_id_assignments":["{user_id}"]}}' 												# This is body of the PUT request. It includes the "user_id" of the limited user you are looking to add.  
	  response = requests.request("PUT", url, data=payload, headers=headers) 							# New response (PUT request) to DigiCert that sets our user  
	  print(response.text)
</code></pre>

