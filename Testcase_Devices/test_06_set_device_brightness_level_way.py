#coding=utf-8
import json
import allure
import socket
import base64
import crcmod.predefined
from binascii import unhexlify
from common.read_host_port import Read_host_port
from common.CRC_16_XMODEM import crc16_xmodem
import random


#  设置可变信息标志的亮度调节方式
class Test_06_set_device_brightness_level_way:
    @allure.epic('X70')
    @allure.feature('设备模块')
    @allure.story('基本功能')
    @allure.title('用例标题：A006-设置可变信息标志的亮度调节方式')
    @allure.severity('blocker')
    def test_06_set_device_brightness_level_way(self):
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
        frame_type2 = b'4'
        # 亮度调节方式
        setting_method = random.choice(['0' , '1'])
        frame_data  = setting_method.encode()
        # 校验码拼接,拼接后为字符串
        check_code = '3{0}3{1}3{2}3{3}3{4}'.format(str(frame_addres1, 'UTF-8'), str(frame_addres2, 'UTF-8'),str(frame_type1,'UTF-8'), str(frame_type2, 'UTF-8'), str(frame_data, 'utf-8'))
        # crc检验
        check_code = crc16_xmodem(check_code)
        # # 转为字节，格式为'\x**\x**'
        check_code = base64.b16decode(check_code.upper())
        # 帧尾
        frame_end = b'\03'
        # 组合帧Data
        data = frame_header + frame_addres1 + frame_addres2 + frame_type1 + frame_type2 + frame_data + check_code + frame_end
        # 发送数据
        a.send(data)
        # 接受返回数据
        msg = a.recv(1024)
        # 断开连接
        a.close()
        # 断言
        msg = str(msg)
        print("\n---------------------------------------------------------------------------")
        msg = msg[8:len(msg)-10:]
        print("设置可变信息标志的亮度调节方式")
        print("返回信息 {}".format(msg))
        print("---------------------------------------------------------------------------")


