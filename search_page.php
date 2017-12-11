<html>
	<head>
		<title>SEARCH PAGE</title>
		<link rel="stylesheet" href="st.css" />
	</head>
	<body>		
		<div class="login">
		<form action="search_result.php" id="search_form" method="GET">
			<p align="center"></p>
			<p><input name="q" autocomplete="off" id="list_search" type="search" required class="search" /></p>
			
			<p align="center">
				<input type="submit" id="click" class="button" value="search"  />
				<input type="submit"  class="button" value="I m Feeling lucky" />
			</p> 			
		</form>
		</div>
	</body>

</html>
<script src="//code.jquery.com/jquery-1.10.2.min.js"></script>
<script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
<link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
<script type="text/javascript">
$(document).ready(function(){
    $(document).on('keyup','#list_search',function(){   
        var value = $(this).val();
        $.getJSON('ajax_search_list.php?q='+value, function (data) {
            var availableTags = data;
            $( "#list_search" ).autocomplete({
                source: availableTags,
                select: function(event, ui) {
                $(event.target).val(ui.item.value);
                $('#search_form').submit();
                return false;
            },
             });
        });
        
    });
});
</script>