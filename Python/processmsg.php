<?php
 if(isset($_POST['mess'])){
     
     if(!file_exists("posts.txt"))
     {
         $fp = fopen('posts.txt', 'a+');
         fwrite($fp, '');   
         chmod("posts.txt", 0644);

            // you may have to use this one
            // remember to comment out the one with 0644 if using this one
            // chmod("posts.txt", 0777);
         fclose($fp);
     }
   $file = 'posts.txt';  
   $str = $_POST['mess'] ;
   $reply="";
   file_put_contents("posts.txt","\r\n".'user-->'.$str,FILE_APPEND);
   $reply=getanswer($str);
//    $finalreply=join($reply,"\n");
   file_put_contents("posts.txt","\r\n\n".'bot-->'.$reply,FILE_APPEND);
   echo $reply;

 }
 else{
     echo "not saved";
 }
function getanswer($str){
     $result = shell_exec('C:\Users\lenovo\Anaconda3\python.exe C:\Users\lenovo\PycharmProjects\CustomerService\check.py '.'"'.$str.'"');
    return $result;
}
?>