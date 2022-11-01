#!/usr/bin/python3


import sqlite3

conn = sqlite3.connect('iptables_database.db')
query = (''' CREATE TABLE IPTABLES_DATABASE
           (CHAIN TEXT,
           TARGET TEXT,
           PROTO TEXT,
           PORT INT,
           OPT TEXT,
           SRC_IP TEXT,
           DEST_IP TEXT);'''
        )
conn.execute(query)
conn.close()
