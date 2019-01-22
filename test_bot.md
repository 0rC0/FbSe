

```python
# Example Usage
```


```python
from time import sleep
from selenium import __version__ as selenium_version
import FbBot
import importlib
importlib.reload(FbBot)
FbBot = FbBot.FbBot
```


```python
selenium_version
```




    '3.141.0'




```python
bot = FbBot('test.json')
```


```python
bot.read_timeline()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~/Programs/anaconda3/envs/fb_se/lib/python3.6/site-packages/urllib3/connectionpool.py in _make_request(self, conn, method, url, timeout, chunked, **httplib_request_kw)
        376             try:  # Python 2.7, use buffering of HTTP responses
    --> 377                 httplib_response = conn.getresponse(buffering=True)
        378             except TypeError:  # Python 3


    TypeError: getresponse() got an unexpected keyword argument 'buffering'

    
    During handling of the above exception, another exception occurred:


    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-11-18d3bfb86a54> in <module>
    ----> 1 bot.read_timeline()
    

    ~/Code/Python/fb_se/FbBot.py in read_timeline(self)
         95         Main function, read timeline posts until everything is seen
         96         """
    ---> 97         self.login()
         98         read = False
         99         old_posts = (len(self.data_seen) if self.data_seen else 0)


    ~/Code/Python/fb_se/FbBot.py in login(self)
         33         self.b.find_element_by_id('email').send_keys(self.email)
         34         self.b.find_element_by_id('pass').send_keys(self.pw)
    ---> 35         self.b.find_element_by_id('loginbutton').click()
         36         try:
         37             WebDriverWait(self.b, 10).until(ec.presence_of_element_located((


    ~/Programs/anaconda3/envs/fb_se/lib/python3.6/site-packages/selenium/webdriver/remote/webelement.py in click(self)
         78     def click(self):
         79         """Clicks the element."""
    ---> 80         self._execute(Command.CLICK_ELEMENT)
         81 
         82     def submit(self):


    ~/Programs/anaconda3/envs/fb_se/lib/python3.6/site-packages/selenium/webdriver/remote/webelement.py in _execute(self, command, params)
        631             params = {}
        632         params['id'] = self._id
    --> 633         return self._parent.execute(command, params)
        634 
        635     def find_element(self, by=By.ID, value=None):


    ~/Programs/anaconda3/envs/fb_se/lib/python3.6/site-packages/selenium/webdriver/remote/webdriver.py in execute(self, driver_command, params)
        317 
        318         params = self._wrap_value(params)
    --> 319         response = self.command_executor.execute(driver_command, params)
        320         if response:
        321             self.error_handler.check_response(response)


    ~/Programs/anaconda3/envs/fb_se/lib/python3.6/site-packages/selenium/webdriver/remote/remote_connection.py in execute(self, command, params)
        372         data = utils.dump_json(params)
        373         url = '%s%s' % (self._url, path)
    --> 374         return self._request(command_info[0], url, body=data)
        375 
        376     def _request(self, method, url, body=None):


    ~/Programs/anaconda3/envs/fb_se/lib/python3.6/site-packages/selenium/webdriver/remote/remote_connection.py in _request(self, method, url, body)
        395 
        396         if self.keep_alive:
    --> 397             resp = self._conn.request(method, url, body=body, headers=headers)
        398 
        399             statuscode = resp.status


    ~/Programs/anaconda3/envs/fb_se/lib/python3.6/site-packages/urllib3/request.py in request(self, method, url, fields, headers, **urlopen_kw)
         70             return self.request_encode_body(method, url, fields=fields,
         71                                             headers=headers,
    ---> 72                                             **urlopen_kw)
         73 
         74     def request_encode_url(self, method, url, fields=None, headers=None,


    ~/Programs/anaconda3/envs/fb_se/lib/python3.6/site-packages/urllib3/request.py in request_encode_body(self, method, url, fields, headers, encode_multipart, multipart_boundary, **urlopen_kw)
        148         extra_kw.update(urlopen_kw)
        149 
    --> 150         return self.urlopen(method, url, **extra_kw)
    

    ~/Programs/anaconda3/envs/fb_se/lib/python3.6/site-packages/urllib3/poolmanager.py in urlopen(self, method, url, redirect, **kw)
        321             response = conn.urlopen(method, url, **kw)
        322         else:
    --> 323             response = conn.urlopen(method, u.request_uri, **kw)
        324 
        325         redirect_location = redirect and response.get_redirect_location()


    ~/Programs/anaconda3/envs/fb_se/lib/python3.6/site-packages/urllib3/connectionpool.py in urlopen(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)
        598                                                   timeout=timeout_obj,
        599                                                   body=body, headers=headers,
    --> 600                                                   chunked=chunked)
        601 
        602             # If we're going to release the connection in ``finally:``, then


    ~/Programs/anaconda3/envs/fb_se/lib/python3.6/site-packages/urllib3/connectionpool.py in _make_request(self, conn, method, url, timeout, chunked, **httplib_request_kw)
        378             except TypeError:  # Python 3
        379                 try:
    --> 380                     httplib_response = conn.getresponse()
        381                 except Exception as e:
        382                     # Remove the TypeError from the exception chain in Python 3;


    ~/Programs/anaconda3/envs/fb_se/lib/python3.6/http/client.py in getresponse(self)
       1329         try:
       1330             try:
    -> 1331                 response.begin()
       1332             except ConnectionError:
       1333                 self.close()


    ~/Programs/anaconda3/envs/fb_se/lib/python3.6/http/client.py in begin(self)
        295         # read until we get a non-100 response
        296         while True:
    --> 297             version, status, reason = self._read_status()
        298             if status != CONTINUE:
        299                 break


    ~/Programs/anaconda3/envs/fb_se/lib/python3.6/http/client.py in _read_status(self)
        256 
        257     def _read_status(self):
    --> 258         line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
        259         if len(line) > _MAXLINE:
        260             raise LineTooLong("status line")


    ~/Programs/anaconda3/envs/fb_se/lib/python3.6/socket.py in readinto(self, b)
        584         while True:
        585             try:
    --> 586                 return self._sock.recv_into(b)
        587             except timeout:
        588                 self._timeout_occurred = True


    KeyboardInterrupt: 

