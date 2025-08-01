import subprocess
from time import sleep


try:
    env_name = 'test_env'  ## Aquí puedes elegir el nombre del ambiente que quieras

    subprocess.run(["conda", "create", "--name", env_name, "python=3.12.4", "-y"])
    sleep(2)
    subprocess.run(["conda", "run", "--name", env_name, "pip", "install", "-r", "requirements.txt"])
    sleep(2)
    print(f"El Ambiente {env_name} ha sido creado con éxito")

except Exception as e:
    print(f"Error: {e}")
    print(f"La creación del ambiente ha tenido un error")


