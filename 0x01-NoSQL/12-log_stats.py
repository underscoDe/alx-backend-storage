#!/usr/bin/env python3
"""Defines a function that  provides some stats
   about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def nginx_stats_check():
    """provides some stats about Nginx logs stored in MongoDB:"""
    client = MongoClient()
    collection = client.logs.nginx

    doc_count = collection.count_documents({})
    print(f'{doc_count} logs')

    methods_list = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods_list:
        nbr = collection.count_documents({"method": method})
        print(f'\tmethod {method}: {nbr}')
    status_count = collection.count_documents({
        "method": "GET", "path": "/status"
    })
    print(f'{status_count} status check')


if __name__ == "__main__":
    nginx_stats_check()
