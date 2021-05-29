$(document).ready(function () {

    var el_def = $(".btn:first");
    var defHeiht = el_def.height()

    $('.btn').click(function (event) {

        if ($(event.delegateTarget).height()>defHeiht){
             $(event.delegateTarget).height(defHeiht)
        }else{
            $(event.delegateTarget).height(defHeiht).animate({ height: 100 })
        }
    })
})

