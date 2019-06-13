# -*- coding: utf-8 -*-
import commands, os
test_name = 'SS-8-2-3-01评分题目十七'
test_vlu = '查看最新 500 行数据库 alert 日志，利用命令检索 ORA-类型错误'

save_address = "./score.txt"
name = '/oracle/diag/rdbms/orcl/orcl/alert/log.xml'


def run():
    f = open(save_address, 'w')
    try:
        if os.path.exists(name):
            f.write("%s:文件%s存在 ---ok\n" % (test_name, name))
            cmd = "tail -n -500 %s | grep ORA-* | wc -l" % name
            com_ret = commands.getoutput(cmd)
            com_ret = int(com_ret)
            if com_ret > 0:
                f.write("%s: %s正确 ---ok\n" % (test_name, test_vlu))
            else:
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))
        else:
            f.write("%s:文件%s不存在 ---error\n" % (test_name, name))
            f.write("%s:文件%s不存在,无法%s ---error\n" % (test_name, name, test_vlu))
    except:
        f.write("%s:打开文件%s错误,无法%s ---error\n" % (test_name, name, test_vlu))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()