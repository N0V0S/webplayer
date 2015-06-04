

<html>

<?php
if ($_GET['info']) {
  
  echo(exec("python song.py info " . $_SERVER["REMOTE_ADDR"]));
}
if ($_GET['next']) {
  echo(exec("python song.py next " . $_SERVER["REMOTE_ADDR"]));
}
if ($_GET['prev']) {
  echo(exec("python song.py prev " . $_SERVER["REMOTE_ADDR"]));
}
if ($_GET['pause']) {
  echo(shell_exec("python song.py pause " . $_SERVER["REMOTE_ADDR"]));
}
if ($_GET['stop']) {
  echo(exec("python song.py stop " . $_SERVER["REMOTE_ADDR"]));
}
if ($_GET['volup']) {
  echo(exec("python song.py volup " . $_SERVER["REMOTE_ADDR"]));
}
if ($_GET['voldown']) {
  echo(exec("python song.py voldown " . $_SERVER["REMOTE_ADDR"]));
}
if ($_GET['mute']) {
  echo(exec("python song.py mute " . $_SERVER["REMOTE_ADDR"]));
}
?>


<body bgcolor="#222326" text="#FFFFFF">
<a href="?prev=true"><img src="image/prev.png"/></a>
<a href="?pause=true"><img src="image/pause.png"/></a>
<a href="?next=true"><img src="image/for.png"/></a>
<a href="?stop=true"><img src="image/stop.png"/></a><br>

<a href="?voldown=true"><img src="image/vol_down.png"/></a>
<a href="?volup=true"><img src="image/vol_up.png"/></a>
<a href="?mute=true"><img src="image/mute.png"/></a><br>

<a href="?info=true"><img src="image/info.png"/></a>
</body>
</html>