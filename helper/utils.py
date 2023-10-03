import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

def load_sidebar():
    show_pages(
        [
            Page("home.py", "/home/nkallergis"),
            Section("/home/nkallergis/bio"),
            Page("pages/bio/about.py", "About"),
            Page("pages/bio/projects.py", "Projects"),
            Page("pages/bio/experience.py", "Experience"),
            Page("pages/bio/education.py", "Education"),
            Section("/home/nkallergis/blog"),
            Page("pages/blog/20231003.py", "Initial commit"),
            Section("/home/nkallergis/notes"),
            Page("pages/notes/ios_cli_accounting.py", "Cisco IOS - CLI accounting"),
            Page("pages/notes/django_verbose_name_plural.py", "Django - Verbose name plural"),
            Page("pages/notes/git_init_repo.py", "Git - Init repo"),
            Page("pages/notes/nautobot_secrets.py", "Nautobot - Retrieve Secrets"),
            Page("pages/notes/ping_mtud.py", "Ping MTUD"),
            Page("pages/notes/powershell_dns_per_domain.py", "Powershell - DNS per domain"),
            Page("pages/notes/powershell_wsl2_port_forward.py", "Powershell - Port forward for WSL2"),
        ]
    )
    add_page_title()
