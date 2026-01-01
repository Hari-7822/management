# management/custom_ad.py

JAZZMIN_SETTINGS = {
    "site_title": "Admin Dashboard",
    "site_header": "Administration",
    "site_brand": "My Platform",
    "site_logo": None,  
    "login_logo": None,
    "login_logo_dark": None,
    "site_logo_classes": "img-circle",
    "site_icon": None,  
    
    "welcome_sign": "Welcome to the Admin Dashboard",
    "copyright": "Your Company Ltd © 2025",
    
    "search_model": [
        "auth.User",
        "auth.Group",
        "students.Student",  
        "Users.User",
    ],
    
    "user_avatar": None,
    
    "topmenu_links": [
        {
            "name": "Home",
            "url": "admin:index",
            "permissions": ["auth.view_user"]
        },
        
        {
            "name": "View Site",
            "url": "/",
            "new_window": True
        },
        
        {"model": "auth.User"},
        
        {"app": "students"},
        {"app": "chat"},
    ],
    
    "usermenu_links": [
        {"model": "auth.user"},
        {
            "name": "Documentation",
            "url": "#",  
            "new_window": True,
            "icon": "fas fa-book"
        },
    ],
    
    "show_sidebar": True,
    "navigation_expanded": True,
    
    "hide_apps": [],
    "hide_models": [],
    
    "order_with_respect_to": [
        "auth",
        "Users",
        "students",
        "chat",
        "utils",
    ],
    
    "custom_links": {
        "students": [
            {
                "name": "Student Reports",
                "url": "#",
                "icon": "fas fa-chart-bar",
                "permissions": ["students.view_student"]
            }
        ],
        "chat": [
            {
                "name": "Chat Analytics",
                "url": "#",
                "icon": "fas fa-chart-line",
                "permissions": ["chat.view_chat"]
            }
        ],
    },
    
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        
        "students": "fas fa-user-graduate",
        "students.Student": "fas fa-graduation-cap",
        
        "chat": "fas fa-comments",
        "chat.Message": "fas fa-comment",
        "chat.Room": "fas fa-door-open",
        
        "Users": "fas fa-id-card",
        "Users.User": "fas fa-user-circle",
        "Users.Profile": "fas fa-address-card",
        
        "utils": "fas fa-tools",
        
        "sites": "fas fa-globe",
        "contenttypes": "fas fa-th-list",
        "sessions": "fas fa-clock",
    },
    
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    
    "related_modal_active": True,
    
    "custom_css": None,  
    "custom_js": None,   
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    
    "changeform_format": "horizontal_tabs",
    
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
        "students.Student": "horizontal_tabs",
    },
    
    "language_chooser": False,
}


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-success",
    "accent": "accent-teal",
    "navbar": "navbar-dark navbar-success",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-success",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "materia",
    "dark_mode_theme": "cyborg",
}
