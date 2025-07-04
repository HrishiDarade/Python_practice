import subprocess

svc = input("Enter the service to check it is running or not: ")

service_check = subprocess.call(["ps", "-C", svc])

if service_check == 0:
    print("service is running")
else:
    print("service is not running") 