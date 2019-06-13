# -*- coding: utf-8 -*-
import commands
test_name = 'SS-8-2-3-01评分题目三'
test_vlu = '检查运行监听器管理工具 lsnrctl'

save_address = "./score.txt"


def run():
    f = open(save_address, 'w')
    # 1 先source .bash_profile环境变量
    cmd = 'source /root/.bash_profile'
    commands.getoutput(cmd)

    # 2
    cmd = "lsnrctl start"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")

    if 'The command  complete successfully'.lower().replace(" ", "") in com_ret or 'LISTENER has already been started'.lower().replace(" ", "") in com_ret:
            f.write("%s: %s正确 ---ok\n" % (test_name, test_vlu))

    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()