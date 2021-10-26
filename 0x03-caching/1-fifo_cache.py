#!/usr/bin/python3
""" FIFO Caching """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Puts item in cache """
        if key is None or item is None:
            return

        if key not in self.queue:
            self.queue.append(key)
        else:
            self.mv_last_list(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.get_first_list(self.queue)
            if first:
                self.queue.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

    def get(self, key):
        """ Gets item from cache """
        return self.cache_data.get(key, None)

    def mv_last_list(self, item):
        """ Moves element to last idx of list """
        length = len(self.queue)
        if self.queue[length - 1] != item:
            self.queue.remove(item)
            self.queue.append(item)

    @staticmethod
    def get_first_list(array):
        """ Get first element of list or None """
        return array[0] if array else None
