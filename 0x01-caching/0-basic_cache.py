#!/usr/bin/python3
"""
Task 0 Create a class BasicCache 
that inherits from BaseCaching
and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Overide methods defined in basecaching
    Args:
        key: the dictionary key.
        item: the data items
    Returns:
        result: return the value of data items.
    """

    def put(self, key, item):
        """assign to the dictionary self.cache_data 
        the item value by key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key
        """
        result = self.cache_data.get(key)
        return result


# #!/usr/bin/env python3
# """ 0-basic_cache.py
# """
# from base_caching import BaseCaching


# class BasicCache(BaseCaching):
#     """
#     Basic Cache System  that have no limit
#      Args:
#         key: the dictionary key.
#         item: the data items
#     Returns:
#         result: return the value of data items.
#     """

#     def __init__(self):
#         """
#         Initialize
#         """
#         super().__init__()

#     def put(self, key, item):
#         """
#         set item to cache
#         """
#         if key and item:
#         # if key is None or item is None:
#         #     return
#             self.cache_data[key] = item

#     def get(self, key):
#         """
#         get item from cache if it exists other none
#         """
#         if key:
#             try:
#                 return self.cache_data[key]
#             except Exception as e:
#                 return None
