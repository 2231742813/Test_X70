# coding=utf-8
import os
import yaml
yaml.warnings({'YAMLLoadWarning': False})

#  读取host与port
class Read_host_port:
    def Read(self):
        # 获取工程目录
        project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # 拼接用例路径
        case_path = project_path + '\Test_data' + '\host_port.yaml'
        f = open(case_path, 'r', encoding='gbk')
        res = f.read()
        res = yaml.load(res)
        res = res['host_port']
        # 返回host与port
        return res['host'], int(res['port'])

# res,port = Read_host_port().Read()
# print(res)


