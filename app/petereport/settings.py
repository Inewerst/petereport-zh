"""
Django settings for petereport project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from django.utils.translation import gettext_lazy as _

from pathlib import Path
import time
import os
from config.startup import *
from config.petereport_config import PETEREPORT_MARKDOWN, DJANGO_CONFIG, PETEREPORT_TEMPLATES


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = DJANGO_CONFIG['secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DJANGO_CONFIG['debug']

ADMIN_ENABLED = DJANGO_CONFIG['admin_module']

ALLOWED_HOSTS = DJANGO_CONFIG['allowed_hosts']

DATA_UPLOAD_MAX_MEMORY_SIZE = DJANGO_CONFIG['upload_memory_size'] 

CSRF_TRUSTED_ORIGINS =  DJANGO_CONFIG['csrf_trusted_origins']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'martor',
    'django_bleach',
    'preport',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'petereport.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'preport.views.header_footer_data'
            ],
        },
    },
]

WSGI_APPLICATION = 'petereport.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ATOMIC_REQUESTS = True


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'en'

TIME_ZONE = DJANGO_CONFIG['time_zone']

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
   os.path.join(BASE_DIR, 'locale')
]

LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
    ('fr', _('French')),
    ('zh-hans', _('Chinese')),
)

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


###################### PETEREPORT ######################

MAIN_PROJECT = os.path.dirname(__file__)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(MAIN_PROJECT, 'static/'),
)

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)


# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# SESSION AGE 480 Minutes
SESSION_COOKIE_AGE = 480*60
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

TEMPLATES_ROOT = os.path.join(BASE_DIR, PETEREPORT_TEMPLATES['templates_root'])

TEMPLATES_DIRECTORIES = {}

TPLS_ROOT = TEMPLATES_ROOT
for tpl in os.listdir(TPLS_ROOT):
    tpl_path = os.path.join(TPLS_ROOT, tpl)
    if os.path.isdir(tpl_path):
        cst_list = []
        for cst in os.listdir(tpl_path):
            cst_path = os.path.join(tpl_path, cst)
            if os.path.isdir(cst_path):
                cst_list.append(cst)
        TEMPLATES_DIRECTORIES[tpl] = cst_list

###################### MARTOR ######################

# Choices are: "semantic", "bootstrap"
MARTOR_THEME = 'bootstrap'

# Global martor settings
# Input: string boolean, `true/false`
MARTOR_ENABLE_CONFIGS = {
    'emoji': 'false',       # to enable/disable emoji icons.
    'imgur': 'true',        # to enable/disable imgur/custom uploader.
    'mention': 'false',     # to enable/disable mention
    'jquery': 'true',       # to include/revoke jquery (require for admin default django)
    'living': 'false',      # to enable/disable live updates in preview
    'spellcheck': 'false',  # to enable/disable spellcheck in form textareas
    'hljs': 'true',         # to enable/disable hljs highlighting in preview
}

# To show the toolbar buttons
MARTOR_TOOLBAR_BUTTONS = [
    'bold', 'italic', 'horizontal', 'heading', 'pre-code',
    'blockquote', 'unordered-list', 'ordered-list',
    'link', 'image-link', 'image-upload', 'emoji', 
    'direct-mention', 'toggle-maximize', 'help'
]

# To setup the martor editor with title label or not (default is False)
MARTOR_ENABLE_LABEL = False

# Markdownify
MARTOR_MARKDOWNIFY_FUNCTION = 'martor.utils.markdownify' # default
MARTOR_MARKDOWNIFY_URL = '/martor/markdownify/' # default

# Markdown extensions (default)
MARTOR_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.nl2br',
    'markdown.extensions.smarty',
    'markdown.extensions.fenced_code',

    # Custom markdown extensions.
    'martor.extensions.urlize',
    'martor.extensions.del_ins',      # ~~strikethrough~~ and ++underscores++
    'martor.extensions.mention',      # to parse markdown mention
    'martor.extensions.emoji',        # to parse markdown emoji
    'martor.extensions.mdx_video',    # to parse embed/iframe video
    'martor.extensions.escape_html',  # to handle the XSS vulnerabilities
]

# Markdown Extensions Configs
MARTOR_MARKDOWN_EXTENSION_CONFIGS = {}

CSRF_COOKIE_HTTPONLY = False

# Upload to locale storage
MARTOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, 'images/uploads')
MARTOR_UPLOAD_URL = '/api/uploader/'  # change to local uploader
MARTOR_MEDIA_URL = os.path.join(PETEREPORT_MARKDOWN['media_host'], MEDIA_URL)

MARTOR_MARKDOWN_BASE_EMOJI_URL = 'https://github.githubassets.com/images/icons/emoji/'                  # default from github


# Maximum Upload Image
# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_IMAGE_UPLOAD_SIZE = 5242880  # 5MB

SERVER_CONF = DJANGO_CONFIG['server_host']

REPORTS_MEDIA_ROOT = os.path.join(BASE_DIR, PETEREPORT_TEMPLATES['storage_reports'])


# URL schemes that are allowed within links
ALLOWED_URL_SCHEMES = [
    "file", "http", "https", "data"
]

# https://gist.github.com/mrmrs/7650266
ALLOWED_HTML_TAGS = [
    "a", "abbr", "b", "blockquote", "br", "cite", "code", "command",
    "dd", "del", "dl", "dt", "em", "fieldset", "h1", "h2", "h3", "h4", "h5", "h6",
    "hr", "i", "iframe", "img", "input", "ins", "kbd", "label", "legend",
    "li", "ol", "optgroup", "option", "p", "pre", "small", "span", "strong",
    "sub", "sup", "table", "tbody", "td", "tfoot", "th", "thead", "tr", "u", "ul"
]

# https://github.com/decal/werdlists/blob/master/html-words/html-attributes-list.txt
ALLOWED_HTML_ATTRIBUTES = [
    "alt", "class", "color", "colspan", "datetime",  "data",
    "height", "href", "id", "name", "reversed", "rowspan",
    "scope", "src", "style", "title", "type", "width"
]


# BLEACH

# Which HTML tags are allowed
BLEACH_ALLOWED_TAGS = ['svg', 'g', 'polygon', 'path', 'text', 'title', 'img', 'p', 'b',
                    'i', 'u', 'em', 'strong', 'a', 'hr', 'h1', 'h2', 'h3', 'h4', 'h5', 'pre',
                    'code', 'blockquote', 'ul', 'ol', 'li', 'figcaption', 'table', 'td', 'tr',
                    'th', 'thead', 'br']

# Which HTML attributes are allowed
BLEACH_ALLOWED_ATTRIBUTES = ['href', 'title', 'style', 'alt', 'src', 'width', 'height',
                            'viewBox', 'id', 'class', 'transform', 'fill', 'stroke', 'points',
                            'd', 'text-anchor', 'x', 'y', 'font-size', 'font-family', 'font-weight',
                            'text-decoration', 'font-variant']

# Which CSS properties are allowed in 'style' attributes (assuming
# style is an allowed attribute)
BLEACH_ALLOWED_STYLES = [
    'font-family', 'font-weight', 'text-decoration', 'font-variant']

# Which protocols (and pseudo-protocols) are allowed in 'src' attributes
# (assuming src is an allowed attribute)
BLEACH_ALLOWED_PROTOCOLS = [
    'http', 'https', 'data'
]

# Strip unknown tags if True, replace with HTML escaped characters if
# False
BLEACH_STRIP_TAGS = True

# Strip comments, or leave them in.
BLEACH_STRIP_COMMENTS = False


# Init Application
initApplication()


