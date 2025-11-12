import urllib.request
import urllib.error
import time
from multiprocessing import Pool

start = time.time()

file = open('/Users/dan/Downloads/external_sites.txt', 'r')
urls = file.readlines()
results_file = open('/Users/dan/Downloads/results.txt', 'w')


#print(urls)

def checkurl(url):
    print("Checking " + url)
    try:
        conn = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        # Return code error (e.g. 404, 501, ...)
        # ...
        results_file.write('HTTPError: {}'.format(e.code) + ', ' + url)
    except urllib.error.URLError as e:
        # Not an HTTP-specific error (e.g. connection refused)
        # ...
        results_file.write('URLError: {}'.format(e.reason) + ', ' + url)
    else:
        # 200
        # ...
        results_file.write('good' + ', ' + url)


if __name__ == "__main__":
    # p = Pool(processes=20)
    # result = p.map(checkurl, urls)
    for url in urls:
        checkurl(url)

print("done in : ", time.time()-start)