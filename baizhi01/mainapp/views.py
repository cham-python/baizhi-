import random
import string
import hashlib
import os
from datetime import datetime
from django.core.mail import send_mail, EmailMultiAlternatives
from django.forms import models
from django.http import HttpResponse

from baizhi import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'amail_testameil.settings'##导入settings配置
from captcha.image import ImageCaptcha
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
from django.shortcuts import render,HttpResponse,redirect

from mainapp.cart import Cart, CartItem
from mainapp.models import Books, ClassBooks, TUser, CustomerAddress, ConfirmlEmail, UOrder, OrderItem


##注册渲染
def register(request):
    return render(request, "register.html")
def registerlogic(request):
    phone=request.GET.get('phone')
    print(phone,"9hang")
    return render(request, "register.html")
###检测用户名

def checkphone(request):
    """
    检测邮箱输入是否存在，这里没有正则验证，有时间一定要加正则验证
    :param request:
    :return:
    """
    phone=request.POST.get("phone")
    print(phone)
    result=TUser.objects.filter(email=phone)
    if result:
        request.session["phone_status"]=0
        return HttpResponse("error")
    else:
        if phone:
            request.session["phone_status"] = 1   ##这是电话或邮箱可有，存一个状态以备后面用
            print("25hang 判断phone_status")
            request.session["surephone"] = phone
            print(phone,'checkphone14行')
            return HttpResponse("right")
        else:
            return HttpResponse("error")


def check_pwd(request):
    """
    检测密码的ajax
    :param request:
    :return:
    """
    pwd = request.POST.get("password")
    request.session['password']=pwd
    ##待正则验证
    print(pwd)
    return HttpResponse("right")


def check_repwd(request):
    """
    检测二次密码的ajax
    :param request:
    :return:
    """
    pwd= request.session.get("password")
    repwd=request.POST.get('repassword')
    if pwd and repwd:
        if pwd == repwd:
            request.session["pwd_status"]=1
            print("判断pwd_status")
            request.session["surepwd"] = pwd
            return HttpResponse("right")
    print(pwd,repwd,"31hang")
    request.session["pwd_status"] = 0
    return HttpResponse("error")


def getcaptcha(request):
    """
    生成验证码
    :param request:
    :return:
    """
    image=ImageCaptcha()
    print(image,'46hang')
    code = random.sample(string.ascii_letters+string.digits,4)
    print(code,'48hang')##这个是列表么？？
    random_code=''.join(code)
    print(random_code,'50hang')
    request.session['code']=random_code
    data=image.generate(random_code)
    print(data)##这个是生成的对象么
    return HttpResponse(data,'image/png')


def checkcaptcha(request):
    """
    这里是之前的验证码，现在变为邮箱验证码的返回时的接受函数了,当邮箱验证通过后才能判断这个之前的验证的结果
    这是网络直接通过连接连过的函数
    :param request:
    :return:
    """
    captcha_code=request.GET.get("code")   ##获得的输入的验证码,如果成功直接跳转到index页面，如果不行还在注册页面
    print(captcha_code,'58hang')
    code=request.session.get('code')
    print(code,'115hang,验证码')
    if  code:
        if code == captcha_code:
            request.session["captcha_status"]=1
            print("captcha_status 状态")
            phone_status = request.session.get("phone_status")
            phone = request.session.get("surephone")
            pwd_status = request.session.get("pwd_status")
            pwd = request.session.get("surepwd")
            captcha_status = request.session.get("captcha_status")
            print(phone_status, pwd_status, captcha_status, "72hang状态")
            if phone_status and pwd_status and captcha_status:
                pwd1 = make_password(pwd)  ##进行加密
                TUser.objects.create(email=phone, password=pwd1)
                books = Books.objects.all().order_by('-shelve_time')[:7]
                editor_book = Books.objects.all().order_by("editor_recommend")[:7]
                return render(request, 'index.html', {"books": books, "editor_book": editor_book})
            else:
                print("78hang,errorhang ")
                return redirect("mainapp:register")
    request.session["captcha_status"] = 0
    return render(request,"register.html")


def manual_input(request):
    """
    注册：手动输入邮箱验证码的ajax函数
    但是不知道怎么样来获得code
    :param request:
    :return:
    """
    ##这是手动输入的验证码
    code = request.session.get("code")
    captcha=request.POST.get("captcha")
    print(code,captcha,"1111111111111111149149149149")
    if str(code) ==str(captcha):
        print(code,captcha,"手动输入的ajax")
        request.session["captcha_status"] = captcha
        return HttpResponse("right")
    return HttpResponse("error")

def register_status(request):
    """
    这是注册所有验证都通过的添加数据到数据库的函数
    :param request:
    :return:
    """
    phone_status=request.session.get("phone_status")
    phone=request.session.get("surephone")
    request.session["reg_session"]=phone
    pwd_status=request.session.get("pwd_status")
    pwd=request.session.get("surepwd")
    captcha_status=request.session.get("captcha_status")
    print(phone_status,pwd_status,captcha_status,"72hang状态")
    if phone_status and pwd_status and captcha_status:
        pwd1=make_password(pwd)  ##进行加密
        TUser.objects.create(email=phone,password=pwd1)
        return redirect("mainapp:register_ok")
    else:
        print("78hang,errorhang ")
        return redirect("mainapp:register") ##弹出alert()进行告诫不能注册

def post_email(code,email):
    """
    是发送邮件的函数
    :param email:
    :param code:
    :return:
    """
    subject='python157'
    from_email='zzb515153177@sina.com'
    text_content = "欢迎访问,祝贺您收到我的文件,您的验证码为{}".format(code)
    html_content = '<p>感谢注册<a href="http://{}/?code={}"target=blank>www.baidu.com</a>,\欢迎你来验证你的邮箱,验证码为，验证结束你就可以登录了！</p>'.format('127.0.0.1:8000/mainapp/checkcaptcha',code)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
    ###发送邮件所执行的方法以及所需参数
    msg.attach_alternative(html_content, "text/html")
    ##发送html文本内容
    msg.send()
    print("发送出去就牛逼")


def send_code(request):
    """
    这里才是发送ajax的邮件函数
    :param request:
    :return:
    """
    email = request.POST.get("email")
    code = request.session.get("code")
    print(email, code, "119hang")
    post_email(code,email)
    return HttpResponse("hehe")




def register_ok(request):
    """
    注册ok,注册不ok返回
    :param request:
    :return:
    """

    return render(request,"register ok.html")

##渲染登录
def login(request):
    return render(request,"login.html")
##登录逻辑
def loginlogic(request):
    email=request.GET.get("email")
    pwd=request.GET.get("password")
    result=TUser.objects.filter(email=email)[0]  ##
    print(result)
    print(pwd,result.password,"两个密码行" )
    print(check_password(pwd,result.password),"105hang密码的验证")
    login_remind=request.session.get("captcha_status")
    print(login_remind)
    flag_cart_login=request.GET.get("flag")
    if result:  ##说明有这个值，已经注册完全了
        if check_password(pwd,result.password) and login_remind:
            books = Books.objects.all().order_by('-shelve_time')[:7]
            editor_book = Books.objects.all().order_by("editor_recommend")[:7]
            flag_cart=request.session.get("flag_cart")  ##这是判断是返回购物车还是返回主页面
            print(flag_cart,121)
            if "flag_cart"==flag_cart:
                print("这是进入购物车页面")
                request.session["login"] = "login"
                request.session["user_id"] = result.user_id  ###用户的id以备能够全局使用，以为只有一个用户

                return render(request,"car.html",{"name":"cham"})
            elif "cart"== str(flag_cart_login):
                return render(request, "car.html",{"name":"cham"})
            else:
                print("这是进入index页面")
                request.session["login"] = "login"
                request.session["user_id"] = result.user_id  ###用户的id以备能够全局使用，以为只有一个用户

                return render(request, 'index.html', {"books": books, "editor_book": editor_book,"name":"cham"})
        else:   ##是验证码错误的时候
            print("验证码为空")
            return render(request,"login.html")
    else:
        return render(request,"login.html")
def login_captcah(request):
    """
    登录的验证码的ajax的函数
    :param request:
    :return:
    """
    code=request.GET.get("code")
    gene_code = request.session.get("code")
    if str(code)==str(gene_code):
        request.session["login_remind"]="success"
        return HttpResponse("right")
    return HttpResponse("error")



##登出的渲染页面
def quit_page(request):
    books = Books.objects.all().order_by('-shelve_time')[:7]
    editor_book = Books.objects.all().order_by("editor_recommend")[:7]
    request.session["login"]="quit"
    return render(request, 'index.html', {"books": books, "editor_book": editor_book})
    # return redirect("mainapp:index")
##主页显示
def index(request):
    books=Books.objects.all().order_by('-shelve_time')[:7]
    editor_book=Books.objects.all().order_by("editor_recommend")[:7]
    return render(request, 'index.html',{"books":books,"editor_book":editor_book})
# ##图书详情页
def detailpage(request):
    book_id=request.GET.get('detail_id')
    onebook=Books.objects.filter(book_id=book_id)[0]
    cart=request.session.get("cart")
    print(type(cart))
    print(cart)
    if cart:
        for i in cart.cartitem:
            if int(i.book.book_id)==int (book_id):
                count=i.amount
                return render(request,'Book details.html',{"onebook":onebook,"count":count})
        else:
            return render(request,'Book details.html',{"onebook":onebook,"count":1})
    else:
        return render(request,'Book details.html',{"onebook":onebook,"count":1})
###分类连接
def category(request):
    l1=[]
    l2=[]
    sp_id=request.GET.get('first_class')
    p_id=int(sp_id)
    sc_id=request.GET.get('second_class')
    c_id=int(sc_id)
    number=request.GET.get('number')   ##这是分页的页码
    print(p_id,c_id,number,"112行的P_id,c_id,number")
    print(type(number),"113hang")  ##返回的的是一个none类型
    print(type(p_id), "114hang")
    print(type(c_id), "115hang")
    if not p_id:     ##取的是一个子类所有的全部，因为父类为零
        print("进来否一级分类")  ##父类为0 ，才求的子类
        c_id1=str(c_id)
        page_book = Books.objects.filter(second_class=c_id1)
        print(c_id, '128hang')
        print(page_book, '129hang')
        if not number:
            number = 1
            print("shi 1 么，145行")
        paginator = Paginator(page_book, per_page=2)
        page = paginator.page(number)
        print(page_book, "38行", {"page": page})
        return render(request, 'booklist.html', {"page": page, "p_id": sp_id, "c_id": sc_id, "number_insert": number})
    elif c_id==0:  ##因为所有的子类不能为零，但是，返回的连接的大类不能为零，子类可以为零，子类为零时是去的大类的页码
        ##判读一下是什么
        p_id1 = str(p_id)
        result = ClassBooks.objects.filter(category_pid=p_id1)  # 这是classbook的queryset对象 ，##根据父类id进行的查找calss_category的queryset对象，books里储存的是二级类
        print(result,"153hang 判断输入的页数")
        for i in result:
            id = i.category_id  ## 这里是查找到的子类id
            l1.append(id)
            print(l1)
        if not number:  ###number返回的是一个none值
            number = 1
        page_book = Books.objects.filter(second_class__in=l1)
        paginator = Paginator(page_book, per_page=2)
        page = paginator.page(number)
        print(page_book, "38行", {"page": page})
        return render(request, 'booklist.html', {"page": page,"p_id": sp_id, "c_id": sc_id})

    else :   ##取的是一个子类的所有书
        result=ClassBooks.objects.filter(category_pid=p_id) #这是classbook的queryset对象 ，##根据父类id进行的查找calss_category的queryset对象，books里储存的是二级类
        for i in result:
            id=i.category_id     ## 这里是查找到的子类id
            l1.append(id)
            print(l1)
        if  not number:  ###number返回的是一个none值
            number=1
        page_book=Books.objects.filter(second_class__in=l1)
        paginator = Paginator(page_book,per_page=2)
        page=paginator.page(number)
        print(page_book,"38行",{"page":page})
        return render(request,'booklist.html',{"page":page,"p_id":p_id,"c_id":c_id,"number_insert":number})

def categorylogic(request):
    ##穿过来的是两个一级分类id,二级分类id,（关联的是category_pid）通过查到分类表一级分类id,可以查到二级,
    result= ClassBooks.objects.filter(category_pid=1)
    return render(request,'booklist.html')
###购物车渲染
def cart(request):
    cart=request.session.get("cart")
    return render(request,"car.html")

###
def add_book(request):
    """
    这是详情页点击购物车，添加图书的
    :param request:
    :return:
    """
    book_id=request.GET.get("book_id") ##id获取的是书的id,这里的id应该是每个书后面绑定的id
    print(book_id,"197hang的book_id")
    cart =request.session.get("cart")  ##取的是存session中的cart
    print(cart,"199hang获得的购物车")

    ##判断cart存在与否
    if cart is None:
        cart=Cart()
        print(cart,"224行cat测试")
        cart.add_book_toCart(bookid=book_id)  ##这里传的是bookid，在模块中就添加了，添加的是书和数量，价格在另外一个方法中
        request.session["cart"]=cart    ##将购物车存入session
        print("成功否1")
        return HttpResponse("hehe")
    else:   ##cart存在
        cart.add_book_toCart(bookid=book_id)  ##这是存在的购物车的添加
        request.session["cart"]=cart
        print("成功否2")
        return  HttpResponse("haha")


###删除购物车书籍
def delect_book(request):
    """
    点击删除，把通过书的id都需要改变了，购车一定与这项，所以都能取到，存session就好
    :param request:
    :return:
    """
    print("进入删除")
    del_id=request.GET.get("delect_id")
    cart=request.session.get("cart")
    for i in cart.cartitem:
        if int(i.book.book_id)== int(del_id):
            cart.total_price=int(cart.total_price)-int(i.book.book_price)*int (i.amount)
            print("不知道这里能不能进来，民天见")
            cart.save_price=int(cart.save_price)-(int(i.book.book_price)-int(i.book.book_dprice))*int(i.amount)
            cart.cartitem.remove(i)
            request.session["cart"] = cart
    return redirect("mainapp:cart")


def on_add(request):
    """
    详情页进行加的ajax操作函数
    :param request:
    :return:
    """
    num_book1=request.GET.get("num_book")
    num_book=int(num_book1)
    cart=request.session.get("cart")
    amount1=cart.CartItem.amount
    amount=int(amount1)
    print(amount,"是存储的书的数量")
    if int(num_book1) < 1 :
        amount=1
    else:
        print("输入的数值正确并且合法 ,236hang" )
        amount=num_book+amount
        print(amount,"打印一下数量238hang")
        cart.CartItem.amount=amount   ##为了在类中从新存数量
        request.session["cart"]=cart
    return HttpResponse(amount)  ##返回的是存入的数


def cart_count(request):
    """
    这里是购物车点击加减的ajax函数，加减已经在ajax里面算完了，所以传过来的就是要存的数值了
    并且已经判断完是加数还是减数，amonut,total_price  都已经算完了。
    :param request:
    :return:
    """
    cart = request.session.get("cart")
    # print(type(cart.total_price),"获取的是什么对象")
    print(cart,"判断购物车")
    book_id = request.POST.get("book_id")
    num_book = request.POST.get("num_book")     ###能够获取 book_id，num_book
    print(type(book_id), type(num_book))
    book = Books.objects.filter(book_id=book_id)[0]
    per_price=book.book_dprice
    print(book.book_id, "对象249")
    print(book_id, num_book, "一个是book_id,一个是num_book  248hang")
    for i in cart.cartitem:
        if int(book_id) == int (i.book.book_id):
            ###如果这本书存在，在原有的基础上进行添加
            print("书籍存在")
            exit_amount=i.amount
            print(exit_amount,"存在的书的数量")
            i.amount=int(exit_amount)   #####在.py文件中只添加一本，而在这里需要加很多本
            print(i.amount,"添加后书的数量")
            ##比对数量判断是加。。。。还是减
            if int(num_book)>int(i.amount):   ##这里就是加了，
                cart.total_price=int(cart.total_price)+int(book.book_dprice)
                total_price=cart.total_price
                print(  cart.total_price,"计算之后书的价格")
                save_price=cart.save_price
                cart.save_price=int(book.book_price)-int(book.book_dprice)+int(save_price)
                cart_save_price=cart.save_price
                print(cart_save_price,"计算已经替换的价格")
                i.amount=int(i.amount+1)

                request.session["cart"]=cart
                return JsonResponse({"per_price": per_price, "save_price": cart_save_price,"total_price":total_price,"amount":i.amount})

            else:
                cart.total_price = int(cart.total_price) - int(book.book_dprice)
                print(cart.total_price, "计算之后书的价格")
                total_price = cart.total_price
                cart.save_price = int(cart.save_price)-int(book.book_price) + int(book.book_dprice)
                cart_save_price=cart.save_price
                print(cart.save_price, "计算已经替换的价格")
                i.amount = int(i.amount)-1
                request.session["cart"] = cart
                print("详情添加已有书籍成功")
                cart=request.session.get("cart")
                a=cart.save_price
                print(a)
                return JsonResponse({"per_price": per_price, "save_price": cart_save_price,"total_price":total_price,"amount":i.amount})



def detail_add(request):
    """
    这里是详情页的添加书籍的函数,1.判断有没有购物车，如果有有没有这本书框，如果有把数值显示到输入框中
    进入详情的ajax
    这里只需改变session里的值即可，因为它到时候会跳转。
    :param request:
    :return:
    """
    print("进入详情的ajax")
    cart = request.session.get("cart")
    book_id = request.GET.get("book_id")
    num_book = request.GET.get("num_book")     ###能够获取 book_id，num_book
    print(num_book,"这是数量是从输入框得来的数量")
    print(type(book_id), type(num_book))
    book = Books.objects.filter(book_id=book_id)[0]
    per_price=book.book_dprice
    print(book.book_id, "对象249")
    print(book_id, num_book, "一个是book_id,一个是num_book  248hang")
    if cart:
        for i in cart.cartitem:
            if int(book_id) == int (i.book.book_id):
                ###如果这本书存在，在原有的基础上进行添加
                print("书籍存在")
                if int(num_book)>int(i.amount):  ##这里是增加书籍了
                    print(i.amount,"添加后书的数量")
                    print(cart.total_price,book.book_dprice,i.amount,num_book,"336行 数据")
                    cart.total_price=int(cart.total_price)+int(book.book_dprice)*(int(num_book)-int(i.amount))
                    print(  cart.total_price,"计算之后书的价格")
                    save_price=cart.save_price
                    cart.save_price=(int(book.book_price)-int(book.book_dprice))*(int(num_book)-int(i.amount))+int(save_price)
                    print(cart.save_price,"计算已经替换的价格")
                    i.amount = int(num_book)  ##傻屌这里的数据用来拿来计算，你先把值附了，值永远不该
                    request.session["cart"]=cart
                    print("书存在加")
                    cart=request.session.get("cart")
                    print(cart.total_price,"存进去了么，这是349行的存储的total_price")
                    return JsonResponse({"per_price": per_price, "save_price": cart.save_price, "total_price": cart.total_price,"amount": i.amount})
                else:

                    print(i.amount, "添加后书的数量")
                    cart.total_price = int(cart.total_price) - int(book.book_dprice) * (int(i.amount)-int(num_book))
                    print(cart.total_price, "计算之后书的价格")
                    save_price = cart.save_price
                    cart.save_price = int(save_price)-(int(book.book_price) - int(book.book_dprice)) * (int(num_book) - int(i.amount))
                    print(cart.save_price, "计算已经替换的价格")
                    i.amount = int(num_book)  #####在.py文件中只添加一本，而在这里需要加很多本
                    request.session["cart"] = cart
                    print("书存在减")
                    return JsonResponse({"per_price": per_price, "save_price": cart.save_price, "total_price": cart.total_price,"amount": i.amount})

        else:  ##购物车存在而书籍不存在的情况
            print("书籍不存在")
            book = Books.objects.filter(book_id=book_id)[0]
            cart.cartitem.append(CartItem(book=book, amount=num_book))
            cart_total_price = int(cart.total_price) + int(book.book_dprice) * (int(num_book))
            print("这个是能够已经存入的验证")
            cart.total_price = cart_total_price
            save_price = cart.save_price
            cart.save_price = (int(book.book_price) - int(book.book_dprice)) * (int(num_book)) + int(save_price)
            request.session["cart_status"] = cart
            print("书不存在")
            return HttpResponse("hehe")
    elif cart is None:  ##购物车不存在
        cart = Cart()
        cart.detail_addbook(num=num_book,bookid=book_id)
        request.session["cart"] = cart
        print("购物车不存在")
        return HttpResponse("hehe")
###这里是结算的渲染函数
def settle_price(request):
    flag_cart=request.GET.get("flag_cart")  ##这里是获取的结算的flag
    print(flag_cart)
    statu=request.session.get("login")
    if "login"==statu:  ###判断状态，如果有登录状态直接返回到地址那个页面
        user_id=request.session.get("user_id")
        print(user_id,"user_id")
        ##能够通过关联的表的id获取所有的在一个用户下的地址id
        address=CustomerAddress.objects.filter(user_id=user_id).values()  ##获取一个列表里是字典的Queryset属性

        print(address,"是取出的地址的Queryset对象  313hang ")
        return render(request, "indent.html", {"address":address})
    else:
        request.session["falg_cart"] = flag_cart
        return render(request,"login.html")


###表单提交的函数，
def submit_info(request):
    """
    这里是当提交订单进行把地址信息进行对比，存入到数据库的操作
    :param request:
    :return:
    """
    amount=0    ##订单数，即有多少本数
    receive_name=request.GET.get("rec_name")
    print("1")
    user_add=CustomerAddress.objects.filter(receive_name=receive_name)
    print("2")
    add_detail=request.GET.get("deta_add")
    print("3")
    zipcode=request.GET.get("code")
    print("4")
    telephone=request.GET.get("pho")
    mobile_phone=request.GET.get("tel")
    user_id=request.session.get("user_id")
    cart=request.session.get("cart")
    print("5")
    if user_add:
        print("有这个地址")
        add_id=user_add[0].ad_id
        # for i in cart.cartitem:
        #     print("进入循环")
        #     book_dprice = i.book.book_dprice
        #     book_id=i.book.book_id
        #     add_id=int(add_id)
        #     user_id=int(user_id)
        #     book_dprice=int(book_dprice)
        #     amount=i.amount
        #     amount=int(amount)
        #     amount+=amount
        #     ##进行数量的填充
        #     print(add_id,book_dprice,book_id,amount,"这个是form系列参数")
        #     # UOrder.objects.create(order_num=1 ,price=1,user_id=1,order_addid=1)     ###order_num = amount,产生
        #     # UOrder.objects.create(order_num=1 ,price=book_dprice,user_id=user_id,order_addid=add_id)     ###order_num = amount,产生
        # print("这里应该能好用")
        # order=UOrder.objects.filter("")  ##取订单的信息
        # total_price=cart.total_price
        # print("应该是下面的值报错")
        # for i in order:
        #     order_id=i[0].order_id
        #     order_id=order_id["order_id"]
        #     print(order_id,"这是id")
        #     OrderItem.objects.creat(shop_itemid=order_id,shop_number=amount,total_price=total_price)


        return render(request,"indent ok.html")
    else:
        # print("进入到没有的地址")
        # CustomerAddress.objects.create(receive_name=receive_name,add_detail=add_detail,zipcode=zipcode,telephone=telephone,mobile_phone=mobile_phone,user_id=user_id)
        # add = CustomerAddress.objects.get("receive_name")
        # add_id=add.id
        # for i in cart.cartitem:
        #     name = i.book.book_name
        #     book_dprice = i.book.book_dprice
        #     book_id = i.book.book_id
        #     amount = i.amount
        #     amount = int(amount)
        #     amount += amount
        #     ##进行数量的填充
        #     UOrder.objects.create(order_num=1, price=book_dprice, user_id=user_id,order_addid=add_id)  ###order_num = amount,产生
        # order = UOrder.objects.filter("user_id")  ##取订单的信息
        # total_price = cart.total_price
        # for i in order:
        #     order_id = i[0].order_id
        #     OrderItem.objects.creat(shop_itemid=order_id, shop_number=amount, total_price=total_price)
        return render(request, "indent ok.html")
##是下拉框的点击的ajax的返回值函数
def drop_box(request):
    print("drop_box")
    ad_id=request.POST.get("ad_id")
    print(ad_id)
    add = CustomerAddress.objects.filter(ad_id=ad_id)
    print(add)
    def mydefault(n):
        if isinstance(n, CustomerAddress):
            return {'id': n.ad_id, 'name': n.receive_name, 'address': n.add_detail, 'zipcode': n.zipcode, 'telephone': n.telephone,
                    'phone': n.mobile_phone, "user_id": n.user_id}
    print("可以吧")
    return JsonResponse(list(add), safe=False, json_dumps_params={"default": mydefault})

































