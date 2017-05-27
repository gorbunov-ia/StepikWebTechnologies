def app(environ, start_response):
	#logic
	QUERY_STRING = environ['QUERY_STRING']
	BODY = ""

	if QUERY_STRING.find("?") <> -1:
        	QUERY_STRING = QUERY_STRING[QUERY_STRING.find("?")+1:]

	for item in QUERY_STRING:
        	if item == "&":
                	BODY = BODY + "\n"
	        else:
        	        BODY = BODY + item
	#end logic
	status = '200 OK'
	headers = [
		('Content-Type','text/plain')
	]
	body = 'Hello, world!'
	start_response(status, headers)
	#return [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
	return [BODY]
