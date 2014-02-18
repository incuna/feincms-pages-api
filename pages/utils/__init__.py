def build_url(url, get):
    params = ''.join('&{}={}'.format(*item) for item in get.items())
    params = params.replace('&', '?', 1)
    return url + params
