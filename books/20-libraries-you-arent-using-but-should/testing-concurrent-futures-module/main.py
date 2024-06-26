from concurrent.futures import ThreadPoolExecutor as Executor
# to use process instead of threads
# from concurrent.futures import ProcessPoolExecutor as Executor

urls = """google reddit facebook youtube""".split()


def fetch(url):
    from urllib import request, error
    try:
        data = request.urlopen(url).read()
        return '{}: length {}'.format(url, len(data))
    except error.HTTPError as e:
        return '{}: {}'.format(url, e)


with Executor(max_workers=4) as exe:
    template = 'http://www.{}.com'
    jobs = [exe.submit(fetch, template.format(u)) for u in urls]
    results = [job.result() for job in jobs]

print('\n'.join(results))
