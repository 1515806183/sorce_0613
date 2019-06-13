# -*- coding: utf-8 -*-
import cx_Oracle
test_name = 'SS-8-2-3-01评分题目六'
test_vlu = '查询v$database,查看数据库运行状态'

save_address = "./score.txt"
# 数据库信息
username = "system"
pwd = "SXadmin#1234"
ip = "127.0.0.1"
tns = "oradb"
port = 1521


def run():
    f = open(save_address, 'w')
    # 1 检查数据库是否能正常打开
    conn = cx_Oracle.connect('{0}/{1}@{2}:{3}/{4}'.format(username, pwd, ip, port, tns))
    cursor = conn.cursor()
    cursor.execute("select status from v$instance")
    ret = cursor.fetchone()  # 返回('OPEN',)

    if "OPEN" in ret:
        f.write('%s:%s ---ok\n' % (test_name, test_vlu))
    else:
        f.write('%s:%s ---error\n' % (test_name, test_vlu))

    f.close()
    cursor.close()
    conn.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()