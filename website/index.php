<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="viewport" content="width=device-width">
        <link rel="stylesheet" href="index.css">
        <title>Lost and found</title>
    </head>
    <body>
        <p></p>
        <?php
            echo file_get_contents("header.html");
            echo file_get_contents("body.html");
            echo file_get_contents("footer.html");
        ?>
    </body>
</html>