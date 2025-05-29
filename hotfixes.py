# hotfixes.py

import wmi

def get_installed_hotfixes():
    hotfixes = []
    
    c = wmi.WMI()
    for hotfix in c.Win32_QuickFixEngineering():
        hotfixes.append({
            'HotFixID': hotfix.HotFixID,
            'Description': hotfix.Description,
            'InstalledOn': hotfix.InstalledOn
        })
    
    return hotfixes
