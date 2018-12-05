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


    opc控制台命令
opc -h 192.168.2.148 -P 7766 -r Read Error.Int2



    重点servicemanager.LogInfoMsg 查看service 报错信息

运行 输入 eventvwr.msc 查看应用日志


**将一维数组，变为二维数组
  tag_groups = [tags[i:i+size] for i in range(0, len(tags), size)]
  
  opc api学习
  
  http://gray-box.net/daawrapper.php
