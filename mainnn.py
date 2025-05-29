
from fpdf import FPDF
from oss import get_os_details
from hotfixes import get_installed_hotfixes
from net import get_dotnet_versions
from amsi import get_amsi_providers
from audit_policies import (
    get_audit_policy_settings,
    get_autorun_entries,
    get_startup_folder_entries,
    get_file_version_info,
)
from local import get_local_groups, get_user_accounts, get_non_empty_groups, get_users_with_status
from update import get_microsoft_updates  
from ntlm import get_ntlm_settings
==
def generate_pdf_report():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, 'System Information Report', ln=True, align='C')

    def add_section_header(title):
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(200, 10, title, ln=True)
        pdf.ln(5)

    def add_text_entry(text):
        pdf.set_font('Arial', '', 10)
        pdf.cell(200, 8, text, ln=True)

    add_section_header('OS Details')
    os_details = get_os_details()
    for key, value in os_details.items():
        add_text_entry(f"{key}: {value}")

    add_section_header('Installed Hotfixes')
    hotfixes = get_installed_hotfixes()
    for hotfix in hotfixes:
        add_text_entry(f"HotFixID: {hotfix['HotFixID']}, Description: {hotfix['Description']}, InstalledOn: {hotfix['InstalledOn']}")

    add_section_header('.NET Versions')
    net_versions = get_dotnet_versions()
    for version in net_versions:
        add_text_entry(version)

    add_section_header('AMSI Providers')
    amsi_providers = get_amsi_providers()
    for provider in amsi_providers:
        add_text_entry(provider)

    add_section_header('Audit Policy Settings')
    audit_policies = get_audit_policy_settings()
    for policy in audit_policies:
        add_text_entry(policy)

    add_section_header('Autorun Entries')
    autorun_entries = get_autorun_entries()
    for entry in autorun_entries:
        add_text_entry(f"Path: {entry['Path']}, Name: {entry['Name']}, Executable: {entry['Executable']}")

    add_section_header('Startup Folder Entries')
    startup_entries = get_startup_folder_entries()
    for entry in startup_entries:
        add_text_entry(f"File: {entry['File']}, Path: {entry['Path']}")

    add_section_header('Local Groups')
    local_groups = get_local_groups()
    for group in local_groups:
        if group:
            add_text_entry(f"Group: {group}")

    add_section_header('Local Users (with Status)')
    local_users_status = get_users_with_status()
    for user, status in local_users_status.items():
        add_text_entry(f"User: {user}, Status: {status}")

    add_section_header('Microsoft Updates')
    microsoft_updates = get_microsoft_updates()
    for update in microsoft_updates:
        add_text_entry(f"Title: {update['Title']}, KBArticleIDs: {update['KBArticleIDs']}, InstalledOn: {update['InstalledOn']}")

    add_section_header('NTLM Authentication Settings')
    ntlm_settings = get_ntlm_settings()
    for key, value in ntlm_settings.items():
        add_text_entry(f"{key}: {value}")

    
    pdf.output('system_report.pdf')
    print("PDF report generated successfully.")

def generate_html_report():
    os_details = get_os_details()
    hotfixes = get_installed_hotfixes()
    net_versions = get_dotnet_versions()
    amsi_providers = get_amsi_providers()
    audit_policies = get_audit_policy_settings()
    autorun_entries = get_autorun_entries()
    startup_entries = get_startup_folder_entries()
    
    html_content = """
    <html>
    <head>
        <title>System Information Report</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
                padding: 0;
                background-color: #f0f0f0;
            }
            h1, h2 {
                color: #333;
            }
            .container {
                background-color: white;
                border-radius: 8px;
                padding: 20px;
                box-shadow: 0 0 15px rgba(255, 0, 0, 0.5);
            }
            .section {
                margin-bottom: 20px;
            }
            .section h2 {
                border-bottom: 2px solid #333;
                padding-bottom: 5px;
                margin-bottom: 15px;
            }
            ul {
                list-style-type: none;
                padding-left: 0;
            }
            li {
                background-color: #f9f9f9;
                margin: 5px 0;
                padding: 10px;
                border-radius: 4px;
                border: 1px solid #ddd;
            }
            a {
                color: #007BFF;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
            .collapsible {
                background-color: #B22222;
                color: white;
                cursor: pointer;
                padding: 10px;
                width: 100%;
                border: none;
                text-align: left;
                outline: none;
                font-size: 16px;
                border-radius: 4px;
                margin-bottom: 10px;
            }
            .content {
                padding: 0 18px;
                display: none;
                overflow: hidden;
                background-color: #f1f1f1;
                margin-bottom: 10px;
                border-radius: 4px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>System Information Report</h1>
            <div class="section">
                <h2>Table of Contents</h2>
                <ul>
                    <li><a href="#os-details">OS Details</a></li>
                    <li><a href="#hotfixes">Installed Hotfixes</a></li>
                    <li><a href="#dotnet-versions">Installed .NET Versions</a></li>
                    <li><a href="#amsi-providers">AMSI Providers</a></li>
                    <li><a href="#audit-policies">Audit Policy Settings</a></li>
                    <li><a href="#autorun-entries">Registry Auto-Run Entries</a></li>
                    <li><a href="#startup-entries">Startup Folder Entries</a></li>
                </ul>
            </div>

            <div class="section" id="os-details">
                <button class="collapsible">OS Details</button>
                <div class="content">
                    <ul>
    """
    
    for key, value in os_details.items():
        html_content += f"<li>{key}: {value}</li>"
    
    html_content += """
                    </ul>
                </div>
            </div>

            <div class="section" id="hotfixes">
                <button class="collapsible">Installed Hotfixes</button>
                <div class="content">
                    <ul>
    """
    
    if hotfixes:
        for hotfix in hotfixes:
            html_content += f"<li>HotFixID: {hotfix['HotFixID']}, Description: {hotfix['Description']}, InstalledOn: {hotfix['InstalledOn']}</li>"
    else:
        html_content += "<li>No hotfixes installed or unable to retrieve hotfixes.</li>"
    
    html_content += """
                    </ul>
                </div>
            </div>

            <div class="section" id="dotnet-versions">
                <button class="collapsible">Installed .NET Versions</button>
                <div class="content">
                    <ul>
    """
    
    for version in net_versions:
        html_content += f"<li>{version}</li>"
    
    html_content += """
                    </ul>
                </div>
            </div>

            <div class="section" id="amsi-providers">
                <button class="collapsible">AMSI Providers</button>
                <div class="content">
                    <ul>
    """
    
    for provider in amsi_providers:
        html_content += f"<li>{provider}</li>"
    
    html_content += """
                    </ul>
                </div>
            </div>

            <div class="section" id="audit-policies">
                <button class="collapsible">Audit Policy Settings</button>
                <div class="content">
                    <ul>
    """
    
    for policy in audit_policies:
        html_content += f"<li>{policy}</li>"
    
    html_content += """
                    </ul>
                </div>
            </div>

            <div class="section" id="autorun-entries">
                <button class="collapsible">Registry Auto-Run Entries</button>
                <div class="content">
                    <ul>
    """
    
    if autorun_entries:
        for entry in autorun_entries:
            html_content += f"<li>Name: {entry['Name']}, Executable: {entry['Executable']}, Path: {entry['Path']}</li>"
    else:
        html_content += "<li>No auto-run entries found or unable to retrieve entries.</li>"
    
    html_content += """
                    </ul>
                </div>
            </div>

            <div class="section" id="startup-entries">
                <button class="collapsible">Startup Folder Entries</button>
                <div class="content">
                    <ul>
    """
    
    if startup_entries:
        for entry in startup_entries:
            html_content += f"<li>File: {entry['File']}, Path: {entry['Path']}</li>"
    else:
        html_content += "<li>No startup folder entries found or unable to retrieve entries.</li>"
    
    html_content += """
                    </ul>
                </div>
            </div>

        </div>
        <script>
            var coll = document.getElementsByClassName("collapsible");
            for (var i = 0; i < coll.length; i++) {
                coll[i].addEventListener("click", function() {
                    this.classList.toggle("active");
                    var content = this.nextElementSibling;
                    if (content.style.display === "block") {
                        content.style.display = "none";
                    } else {
                        content.style.display = "block";
                    }
                });
            }
        </script>
    </body>
    </html>
    """

    with open("system_report.html", "w") as file:
            file.write(html_content)

    print("HTML report generated successfully.")

   
   


if __name__ == "__main__":
    user_choice = input("Do you want to generate an HTML or PDF report? (html/pdf): ").strip().lower()
    
    if user_choice == "html":
        generate_html_report()
    elif user_choice == "pdf":
        generate_pdf_report()
    else:
        print("Invalid choice. Please choose either 'html' or 'pdf'.")