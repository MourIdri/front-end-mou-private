<?php
include("config.php");
if(isset($_GET['q']) && $_GET['q']!="") :
    $data = mysqli_real_escape_string($db,$_GET['q']);
    $keyword =  trim(preg_replace('/\s+/',' ',$data));
    $sql=$db->query("SELECT distinct * FROM `web_information` WHERE CurrentMail LIKE '%$keyword%' OR CurrentCompany LIKE '%$keyword%' OR LastName LIKE '%$keyword%'");
    // $sql=$db->query("SELECT distinct * FROM `web_information` WHERE meta_title LIKE '%$keyword%' OR meta_description LIKE '%$keyword%' OR site_url LIKE '%$keyword%'");
?>
    <html>
    <head>
        <title>SEARCH RESULT PAGE</title>        
        <link rel="stylesheet" href="st.css" />
    </head>
    <body>
    <div>
        <form action="search_result.php" id="search_form" method="GET">
            <input name="q" autocomplete="off" id="list_search" type="search" required value="<?=@$keyword;?>" class="search" />
            <button type="submit"  class="button">Search</button>      
        </form>
    </div>
    

    <?php if(isset($sql) && count($sql) && ($sql->num_rows)) : ?>


    <div class="reslt_bar">                
        <?php foreach ($sql as $key => $search_data) : ?>
            <?php

            $UserMail = $search_data['CurrentMail'];
            $UsersName = $search_data['LastName'];
            $UserCompany = $search_data['CurrentCompany'];           
            ?>
            <div style="width: 80%; margin: 0 auto;">
            <table style="display: inline-block"> 
                <tr>
                    <th "> Display Result of Search </th>
                </tr> 
                <tr>
                    <td> USER NAME : <br/>
                    <p><a><?=$UsersName?> </a><br/>
                    <p> USER MAIL : <br/>
                    <p><a><?=$UserMail ?></a><br/>
                    <p> USER COMPANY : <br/>
                    <p><a><?=$UserCompany ?></a><br/></td>
                </tr>
            </table>

            </div>
        <br/>
        <br/>
        <br/>
        <?php endforeach; ?> 
              
    </div>
    <?php else :?>
    <p>Your search - <b><?=@$keyword;?></b> - did not match any documents.</p>        
    <?php endif; ?>    
 <?php endif; ?>


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
            
            
   

