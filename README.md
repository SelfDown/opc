# opc
opc 协议采集


pip install OpenOPC

cmd 读取命令
opc -r Random.String Random.Int4 Random.Real8

python 命令

import OpenOPC

opc = OpenOPC.client() 或者opc = OpenOPC.open_client('localhost')


opc.servers()


opc.connect('Matrikon.OPC.Simulation')

opc.read( ['Random.Int2', 'Random.Real4', 'Random.String'] )

可以去下载Matrikon的模拟器

学习网站
http://openopc.sourceforge.net/other.html

OPCClient 是可视化客户端。


opc 如果是dcom 方式读取，OpenOPC.client() 会包pythoncom 不存在，安装pypiwin32 即可，220版本
