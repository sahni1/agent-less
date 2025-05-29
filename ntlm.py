import subprocess

def get_ntlm_settings():
    try:
        # Use PowerShell to retrieve NTLM authentication settings via the Windows registry
        command = 'powershell "Get-ItemProperty -Path HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Lsa\\MSV1_0 | Select-Object -Property NtlmMinClientSec,NtlmMinServerSec"'
        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
        
        # Parse the output
        ntlm_settings = {}
        for line in result.stdout.splitlines():
            if 'NtlmMinClientSec' in line:
                ntlm_settings['NtlmMinClientSec'] = line.split(':')[-1].strip()
            if 'NtlmMinServerSec' in line:
                ntlm_settings['NtlmMinServerSec'] = line.split(':')[-1].strip()

        return ntlm_settings
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving NTLM settings: {e}")
        return {}

