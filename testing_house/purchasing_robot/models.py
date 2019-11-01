from django.db import models

# Create your models here.

# TODO   采购合同机器人数据表

# class purchase_contract_table(models.Model):
#     id  = models.AutoField(primary_key=True,verbose_name="id")
#     user_name = models.CharField(max_length=20, null=True, verbose_name='用户名')
#     gmt_create = models.DateTimeField(null=True, verbose_name='创建时间')
#     gmt_modified = models.DateTimeField(null=True, verbose_name='修改时间')
#     purchase_number = models.CharField(max_length=20, null=True, verbose_name='请购单编号')
#     contract_number  = models.CharField(max_length=20, null=True, verbose_name='采购合同编号')
#     supplier_name = models.CharField(max_length=20, null=True, verbose_name='供应商')
#     tax_rate   = models.CharField(max_length=20, null=True, verbose_name='税率')
#     free_tax_unit_price  = models.CharField(max_length=20, null=True, verbose_name='免税单价')
#     count = models.CharField(max_length=20, null=True, verbose_name='数量')
#     summary_price = models.CharField(max_length=20, null=True, verbose_name='总价')
#     applicant = models.CharField(max_length=20, null=True, verbose_name='申请人')
#     application_sector = models.CharField(max_length=20, null=True, verbose_name='申请部门')
#     application_date = models.CharField(max_length=20, null=True, verbose_name='申请日期')
#     department_head = models.CharField(max_length=20, null=True, verbose_name='用户名')
#     company_head = models.CharField(max_length=20, null=True, verbose_name='公司领导')
#     contract_apply_status = models.CharField(max_length=20, null=True, verbose_name='合同机器人状态')
#     business_name = models.CharField(max_length=50, null=True, verbose_name='业务名称')
#     business_type = models.CharField(max_length=20, null=True, verbose_name='业务类型')
#     purchase_type = models.CharField(max_length=20, null=True, verbose_name='采购类型')
#     planne_arrive_date = models.CharField(max_length=20, null=True, verbose_name='预计到达日期')
#     demand_date = models.CharField(max_length=50, null=True, verbose_name='需求日期')
#
#
#     def __str__(self):
#         return self.contract_number
#
#     class Meta:
#         db_table = 'purchase_contract_table'



# TODO   采购请购机器人数据表

class purchase_apply_table(models.Model):
    id= models.AutoField(primary_key=True,verbose_name="id")
    gmt_create= models.DateTimeField(null=True, verbose_name='创建时间')
    gmt_modified = models.DateTimeField(null=True, verbose_name='修改时间')
    purchase_number = models.CharField(max_length=20, null=True, verbose_name='请购单编号')
    purchase_usesing = models.CharField(max_length=20, null=True, verbose_name='请购类型')
    goods_number = models.CharField(max_length=20, null=True, verbose_name='货物编号')
    recommended_unite_price = models.CharField(max_length=20, null=True, verbose_name='需求单价')
    specification = models.CharField(max_length=20, null=True, verbose_name='规格信号')
    goods_count = models.CharField(max_length=20, null=True, verbose_name='货物数量')
    recommended_price = models.CharField(max_length=20, null=True, verbose_name='需求价格')
    applicant = models.CharField(max_length=20, null=True, verbose_name='申请人')
    user_name = models.CharField(max_length=20, null=True, verbose_name='用户名字')
    business_type = models.CharField(max_length=50, null=True, verbose_name='业务类型')
    purchase_time = models.CharField(max_length=50, null=True, verbose_name='请购时间')
    application_depart = models.CharField(max_length=50, null=True, verbose_name='请购部门')
    recommended_date = models.CharField(max_length=10,null=True, verbose_name='需求日期')
    purchase_apply_status = models.CharField(max_length=20, null=True, verbose_name='请购状态')
    department_head = models.CharField(max_length=50, null=True, verbose_name='部门领导')
    company_head = models.CharField(max_length=50, null=True, verbose_name='公司领导')
    business_name = models.CharField(max_length=50, null=True, verbose_name='业务名称')
    procurement_type = models.CharField(max_length=50, null=True, verbose_name='采购类类型')


    def __str__(self):
        return self.purchase_usesing

    class Meta:
        db_table = 'purchase_apply_table'

