import os
import subprocess

def git_pull():
    subprocess.run(["git", "pull", "origin", "main"])

def git_push():
    subprocess.run(["git", "push", "origin", "main"])

def create_virtualenv(env_name):
    subprocess.run([f"python -m venv {env_name}"])

def activate_virtualenv(env_name):
    if os.name == 'nt':  # Windows
        subprocess.run([f"{env_name}\\Scripts\\activate"])
    else:  # macOS/Linux
        subprocess.run([f"source {env_name}/bin/activate"])

def docker_run(image_name):
    subprocess.run(["docker", "run", "-it", image_name])

def docker_build(image_name):
    subprocess.run(["docker", "build", "-t", image_name, "."])

def docker_compose_up():
    subprocess.run(["docker-compose", "up"])

def docker_compose_down():
    subprocess.run(["docker-compose", "down"])

# Utiliza las funciones según tus necesidades
'''
git clone <URL_del_repositorio>


'''