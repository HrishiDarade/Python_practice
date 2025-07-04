import subprocess

svc = input("Enter the service to check is running or not: ")

check_cmd = [ "ps",
              "-C",
               svc ]
service_check = subprocess.call(check_cmd)

if service_check == 0:
    print("The service is running")
else:
    print("Service is not running")
    print("Starting it.....")
    try:
        subprocess.check_output(["systemctl", "start", svc])
    except subprocess.CalledProcessError as e:
        print("There was an error starting the process")
        print(e)
        exit(1)
        