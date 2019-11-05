
/*点击新增*/
document.getElementById('add1').addEventListener('click',function (data) {
    let oldData = table.cache["table_user"];
    let data1 = {};
    oldData.push(data1);
    table.reload('table_user', {data: oldData});
});

/*点击删除*/
if(obj.event === "del"){
    layer.confirm("你确定要删除么？",{btn:['是的,我确定','我再想想']},
            function(){
                let oldData =  table.cache["table_user"];
                oldData.splice(obj.tr.data('index'),1);
                layer.msg("删除成功",{time: 10},function(){
                    table.reload('table_user',{data : oldData});
                });
            }
    )
}
 