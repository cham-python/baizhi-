from django.test import TestCase
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "baizhi.settings")
# Create your tests here.
django.setup()
from mainapp.models import Books
# Books.objects.create(book_id=1,book_name="名人传",book_author="罗曼·罗兰",book_publish="译林出版社",word_count=268000,page_count=452,open_type=16,book_page='凸版二号',book_price=40,book_dprice=32,editor_recommend=86,score='20175470-1_l.jpg',book_serice='名著',putaway_date='2010-9-18',print_count=2,stock=130,shelve_time='2019-1-3',customer_score=78,market_status=1,sale_count=43,author_score=11,first_class=5,second_class=6)
# Books.objects.create(book_id=1,book_name='名人传',book_author='罗曼罗兰',book_publish='',version='1',word_count=268000,page_count='452',open_type=32,book_page=,book_wrapper='平装',book_price=40,book_dprice=32,editor_recommend=86,score='20175470-1_l.jpg',book_serice='名著',putaway_date='2010-9-18',print_count=2,stock=130,shelve_time='2019-1-3',customer_score=78,market_status=1,sale_count=43,author_score=11,first_class=1,second_class=11)
# Books.objects.create(book_id=2,book_name='哈哈',book_author='洪恩赐',book_publish='江西教育出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=85,score='22860102-1_l_1.jpg',book_serice='哲学',putaway_date='2010-9-18',print_count=2,stock=130,shelve_time='2019-1-3',customer_score=78,market_status=1,sale_count=43,author_score=87,first_class=1)
# Books.objects.create(book_id=3,book_name='福尔摩斯',book_author='阿瑟·柯南·道尔',book_publish='国际文化出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=82,score='20531088-1_l_4.jpg',book_serice='小说',putaway_date='2010-9-18',print_count=2,stock=130,shelve_time='2019-1-3',customer_score=78,market_status=1,sale_count=43,author_score=87,first_class=1)
# Books.objects.create(book_id=4,book_name='三国演义',book_author='吴承恩',book_publish='教育出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=63,score='21015000-1_l_2.jpg',book_serice='名著',putaway_date='2010-9-18',print_count=2,stock=130,shelve_time='2019-1-3',customer_score=78,market_status=1,sale_count=43,author_score=87,first_class=1)
# Books.objects.create(book_id=5,book_name='遇见未知的自己',book_author='和云峰',book_publish='长江文艺出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=85,score='22855492-1_l_3.jpg',book_serice='社会',putaway_date='2010-9-18',print_count=2,stock=130,shelve_time='2019-1-3',customer_score=78,market_status=1,sale_count=43,author_score=87,second_class=13,first_class=1)
# Books.objects.create(book_id=6,book_name='遇见未知的自己',book_author='张忠恕',book_publish='天津人民出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=63,score='1900542997-1_l_4.jpg',book_serice='社会',putaway_date='2010-9-18',print_count=2,stock=130,shelve_time='2019-1-3',customer_score=78,market_status=1,sale_count=43,author_score=87,second_class=14,first_class=1)
# Books.objects.create(book_id=74,book_name='之火女孩',book_author='查克·温迪格',book_publish='国际文化出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=88,score='1900560686-1_l_8.jpg',book_serice='小说',putaway_date='2010-9-18',print_count=2,stock=130,shelve_time='2019-1-3',customer_score=78,market_status=1,sale_count=43,author_score=87,second_class=13,first_class=1)
# Books.objects.create(book_id=8,book_name='遇见未知的自己',book_author='我自己写的',book_publish='教育出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=86,score='22876893-1_l.jpg',book_serice='社会',putaway_date='2010-9-18',print_count=2,stock=130,shelve_time='2019-1-3',customer_score=78,market_status=1,sale_count=43,author_score=87,second_class=15,first_class=1)
# Books.objects.create(book_id=9,book_name='我们仨',book_author='我自己写的',book_publish='教育出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=86,score='22880790-1_l_2.jpg',book_serice='社会',putaway_date='2010-9-18',print_count=2,stock=130,shelve_time='2019-3-12',customer_score=78,market_status=1,sale_count=43,author_score=73,second_class=13,first_class=1)
# Books.objects.create(book_id=10,book_name='启蒙',book_author='我自己写的',book_publish='教育出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=86,score="22882241-1_l_1.jpg",book_serice='小说',putaway_date='2010-9-18',print_count=2,stock=130,shelve_time='2019-4-12',customer_score=78,market_status=1,sale_count=43,author_score=89,second_class=14,first_class=1)
# Books.objects.create(book_id=11,book_name='走进奇妙的数学世界',book_author='我自己写的',book_publish='教育出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=86,score='22914275-1_l_5.jpg',book_serice='哲学',putaway_date='2010-9-18',print_count=2,stock=130,shelve_time='2018-3-12',customer_score=78,market_status=1,sale_count=43,author_score=88,second_class=14,first_class=1)
# Books.objects.create(book_id=12,book_name='从你的全世界路过',book_author='我自己写的',book_publish='教育出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=86,score='23353342-1_l.jpg',book_serice='社会',putaway_date='2010-9-18',print_count=2,stock=130,shelve_time='2017-5-8',customer_score=78,market_status=1,sale_count=43,author_score=75,second_class=13,first_class=1)
# Books.objects.create(book_id=13,book_name='三国演义',book_author='我自己写的',book_publish='教育出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=86,score='23356962-1_l_19.jpg',book_serice='名著',putaway_date='2010-9-18',print_count=2,stock=130,shelve_time='2016-8-23',customer_score=78,market_status=1,sale_count=43,author_score=96,second_class=11,first_class=1)
# # result=Books.objects.filter(book_id=1).values()
# # print(result)
# Books.objects.create(book_id=14,book_name='大败局',book_author='我自己写的',book_publish='教育出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=81,score='23368526-1_l.jpg',book_serice='小说',putaway_date='2010-9-18',print_count=2,stock=130,customer_score=78,market_status=1,sale_count=43,author_score=87,second_class=13,first_class=1)
# Books.objects.create(book_id=15,book_name='摆渡人',book_author='我自己写的',book_publish='教育出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=81,score='23694647-1_l_1.jpg',book_serice='小说',putaway_date='2010-9-18',print_count=2,stock=130,customer_score=78,market_status=1,sale_count=43,author_score=87,second_class=13,first_class=1)
# Books.objects.create(book_id=16,book_name='畅销的原理',book_author='我自己写的',book_publish='教育出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=81,score='24144199-1_l_9.jpg',book_serice='哲学',putaway_date='2010-9-18',print_count=2,stock=130,customer_score=78,market_status=1,sale_count=43,author_score=87,second_class=14,first_class=1)
# Books.objects.create(book_id=17,book_name='喜欢我也没关系',book_author='我自己写的',book_publish='教育出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=81,score='24156322-1_l_6.jpg',book_serice='社会',putaway_date='2010-9-18',print_count=2,stock=130,customer_score=78,market_status=1,sale_count=43,author_score=87,second_class=13,first_class=1)
# Books.objects.create(book_id=18,book_name='把你的英语用起来',book_author='我自己写的',book_publish='教育出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=81,score='1900494200-1_l_5.jpg',book_serice='社会',putaway_date='2010-9-18',print_count=2,stock=130,customer_score=78,market_status=1,sale_count=43,author_score=87,second_class=14,first_class=1)
# Books.objects.create(book_id=19,book_name='你要努力',book_author='我自己写的',book_publish='教育出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=81,score='1900513383-1_l_3.jpg',book_serice='哲学',putaway_date='2010-9-18',print_count=2,stock=130,customer_score=78,market_status=1,sale_count=43,author_score=87,second_class=13,first_class=1)
# Books.objects.create(book_id=20,book_name='自控力和压力做朋友',book_author='我自己写的',book_publish='教育出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=81,score='1900537714-1_l_4.jpg',book_serice='哲学',putaway_date='2010-9-18',print_count=2,stock=130,customer_score=78,market_status=1,sale_count=43,author_score=87,second_class=14,first_class=1)
# Books.objects.create(book_id=21,book_name='寻找时间的灰度',book_author='我自己写的',book_publish='教育出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=81,score='1900600235-1_l_7.jpg',book_serice='小说',putaway_date='2010-9-18',print_count=2,stock=130,customer_score=78,market_status=1,sale_count=43,author_score=87,second_class=15,first_class=1)
# Books.objects.create(book_id=22,book_name='战争就是这么回事',book_author='我自己写的',book_publish='教育出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=81,score='1900625661-1_l_5.jpg',book_serice='社会',putaway_date='2010-9-18',print_count=2,stock=130,customer_score=78,market_status=1,sale_count=43,author_score=87,second_class=15,first_class=1)
# Books.objects.create(book_id=23,book_name='不完美才美',book_author='我自己写的',book_publish='教育出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=81,score='1900625776-1_l_4.jpg',book_serice='哲学',putaway_date='2010-9-18',print_count=2,stock=130,customer_score=78,market_status=1,sale_count=43,author_score=87,second_class=13,first_class=1)
# Books.objects.create(book_id=24,book_name='匠人',book_author='我自己写的',book_publish='教育出版社',version=2,word_count=15686,page_count=238,open_type=16,book_page='凸版二号',book_wrapper='平装',book_price=38,book_dprice='36',editor_recommend=81,score='1900650062-1_l_1.jpg',book_serice='名著',putaway_date='2010-9-18',print_count=2,stock=130,customer_score=78,market_status=1,sale_count=43,author_score=87,second_class=12,first_class=1)

