$( document ).ready(function() {

    var csrfToken = $('[name="csrfmiddlewaretoken"]').val(); 

    setInterval(checkUrls, 4000)

    function radioCollector(){
            // here I will be stote id of rows, which have checked radio
            var id_for_check = [];
            //here I store all rows in allRows
            var table = document.getElementById("main_table");
            var allRows = table.getElementsByTagName("tr");
            for (let i = 1; i < allRows.length; i++) {
                let current_id = allRows[i].id;
                // here I take td with input(checkbox) from children of every row
                let checkbox = allRows[i].children[4].firstChild;
                if($(checkbox).prop('checked')) {
                    id_for_check.push(current_id);
                }            
        }
        return id_for_check;
    }

    var result = radioCollector();


    function checkUrls() {   
            $.ajax({
                type: "POST",
                url: 'ajax/check/',
                dataType: "json",
                data: { checked_ids: JSON.stringify(result)},
                success: function(response) {
                    $('#main_table').load("" + " #main_table");
                }
            });
        }
});