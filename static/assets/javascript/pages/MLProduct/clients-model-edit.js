$(function () {
	$('#btnSubmit').click(function () {
		post_edit_form_data();
	});
});

function post_edit_form_data() {
	var data_string = $("#edit_form").serialize();
	var data_url = $("#edit_form").attr('data-url');
	console.log(data_url);
	$.ajax({
		url: data_url,
		data: data_string,
		type: 'POST',
		dataType: 'json',
		success: function (data) {
			if (data.form_is_valid) {
				$('#edit_model').modal('hide');
				table_data.ajax.reload();
			} else {
				alert(data.error_message);
				table_data.ajax.reload();
			}
		}
	})
	return false;
}