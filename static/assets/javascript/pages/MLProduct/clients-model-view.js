"use strict";

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }

var table_data

// DataTables Demo
// =============================================================
var fn_data_table =
    /*#__PURE__*/
    function () {
        function fn_data_table() {
            _classCallCheck(this, fn_data_table);

            this.init();
        }

        _createClass(fn_data_table, [{
            key: "init",
            value: function init() {
                // event handlers
                this.table = this.table();
            }
        }, {
            key: "table",
            value: function table() {
                var search_url = "/clients-api/";   //change
                table_data = $('#dt-table-list').DataTable({
                    "processing": true,
                    destroy: true,
                    "ajax": {
                        "url": search_url,
                        "type": "GET",
                        "dataSrc": ""
                    },
                    responsive: true,
                    dom: "<'row'<'col-sm-12 col-md-6'l><'col-sm-12 col-md-6'f>>\n        <'table-responsive'tr>\n        <'row align-items-center'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7 d-flex justify-content-end'p>>",
                    language: {
                        paginate: {
                            previous: '<i class="fa fa-lg fa-angle-left"></i>',
                            next: '<i class="fa fa-lg fa-angle-right"></i>'
                        }
                    },
                    columns: [
                        { data: 'client_name' },
                        { data: 'client_type' },
                        { data: 'client_category' },
                        { data: 'client_segment_code' },
                        { data: 'client_father_name' },
                        { data: 'client_mother_name' },
                        { data: 'client_blood_group' },
                        { data: 'client_sex' },
                        { data: 'client_religion' },
                        { data: 'client_marital_status' },
                        { data: 'client_national_id'},
                        { data: 'client_nationality' },
                        { data: 'client_tin_number'},
                        { data: 'client_present_address' },
                        { data: 'client_permanent_address' },
                        { data: 'client_risk_category'},
                        { data: 'client_tds_exemption'},
                        { data: 'client_monthly_limit'},
                        { data: 'client_occupation_code' },
                        { data: 'client_accom_type' },
                        { data: 'client_have_insurance_policy'},
                        { data: 'client_plan_for_insurance_policy'},
                        { data: 'client_phone' },
                        { data: 'client_email' },
                        { data: 'client_opening_date' },
                        { data: 'client_education' },
                        { data: 'client_date_of_birth' },
                        { data: 'client_birth_place' },
                        { data: 'client_monthly_income' },
                        { data: 'client_annual_income' },
                        { data: 'client_annual_income_slab' },
                        { data: 'client_number_of_debit_tran_a_month' },
                        { data: 'client_number_of_credit_tran_a_month' },
                        { data: 'client_amount_of_debit_tran_a_month' },
                        { data: 'client_amount_of_credit_tran_a_month'},
                        {
                            "data": null,
                            "defaultContent": '<button type="button" class="btn btn-info btn-sm">Edit</button>'
                        }
                    ]
                });
            }
        }]);

        return fn_data_table;
    }();

var id = 0

$(function () {
    $('#btnSearch').click(function () {
        new fn_data_table();
    });
})

$(function () {

    $('#dt-table-list').on('click', 'button', function () {

        try {
            var table_row = table_data.row(this).data();
            id = table_row['id']
        }
        catch (e) {
            var table_row = table_data.row($(this).parents('tr')).data();
            id = table_row['id']
        }

        var class_name = $(this).attr('class');
        if (class_name == 'btn btn-info btn-sm') {
            show_edit_form(id);
        }

    })

    function show_edit_form(id) {
        $.ajax({
            url: '/clients-model-edit/' + id, //change
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $('#edit_model').modal('show');
            },
            success: function (data) {
                $('#edit_model .modal-content').html(data.html_form);
            }
        })
    }

});

$(function () {

    $(function () {
        $('#btnAddItem').click(function () {
            post_tran_table_data();

        });
    });

    $(function () {
        $('#btnPredictProduct').click(function () {
            show_prediction();

        });
    });



    function show_prediction() {
        var client_id = document.getElementById('id_user_client_code').value;
        $.ajax({
            url: "/product-predict-customer/" + client_id,
            type: 'GET',
            success: function (data) {
                if (data.form_is_valid) {
                    alert('Got the Client Code');
                    //$('#id_client_name').val(data.client_name);
                } else {
                    alert("Invalid Cusomer number");
                    //$('#id_client_name').val('');
                }
            }
        })
        return false;
    }

    function post_tran_table_data() {
        var data_string = $("#tran_table_data").serialize();
        var data_url = $("#tran_table_data").attr('data-url');
        $.ajax({
            url: data_url,
            data: data_string,
            type: 'POST',
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    document.getElementById("tran_table_data").reset();
                    table_data.ajax.reload();
                } else {
                    alert(data.error_message);
                }
            }
        })
        return false;
    }

    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});

