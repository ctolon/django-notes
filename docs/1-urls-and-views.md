# Django Urls and Views

Bir app yaratıldığına routing için urls.py dosyası oluşturulur. Bu dosyada url'ler ve view'lar eşleştirilir. Django'nun url'leri eşleştirme yöntemi regex'e benzer.

views.py'da bir http response yaratma:
```python
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

urls.py'da view'ı eşleştirme:
```python
from django.urls import path
from . import views # burada views.py'daki view'ları import ediyoruz

urlpatterns = [
    path('', views.index, name='index')
]
```

Sonrasında yaratılan app'nin settings.py'daki INSTALLED_APPS listesine eklenmesi gerekir:

eklemek için iki yol var:
```python
'myapp.apps.MyappConfig'
'myapp'
```

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp.apps.MyappConfig'
]
```

url şeması tanımlandıktan sonra proje ile ilişkilendirilmesi gerekir. Bunun için proje urls.py dosyasına include edilir:

```python

from django.contrib import admin
from django.urls import path, include # burada include import edilir

# http://<host>:<port>/ ==> index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'))
]

```


