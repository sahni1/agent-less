import subprocess

def get_amsi_providers():
    amsi_providers = []
    command = r'wmic /namespace:\\root\SecurityCenter2 path AntiVirusProduct get displayName'

    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        if result.returncode != 0:
            return []
        
        output = result.stdout.strip()
        lines = output.splitlines()
        for line in lines[1:]:
            provider_name = line.strip()
            if provider_name:
                amsi_providers.append(provider_name)
    
    except Exception as e:
        amsi_providers.append(f"Error retrieving AMSI providers: {str(e)}")
    
    return amsi_providers  