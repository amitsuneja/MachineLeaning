# Importing the wmi module in python
import wmi

# define variables for ip , username and password.
ip = '192.168.1.101'
username = 'test'
password = 'test'

try:
    # printing message that we are trying to connect to remote host
    print("Establishing connection to {0}".format(ip))
    # creating WMI connection
    connection = wmi.WMI(ip, user=username, password=password)
    # printing message if connection is established successfully
    print("Connection established")
    # running ipconfig /release command on remote host
    connection.Win32_Process.Create(CommandLine='cmd.exe /c ipconfig /registerdns >> c:\\Users\\test\\Desktop\\log.txt')

# raising exception incase remote host is not connecting.
except wmi.x_wmi:
    print("Your Username and Password of {0} are wrong.".format(ip))