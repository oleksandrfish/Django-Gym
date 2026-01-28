import os
from pathlib import Path
from dotenv import load_dotenv

                                                                
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')

                                                              
                                                                       

                                                                  
SECRET_KEY = 'django-insecure-z0)6mvns1y51k^gk+sizg3m024kl#ttzr)c&jiuh4f^hcr2z_r'

                                                                 
DEBUG = True

ALLOWED_HOSTS = ['*']


                        

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'treners.apps.BarbersConfig',
    'services',
    'home',
    'favorites',
    'reviews',
    'storages',
    'rest_framework',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoproj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'favorites.context_processor.favorite_barbers_count',
                'home.context_processors.ui_text',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoproj.wsgi.application'


          
                                                               

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


                     
                                                                              

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

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


                      
                                                    

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


                                        
                                                           

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
                                   
    
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

                                                                
                                                                

STATIC_LOCATION = "static"
MEDIA_LOCATION = "media"

                         
                                   
                                 

                                                  
                                                                     
                                                                         
                                                                       

        
                                                    
                                                                

              
                  
                                                                    
                      
                                                       
                                                 
                                               
                                                           
            
        
                      
                                                                    
                      
                                                        
                                                 
                                               
                                                           
            
        
   
