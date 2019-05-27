from django.urls import path
from mainapp import views
app_name="mainapp"
urlpatterns=[

    path('index/',views.index,name='index'),
    path('detailpage/',views.detailpage,name='detailpage'),
    path('category/',views.category,name='category'),    ##图书分类
    path('categorylogic/',views.categorylogic,name='categorylogic'),
    path('register/',views.register,name='register'),
    path('register_ok/',views.register_ok,name='register_ok'),
    path('checkphone/',views.checkphone,name='checkphone'),
    path('checkpwd/',views.check_pwd,name='checkpwd'),
    path('checkrepwd/',views.check_repwd,name='checkrepwd'),
    path('getcaptcha/',views.getcaptcha,name='getcaptcha'),
    path('checkcaptcha/',views.checkcaptcha,name="checkcaptcha"),
    path('registerstatus/',views.register_status,name="registerstatus"),
    path('login/',views.login,name="login"),
    path("loginlogic/",views.loginlogic,name="loginlogic"),
    path("cart/",views.cart,name="cart"),
    path("addbook/",views.add_book,name="addbook"),
    path("delectbook/",views.delect_book,name="delectbook"),
    path("addone/",views.on_add,name="onadd"),
    path("cartcount/",views.cart_count,name="cartcount"),
    path("settleprice/",views.settle_price,name="settleprice"),
    path("quitpage/",views.quit_page,name="quitpage"),
    path("submitinfo/",views.submit_info,name="submitinfo"),
    path("dropbox/",views.drop_box,name="dropbox"),
    path("detailadd/",views.detail_add,name="detailadd"),
    path("sendcode/",views.send_code,name="sendcode"),
    path("manualinput/",views.manual_input,name="manualinput"),

    
]
