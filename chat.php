<html>
<head>
<title>
</title>
<link href='http://fonts.googleapis.com/css?family=Oxygen:400,300,700' rel='stylesheet' type='text/css'/>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<script>
    $(document).ready(function(){

    $('button').click(function() {
           var message=document.getElementById("text").value;
           alert("success"+message);
            $.ajax({
            url : "Python/processmsg.php",
            type : "post",
            data: { mess : message},
            success : function(response) {
                alert("success"+response);
            } 
        });
    });

});
</script>
</head>
<body id="b">
<div>
    <div class="showchat">
    <ul>
        <?php
        /*$fh = fopen('posts.txt','r');
        while ($line = fgets($fh)) {
            // <... Do your work with the line ...>
             // echo($line);
             if(isset($line)){
                  $msg=join('<br/>',$line);
                  ?>
                  <li class="customer"><?php echo $msg; ?></li>
                  <li class="bot"><?php echo $botmsg; ?></li>
        <?php
             }
        }
        fclose($fh);*/
        ?>
        </ul>
    </div>
<textarea id="text" rows="5" cols="5"></textarea>
<button id="post"  type="button">POST</button>
</div>
</body>
</html>
