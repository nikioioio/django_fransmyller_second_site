$(document).ready(function () {

    var el_def = $(".btn:first");
    var defHeiht = el_def.height()

    // $('.btn').click(function (event) {
    //
    //     if ($(event.delegateTarget).height()>defHeiht){
    //          $(event.delegateTarget).height(defHeiht)
    //     }else{
    //         $(event.delegateTarget).height(defHeiht).animate({ height: 100 })
    //     }
    // })


    $('.btn').hover(function (event) {
            $(event.delegateTarget).height(defHeiht).animate({ height: 150},1 )
            $(event.delegateTarget).children(".hidden_elements").css({'display':'flex'})
    },function (event){
             $(event.delegateTarget).height(defHeiht)
            $(event.delegateTarget).children(".hidden_elements").css({'display':'none'})
    });




    $('.pagenav-item').click(function (event){
        $(event.delegateTarget).addClass('active')
    })
})

