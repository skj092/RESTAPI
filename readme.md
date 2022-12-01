# REST API

Web Services like YouTube, GitHub make their data accessible to their-party applications through an application programming interface (API). One of the most popular way to build API is the REST architecture style. 

HTTP Request Methods: ( From the client)
1. GET: To Get Data from a resource
2. PUT: to Update Data at the resource
3. POST: to Create data at a resource
4. DELETE: to Delete data at a resource
5. PATCH: to partically update data at a resource

HTTP Reponse ( From server):
1. Status code
2. Conntent Type
3. Content-Length
4. json

# here we have 3 script 
`httpmethod.py` will show you the action of different HTTP request methods
`main.py` fun main.py with the command `uvicorn main:app --reload --port 7000` it wll start the app
`test.py` can be use to test `main.py`