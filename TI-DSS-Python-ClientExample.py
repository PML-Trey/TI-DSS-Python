import Pyro4

dss = Pyro4.Proxy("PYRONAME:dss")    # use name server object lookup uri shortcut

# Setup target configuration
# Populated with a path/file of a target configuraiton made using CCS
dss.setConfig("./targetConfig.ccxml")

# Connect to debugger and configure this debug session
# Populate with the name of the connection and the target cpu
# For instance "Texas Instruments XDS110 USB Debug Probe_0/C28xx_CPU1"
# This returns the session name that is used in all subsequent calls 
# that interact with the target device
sessionName = dss.startDebugSession("Connection Name")
print('Connected to debugger')

# Connect to the target CPU using the debugger
dss.connectTarget(sessionName)
print('Connected to targets')

# Program the target device
# Change application.out to be the path to your executable
# This can take a while depending on the device
print('Programming target')
dss.loadProgram(sessionName, "./application.out")
print("Done programming")

# End the debug session and stop the debug server
dss.endDebugSession(sessionName)
dss.stopDebugServer()
