import sys
import subprocess

def dump(url):
	try:
		return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
	except OSError as err:
		print("ERROR: pg_dump not found")
		sys.exit(2)
