<h1 id="digicert-user-access">DigiCert User-Access</h1>
<p>Here’s an example using DigiCert’s API and Python to manage limited user-access on a set of orders. Case usage was an employee leaving the company and they needed to give control to another user.</p>
<h3 id="pre-requisites">Pre-Requisites</h3>
<ul>
<li>DigiCert API Key</li>
<li>user_id of the current owner</li>
<li>user_id of the user you want to give access</li>
</ul>
<h3 id="some-considerations">Some Considerations</h3>
<ul>
<li>
<p>The URL used to get the orders in this example grabs everything for that user. This includes expired, rejected or renewed. If you are looking for a subset of orders there is some URL filtering that can be done. Take a look at DigiCert’s docs for some more info. <a href="https://dev.digicert.com/services-api/#url-query-strings">https://dev.digicert.com/services-api/#url-query-strings</a></p>
</li>
<li>
<p>User access with DigiCert orders is reserved for the “limited_user” role. The users that have access is just an array of user_id’s. I’ve found you can never remove the original requestor/owner but you can append to the array without needing to provide their user_id. Like any settings array with the DigiCert API any new one sent overwirtes the previous. So if you want to give multiple additional users access, you need to provide all their user_id’s in the same payload.</p>
<pre><code>  {"user_id_assignments":["111111"]}  # Adds a single user with  original requestor
  {"user_id_assignments":["222222", "33333"]} # Adds two users in addition to original requestor. Could potentially remove user "11111" if previously set. 
</code></pre>
</li>
</ul>
<h1 id="section"></h1>
<p><a href="https://github.com/remorseville/digicert_scripts/blob/master/user_access.py">user_access.py</a></p>

