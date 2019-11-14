from django.db import models


# Create your models here.

# #
# # # TODO   采购请购机器人数据表





# # # # TODO   采购请购机器人数据表

# # # # TODO   采购请购机器人数据表


class purchase_apply_table(models.Model):
    id= models.AutoField(primary_key=True,verbose_name="id")
    gmt_create= models.DateTimeField(null=True, verbose_name='创建时间')
    gmt_modified = models.DateTimeField(null=True, verbose_name='修改时间')
    user_name = models.CharField(max_length=20, null=True, verbose_name='用户名字')
    purchase_apply_status = models.CharField(max_length=20, null=True, verbose_name='请购状态')
    purchase_number = models.CharField(max_length=20, null=True, verbose_name='请购单编号')
    module_number = models.CharField(max_length=50, null=True, verbose_name='模块编号')
    business_name = models.CharField(max_length=50, null=True, verbose_name='业务名称')
    procurement_type = models.CharField(max_length=50, null=True, verbose_name='采购类类型')
    purchase_usesing = models.CharField(max_length=20, null=True, verbose_name='采购用途')
    goods_name = models.CharField(max_length=50, null=True, verbose_name='货物名称')
    goods_number = models.CharField(max_length=20, null=True, verbose_name='货物编号')
    recommended_unite_price = models.CharField(max_length=20, null=True, verbose_name='需求单价')
    goods_unit = models.CharField(max_length=20, null=True, verbose_name='货物单位')
    goods_count = models.CharField(max_length=20, null=True, verbose_name='货物数量')
    recommended_price = models.CharField(max_length=20, null=True, verbose_name='需求价格')
    recommended_date = models.CharField(max_length=10, null=True, verbose_name='需求日期')
    applicant = models.CharField(max_length=20, null=True, verbose_name='申请人')
    application_depart = models.CharField(max_length=50, null=True, verbose_name='申请部门')
    application_date = models.CharField(max_length=50, null=True, verbose_name='申请日期')
    department_head = models.CharField(max_length=50, null=True, verbose_name='部门领导')
    department_head_date = models.CharField(max_length=50, null=True, verbose_name='部门领导审批日期')
    company_head = models.CharField(max_length=50, null=True, verbose_name='公司领导')
    company_head_date = models.CharField(max_length=50, null=True, verbose_name='公司领导审批日期')




    def __str__(self):
        return self.purchase_usesing

    class Meta:
        db_table = 'purchase_apply_table'


#

# # #
# # # # TODO   采购合同机器人数据表
# # #
class purchase_contract_table(models.Model):
    id  = models.AutoField(primary_key=True,verbose_name="id")
    user_name = models.CharField(max_length=20, null=True, verbose_name='用户名')
    gmt_create = models.DateTimeField(null=True, verbose_name='创建时间',auto_now=True)
    gmt_modified = models.DateTimeField(null=True, verbose_name='修改时间',auto_now=True)
    contract_apply_status = models.CharField(max_length=20, null=True, verbose_name='合同机器人状态')


    purchase_number = models.CharField(max_length=20, null=True, verbose_name='请购单编号')
    module_number = models.CharField(max_length=50, null=True, verbose_name='模块编号')
    business_name = models.CharField(max_length=50, null=True, verbose_name='业务名称')
    contract_number  = models.CharField(max_length=20, null=True, verbose_name='采购合同编号')
    supplier_name = models.CharField(max_length=20, null=True, verbose_name='供应商')
    goods_name = models.CharField(max_length=50, null=True, verbose_name='货物名称')
    free_tax_unit_price  = models.CharField(max_length=20, null=True, verbose_name='免税单价')
    goods_count = models.CharField(max_length=20, null=True, verbose_name='数量')
    goods_unit = models.CharField(max_length=20, null=True, verbose_name='货物单位')
    tax_rate   = models.CharField(max_length=20, null=True, verbose_name='税率')
    summary_price = models.CharField(max_length=20, null=True, verbose_name='总价')
    recommended_date = models.CharField(max_length=10, null=True, verbose_name='需求日期')
    applicant = models.CharField(max_length=20, null=True, verbose_name='申请人')
    application_sector = models.CharField(max_length=20, null=True, verbose_name='申请部门')
    application_date = models.CharField(max_length=20, null=True, verbose_name='申请日期')


    department_head = models.CharField(max_length=50, null=True, verbose_name='部门领导')
    department_head_date = models.CharField(max_length=50, null=True, verbose_name='部门领导审批日期')
    company_head = models.CharField(max_length=50, null=True, verbose_name='公司领导')
    company_head_date = models.CharField(max_length=50, null=True, verbose_name='公司领导审批日期')


    business_type = models.CharField(max_length=20, null=True, verbose_name='业务类型')
    purchase_type = models.CharField(max_length=20, null=True, verbose_name='采购类型')
    planne_arrive_date = models.CharField(max_length=20, null=True, verbose_name='预计到达日期')




    def __str__(self):
        return self.contract_number

    class Meta:
        db_table = 'purchase_contract_table'



    def __str__(self):
        return self.contract_number

    class Meta:
        db_table = 'purchase_contract_table'



# TODO   采购入库机器人数据表

class purchase_warehousing_table(models.Model):


    id = models.AutoField(primary_key=True, verbose_name="id")
    gmt_create = models.DateTimeField(null=True, verbose_name='创建时间')
    user_name = models.CharField(max_length=20, null=True, verbose_name='用户名')
    gmt_modified = models.DateTimeField(null=True, verbose_name='修改时间')
    approval_date = models.DateTimeField(null=True, verbose_name='审批日期')
    purchase_number = models.CharField(max_length=20, null=True, verbose_name='请购单编号')
    contract_number = models.CharField(max_length=20, null=True, verbose_name='合同编号')
    warehouse_number = models.CharField(max_length=20, null=True, verbose_name='仓库编号')
    warehouse_date = models.CharField(max_length=20, null=True, verbose_name='入库日期')
    application = models.CharField(max_length=20, null=True, verbose_name='点验人员')
    application_sector = models.CharField(max_length=20, null=True, verbose_name='申请部门')

    purchase_warehousing_status = models.CharField(max_length=20, null=True, verbose_name='入库状态')
    business_name = models.CharField(max_length=50, null=True, verbose_name='业务名称')


    def __str__(self):
        return self.warehouse_number

    class Meta:
        db_table = 'purchase_warehousing_table'


#
#
# # TODO   采购发票机器人数据表

class purchase_invoice_table(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    user_name = models.CharField(max_length=20, null=True, verbose_name='用户名')
    gmt_create = models.DateTimeField(null=True, verbose_name='创建时间')
    gmt_modified = models.DateTimeField(null=True, verbose_name='修改时间')
    purchase_number = models.CharField(max_length=20, null=True, verbose_name='请购单编号')
    contract_number = models.CharField(max_length=20, null=True, verbose_name='采购合同编号')
    incoive_number = models.CharField(max_length=20, null=True, verbose_name='发票号码')
    reimbursement_type = models.CharField(max_length=20, null=True, verbose_name='报销类别')
    reimbursement_money = models.CharField(max_length=20, null=True, verbose_name='报销金额')
    money_details = models.CharField(max_length=20, null=True, verbose_name='费用明细')
    supplier_name = models.CharField(max_length=20, null=True, verbose_name='供应商信息')
    application_date = models.CharField(max_length=20, null=True, verbose_name='申请日期')
    application = models.CharField(max_length=20, null=True, verbose_name='申请人')
    application_sector = models.CharField(max_length=20, null=True, verbose_name='申请部门')
    department_head = models.CharField(max_length=20, null=True, verbose_name='部门领导')
    company_head = models.CharField(max_length=20, null=True, verbose_name='公司领导')

    purchase_invoice_status = models.CharField(max_length=20, null=True, verbose_name='发票状态')
    business_name = models.CharField(max_length=50, null=True, verbose_name='业务名称')


    def __str__(self):
        return self.incoive_number

    class Meta:
        db_table = 'purchase_invoice_table'


#
#
#
# # TODO   采购付款机器人数据表
#
class purchase_payment_table(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    user_name = models.CharField(max_length=20, null=True, verbose_name='用户名')
    gmt_create = models.DateTimeField(null=True, verbose_name='创建时间')
    gmt_modified = models.DateTimeField(null=True, verbose_name='修改时间')
    business_name = models.CharField(max_length=50, null=True, verbose_name='业务名称')
    purchase_payment_status = models.CharField(max_length=20, null=True, verbose_name='付款状态')

    purchase_number = models.CharField(max_length=20, null=True, verbose_name='请购单编号')
    contract_number = models.CharField(max_length=20, null=True, verbose_name='采购合同编号')
    payment_reason = models.CharField(max_length=20, null=True, verbose_name='付款事由')
    payment_money = models.CharField(max_length=20, null=True, verbose_name='付款金额')
    payment_type = models.CharField(max_length=20, null=True, verbose_name='付款类型')
    payment_date = models.CharField(max_length=20, null=True, verbose_name='支付日期')
    payment_object = models.CharField(max_length=20, null=True, verbose_name='支付对象')
    payment_bank = models.CharField(max_length=20, null=True, verbose_name='开户行')
    bank_account = models.CharField(max_length=20, null=True, verbose_name='银行账号')
    application_date = models.CharField(max_length=20, null=True, verbose_name='银行账号')
    application = models.CharField(max_length=20, null=True, verbose_name='申请人')
    application_sector = models.CharField(max_length=20, null=True, verbose_name='申请部门')
    department_head = models.CharField(max_length=20, null=True, verbose_name='部门领导')
    company_head = models.CharField(max_length=20, null=True, verbose_name='公司领导')





    def __str__(self):
        return self.payment_object

    class Meta:
        db_table = 'purchase_payment_table'
