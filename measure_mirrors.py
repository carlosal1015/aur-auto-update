#!/usr/bin/env python

import requests
import re


def get_arch4edu_mirrors():
    mirrorlist = "https://raw.githubusercontent.com/arch4edu/mirrorlist/master/mirrorlist.arch4edu"
    content = requests.get(url=mirrorlist).content.decode(encoding="utf-8")
    return re.findall(pattern=r"http.*\/", string=content)


def get_delay(mirror):
    try:
        # https://stackoverflow.com/a/21017825
        r = requests.get(url=mirror, timeout=(3.05, 27))
        delay = r.elapsed.total_seconds()
        # print(f'{mirror} is online and took {delay:.2f} seconds.')
        return delay
    except requests.exceptions.RequestException:
        # print(f'{mirror} is offline.')
        return "NaN"


if __name__ == "__main__":
    mirrors = get_arch4edu_mirrors()
    delay_mirors = dict()
    for mirror in mirrors:
        delay_mirors[mirror] = get_delay(mirror=mirror)

    print(delay_mirors)
