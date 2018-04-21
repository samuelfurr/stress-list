# stress-list

To set up a virtualenv:

$> virtualenv

Then cd into the virtualenv folder, and clone the project from github into the folder. In the upper level of the virtualenv folder, type:

$> source bin/activate

Then cd into the repo folder, and type:

$> pip install -r requirements.txt

Last but not least, in the same directory as stress.py, run:

export FLASK_APP=stress.py

Type flask run to run the app
