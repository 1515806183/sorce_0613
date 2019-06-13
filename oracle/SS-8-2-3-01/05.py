# -*- coding: utf-8 -*-
import commands, pexpect

test_name = 'SS-8-2-3-01评分题目五'
test_vlu = '检查sqlplus 工具'

save_address = "./score.txt"


def run():
    f = open(save_address, 'w')
    # 1 先source .bash_profile环境变量
    cmd = 'source /root/.bash_profile'
    commands.getoutput(cmd)

    # 2
    child = pexpect.spawn('sqlplus / as sysdba')
    ret = child.expect([pexpect.TIMEOUT, 'Enter user-name', 'SQL>'])
    if ret == 0:
        print('[-] Error connecting')
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))
        return

    if ret == 1:
        child.sendcontrol('c')
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    if ret == 2:
        child.sendline('exit')
        f.write("%s: %s正确 ---ok\n" % (test_name, test_vlu))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()