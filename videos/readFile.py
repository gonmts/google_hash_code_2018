def read_videos_file(fname):
    file_content = open(fname, 'rb').read().decode('iso-8859-1')
    content = file_content.splitlines()

    first_line = content[0].split(" ")
    videos = int(first_line[0])
    number_endpoints = int(first_line[1])
    requests = int(first_line[2])
    cache_number = int(first_line[3])
    size_cache = int(first_line[4])
    videos_size = [int(x) for x in content[1].split(" ")]
    endpoints = {}
    videos_per_endpoint = {}

    line_number = 2

    for i in range(number_endpoints):
        line = content[line_number].split(" ")
        latency = int(line[0])
        caches_number = int(line[1])
        res = [latency]
        for k in range(caches_number):
            line_number += 1
            line = content[line_number].split(" ")
            res += [(int(line[0]), int(line[1]))]
        line_number += 1
        endpoints[i] = res
        videos_per_endpoint[i] = []        

    for i in range(requests):
        line = content[line_number].split(" ")
        e = int(line[1])
        videos_per_endpoint[e] += [(int(line[0]), int(line[2]))]
        line_number += 1

    return videos, number_endpoints, requests, cache_number, size_cache, videos_size, endpoints, videos_per_endpoint
