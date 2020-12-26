from django.db import models

# Create your models here.
booleanChoices = ((0,"否"),(1,"是"))

class Company(models.Model):
    name = models.CharField('商家名称', max_length=256, unique=True)
    url = models.CharField('网址', max_length=256,blank=False,null=False , help_text='https://bwh88.net/aff.php?aff=991&pid=')
    connect_pid = models.IntegerField(verbose_name='连接PID',choices=booleanChoices,default=1)
    need_monitor = models.IntegerField(verbose_name='检查库存',choices=booleanChoices,default=1)
    out_of_stock_string = models.CharField('缺货字符串',max_length=256,default='Out of Stock') 
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'company'        
        verbose_name = '商家信息'
        verbose_name_plural = '商家信息'


class Goods(models.Model):
    archChoices = (
        ('KVM','KVM'),
        ('OpenVZ','OpenVZ')
    )
    stockChoices = (
        (0,'无货'),
        (1,'有货')        
    )
    lineChoices = (
        ('GIA','GIA'),
        ('BGP', 'BGP'),
        ('NTT','NTT'),
        ('IIJ','IIJ'),
        ('SoftBank','SoftBank'),
        ('PCCW','PCCW'),
        ('HKBN','HKBN'),
        ('HGC','HGC'),
        ('SINGTEL','Singtel'),
        ('GTT','GTT'),
        ('Telia','Telia'),
        ('Other','Other'),
    )
    dcChoices = (
        ('HK','Hong Kong'),
        ('TYO','Tokyo, Japan'),
        ('OSA','Osaka, Japan'),
        ('SEO','Seoul, KR'),
        ('SG','Singapore'),
        ('SJ','San Jose, US'),
        ('LAX','Los Angeles, US'),
        ('FFM','Frankfurt, DE'),
        ('CN','China'),
        ('上海CN2','SHCN2'),
        ('泉州CN2','QZCN2'),
        ('上海联通','SHCU'),
        ('香港IPLC','HKIPLC'),
        ('Other','Other'),
    )
    company = models.ForeignKey(Company , to_field='id' , on_delete=models.DO_NOTHING , verbose_name="商家",blank=False,null=False)
    pid = models.IntegerField(verbose_name='PID',blank=False,null=False ,default=0 )
    dc = models.CharField('机房位置', max_length=256,choices=dcChoices)
    cpu = models.IntegerField('CPU', default=1)
    ram = models.CharField('内存', max_length=256)
    disk = models.CharField('硬盘', max_length=256)
    bandwidth = models.CharField('带宽', max_length=256)
    traffic = models.CharField('流量', max_length=256)
    route = models.CharField('线路', max_length=256,choices=lineChoices)
    ipv4 = models.IntegerField('IPV4',default=1)
    arch = models.CharField('架构', max_length=256,choices=archChoices,default='KVM')
    annual = models.CharField('年付', max_length=256,blank=True,null=False )
    quarter = models.CharField('季付', max_length=256,blank=True,null=True)
    month = models.CharField('月付', max_length=256,blank=True,null=True)
    stock = models.IntegerField( choices=stockChoices,verbose_name='库存' , default=0 )
    sort = models.IntegerField(verbose_name='排序',default=66,help_text='数字越大越靠前')
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - PID：{} - {}/年 - {}/月'.format(self.company.name,self.pid,self.annual,self.month)

    class Meta:
        managed = True
        db_table = 'goods'
        verbose_name = '商品信息'
        verbose_name_plural = '商品信息'


class Subscribe(models.Model):
    email = models.EmailField(verbose_name="邮箱",unique=True)
    status = models.IntegerField(verbose_name='有效',choices=booleanChoices,default=1)
    update_time = models.DateTimeField(auto_now=True)    

    class Meta:
        managed = True
        db_table = 'subscribe'
        verbose_name = '订阅通知'
        verbose_name_plural = '订阅通知'


class Passwd(models.Model):
    strings = models.CharField(verbose_name='字符',blank=False,unique=True,null=False,max_length=128)
    md5 = models.CharField(verbose_name='MD5值',blank=False,null=False,max_length=128)
    update_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)


