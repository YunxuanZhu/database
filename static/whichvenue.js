$(document).ready(function() {
	$("#venue_on_change").hide();
	$("#which_venue li").on("click",function() {
		console.log($(this).text().split(" ")[1]);
		console.log($("#username").val());
		$.ajax({
            async: false,
            type: 'post',
            url: '/getvenues',
            data: {
                username: $("#username").val(),
                vid: $(this).text().split(" ")[1]
            },
            success: function(data) {
                $("#venue_on_change").show();
                $("#vidm").val(data);
                $("#vidmform").val(data);
            },
            error: function() {
            },
            complete: function() {
            }
        });
	})
})