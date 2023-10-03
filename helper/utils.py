import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

def load_sidebar():
    show_pages(
        [
            Page("home.py", "/home/nkallergis"),
            Section("/home/nkallergis/bio"),
            Page("pages/bio/about.py", "./about"),
            Page("pages/bio/projects.py", "./projects"),
            Page("pages/bio/experience.py", "./experience"),
            Page("pages/bio/education.py", "./education"),
            Section("/home/nkallergis/blog"),
            Page("pages/blog/20231003.py", "./20231003"),
        ]
    )
    add_page_title()
