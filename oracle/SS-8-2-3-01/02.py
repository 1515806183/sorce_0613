# -*- coding: utf-8 -*-
import commands
test_name = 'SS-8-2-3-01评分题目二'
test_vlu = '检查系统层面查看所有 ora_后台进程'

save_address = "./score.txt"


def run():
    f = open(save_address, 'w')
    cmd = "ps  aux|grep ora_* | awk '{print $1}' | wc -l"
    com_ret = commands.getoutput(cmd)
    com_ret= int(com_ret)

    if com_ret > 1:
            f.write("%s: %s正确 ---ok\n" % (test_name, test_vlu))

    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()