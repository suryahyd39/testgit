from time import perf_counter
import urllib.request
"""
This class takes a URL and calculates the length of page , time taken to download

"""
class webPage:
    def __init__(self,url):
        self.url=url 
        self._page=None
        self._pagesize=None
        self._time_to_download=None 
    @property
    def url(self):
        return self._url
    @url.setter
    def url(self,value):
        print('setter called .....')
        self._url=value
    @property
    def page(self):
        if self._page is None:
            self.download_page()
        return self._page 
    @property
    def pagesize(self):
        if self._page is  None:
            self.download_page()
        return self._pagesize
    def download_page(self):
        self._page=None
        self._time_to_download=None        
        start_time=perf_counter()
        with urllib.request.urlopen(self.url) as f:
            self._page=f.read()
        self._pagesize=len(self._page)
        end_time=perf_counter()
        self._time_to_download=end_time-start_time
    @property
    def time_to_download(self):
        if self._time_to_download is None:
            self.download_page()
        return self._time_to_download
    
urls=['https://wwww.google.com']
for url in urls:
    page=webPage(url)
    print(page.pagesize)
    # print(page.pagesize)
    # print(page.page)

# page1=webPage('https://www.google.com')
# print(page1.page)
# print(page1.pagesize)
# print(page1.time_to_download)