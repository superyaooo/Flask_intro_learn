[[About gunicorn]]

since gunicorn doesn't work with windows, pip install waitress instead.
Waitress in command line:
	waitress-serve --host=127.0.0.1 --port=4000 app:app	


In Procfile:
	waitress-serve --host=127.0.0.1 --port=4000 app:app







[[About Configuration]]


import os
app.config.from_object(os.environ['APP_SETTINGS'])


# there should be no value set to APP_SETTINGS here.

# at command line, instead of:  export APP_SETTINGS="config.DevelopmentConfig" (linux)
	
	on Windows it should be:  set APP_SETTINGS=config.DevelopmentConfig  
					(NO quotation marks here)
				

