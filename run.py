import subprocess
import time

# Creating the database
subprocess.run('python3 ./models.py')

time.sleep(1)

# Starting the app
subprocess.run('python3 ./app.py')
