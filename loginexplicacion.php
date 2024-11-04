<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Inicio de sesión</title>
</head>
<body>
// Creamos el formulario que envía los datos al archivo loginManager.php.
    <form action="managers/loginManager.php" method="post">
        //Este primer input tiene un campo oculto.
        <input type="hidden" name="op" value="in">
        <input type="email" name="mail" placeholder="Correo electrónico">
        <input type="password" name="pass" placeholder="Contraseña">
        <input type="submit" value="Entrar">
<?php
    if(isset($_POST['msg'])) echo $_POST['msg'];
?>
</body>
</html>