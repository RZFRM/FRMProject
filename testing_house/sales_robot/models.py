from django.db import models

# Create your models here.
# # # TODO   销售申请(订单)机器人数据表
class sale_apply_table(models.Model):
    id= models.AutoField(primary_key=True,verbose_name="id")
    user_name = models.CharField(max_length=20, null=True, verbose_name='用户名字')
    gmt_create= models.DateTimeField(null=True, verbose_name='创建时间')
    gmt_modified = models.DateTimeField(null=True, verbose_name='修改时间')
    sales_apply_status = models.CharField(max_length=20, null=True, verbose_name='状态信息')

    contract_number = models.CharField(max_length=20, null=True, verbose_name='销售订单编号')
    client_name = models.CharField(max_length=100, null=True, verbose_name='客户名称')
    business_type = models.CharField(max_length=20, null=True, verbose_name='业务类型')
    sales_type = models.CharField(max_length=20, null=True, verbose_name='销售类型')
    product_name = models.CharField(max_length=50, null=True, verbose_name='产品名称')
    quantity = models.CharField(max_length=20, null=True, verbose_name='订单物品数量')
    unit = models.CharField(max_length=10, null=True, verbose_name='单位')
    excluding_tax_univalent = models.CharField(max_length=10, null=True, verbose_name='不含税单价')
    tax_rate_or_levy_rate = models.CharField(max_length=10, null=True, verbose_name='税率/征收率')
    total_amount = models.CharField(max_length=10, null=True, verbose_name='总金额')
    delivery_dates = models.CharField(max_length=16, null=True, verbose_name='交货日期')
    applicant = models.CharField(max_length=20, null=True, verbose_name='申请人')
    application_sector = models.CharField(max_length=40, null=True, verbose_name='申请部门')
    application_date = models.CharField(max_length=16, null=True, verbose_name='申请日期')
    department_head = models.CharField(max_length=20, null=True, verbose_name='部门负责人')
    company_representative = models.CharField(max_length=20, null=True, verbose_name='公司负责人')


    def __str__(self):
        return self.contract_number

    class Meta:
        db_table = 'sale_apply_table'


