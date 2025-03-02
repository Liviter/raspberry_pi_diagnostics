# Hi this python script is to help me log stats about my raspberry pi performance
from gpiozero import CPUTemperature
from datetime import datetime
import subprocess

LOG_FILE = "/home/raspberrylex/pi_diagnostics.log"

def run_speedtest():
	"""Run Ookla speedtest and log resulst."""
	try:
		# data is a huge string, full of useful info but we only want download speed for now
		data =  subprocess.check_output(["speedtest", "--format=json"]).decode("utf-8")
		string_list = data.split(",")
		for string in string_list:
			if "bytes" in string:
				download_byte = string.split(":")
				return("Download speed : {}MB".format(round(int(download_byte[1])/1000000)))
				break
	
	except Exception as e:
		print(f"Error running speedtest: {e}")


def get_cpu_gpu_temp():
	"""returns a combination of CPU and GPU temp in Celcius, could not find a lib/method which will return both CPU and GPU individually"""
	cpu_gpu_temp = CPUTemperature().temperature
	return f"CPU Temp: {cpu_gpu_temp}°C"


def log_data():
	"""Using all functions here to log results"""
	time_now = datetime.now().strftime("%Y-%m-%d at %H:%M:%S")
	speedtest = run_speedtest()
	cpu_temp = get_cpu_gpu_temp()
	
	log_entry = f"{time_now} | {speedtest} | {cpu_temp}\n"

	with open(LOG_FILE, "a") as log_file:
		log_file.write(log_entry)

def main():
	log_data()

if __name__ == "__main__":
	main()
