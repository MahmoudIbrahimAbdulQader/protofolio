import base64
from pathlib import Path
import textwrap
import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------------------------
# 1. Page Configuration & Contact Details
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Mahmoud Ibrahim | Data & ML Engineer Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".JPG", ".JPEG", ".PNG", ".WEBP")

CONTACT_EMAIL = "mahmoud.ibrahim.eg1@yahoo.com"
GMAIL_URL = f"https://mail.google.com/mail/?view=cm&fs=1&to={CONTACT_EMAIL}"
LINKEDIN_URL = "https://www.linkedin.com/in/eng--mahmoud-ibrahim"


def resolve_image_path(base_name: str) -> Path | None:
    """Resolve an image path from assets/ or the project root."""
    for directory in (ASSETS_DIR, BASE_DIR):
        if directory.is_dir():
            for ext in IMAGE_EXTENSIONS:
                candidate = directory / f"{base_name}{ext}"
                if candidate.is_file():
                    return candidate
    return None


def image_to_data_uri(base_name: str) -> str:
    """Encode a local image into a base64 data URI for HTML embedding."""
    img_path = resolve_image_path(base_name)
    if not img_path:
        return ""
    ext = img_path.suffix.lower().lstrip(".")
    mime_subtype = "jpeg" if ext in ("jpg", "jpeg") else ext
    encoded = base64.b64encode(img_path.read_bytes()).decode("utf-8")
    return f"data:image/{mime_subtype};base64,{encoded}"


@st.dialog("Certificate Preview")
def open_certificate_dialog(base_name: str, title: str) -> None:
    """Render a certificate preview inside a Streamlit modal dialog."""
    st.markdown(f"### {title}")
    img_path = resolve_image_path(base_name)
    if img_path:
        st.image(str(img_path), use_container_width=True)
    else:
        st.warning(
            f"Certificate image not found in `assets/` as `{base_name}.jpg` or `{base_name}.png`."
        )


# ---------------------------------------------------------------------------
# 2. Portfolio Content Definitions
# ---------------------------------------------------------------------------
SKILLS_DATA = [
    (
        "fas fa-spider",
        "Web Scraping Frameworks",
        "Python, Playwright, BeautifulSoup4, Requests, Asyncio, Regex, structured data extraction.",
    ),
    (
        "fas fa-database",
        "Database & SQL Design",
        "SQL, PostgreSQL, MySQL, Supabase, Relational & Dimensional Schemas (Star Schema), Query Optimization.",
    ),
    (
        "fas fa-brain",
        "Machine Learning",
        "Scikit-learn, TensorFlow, LightGBM, XGBoost, CatBoost, Optuna, Feature Engineering, Predictive Modeling.",
    ),
    (
        "fas fa-sitemap",
        "ETL & Data Engineering",
        "Pandas, NumPy, ETL/ELT Pipelines, Apache Kafka, Apache Airflow, Data Cleansing, Schema Mapping.",
    ),
    (
        "fas fa-code",
        "Programming & Data Processing",
        "Python (Data Engineering & ML), SQL (Complex Queries & Optimization), Data Transformation.",
    ),
    (
        "fas fa-cloud",
        "Cloud & Dev Tools",
        "Microsoft Azure, Docker, Git, VS Code, Jupyter Notebook, Miniconda.",
    ),
]

SERVICES_DATA = [
    (
        "fa-solid fa-spider",
        "Automated Web Scraping & Extraction",
        "Custom scrapers and asynchronous data extractors built to collect clean, structured datasets from dynamic websites and diverse sources.",
        ["Python", "Playwright", "BeautifulSoup4", "Asyncio"],
    ),
    (
        "fa-solid fa-database",
        "Database Design & Architecture",
        "Designing normalized relational schemas and dimensional analytical models (Star Schemas) with optimized SQL queries for fast retrieval and data integrity.",
        ["SQL", "PostgreSQL", "MySQL", "Supabase"],
    ),
    (
        "fa-solid fa-diagram-project",
        "Automated ETL/ELT Pipelines",
        "Building repeatable ingestion, transformation, and loading pipelines with workflow orchestration and event streaming for reliable data flow.",
        ["Pandas", "NumPy", "Apache Kafka", "Apache Airflow"],
    ),
    (
        "fa-solid fa-brain",
        "Predictive ML & Feature Engineering",
        "Developing classification, regression, and clustering models with domain feature engineering and hyperparameter optimization.",
        ["Scikit-learn", "LightGBM / XGBoost", "CatBoost", "Optuna"],
    ),
    (
        "fa-brands fa-microsoft",
        "Cloud & Containerized Workflows",
        "Structuring reproducible data workflows and containerized environments with Microsoft Azure and Docker.",
        ["Microsoft Azure", "Docker", "TensorFlow"],
    ),
    (
        "fa-solid fa-list-check",
        "Data Quality & Cleansing",
        "Transforming raw JSON, HTML, and unstructured text into clean, normalized tables with strict schema validation and missing-field handling.",
        ["Data Cleansing", "Regex", "Schema Validation"],
    ),
]

CERTIFICATIONS_DATA = [
    (
        "depi",
        "Microsoft Data Engineer Track",
        "DEPI",
        "rgba(56,189,248,0.10)",
        "#38BDF8",
        "rgba(56,189,248,0.20)",
        "Digital Egypt Pioneers Initiative (DEPI)",
        "Cloud data pipelines, Azure services, SQL Server & data engineering workflows.",
    ),
    (
        "huawei",
        "Huawei ICT Academy Certification",
        "Huawei",
        "rgba(239,68,68,0.10)",
        "#f87171",
        "rgba(239,68,68,0.20)",
        "Huawei ICT Academy",
        "Machine learning fundamentals, model training, and technical certification (Issued July 2025).",
    ),
    (
        "iti",
        "ITI Professional Training Program",
        "ITI",
        "rgba(16,185,129,0.10)",
        "#34d399",
        "rgba(16,185,129,0.20)",
        "Information Technology Institute (ITI)",
        "Front-end web development training and foundational engineering principles (Completed February 2025).",
    ),
]


def render_skills_cards() -> str:
    return "\n".join(
        f"""
        <div class="bg-[#131B2E] border border-[#222F43] rounded-2xl p-7 hover:border-sky-500/40 transition duration-300">
            <div class="w-12 h-12 rounded-xl bg-[#102136] border border-[#1D3B5E] text-sky-400 flex items-center justify-center text-xl mb-6">
                <i class="{icon}"></i>
            </div>
            <h3 class="text-xl font-bold text-white mb-3">{title}</h3>
            <p class="text-slate-400 text-sm leading-relaxed">{desc}</p>
        </div>
        """
        for icon, title, desc in SKILLS_DATA
    )


def render_services_cards() -> str:
    cards = []
    for icon, title, desc, tags in SERVICES_DATA:
        tags_html = "\n".join(
            f'<span class="text-[11px] px-2.5 py-1 rounded-md bg-slate-800/80 text-sky-300 border border-slate-700/60 font-mono">{tag}</span>'
            for tag in tags
        )
        cards.append(
            f"""
            <div class="group relative p-8 rounded-2xl bg-slate-900/50 border border-slate-800 hover:border-sky-500/50 transition-all duration-300 backdrop-blur-xl shadow-xl hover:-translate-y-2 flex flex-col justify-between">
                <div>
                    <div class="w-14 h-14 rounded-xl bg-sky-500/10 border border-sky-500/20 flex items-center justify-center text-sky-400 text-2xl mb-6 group-hover:scale-110 group-hover:bg-sky-500 group-hover:text-slate-950 transition duration-300 shadow-inner">
                        <i class="{icon}"></i>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-3 group-hover:text-sky-400 transition">{title}</h3>
                    <p class="text-slate-400 text-sm leading-relaxed mb-6">{desc}</p>
                </div>
                <div class="flex flex-wrap gap-1.5 pt-4 border-t border-slate-800/80">
                    {tags_html}
                </div>
            </div>
            """
        )
    return "\n".join(cards)


# ---------------------------------------------------------------------------
# 3. Global Styles & Fixed Top Navigation Bar
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=Inter:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap');

        html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
            background-color: #0B1120 !important;
            color: #f1f5f9 !important;
            font-family: 'Inter', 'Cairo', sans-serif !important;
            scroll-behavior: smooth !important;
        }

        #MainMenu, footer, header, [data-testid="stHeader"], [data-testid="stToolbar"] {
            display: none !important;
            visibility: hidden !important;
        }

        .block-container {
            padding-top: 74px !important;
            padding-bottom: 2.5rem !important;
            padding-left: 0 !important;
            padding-right: 0 !important;
            max-width: 100% !important;
        }

        [data-testid="stVerticalBlock"], [data-testid="stHorizontalBlock"], .element-container {
            overflow: visible !important;
        }

        iframe {
            border: none !important;
            display: block !important;
            max-width: 100% !important;
        }

        .portfolio-topbar {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            right: 0 !important;
            width: 100% !important;
            height: 64px;
            z-index: 999999 !important;
            background-color: rgba(11, 17, 32, 0.92);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(30, 41, 59, 0.9);
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 0 24px;
            box-sizing: border-box;
        }

        .portfolio-topbar-inner {
            width: 100%;
            max-width: 1152px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
        }

        .portfolio-brand {
            font-family: 'Fira Code', monospace;
            font-size: 18px;
            font-weight: 700;
            color: #ffffff !important;
            text-decoration: none !important;
            white-space: nowrap;
        }

        .portfolio-brand span {
            color: #38BDF8;
        }

        .portfolio-nav-links {
            display: flex;
            align-items: center;
            gap: 28px;
            font-size: 14px;
            font-weight: 500;
        }

        .portfolio-nav-links a {
            color: #cbd5e1 !important;
            text-decoration: none !important;
            transition: color 0.2s ease;
            white-space: nowrap;
        }

        .portfolio-nav-links a:hover {
            color: #38BDF8 !important;
        }

        .portfolio-cta {
            padding: 8px 20px;
            font-size: 12px;
            font-weight: 700;
            border-radius: 8px;
            background-color: #38BDF8;
            color: #020617 !important;
            text-decoration: none !important;
            box-shadow: 0 0 15px rgba(56, 189, 248, 0.30);
            transition: all 0.2s ease;
            white-space: nowrap;
        }

        .portfolio-cta:hover {
            background-color: #7dd3fc;
        }

        .cert-card-box > div[data-testid="stVerticalBlockBorderWrapper"] {
            background: rgba(30, 41, 59, 0.72) !important;
            backdrop-filter: blur(12px) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 16px !important;
            padding: 20px 24px !important;
            margin-bottom: 14px !important;
            transition: all 0.25s ease !important;
        }

        .cert-card-box > div[data-testid="stVerticalBlockBorderWrapper"]:hover {
            border-color: rgba(56, 189, 248, 0.40) !important;
            box-shadow: 0 10px 30px -10px rgba(56, 189, 248, 0.20) !important;
        }

        .cert-card-box div[data-testid="stButton"] > button {
            background-color: rgba(56, 189, 248, 0.12) !important;
            color: #38BDF8 !important;
            border: 1px solid rgba(56, 189, 248, 0.25) !important;
            border-radius: 12px !important;
            font-weight: 700 !important;
            font-size: 12px !important;
            padding: 8px 16px !important;
            min-height: 38px !important;
            white-space: nowrap !important;
            transition: all 0.2s ease !important;
        }

        .cert-card-box div[data-testid="stButton"] > button:hover {
            background-color: rgba(56, 189, 248, 0.22) !important;
        }

        @media (max-width: 768px) {
            .portfolio-nav-links {
                display: none;
            }
        }
    </style>

    <div class="portfolio-topbar" id="portfolio-topbar">
        <div class="portfolio-topbar-inner">
            <a href="#about" data-section="about" class="portfolio-brand">
                <span>&lt;</span>Mahmoud.DE &amp; ML <span>/&gt;</span>
            </a>
            <div class="portfolio-nav-links">
                <a href="#about" data-section="about">About</a>
                <a href="#expertise" data-section="expertise">Skills</a>
                <a href="#services" data-section="services">Services</a>
                <a href="#certifications" data-section="certifications">Certifications</a>
                <a href="#education" data-section="education">Education</a>
            </div>
            <a href="#contact" data-section="contact" class="portfolio-cta">Get In Touch</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# 4. Top Sections (About, Technical Expertise, Services)
# ---------------------------------------------------------------------------
profile_uri = image_to_data_uri("profile")
profile_img_html = (
    f'<img src="{profile_uri}" alt="Mahmoud Ibrahim" class="w-full h-auto block -mb-5">'
    if profile_uri
    else (
        '<div class="w-full h-48 bg-slate-800/90 flex items-center justify-center '
        'text-xs text-slate-400 p-4 text-center">Put profile.jpg in assets/</div>'
    )
)

top_html = textwrap.dedent(
    f"""<!DOCTYPE html>
<html lang="en" class="dark scroll-smooth">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config = {{
darkMode: 'class',
theme: {{
extend: {{
colors: {{
brand: {{
dark: '#0B1120',
card: '#1E293B',
accent: '#38BDF8',
blue: '#0284C7'
}}
}},
fontFamily: {{
sans: ['Inter', 'Cairo', 'sans-serif'],
mono: ['Fira Code', 'monospace']
}}
}}
}}
}}
</script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=Inter:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
<style>
body {{ font-family: 'Inter', 'Cairo', sans-serif; margin: 0; padding: 0; overflow: hidden; }}
.code-font {{ font-family: 'Fira Code', monospace; }}
.bg-grid {{
background-image: radial-gradient(rgba(56, 189, 248, 0.1) 1px, transparent 1px);
background-size: 24px 24px;
}}
</style>
</head>
<body class="bg-[#0B1120] text-slate-100 antialiased selection:bg-sky-500 selection:text-white bg-grid relative">

<div class="absolute top-0 left-1/2 -translate-x-1/2 w-[1000px] h-[500px] bg-gradient-to-b from-sky-500/10 via-blue-600/5 to-transparent blur-3xl pointer-events-none -z-10"></div>

<section id="about" class="pt-10 pb-14 px-6 max-w-6xl mx-auto flex items-center">
<div class="flex flex-col md:flex-row items-center gap-10 md:gap-14 w-full">
<div class="relative group shrink-0 w-36 md:w-48">
<div class="absolute -inset-0.5 bg-gradient-to-r from-sky-500 to-blue-600 rounded-2xl blur-sm opacity-30 group-hover:opacity-60 transition duration-500"></div>
<div class="relative overflow-hidden rounded-2xl border border-sky-400/60 shadow-md">
{profile_img_html}
</div>
</div>

<div class="flex-1 text-center md:text-left">
<div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-sky-500/10 border border-sky-500/20 text-sky-400 text-xs font-semibold mb-5">
<span class="w-2 h-2 rounded-full bg-sky-400 animate-ping"></span> Available for Data &amp; ML Engineering Roles
</div>
<h1 class="text-4xl md:text-5xl font-extrabold tracking-tight mb-2 text-white">Mahmoud Ibrahim</h1>
<h2 class="text-xl md:text-2xl font-bold text-sky-400 mb-5 code-font">Data Engineer &amp; Machine Learning Engineer</h2>
<p class="text-slate-300 leading-relaxed text-sm md:text-base mb-8 max-w-2xl">
Data Engineer and Machine Learning Engineer bridging business strategy with engineering rigor. Backed by an <strong class="text-white">IT Management</strong> background and specialized <strong class="text-white">DEPI &amp; GCI</strong> training, I build end-to-end ETL/ELT pipelines, relational database schemas, automated web scraping workflows, and machine learning models across diverse data types.
</p>
<div class="flex flex-wrap justify-center md:justify-start gap-4">
<a href="{LINKEDIN_URL}" target="_blank" rel="noopener noreferrer" class="px-6 py-3 rounded-xl bg-slate-800/80 hover:bg-slate-700 border border-slate-700 text-sm font-bold text-slate-200 transition flex items-center gap-2">
<i class="fab fa-linkedin text-lg text-sky-400"></i> LinkedIn Profile
</a>
<a href="{GMAIL_URL}" target="_blank" rel="noopener noreferrer" title="{CONTACT_EMAIL}" class="px-6 py-3 rounded-xl bg-sky-500/15 hover:bg-sky-500/25 border border-sky-500/40 text-sm font-bold text-sky-300 transition flex items-center gap-2">
<i class="fas fa-envelope text-base text-sky-400"></i> Gmail
</a>
</div>
</div>
</div>
</section>

<section id="expertise" class="py-14 px-6 max-w-6xl mx-auto">
<div class="mb-10 text-left">
<h2 class="text-3xl font-extrabold text-white tracking-tight mb-2">Technical Expertise</h2>
<p class="text-slate-400 text-sm">Technologies, libraries, and frameworks I leverage to build robust solutions.</p>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
{render_skills_cards()}
</div>
</section>

<section id="services" class="py-16 pb-20 px-6 relative max-w-7xl mx-auto">
<div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-sky-500/5 blur-[120px] rounded-full pointer-events-none"></div>

<div class="text-center space-y-4 mb-14 relative z-10">
<span class="px-4 py-1.5 rounded-full text-xs font-semibold bg-sky-500/10 text-sky-400 border border-sky-500/20 tracking-wider uppercase inline-block shadow-sm">
What I Offer
</span>
<h2 class="text-3xl md:text-5xl font-extrabold text-white tracking-tight">
Services &amp; <span class="text-transparent bg-clip-text bg-gradient-to-r from-sky-400 via-blue-400 to-indigo-500">Engineering Solutions</span>
</h2>
<p class="text-slate-400 text-sm md:text-base max-w-2xl mx-auto leading-relaxed">
End-to-end data and machine learning engineering across diverse data types: web extraction, database design, automated pipelines, and predictive modeling.
</p>
</div>

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 relative z-10">
{render_services_cards()}
</div>
</section>

</body>
</html>"""
)

components.html(top_html, height=2380, scrolling=False)

# ---------------------------------------------------------------------------
# 5. Certifications Section
# ---------------------------------------------------------------------------
_, cert_col, _ = st.columns([0.05, 0.9, 0.05])
with cert_col:
    st.markdown(
        """
        <div id="certifications-anchor" style="padding: 16px 24px 10px 24px; max-width: 1152px; margin: 0 auto;">
            <h2 style="color: #ffffff; font-size: 28px; font-weight: 800; margin: 0 0 6px 0; font-family: 'Inter', 'Cairo', sans-serif;">
                <span style="color: #38BDF8; margin-right: 12px;">🏅</span>Certifications &amp; Training
            </h2>
            <p style="color: #94a3b8; font-size: 13px; margin: 0; font-family: 'Inter', 'Cairo', sans-serif;">
                Verified professional credentials with certificate preview support.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for idx, (file_stem, title, badge, bg_b, fg_b, bd_b, org, desc) in enumerate(CERTIFICATIONS_DATA):
        st.markdown('<div class="cert-card-box">', unsafe_allow_html=True)
        with st.container(border=True):
            c_left, c_right = st.columns([4.5, 1.15], vertical_alignment="center")
            with c_left:
                st.markdown(
                    f"""
                    <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap; margin-bottom:4px;">
                        <span style="font-size:10px; font-weight:700; padding:2px 8px; border-radius:6px;
                                     background:{bg_b}; color:{fg_b}; border:1px solid {bd_b};">
                            {badge}
                        </span>
                        <span style="color:#ffffff; font-weight:700; font-size:16px;">{title}</span>
                    </div>
                    <div style="color:#cbd5e1; font-size:12px; font-weight:500; margin-bottom:3px;">{org}</div>
                    <div style="color:#94a3b8; font-size:12px;">{desc}</div>
                    """,
                    unsafe_allow_html=True,
                )
            with c_right:
                if st.button("🖼️ View Certificate", key=f"cert_btn_{idx}", use_container_width=True):
                    open_certificate_dialog(file_stem, title)
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# 6. Bottom Sections (Education & Footer with LinkedIn + Gmail Buttons)
# ---------------------------------------------------------------------------
bottom_html = textwrap.dedent(
    f"""<!DOCTYPE html>
<html lang="en" class="dark scroll-smooth">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
body {{ font-family: 'Inter', 'Cairo', sans-serif; margin: 0; padding: 0; overflow: hidden; }}
.glass-card {{
background: rgba(30, 41, 59, 0.7);
backdrop-filter: blur(12px);
border: 1px solid rgba(255, 255, 255, 0.08);
transition: all 0.3s ease;
}}
.glass-card:hover {{
border-color: rgba(56, 189, 248, 0.4);
box-shadow: 0 10px 30px -10px rgba(56, 189, 248, 0.2);
transform: translateY(-2px);
}}
</style>
</head>
<body class="bg-[#0B1120] text-slate-100 antialiased">

<section id="education" class="py-12 px-6 max-w-6xl mx-auto">
<div class="mb-10">
<h2 class="text-2xl md:text-3xl font-extrabold text-white mb-2">
<i class="fas fa-graduation-cap text-sky-400 mr-3"></i>Academic Education &amp; Specialized Tracks
</h2>
<p class="text-slate-400 text-xs md:text-sm">Formal academic qualifications and specialized professional tracks.</p>
</div>

<div class="space-y-6">
<div class="glass-card p-6 md:p-8 rounded-2xl">
<div class="flex flex-col md:flex-row justify-between md:items-center gap-3 mb-4">
<h3 class="text-lg md:text-xl font-extrabold text-white">Bachelor of Science in Information Technology Management (ITM)</h3>
<span class="px-4 py-1.5 rounded-full bg-slate-800 text-slate-300 text-[11px] font-bold border border-slate-700 w-fit shrink-0">
Expected Graduation: July 2028
</span>
</div>
<p class="text-sky-400 font-semibold text-xs md:text-sm mb-5">Faculty of Management Technology and Information Systems, Port Said, Egypt</p>
<div class="inline-flex items-center gap-2 px-4 py-2 rounded-lg bg-sky-500/10 text-sky-400 text-xs font-bold border border-sky-500/20 shadow-inner">
<i class="fas fa-star text-[#FBBF24]"></i> Academic Performance: GPA 3.56 / 4.00
</div>
</div>

<div class="glass-card p-6 md:p-8 rounded-2xl border border-slate-800 hover:border-sky-500/30 transition">
<div class="flex flex-col md:flex-row justify-between md:items-center gap-3 mb-3">
<h3 class="text-lg md:text-xl font-extrabold text-white">GCI Data Science Course (3 Months) — University of Tokyo (Matsuo Institute)</h3>
<span class="px-4 py-1.5 rounded-full bg-slate-800 text-slate-300 text-[11px] font-bold border border-slate-700 w-fit shrink-0">
Completed: October 2026
</span>
</div>
<p class="text-slate-400 text-xs md:text-sm leading-relaxed">
Three-month course focused on Python, Pandas, and Machine Learning fundamentals.
</p>
</div>
</div>
</section>

<footer id="contact" class="py-10 px-6 border-t border-slate-800/80 max-w-6xl mx-auto">
<div class="flex flex-col md:flex-row items-center justify-between gap-4">
<div class="text-xs text-slate-400 text-center md:text-left">
Mahmoud Ibrahim • Data Engineer &amp; Machine Learning Engineer • Alexandria, Egypt
</div>

<div class="flex flex-wrap items-center justify-center gap-3">
<a href="{LINKEDIN_URL}" target="_blank" rel="noopener noreferrer"
   class="px-5 py-2.5 rounded-xl bg-sky-500 hover:bg-sky-400 text-slate-950 text-xs font-bold transition flex items-center gap-2">
<i class="fab fa-linkedin-in"></i>
<span>LinkedIn</span>
</a>

<a href="{GMAIL_URL}" target="_blank" rel="noopener noreferrer" title="{CONTACT_EMAIL}"
   class="px-5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 hover:border-sky-400/50 text-sky-400 text-xs font-bold transition flex items-center gap-2">
<i class="fas fa-envelope"></i>
<span>Gmail</span>
</a>
</div>
</div>
</footer>

</body>
</html>"""
)

components.html(bottom_html, height=560, scrolling=False)

# ---------------------------------------------------------------------------
# 7. Parent-Container Navigation Controller
# ---------------------------------------------------------------------------
components.html(
    """
    <script>
    (function() {
        const win = window.parent;
        const doc = win ? win.document : null;
        if (!win || !doc) return;

        function resolveScrollContainer() {
            const selectors = [
                '[data-testid="stAppViewContainer"]',
                '[data-testid="stMain"]',
                '.main'
            ];
            for (const selector of selectors) {
                const el = doc.querySelector(selector);
                if (el && el.scrollHeight > el.clientHeight + 20) {
                    const overflowY = win.getComputedStyle(el).overflowY;
                    if (overflowY === 'auto' || overflowY === 'scroll') {
                        return el;
                    }
                }
            }
            return doc.documentElement;
        }

        function readScrollTop(container) {
            if (container === doc.documentElement || container === doc.body) {
                return win.scrollY || win.pageYOffset || container.scrollTop || 0;
            }
            return container.scrollTop || 0;
        }

        function writeScrollTop(container, value) {
            const target = Math.max(0, Math.round(value));
            if (container === doc.documentElement || container === doc.body) {
                win.scrollTo({ top: target, behavior: 'smooth' });
            } else {
                container.scrollTo({ top: target, behavior: 'smooth' });
            }
        }

        function getSectionY(section, container) {
            const iframes = Array.from(doc.querySelectorAll('iframe'));
            const currentTop = readScrollTop(container);
            const headerOffset = 72;

            if (section === 'about') return 0;
            if (section === 'expertise' && iframes[0]) {
                return iframes[0].getBoundingClientRect().top + currentTop + 370 - headerOffset;
            }
            if (section === 'services' && iframes[0]) {
                return iframes[0].getBoundingClientRect().top + currentTop + 980 - headerOffset;
            }
            if (section === 'certifications') {
                const certAnchor = doc.getElementById('certifications-anchor');
                if (certAnchor) {
                    return certAnchor.getBoundingClientRect().top + currentTop - headerOffset;
                }
            }
            if (section === 'education' && iframes[1]) {
                return iframes[1].getBoundingClientRect().top + currentTop - headerOffset;
            }
            if (section === 'contact') {
                return container.scrollHeight;
            }
            return 0;
        }

        doc.querySelectorAll('#portfolio-topbar a[data-section]').forEach(function(link) {
            if (link.dataset.navReady === '1') return;
            link.dataset.navReady = '1';
            link.addEventListener('click', function(event) {
                event.preventDefault();
                const section = this.getAttribute('data-section');
                const container = resolveScrollContainer();
                writeScrollTop(container, getSectionY(section, container));
            });
        });
    })();
    </script>
    """,
    height=0,
    scrolling=False,
)