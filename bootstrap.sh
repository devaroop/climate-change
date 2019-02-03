
source ../venv_climate_change/bin/activate
if test "$?" -ne "0"; then
	printf "Did you create the venv using 'python3 -m venv ../venv_climate_change'?. After that run 'pip install -r requirements.txt'"
	exit 2
fi

export FLASK_APP=climate_change_app
export FLASK_ENV=development
    
printf "Running server......... \n\n"
flask run
