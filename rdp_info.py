import subprocess
import winreg



def get_saved_rdp_connections():
    connections = []
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Terminal Server Client\Default")
        for i in range(0, winreg.QueryInfoKey(key)[1]):
            connection_name = winreg.EnumKey(key, i)
            connections.append(connection_name)
        winreg.CloseKey(key)
    except WindowsError as e:
        print(f"Error retrieving saved RDP connections: {e}")
    return connections



def get_incoming_rdp_sessions():
    try:
        result = subprocess.run(['query', 'session'], capture_output=True, text=True, check=True)
        sessions = result.stdout.splitlines()
        return sessions[1:]  
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving current RDP sessions: {e}")
        return []

def get_rdp_settings():
    rdp_settings = {}
    try:
        registry_path = r"System\CurrentControlSet\Control\Terminal Server"
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path)
        fDenyTSConnections, _ = winreg.QueryValueEx(registry_key, "fDenyTSConnections")
        rdp_settings["fDenyTSConnections"] = "Disabled" if fDenyTSConnections == 0 else "Enabled"
        
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services")
        try:
            fDisableCdm, _ = winreg.QueryValueEx(registry_key, "fDisableCdm")
            rdp_settings["fDisableCdm"] = "Disabled" if fDisableCdm == 0 else "Enabled"
        except FileNotFoundError:
            rdp_settings["fDisableCdm"] = "Not Configured"

        winreg.CloseKey(registry_key)
    except Exception as e:
        print(f"Error retrieving RDP settings: {e}")
    
    return rdp_settings
