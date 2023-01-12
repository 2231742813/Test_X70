#coding=utf-8
import json
import allure
import socket
import base64
import crcmod.predefined
from binascii import unhexlify
from common.read_host_port import Read_host_port
from common.CRC_16_XMODEM import crc16_xmodem


#  获取设备当前故障
class Test_01_read_device_breakdown:
    @allure.epic('X70')
    @allure.feature('设备模块')
    @allure.story('基本功能')
    @allure.title('用例标题：A001-获取设备故障信息')
    @allure.severity('blocker')
    def test_01_read_device_breakdown(self):
        a = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        host,port = Read_host_port().Read()
        a.connect(tuple((host,port)))
        # 帧头
        frame_header = b'\x02'
        # 地址
        frame_addres1 = b'0'
        frame_addres2 = b'0'
        # 帧类型
        frame_type1 = b'0'
        frame_type2 = b'1'
        # 校验码拼接,拼接后为字符串
        check_code = '3{0}3{1}3{2}3{3}'.format(str(frame_addres1, 'UTF-8'), str(frame_addres2, 'UTF-8'),str(frame_type1,'UTF-8'), str(frame_type2, 'UTF-8'))
        # crc检验
        check_code = crc16_xmodem(check_code)
        # # 转为字节，格式为'\x**\x**'
        check_code = base64.b16decode(check_code.upper())
        # 帧尾
        frame_end = b'\03'
        # 组合帧Data
        data = frame_header + frame_addres1 + frame_addres2 + frame_type1 + frame_type2 + check_code + frame_end
        # 发送数据
        a.send(data)
        # 接受返回数据
        msg = a.recv(1024)
        # 断开连接
        a.close()
        # 断言
        msg = str(msg)
        length = len(msg)
        msg = msg[8:length-10:]
        # 转为2进制
        print("\n---------------------------------------------------------------------------")
        print("取可变信息标志的当前故障")
        print("返回信息为：{}".format(msg))
        state_16 = msg
        state_10 = int(state_16 , 16)
        Binary = '{:016b}'.format(state_10)
        begin_color = '\033[1;31m'
        end_color = '\033[0m'
        if Binary[-2] == '1':
            print(begin_color + "控制器Failed" + end_color)
        else:
            print("控制器Pass")
        if Binary[-3] == '1':
            print(begin_color + "显示模组Failed" + end_color)
        else:
            print("显示模组Pass")
        if Binary[-4] == '1':
            print("begin_color + 模组电源Failed" + end_color)
        else:
            print("模组电源Pass")
        if Binary[-5] == '1':
            print(begin_color + "单像素Failed" + end_color)
        else:
            print("单像素Pass")
        if Binary[-6] == '1':
            print("begin_color + 检测系统Failed" + end_color)
        else:
            print("检测系统Pass")
        if Binary[-7] == '1':
            print(begin_color + "输入220V交流电Failed" + end_color)
        else:
            print("输入220V交流电Pass")
        if Binary[-8] == '1':
            print(begin_color + "防雷器Failed" + end_color)
        else:
            print("防雷器Pass")
        if Binary[-9] == '1':
            print(begin_color + "光敏部件Failed" + end_color)
        else:
            print("光敏部件Pass")
        if Binary[-10] == '1':
            print(begin_color + "温度Failed" + end_color)
        else:
            print("温度Pass")
        if Binary[-11] == '1':
            print(begin_color + "门开关Failed" + end_color)
        else:
            print("门开关Pass")
        print("---------------------------------------------------------------------------")


