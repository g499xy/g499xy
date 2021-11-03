import pymysql
import configparser
import os
def getConf(confFileName,env):
    path = os.path.dirname(os.path.realpath(__file__))
    cfgpath = os.path.join(path,confFileName)
    # print(cfgpath)

    conf = configparser.ConfigParser()
    conf.read(cfgpath, encoding="utf-8-sig")
    host=conf.get(env,"host")
    port= conf.get(env, "port")
    uname=conf.get(env,"username")
    pswd=conf.get(env,"pswd")
    db=conf.get(env,"db")
    # print(type(host))
    return  host,port,uname,pswd,db

def link_mysql(sql,confFileName,env):
    confdata=getConf(confFileName,env)
    db=pymysql.connect(host=confdata[0],port=int(confdata[1]),user=confdata[2],password=confdata[3],db=confdata[4])
    cr=db.cursor()
    cr.execute(sql)
    data =cr.fetchall()
    db.commit()
    db.close()
    return data
if __name__ == '__main__':
    print(link_mysql("select * from users;","database.ini","dev"))
