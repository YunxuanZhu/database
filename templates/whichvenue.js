$(document).ready(function() {
	$("#venue_on_change").hide();
    $("#add_time_slot").hide();
    $("#options").hide();
    $("#confirm_request").hide();
	$("#which_venue li").on("click",function() {
        $("#selected_venue").val($(this).text().split(" ")[1]);
        $("#venue_on_change").hide();
        $("#add_time_slot").hide();
        $("#confirm_request").hide();
        $("#options").show();
        $("#vidts").val($(this).text().split(" ")[1]);
        $("#vidtsform").val($(this).text().split(" ")[1]);
	})

    $("#options li").on("click",function() {
        if ($(this).text()=="Edit Venue") {
            $("#add_time_slot").hide();
            $("#confirm_request").hide();
            $("#options").show();
            $("#venue_on_change").show();
            var selected="#"+"venue_on_change"+$("#selected_venue").val();
            $(selected).show();
            var venue={{venue|tojson}};
            $.each( venue, function( key, value ) {
                if (key!=$("#selected_venue").val()) {
                    var notselected="#"+"venue_on_change"+key;
                    $(notselected).hide();
                }
            })
        };
        if ($(this).text()=="Add Time Slot"){
            $("#venue_on_change").hide();
            $("#confirm_request").hide();
            $("#options").show();
            $("#add_time_slot").show();
        };
        if ($(this).text()=="Confirm Requests"){
            $("#venue_on_change").hide();
            $("#add_time_slot").hide();
            $("#options").show();
            $("#confirm_request").show();
            var selected="#"+"confirm_request"+$("#selected_venue").val();
            $(selected).show();
            var venue={{venue|tojson}};
            $.each( venue, function( key, value ) {
                if (key!=$("#selected_venue").val()) {
                    var notselected="#"+"confirm_request"+key;
                    $(notselected).hide();
                }
            })
        }});
    })


