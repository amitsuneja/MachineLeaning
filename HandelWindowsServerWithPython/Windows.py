import wmi

c = wmi.WMI ()

# List all Services Names name and there state
for s in c.Win32_Service ():
    if s.State == 'Stopped':
        print (s.Caption, s.State)

# List all running processes
for process in c.Win32_Process ():
    print (process.ProcessId, process.Name)

# List all running notepad processes
for process in c.Win32_Process (name="notepad.exe"):
    print (process.ProcessId, process.Name)

# Show all automatic services which are not running
stopped_services = c.Win32_Service (StartMode="Auto", State="Stopped")
if stopped_services:
    for s in stopped_services:
        print (s.Caption, "service is not running")
else:
    print ("No auto services stopped")

# Disk info for each  fixed disk
for disk in c.Win32_LogicalDisk (DriveType=3):
    print (disk.Caption) #, "%0.2f%% free" % (100.0 * long (disk.FreeSpace) / long (disk.Size)))
    print (disk.Size)
    print (disk.FreeSpace)
    print (disk)

# Show the IP and MAC addresses for IP-enabled network interfaces
for interface in c.Win32_NetworkAdapterConfiguration (IPEnabled=1):
    print (interface.Description, interface.MACAddress)
    for ip_address in interface.IPAddress:
        print (ip_address)
    print

# What’s running on startup and from where?
for s in c.Win32_StartupCommand ():
    print (s.Location, s.Caption, s.Command)

# Show shared drive
for share in c.Win32_Share ():
    print (share.Name, share.Path)

# Display print jobs
for printer in c.Win32_Printer ():
    print (printer.Caption)
    for job in c.Win32_PrintJob (DriverName=printer.DriverName):
        print ("  ", job.Document)
    print

# Display User Account
for user in c.Win32_useraccount ():
    print(user)



for vol in c.Win32_volume():
    print(vol)


#Display OS

for os in c.Win32_OperatingSystem():
    print (os)
    print (os.NumberOfProcesses)



# Display boot configuration
for My in c.Win32_BootConfiguration():
    print(My)
