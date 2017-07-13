$(document).ready(function() {
	$.getJSON($SCRIPT_ROOT + '/_data-monitor', function(json) {
		console.log("JSON Data ": + json);
	});
});


    