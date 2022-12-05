DELETE BACKUP TAG="last_db";
shutdown IMMEDIATE;
startup mount;
BACKUP DATABASE TAG last_db;
startup;