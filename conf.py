# --- Project Information ---
project = 'GEICO Insurance Guide'
copyright = '2026, Insurance Solutions Team'
author = 'Professional Web Dev Team'
release = '1.0'

# --- SEO & Title Configuration ---
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
html_static_path = ['_static']

# UPDATED: Match the PNG files I'm generating for you
html_logo = "_static/logo.png" 
html_favicon = "_static/favicon.png"

html_theme_options = {
    'logo_only': False, # Set to False so the Project Name shows next to the icon
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'sticky_navigation': True,
}

# Add this to force custom CSS injection
def setup(app):
    app.add_css_file('style.css')
