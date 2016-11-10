$(document).ready(function() {
	$("#my_event").hide();
	$("#new_event").hide();
	$("#new_venue").hide();
	$("#my_venue").hide();
	$("#navbar li").on("click",function() {
		console.log($(this).text());
		if ($(this).text()=="Create Event") {
			$("#new_venue").hide();
			$("#my_venue").hide();
			$("#my_event").hide();
			$("#new_event").show();
		};
		if ($(this).text()=="My Events") {
			$("#new_event").hide();
			$("#new_venue").hide();
			$("#my_venue").hide();
			$("#my_event").show();
		};
		if ($(this).text()=="Manage Venue") {
			$("#my_event").hide();
			$("#new_event").hide();
			$("#my_venue").show();
			$("#new_venue").hide();
		};
		if ($(this).text()=="Register Venue") {
			$("#my_event").hide();
			$("#new_event").hide();
			$("#my_venue").hide();
			$("#new_venue").show();
		};
	})
})