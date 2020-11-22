#! /usr/env/python3

# Run Docker containers from a Tkinter GUI.
#
# Ideally, we would use the Docker API for Python, but for some reason, we
# are unable to run GUI applications with it. Instead, the shell commands
# are used. 
#
# +***************************************************+
# * WARNING: !!! THIS IS SUPER BAD AND DANGEROUS  !!! *
# *          !!! DO NOT USE IN A REAL ENVIRONMENT !!! *
# +***************************************************+
#
# Additionally, there is probably a much cleaner way to launch each
# program, instead of having a separate function for each, but I don't know
# what that would be.

#import docker
import os
import tkinter as tk

# Build a container from the given directory with the given name
def build_container(build_dir, name):
	build_command = 'docker build -t {} /home/1660/{}'.format(name, build_dir)

	print('\n\n ----- BEGIN CONTAINER BUILD -----\n{}\n'.format(build_command))
	os.system(build_command)

# Run the container with the given name This can be used for both
# containers that require GUI, and those that don't.
# Run the container with the given name
def run_container(name):
	run_command = 'docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -it {}'.format(name)


	print('\n\n ----- BEGIN CONTAINER EXECUTION -----\n{}\n'.format(run_command))
	os.system(run_command)


def launch_app(build_dir, name):
	build_container(build_dir, name)
	run_container(name)

#	build_command = 'docker build -t {} /home/1660/{}'.format(name, build_dir)
#	run_command = 'docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -it {}'.format(name)
#
#	print(build_command)
#	os.system(build_command)
#	print(run_command)
#	os.system(run_command)
	


# OK!
def run_xclock():
	launch_app('xclock', 'my-xclock-test')


# OK!
def run_rstudio():
	launch_app('rstudio', 'my-rstudio-test')


# OK!
def run_spyder():
	launch_app('spyder', 'my-spyder-test')


# OK!
def run_sas():
	launch_app('ibm_sas', 'my-sas-test')


# OK!
def run_git():
	launch_app('git', 'my-git-test')


# OK!
def run_jupyter():
	launch_app('jupyter', 'my-jupyter-test')


# OK!
def run_orange():
	launch_app('orange', 'my-orange-test')


# OK!
def run_vscode():
	launch_app('vscode', 'my-vscode-test')


# OK!
def run_hadoop():
	launch_app('hadoop', 'my-hadoop-test')


# OK!
def run_spark():
	launch_app('spark', 'my-spark-test')


# OK!
def run_tableau():
	launch_app('tableau', 'my-tableau-test')


def run_sonar():
	# Do nothing. This is a special case handled separately.
	return

# OK!
def run_tensorflow():
	launch_app('tensorflow', 'my-tensorflow-test')


# OK!
def run_markdown():
	launch_app('markdown', 'my-markdown-test')

commands = {
	'xclock': run_xclock,
	'rstudio': run_rstudio,
	'spyder': run_spyder,
	'ibm sas': run_sas,
	'git': run_git,
	'jupyter': run_jupyter,
	'orange': run_orange,
	'vscode': run_vscode,
	'hadoop': run_hadoop,
	'spark': run_spark,
	'tableau': run_tableau,
	'tensorflow': run_tensorflow,
	'markdown': run_markdown
}

class AppSelect(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)

#		self.docker_client = docker.from_env()

		self.app_buttons = []

		self.pack()
		self.create_widgets()


	def create_widgets(self):
		# Buttons to launch applications
		for app_name in sorted(commands.keys()):
			b = tk.Button(self)
			b['text'] = app_name
			b['command'] = commands[app_name]
			b.pack(side='top')
			self.app_buttons.append(b)

		# Special case for SonarQubue
		b = tk.Button(self)
		b['text'] = 'sonarqube'
		b['command'] = self.sonar_run
		b.pack(side='top')
		self.app_buttons.append(b)

		# Arguments for SonarQube
		self.sonar_dir = tk.Entry(self)
		self.sonar_dir.insert(tk.END, 'Sonar Project Directory (host)')
		self.sonar_dir.pack(side='top')
		self.sonar_key = tk.Entry(self)
		self.sonar_key.insert(tk.END, 'Sonar Project Key')
		self.sonar_key.pack(side='top')

	def sonar_run(self):
		# Instead of building, we need to create a new container
		build_qube = 'docker create --name my-sonarqube-test-1660 -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest'
		print('\n\n ----- BEGIN CONTAINER BUILDING -----\n{}\n'.format(build_qube))
		os.system(build_qube)
		
		# If it already exists and fails, just ignore it?


		# Start normal SonarCube
		run_qube = 'docker start my-sonarqube-test-1660'
		print('\n\n ----- BEGIN CONTAINER EXECUTION -----\n{}\n'.format(run_qube))
		os.system(run_qube)
		
		# Only start Scanner if the key and directory was specified.
		directory = self.sonar_dir.get()
		sonar_key = self.sonar_key.get()
		if not directory or not sonar_key:
			print('GUI: W: Directory and key not specified! Starting without Scanner!')
		else:
			run_scanner = 'docker run --rm -e SONAR_HOST_URL=http://my-sonarqube-test-1660:9000 --link my-sonarqube-test-1660 -v {}:/usr/src sonarsource/sonar-scanner-cli -Dsonar.projectKey={}'.format(directory, sonar_key)

			print('\n\n ----- BEGIN CONTAINER EXECUTION -----\n{}\n'.format(run_scanner))
			os.system(run_scanner)

		print('The interface is available on localhost:9000 and can be viewed with a web browser')
			


def main():
	root = tk.Tk()
	app = AppSelect()
	app.mainloop()


if __name__ == '__main__':
	main()
