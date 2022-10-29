#!/usr/bin/python3


import sqlite3

conn = sqlite3.connect('iptables_database.db')
query = (''' CREATE TABLE IPTABLES_DATABASE
           (CHAIN TEXT,
           TARGET TEXT,
           PROTO TEXT,
           PORT INT,
           OPT TEXT,
           SRC_IP INT,
           DEST_IP INT);'''
        )
conn.execute(query)
conn.close()
