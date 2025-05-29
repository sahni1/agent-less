import subprocess
import os

def get_audit_policy_settings():
    audit_policies = []
    registry_path = r"HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System"
    
    try:
        output = subprocess.check_output(['reg', 'query', registry_path, '/s'], shell=True).decode()
        lines = output.splitlines()
        
        for line in lines:
            if line.strip() and not line.startswith("HKEY"):
                audit_policies.append(line.strip())
    
    except subprocess.CalledProcessError as e:
        audit_policies.append(f"Error retrieving audit policies: {str(e)}")
    except Exception as e:
        audit_policies.append(f"Unexpected error: {str(e)}")
    
    return audit_policies

def get_autorun_entries():
    autorun_entries = []
    paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run"
    ]
    
    try:
        for path in paths:
            output = subprocess.check_output(['reg', 'query', f"HKLM\\{path}", '/s'], shell=True).decode()
            lines = output.splitlines()
            for i in range(len(lines)):
                if "REG_SZ" in lines[i]:
                    entry = lines[i].split("    ")
                    autorun_entries.append({
                        'Path': path,
                        'Name': entry[0].strip(),
                        'Executable': entry[-1].strip()
                    })
    except subprocess.CalledProcessError as e:
        autorun_entries.append(f"Error retrieving auto-run entries: {str(e)}")
    
    return autorun_entries

def get_startup_folder_entries():
    startup_entries = []
    paths = [
        os.path.join(os.getenv('APPDATA'), r"Microsoft\Windows\Start Menu\Programs\Startup"),
        os.path.join(os.getenv('PROGRAMDATA'), r"Microsoft\Windows\Start Menu\Programs\Startup")
    ]
    
    for path in paths:
        for root, dirs, files in os.walk(path):
            for file in files:
                startup_entries.append({
                    'Folder': path,
                    'File': file,
                    'Path': os.path.join(root, file)
                })
    
    return startup_entries

import ctypes
from ctypes import wintypes

import ctypes
from ctypes import wintypes

def get_file_version_info(file_path):
    try:
        size = ctypes.windll.version.GetFileVersionInfoSizeW(file_path, None)
        if size == 0:
            return f"Unable to get file version info for: {file_path}"

        res = ctypes.create_string_buffer(size)
        ctypes.windll.version.GetFileVersionInfoW(file_path, 0, size, res)

        r = ctypes.c_void_p()
        l = wintypes.UINT()

        # Query the root block for version information
        ctypes.windll.version.VerQueryValueW(res, '\\', ctypes.byref(r), ctypes.byref(l))

        if l.value:
            fixed_file_info = ctypes.cast(r, ctypes.POINTER(ctypes.c_uint32 * (l.value // 4))).contents
            major = fixed_file_info[1] >> 16
            minor = fixed_file_info[1] & 0xFFFF
            build = fixed_file_info[0] >> 16
            revision = fixed_file_info[0] & 0xFFFF
            version = f"{major}.{minor}.{build}.{revision}"
            return version
        else:
            return "No version info available."

    except Exception as e:
        return f"Error retrieving version info: {str(e)}"
