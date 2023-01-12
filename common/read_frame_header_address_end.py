# coding=utf-8
import os
import yaml
yaml.warnings({'YAMLLoadWarning': False})

#  读取帧头，帧地址，帧尾
class Read_frame_header_address_end:
    def Read(self):
        # 获取工程目录
        project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # 拼接用例路径
        case_path = project_path + '\Test_data' + r'\frame_header_address_end.yaml'
        f = open(case_path, 'r', encoding='utf-8')
        res = f.read()
        res = yaml.load(res)
        res = res['frame_header_address_end']
        # 返回host与port
        return res

res = Read_frame_header_address_end().Read()
print(res)
print(type(res))
frame_header = res['frame_header']
print(frame_header.encode())
print(type(frame_header.encode()))
# print(res['frame_header'])
# print(type(res['frame_header']))
