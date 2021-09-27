from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse



class Action(models.Model):
    title = models.CharField(max_length=50) #Reiterates, Initiates, Raises Target, Upgrades(from sell to buy), Downgrades, Lowers Target, Set Price Target

    def __str__(self):
        return self.title



class Timeframe (models.Model):
    title = models.CharField(max_length=50) 
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Status (models.Model):
    title = models.CharField(max_length=10) #Buy Hold Sell Strong-Buy

    def __str__(self):
        return self.title



class Exchange (models.Model): 
    title = models.CharField(max_length=50)
    ticker =  models.CharField(max_length=50, blank=True, null=True)
    #nickname = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.ticker

    class Meta:
        verbose_name = 'Биржа'
        verbose_name_plural = 'Биржи'
        ordering = ['title']


class Market (models.Model):
    title = models.CharField(max_length=150, db_index=True,verbose_name='Рынок')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    
    def get_absolute_url(self):
        return reverse('market', kwargs={"slug":self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рынок'
        verbose_name_plural = "Рынки"
        ordering = ['title']


class Asset(models.Model):
    title = models.CharField(max_length=50)
    acronym = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def get_absolute_url(self):
        return reverse('Asset', kwargs={"slug":self.slug})

    def __str__(self):
        return self.acronym

    class Meta:
        verbose_name = 'Актив'
        verbose_name_plural = "Активы"
        ordering = ['title']


class Symbol(models.Model):
    title = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50,unique=True)
    market = models.ForeignKey('Market', on_delete = models.PROTECT) #, verbose_name='Market')
    exchange = models.ForeignKey('Exchange', on_delete = models.PROTECT) #, verbose_name='Market')
    base = models.ForeignKey('Asset', on_delete = models.PROTECT, related_name='Symbol') #, verbose_name='Market')
    second = models.ForeignKey('Asset', on_delete = models.PROTECT, null=True, blank = True) 

    def get_absolute_url(self):
        return reverse('Asset', kwargs={"slug":self.slug})

    def __str__(self):
        return self.symbol

    class Meta:
        verbose_name = 'Тикер'
        verbose_name_plural = "Тикеры"
        ordering = ['title']


class Channel(models.Model):
    title = models.CharField(max_length=50,unique=True)
    link = models.URLField(max_length = 200)

    def __str__(self):
        return self.title


class Analysis(models.Model):
    title = models.CharField(max_length = 255, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    content = models.TextField(blank=True, verbose_name='Контент')
    content_upd_one = models.TextField(blank=True, verbose_name='Обновление 1')
    content_upd_two = models.TextField(blank=True, verbose_name='Обновление 1')
    content_upd_three = models.TextField(blank=True, verbose_name='Обновление 1')
    content_upd_four = models.TextField(blank=True, verbose_name='Обновление 1')
    content_upd_five = models.TextField(blank=True, verbose_name='Обновление 1')
    published_at = models.DateTimeField(verbose_name='Дата публикации на TV')
    published_upd_one = models.DateTimeField(verbose_name='Дата публикации на TV',blank=True, null=True)
    published_upd_two = models.DateTimeField(verbose_name='Дата публикации на TV',blank=True, null=True)
    published_upd_three = models.DateTimeField(verbose_name='Дата публикации на TV',blank=True, null=True)
    published_upd_four = models.DateTimeField(verbose_name='Дата публикации на TV',blank=True, null=True)
    published_upd_five = models.DateTimeField(verbose_name='Дата публикации на TV',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now = True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank = True)
    photo_upd_one = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото обновления 1', blank = True)
    photo_upd_two = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото обновления 2', blank = True)
    photo_upd_three = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото обновления 3', blank = True)
    photo_upd_four = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото обновления 4', blank = True)
    photo_upd_five = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото обновления 5', blank = True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')
    channel = models.ManyToManyField(Channel, blank=True, related_name='posts')
    #market = models.ForeignKey('Market', on_delete = models.PROTECT, verbose_name='Наименование категории')
    views = models.IntegerField(default=0)
    #pair = models.ForeignKey('Category', on_delete = models.PROTECT, verbose_name='Наименование категории')
    #exchange = models.ForeignKey('Category', on_delete = models.PROTECT, verbose_name='Наименование категории')
    #tags = models.ForeignKey('Category', on_delete = models.PROTECT, verbose_name='Метки')
    link_to_TV = models.URLField(max_length = 200, blank=True, null = True)
    symbol = models.ForeignKey('Symbol', on_delete = models.PROTECT, verbose_name='Тикер TV')
    slide = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Слайд', blank = True)
    slide_title = models.CharField(max_length = 255, verbose_name='Наименование слайда', blank = True,null=True)
    locale = models.CharField(
       max_length=2,
       choices=[
           ('en', 'English'),
           ('ru', 'Русский'),
           ],  # some list of choices
       blank = True,
       null= True,
       default='en'
   )
    timeframe = models.ForeignKey('Timeframe', on_delete = models.PROTECT, verbose_name='Таймфрэйм')
    label = models.CharField(
       max_length=10,
       choices=[
           ('long', 'Покупать'),
           ('short', 'Продавать'),
           ('education', 'Обучение'),
           ('neutral', 'Нейтрально'),
           ],  # some list of choices
       blank = True,
       null= True
   )
    #publication_date = models.DateTimeField(blank=True, null=True)
    publication_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    tp_price_first = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    tp_price_second = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    tp_price_third = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    sl_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    
    lowest_price_after = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    highest_price_after = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)

    related_analysis_one = models.URLField(max_length = 200,blank=True, null=True)
    related_analysis_two = models.URLField(max_length = 200,blank=True, null=True)
    related_analysis_three = models.URLField(max_length = 200,blank=True, null=True)
    related_analysis_four = models.URLField(max_length = 200,blank=True, null=True)
    related_analysis_five = models.URLField(max_length = 200,blank=True, null=True)

    def get_absolute_url (self):
        return reverse('analysis', kwargs={"slug":self.slug})
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Анализ'
        verbose_name_plural = "Аналитика"
        ordering = ['-published_at']



class Rating(models.Model):
    #title = models.CharField(max_length = 255, verbose_name='Наименование')
    symbol = models.ForeignKey('Symbol', on_delete = models.PROTECT, verbose_name='Тикер TV') #Amazon или TRY USD
    status_lt = models.ForeignKey('Status', on_delete = models.PROTECT,blank=True, null=True,related_name='lt') #buy
    status_mt = models.ForeignKey('Status', on_delete = models.PROTECT,blank=True, null=True,related_name='mt') #buy
    price_when_issued = models.DecimalField(max_digits=10, decimal_places=4,blank=True, null=True) #17.25
    current_price = models.DecimalField(max_digits=10, decimal_places=4,blank=True, null=True)   #если подключим
    updated_at = models.DateTimeField(auto_now = True, verbose_name='Обновлено') # обновление в системе авто
    status_updated_at = models.DateTimeField(verbose_name='Дата обновления',blank=True, null=True) # обновление статуса последнее
    status_changed_to =  models.ForeignKey('Action', on_delete = models.PROTECT)                                #повышена цена LT, повторен
    target_price_lt =  models.DecimalField(max_digits=10, decimal_places=4,blank=True, null=True)                                #250K
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')
  

RESULT_CHOICES = [
    ('w', 'Win'),
    ('l', 'Loss'),
    ('c', 'Canceled'),
]

class Alert(models.Model):
    symbol = models.ForeignKey('Symbol', on_delete = models.PROTECT, verbose_name='Тикер TV') #Amazon или TRY USD
    status = models.ForeignKey('Status', on_delete = models.PROTECT,blank=True, null=True) #buy
    #body = models.TextField()
    #status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    crated_at = models.DateTimeField(verbose_name='Дата добавления',blank=True, null=True)
    finished_at = models.DateTimeField(verbose_name='Дата завершения',blank=True, null=True)
    entry = models.DecimalField(max_digits=10, decimal_places=4,blank=True, null=True)       
    tp = models.DecimalField(max_digits=10, decimal_places=4,blank=True, null=True)       
    sl = models.DecimalField(max_digits=10, decimal_places=4,blank=True, null=True)       
    result = models.CharField(max_length=1, choices=RESULT_CHOICES)#win loss canceled

    class Meta:
        ordering = ['-crated_at']