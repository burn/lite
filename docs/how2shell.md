<a name=top><p>
<img src="/etc/img/lite.png" align=right width=300>
<a href="/">home</a> |
<a href="/README.md#top">about</a> |
<a href="/LICENSE.md#top">license</a>
<a href="http://github.com/burn/lite/issues">issues</a>

# Tips and Tricks for Using the Shell

## hashbangs

COntrol what interpreter runs a file

Add "hash bang" at start of file.  (non portable version)

```python
#!/usr/local/bin/python3
print([1,2,3])
```

Portable version

```python
#!/usr/bin/env python3
print([1,2,3])
```

Make the file executable

```sh
chmod +x file
```

Now any combination of languages can all exist in the same pipeline

```sh
ps aux | gawk '/bash/ && !/grep/ {print $2}'  | xargs kill
```

How it works

```
1- ps aux
```

This command will output the list of running processes and some info about them. The interesting info is that it'll output the PID of each process in its 2nd column. Here's an extract from the output of the command on my box:

```sh
$ ps aux
 rahmu     1925  0.0  0.1 129328  6112 ?        S    11:55   0:06 tint2
 rahmu     1931  0.0  0.3 154992 12108 ?        S    11:55   0:00 volumeicon
 rahmu     1933  0.1  0.2 134716  9460 ?        S    11:55   0:24 parcellite
 rahmu     1940  0.0  0.0  30416  3008 ?        S    11:55   0:10 xcompmgr -cC -t-5 -l-5 -r4.2 -o.55 -D6
 rahmu     1941  0.0  0.2 160336  8928 ?        Ss   11:55   0:00 xfce4-power-manager
 rahmu     1943  0.0  0.0  32792  1964 ?        S    11:55   0:00 /usr/lib/xfconf/xfconfd
 rahmu     1945  0.0  0.0  17584  1292 ?        S    11:55   0:00 /usr/lib/gamin/gam_server
 rahmu     1946  0.0  0.5 203016 19552 ?        S    11:55   0:00 python /usr/bin/system-config-printer-applet
 rahmu     1947  0.0  0.3 171840 12872 ?        S    11:55   0:00 nm-applet --sm-disable
 rahmu     1948  0.2  0.0 276000  3564 ?        Sl   11:55   0:38 conky -q
```

```sh
2- gawk '/conky/ && !/grep/ {print $2}'
```

I'm only interested in one process, so I use grep to find the entry corresponding to my program conky.

```sh
$ ps aux | gawk '/conky/ && !/grep/ {print $2}'
 rahmu     1948  0.2  0.0 276000  3564 ?        Sl   11:55   0:39 conky -q 
```

Note that I had to add two patterns to gawk: one to find conky and one to kill the grep. If I had just done
`gawk '/conky/   {print $2}'`, I would had

```sh
$ ps aux | gawk '/conky/ {print $2}'
 rahmu     1948  0.2  0.0 276000  3564 ?        Sl   11:55   0:39 conky -q
 rahmu     3233  0.0  0.0   7592   840 pts/1    S+   16:55   0:00 grep conky
```

```sh
3- xargs kill
```

I have the PID. All I need is to pass it to kill. To do this, I will use xargs.

xargs kill will read from the input (in our case from the pipe), form a command consisting of kill `<items>` (`<items>` are whatever it read from the input), and then execute the command created. In our case it will execute kill 1948. Mission accomplished.

BTW, pipelines are so cool they are now common in many languages. e.g. in Julia, lets say we have two
functions:

```julia
dd6(a) = a+6
div4(a) = 4/a;
```

You could either introduce temporary variables or embed the function calls:

```julia 
a = 2; b = add6(a); c = div4(b); println(c) # 0.5  
println(div4(add6(a)))
```

With piping you can write instead:

```julia
a |> add6 |> div4 |> println
```

Neat, heh?