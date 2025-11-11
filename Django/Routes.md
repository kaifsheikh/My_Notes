# What is Routes?
1. Django ko batana ke “jab koi user ek specific URL open kare,
2. to kaunsa function ya page dikhana hai.”
3. Django ko batana ke user kis page par gaya hai aur us page ke liye kaunsa function (view) run karna hai. Har page ke liye alag route banana hota hai

## `Example : 01`

```py
# views.py -> File Name
from django.http import HttpResponse # Request and Response ko Manage karne ka liya import kiya hai

def abc(request):
    return HttpResponse("Welcome Django")

# urls.py -> File Name
from firstSite import views # import views.py 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/' , views.abc ),
]

# 'home/' -> yeah mera Route ka naam hai kch bhe rekh sekhte hai
# views.abc -> views.abc: Jab user '/home/' type karega, toh Django views.py file mein mojood abc naam ke function ko chala dega (jis mein aapne return HttpResponse("Welcome Django") likha tha).
```

# What is Dynamic Routes:

```py
# views.py -> File Name
from django.http import HttpResponse # Request and Response ko Manage karne ka liya import kiya hai

def courseDetail(request , courseId):
    return HttpResponse(f"Course Id : {courseId}")

# urls.py -> File Name
from firstSite import views # import views.py 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/<int:courseId>' , views.courseDetail ),
]
```

https://youtu.be/ZtiPjEarJyU?si=yWsWvDI2KyHMuxKg&t=628