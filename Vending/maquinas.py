#!/usr/bin/python3

import sqlite3

def insert(db, tbl,  row):
    if tbl == 'maquinas':
    	db.execute('INSERT INTO maquinas (maqid, maqmod, maqloc) VALUES (?, ?, ?)', (row['maqid'], row['maqmod'], row['maqloc']))
    elif tbl == 'producto':
    	db.execute('INSERT INTO producto (prodid, prodname, prodcate, proddesc) VALUES (?, ?, ?, ?)', (row['prodid'], row['prodname'], row['prodcate'], row['proddesc']))
    db.commit()

def retrieve(db, maqid):
    cursor = db.execute('SELECT * FROM maquinas WHERE maqid = ?', (maqid,))
    return cursor.fetchone()

def disp_rows(db, tbl):
    if tbl == 'maquinas':
        cursor = db.execute('SELECT * FROM maquinas ORDER BY maqid')
        for row in cursor:
            print('  {}: {}: {}'.format(row['maqid'], row['maqmod'], row['maqloc']))
    elif tbl == 'producto':
        cursor = db.execute('SELECT * FROM producto ORDER BY prodid')
        for row in cursor:
            print('  {}: {}: {}: {}'.format(row['prodid'], row['prodname'], row['prodcate'], row['proddesc']))

##### Main #####
def main():

#def create_db():
    db = sqlite3.connect('maquinas.db')
    db.row_factory = sqlite3.Row
    print('Creating tables...')
    print('CREATE TABLE maquinas')
    db.execute('DROP TABLE IF EXISTS maquinas')
    db.execute('CREATE TABLE maquinas ( maqid text PRIMARY KEY NOT NULL, maqmod text NOT NULL, maqloc text NOT NULL)')
    print('CREATE TABLE producto')
    db.execute('DROP TABLE IF EXISTS producto')
    db.execute('CREATE TABLE producto ( prodid int PRIMARY KEY NOT NULL, prodname text NOT NULL, prodcate text NOT NULL, proddesc text)')

##### Main #####
#def main():
#    create_db()

# Ask for the values
#   maqidx = input("Numero Serial? ")
#   maqmodx = input("Modelo? ")
#   maqlocx = input("Localidad? ")
#   insert(db,'maquinas',dict(maqid = maqidx, maqmod = maqmodx, maqloc = maqlocx))

# Test of inserting rows
# maquinas ( maqid text PRIMARY KEY NOT NULL, maqmod text NOT NULL, maqloc text NOT NULL)')
    print('Inserting rows for maquinas...')
    insert(db,'maquinas',dict(maqid = '1234a', maqmod = 'AMS-360' , maqloc = 'PROGRESO'))
    insert(db,'maquinas',dict(maqid = '1234A', maqmod = 'AMS-360' , maqloc = 'FEDEX'))
#
# Duplicates are not allowed, but A != a
#    insert(db, dict(maqid = '1234A', maqmod = 'AMS-360' , maqloc = 'COMUDE'))
#
    insert(db,'maquinas',dict(maqid = '1234b', maqmod = 'AMS-360' , maqloc = 'TOSHIBA'))
    insert(db,'maquinas',dict(maqid = '1234c', maqmod = 'AMS-360' , maqloc = 'COTTON'))
    print('Inserting successfully')

# Retriving rows
    disp_rows(db,'maquinas')

# Test of inserting rows
# producto ( prodid int PRIMARY KEY NOT NULL, prodname text NOT NULL, prodcate text NOT NULL, proddesc text)')
    print('Inserting rows for producto...')
    insert(db,'producto',dict(prodid = '1234a', prodname = 'AMS-360' , prodcate = 'PROGRESO', proddesc = ''))
    insert(db,'producto',dict(prodid = '1234b', prodname = 'AMS-360' , prodcate = 'PROGRESO', proddesc = ''))
#
# Duplicates are not allowed, but A != a
#    insert(db, dict(prodid = '1234a', prodname = 'AMS-360' , prodcate = 'PROGRESO', proddesc = ''))
#
    insert(db,'producto',dict(prodid = '1234c', prodname = 'AMS-360' , prodcate = 'PROGRESO', proddesc = ''))
    insert(db,'producto',dict(prodid = '1234d', prodname = 'AMS-360' , prodcate = 'PROGRESO', proddesc = ''))
    print('Inserting successfully')

# Retriving rows
    disp_rows(db,'producto')
	
if __name__ == "__main__": main()
