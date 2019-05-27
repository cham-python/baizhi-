from mainapp.models import Books


class CartItem():   ##这个有卵用呀
    def __init__(self,book,amount,perprice=None):
        self.amount = amount
        self.book=book
        self.per_price=perprice
        self.status = 1

class Cart():

    def __init__(self):   ###调用类方法会自动还行这个，
        self.save_price=0
        self.total=0
        self.cartitem=[]
    ###计算购物车中商品的节省金额一级总金额
    def sums(self):   ##这里得加书的市场价格，和当当价格的参数
        self.total_price=0
        self.save_price=0
        for i in self.cartitem:   ##
            self.total_price+=int(i.book.book_dprice)      ##这里存的不是queryset对象么？，i.属性不是属性的的值么，老师的家了i.book.属性
            self.save_price+=(int(i.book.book_price)-int(i.book.book_dprice))

    ##向购物车中添加书籍
    def add_book_toCart(self,bookid):
        print(bookid,"26hang,是传过来的bookid")
        for i in self.cartitem:
            print(i.book.book_id,"这个是储存的书的id")
            if int(i.book.book_id)==int(bookid):
                i.amount+=1
                print(i.amount,"这是amount的个数")
                self.sums( )
                print("进来来么，if的判断32行")
                return None
        book=Books.objects.filter(book_id=bookid)[0]
        print(book.book_dprice,"cart模块存入的对象")
        print("进来第几次：1111111111111111111111111111111111111111111111111111")
        permoney=book.book_dprice
        self.cartitem.append(CartItem(book=book,amount=1,perprice=permoney))    ####CartItem这里已经声明了一个了，所以应该有了
        print("这里也ok把")
        self.sums()
        print("zheli haineng jin么？36行")
    ##修改购物车的商品新信息
    def modify_cart(self,bookid,amount):
        for i in self.cartitem:
            if i.book.id==bookid:
                i.amount=amount
        self.sums()

    ##删除购物车
    def delecte_book(self,bookid):
        print(bookid,"这是删除的bookid")
        for i in self.cartitem:
            print("删除循环")
            if int(i.book.book_id)==int(bookid):
                print(i.book.book_id,"删除前的id")
                self.cartitem.remove(i)
                print(i.book.book_id,"删除后的id")
        print("删完了么？")
        self.sums()

 ##这是详情页的传输书籍的函数
    def detail_addbook(self,num,bookid):
        print(bookid, "63hang,是传过来的bookid")
        book = Books.objects.filter(book_id=bookid)[0]
        per_money = int(num)*int(book.book_dprice)
        self.cartitem.append(CartItem(book=book, amount=num,perprice=per_money))   ##把book和数量直接加里了
        self.total_price=int(book.book_dprice)*int(num)  ##总价格
        self.save_price=(int(book.book_price)-int(book.book_dprice))*int(num)
        print("zheli haineng jin么？36行")
























