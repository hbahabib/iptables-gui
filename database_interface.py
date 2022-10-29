#!/usr/bin/python3
import sqlite3

def insert_rules(chain, target, proto, opt, port, src_ip, dest_ip):
  conn = sqlite3.connect('iptables_database.db')
  conn.execute("INSERT INTO IPTABLES_DATABASE (CHAIN, TARGET, PROTO, OPT, PORT, SRC_IP, DEST_IP) \
  VALUES (?, ?, ?, ?, ?, ?, ?)",(chain, target, proto, opt, port, src_ip, dest_ip))
  conn.commit()
  conn.close()
  







def retrieve_rules():
  results = []
  conn = sqlite3.connect('iptables_database.db')
  cursor = conn.execute("SELECT CHAIN, TARGET, PROTO, OPT, PORT, SRC_IP, DEST_IP FROM IPTABLES_DATABASE")
  for row in cursor:
      results.append(list(row))
  return results