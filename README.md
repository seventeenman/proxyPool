# proxyPool
 A lightweight proxy pool based on automated crawlers.Simple implementation of functions, self-fetching if necessary, my computer is macOS, not tested on Windows and Linux.If you need automated crawlers, you may need to configure the selenium module.

 I tested that the free agent website actually available agents rarely can be used, there are about two available on each page. 

 lol

## Requirements

> python >= 3.0
>
> requests==2.25.1
>
> selenium==3.141.0

## QUICK START

### Crawl ip

Crawl the ip address on the free proxy website through the selenium module and save it to ip.txt.

```python
python3 save.py -p {page_count}
python3 save.py -p 2
```

### Survival detection

Check the survival of the ip address in ip.txt in a multi-threaded form.

```pyt
python3 check.py -t {thread_count}
python3 check.py -t 2
```

### usage

Send a request to the interface of the local python server to obtain the ip address of the proxy.

```pyth
# server
python3 server.py
# example
python3 example.py
```

