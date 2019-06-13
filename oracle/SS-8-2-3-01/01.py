# -*- coding: utf-8 -*-
import commands
test_name = 'SS-8-2-3-01评分题目一'
test_vlu = '检查操作系统空间使用情况'

save_address = "./score.txt"


def run():
    f = open(save_address, 'w')
    cmd = "df -h"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")

    if com_ret:
            f.write("%s: %s正确 ---ok\n" % (test_name, test_vlu))

    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()