# opc
opc 协议采集


pip install OpenOPC

读取命令
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
