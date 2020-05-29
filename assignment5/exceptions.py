import sys

def getFile(filename):
	try:
		file = open(filename, "r")
	except FileNotFoundError as fnf_error:
		print(fnf_error)
	else:
		print("File open successfully")
		return file

def getNumber():
	while True:
		num = int(input("Enter positive Number : "))
		try:
			if num < 0:
				raise Exception(f'number should be positive.')
		except Exception as e:
			print(e)
		else:
			return num

