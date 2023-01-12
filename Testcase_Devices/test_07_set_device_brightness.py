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


#  设置可变信息标志的当前显示亮度
class Test_07_set_device_brightness:
    @allure.epic('X70')
    @allure.feature('设备模块')
    @allure.story('基本功能')
    @allure.title('用例标题：A007-设置可变信息标志的当前显示亮度')
    @allure.severity('blocker')
    def test_07_set_device_brightness(self):
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
        frame_type2 = b'5'
        # 调节亮度值
        setting_lights = random.randint(00 , 31)
        # 将0-31转为00-31格式字符串
        if setting_lights <= 9 :
            setting_lights = '0' + str(setting_lights)
        else :
            setting_lights = str(setting_lights)
        # str转为字节形式
        # lipu = str(setting_lights[-1])
        frame_data1 = str(setting_lights[0]).encode()
        frame_data2 = str(setting_lights[-1]).encode()
        # 离谱【1】不行，【-1】可以,且设置成setting_lights1转换异常，因此用lipu来接受第二个字节
        # 校验码拼接,拼接后为字符串
        check_code = '3{0}3{1}3{2}3{3}3{4}3{5}3{4}3{5}3{4}3{5}'.format(str(frame_addres1, 'UTF-8'), str(frame_addres2, 'UTF-8'),str(frame_type1,'UTF-8'), str(frame_type2, 'UTF-8'), str(frame_data1, 'utf-8'), str(frame_data2, 'utf-8'))
        # crc检验
        check_code = crc16_xmodem(check_code)
        # # 转为字节，格式为'\x**\x**'
        check_code = base64.b16decode(check_code.upper())
        # 帧尾
        frame_end = b'\03'
        # 组合帧Data
        data = frame_header + frame_addres1 + frame_addres2 + frame_type1 + frame_type2 + frame_data1 + frame_data2 + frame_data1 + frame_data2 + frame_data1 + frame_data2 + check_code + frame_end
        # 发送数据
        a.send(data)
        # 接受返回数据
        msg = a.recv(1024)
        # 断开连接
        a.close()
        # 断言
        msg = str(msg)
        print("\n---------------------------------------------------------------------------")
        print("设置可变信息标志的当前显示亮度")
        print("返回结果待完善")
        print(msg)
        msg = msg[8:len(msg)-10:]
        print("---------------------------------------------------------------------------")


