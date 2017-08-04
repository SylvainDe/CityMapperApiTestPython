#! /usr/bin/python3
# vim: set expandtab tabstop=4 shiftwidth=4 :
"""Code using the API."""
from util_api import get_travel_time
from paris_addresses import swimming_pools
from friends import friends


if __name__ == '__main__':
    for name1, end in swimming_pools.items():
        print(name1)
        for name2, start in friends.items():
            val = get_travel_time(start, end)
            print(name2, '->', val)
        print()
