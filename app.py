from pathlib import Path

import streamlit as st
from PIL import Image

# PATH SETTINGS
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"assets"/"Mohibullah_Kamran_resume.pdf"
profile_pic = current_dir/"assets"/"profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Mohibullah Kamran"
PAGE_ICON = ":wave:"
NAME = "Mohibullah Kamran"
DESCRIPTION = """
Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "mohibullah.kamran@colorado.edu"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/mohibullah-k-a7307a20a/",
    "GitHub": "https://github.com/Mohib9",
    "Medium": "https://medium.com/@mohib94"
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 7 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Flight Instructor & ML Engineer | Pakistan Airforce**")
st.write("July, 2023 – Present")
st.write(
    """
- ► Air Crash Investigation
- ► Student Success Prediction
- ► Student Book Responses
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Machine Learning Intern | SkyIT**")
st.write("Feb, 2023 – May, 2023")
st.write(
    """
- ► Developed a Deep Learning Model to identify engine start/stop time through Signal Processing Audio Classification
- ► Integrated a scalable TFLite model to Android
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Machine Learning Fellow | Fellowship.AI**")
st.write("Apr, 2023 – June, 2023")
st.write(
    """
- ► Worked on the Development of a Robotic Arm for to optimize customized patient medicine production using PyTorch, PyBullet and CoppeliaSim.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Fighter Pilot | Pakistan Airforce**")
st.write("2017 - 2021")
st.write(
    """
- ► 800+ flying hours with Instructional Experience
- ► Teaching Fluid Dynamics, Aero-Engines & Meteorology
- ► Lead multiple aircraft in flight formation
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")