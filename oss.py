
import platform
import subprocess

def get_os_details():
    os_details = {}
    
    os_details['OS'] = platform.system()
    os_details['Version'] = platform.version()
    os_details['Release'] = platform.release()
    os_details['Platform Version'] = platform.platform()
    os_details['Machine'] = platform.machine()
    os_details['Processor'] = platform.processor()

    if os_details['OS'] == 'Windows':
        try:
            os_details['Build'] = subprocess.check_output(['wmic', 'os', 'get', 'BuildNumber'], shell=True).decode().split()[1]
        except Exception as e:
            os_details['Build'] = f"Error retrieving build number: {str(e)}"
    
    return os_details
