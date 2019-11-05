
table.render({
    elem:'#table_user'

});

let school_name=document.getElementById("school_name").value; //获取学校名称

let school_code=document.getElementById('school_code').value;//获取学校代码

let school_rank=document.getElementById('school_rank');//获取办学层次
let indexRank=school_rank.selectedIndex;//获取办学层次索引
let school_rankId=school_rank.options[index].value;//获取当前下拉框索引值



let school_type=document.getElementById('school_type');//获取办学类型
let indexType=school_type.selectedIndex;//获取办学类型索引
let school_typeId=school_type.options[index].value;//获取当前下拉框索引值

let school_province=document.getElementById('school_province');//获取省份
let indexProvince=school_province.selectedIndex;//获取省份索引
let school_provinceId=school_province.options[index].value;//获取当前下拉框索引值

let school_city=document.getElementById('school_city');//获取城市
let indexCity=school_city.selectedIndex;//获取城市索引
let school_cityId=school_city.options[index].value;//获取当前下拉框索引值

let admin_name=document.getElementById('admin_name');//获取教务管理员
let indexAdmin=admin_name.selectedIndex;//获取教务管理员索引
let admin_nameId=admin_name.options[index].value;//获取当前下拉框索引值


let school_rank=null;
if(school_typeId=='1'){
    school_rank='本科';
}
if(school_typeId=='2'){
    school_rank='专科';
}


let data={
    'school_name':school_name,
    'school_code':school_code,
    'school_rank':school_rank,
    'school_type':school_type,
    'school_province':school_province,
    'school_city':school_city,
    'admin_name':admin_name
}




//button提交监听
        form.on('submit(btn_school)', function (data) {
            //通用表单提交(AJAX方式)
            $.ajax({
                url: "/school",
                type: "post",
                data: data,
                success: function (res) {
                    parent.layer.msg('操作成功',{time:500},function () {
                        //重新加载当前页面
                        location.reload();
                    });
                }
            });
        });














/*点击删除*/

 