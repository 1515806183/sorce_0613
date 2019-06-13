# -*- coding: utf-8 -*-
import cx_Oracle, pexpect, sys

test_name = 'SS-8-2-3-01评分题目八'
test_vlu = '数据库运行状态'
test_vlu1 = '查看数据库的归档模式'

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

    # 关闭连接
    cursor.close()
    conn.close()

    # 2
    try:

        child = pexpect.spawn('sqlplus / as sysdba')
        ret = child.expect([pexpect.TIMEOUT, 'Enter user-name', 'SQL'])
        if ret == 0:
            print('[-] Error connecting')
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))
            return

        if ret == 1:
            child.sendcontrol('c')
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

        if ret == 2:
            child.buffer = ""
            child.sendline('archive log list;')  # 执行查询命令
            child.expect('Current')  # 辅助命令，为了before能取到要的结果
            cmd_ret = child.before.strip().lower().replace(" ", "")
            if 'No Archive Mode'.lower().replace(" ", "") in cmd_ret:
                f.write("%s: %s正确 ---ok\n" % (test_name, test_vlu1))

            else:
                f.write("%s: %s错误 ---error\n" % (test_name, test_vlu1))
            # 关闭退出sqlplus
            child.sendline('')
            child.expect('SQL>')
            child.sendline('exit')


    except:
        f.write('%s:查询数据库错误,无法%s ---error\n' % (test_name, test_vlu1))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()