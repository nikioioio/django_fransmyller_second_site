$(document).ready(function () {
    $("#test").submit(function (event) {
        $.ajax({
            type: "POST",
            url: "upload/",
            data: {
                'video': 1111 // from form
            },
            headers: {"X-CSRFToken": "{{ csrf_token }}"},
            success: function () {
                $('#message').html("<h2>Contact Form Submitted!</h2>")
            }
        });
        return false; //<---- move it here
    });

});




