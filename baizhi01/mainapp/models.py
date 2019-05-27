# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Books(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=40, blank=True, null=True)
    book_author = models.CharField(max_length=40, blank=True, null=True)
    book_publish = models.CharField(max_length=60, blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    version = models.CharField(max_length=3, blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    word_count = models.IntegerField(blank=True, null=True)
    page_count = models.CharField(max_length=4, blank=True, null=True)
    open_type = models.CharField(max_length=2, blank=True, null=True)
    book_page = models.CharField(max_length=20, blank=True, null=True)
    book_wrapper = models.CharField(max_length=8, blank=True, null=True)
    book_price = models.CharField(max_length=4, blank=True, null=True)
    book_dprice = models.CharField(max_length=4, blank=True, null=True)
    editor_recommend = models.TextField(blank=True, null=True)
    book_content = models.TextField(blank=True, null=True)
    author_introduce = models.TextField(blank=True, null=True)
    menu = models.TextField(blank=True, null=True)
    media_comment = models.TextField(blank=True, null=True)
    excerpt_inlustration = models.TextField(blank=True, null=True)
    score = models.CharField(max_length=60, blank=True, null=True)
    book_serice = models.CharField(max_length=30, blank=True, null=True)
    putaway_date = models.DateTimeField(blank=True, null=True)
    print_count = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    shelve_time = models.DateField(blank=True, null=True)
    customer_score = models.IntegerField(blank=True, null=True)
    market_status = models.IntegerField(blank=True, null=True)
    sale_count = models.IntegerField(blank=True, null=True)
    author_score = models.CharField(max_length=10, blank=True, null=True)
    shop_id = models.IntegerField(blank=True, null=True)
    first_class = models.IntegerField(blank=True, null=True)
    second_class = models.ForeignKey('ClassBooks', models.DO_NOTHING, db_column='second_class', blank=True, null=True)
    save1 = models.CharField(max_length=10, blank=True, null=True)
    save2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'


class ClassBooks(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=40, blank=True, null=True)
    book_counts = models.CharField(max_length=20, blank=True, null=True)
    category_pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_books'


class ConfirmlEmail(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=200, blank=True, null=True)
    user = models.CharField(max_length=200, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    u_emiid = models.ForeignKey('TUser', models.DO_NOTHING, db_column='u_emiid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confirml_email'


class CustomerAddress(models.Model):
    ad_id = models.AutoField(primary_key=True)
    receive_name = models.CharField(max_length=20, blank=True, null=True)
    add_detail = models.CharField(max_length=40, blank=True, null=True)
    telephone = models.CharField(max_length=11, blank=True, null=True)
    mobile_phone = models.CharField(max_length=11, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    zipcode = models.CharField(max_length=40, blank=True, null=True)
    territory = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_address'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class OrderItem(models.Model):
    shop_id = models.IntegerField(primary_key=True)
    shop_bookid = models.ForeignKey(Books, models.DO_NOTHING, db_column='shop_bookid', blank=True, null=True)
    shop_itemid = models.ForeignKey('UOrder', models.DO_NOTHING, db_column='shop_itemid', blank=True, null=True)
    shop_number = models.IntegerField(blank=True, null=True)
    total_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item'


class TUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=80, blank=True, null=True)
    user_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'


class UOrder(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_num = models.IntegerField(blank=True, null=True)
    creat_time = models.DateField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    u = models.ForeignKey(TUser, models.DO_NOTHING, blank=True, null=True)
    order_addid = models.ForeignKey(CustomerAddress, models.DO_NOTHING, db_column='order_addid', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'u_order'
