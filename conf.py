# --- Project Information ---
project = 'GEICO Insurance Guide'
copyright = '2026, Insurance Solutions Team'
author = 'Professional Web Dev Team'
release = '1.0'

# --- SEO & Title Configuration ---
# This is what appears in the Google Search results tab
html_title = "GEICO Insurance | Get a Quote & Save 15% on Auto & Home"
html_short_title = "GEICO Quote Guide"

# --- General Configuration ---
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autosectionlabel',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# --- HTML Output Options ---
html_theme = 'sphinx_rtd_theme'

# Ensure your style.css is recognized
html_static_path = ['_static']

# This helps with branding on the sidebar
html_logo = "_static/logo.png" 
html_favicon = "_static/favicon.ico"

html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
}
