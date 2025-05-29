import subprocess

def get_arp_table():
    
    try:
        result = subprocess.check_output(['arp', '-a'], universal_newlines=True)
        return result.strip().split('\n')
    except subprocess.CalledProcessError as e:
        print(f"Error fetching ARP table: {e}")
        return []

def get_adapter_info():
    
    try:
        result = subprocess.check_output(['ipconfig', '/all'], universal_newlines=True)

       
        return result.strip().split('\n')
    except subprocess.CalledProcessError as e:
        print(f"Error fetching adapter information: {e}")
        return []
