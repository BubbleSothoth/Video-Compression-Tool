#coding:gbk
import subprocess
from sys import argv

def compress_video(input_file, output_file):
    try:
        # 设置FFmpeg命令
        command = [
            'ffmpeg',
            '-i', input_file,
            '-vf', 'scale=1920:1080',  # 设置分辨率
            '-r', '23.98',             # 设置帧率
            '-c:a', 'copy',            # 保持音频编码不变
            output_file
        ]
        
        # 运行FFmpeg命令
        subprocess.run(command, check=True)
        
        print(f"视频已成功压缩并保存为 {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"压缩视频时出错: {e}")

def __back(list:list):
    return list[list.__len__()-1]

def __find(list,val)->int:
    for i in len(list):
        if list[i]==val:
            return i
        pass
    return len(list)

def main() -> int:
    fin=""
    fout=""
    index=argv.__len__()


    if "-?" in argv:
        print("""使用说明:
%s -i InputVideo -o OutputVideo")
-i InputVideo:\t导入视频文件
-o OutputVideo:\t输出视频文件"""%(__back(__file__.split('\\')))
        )
        return 0x00

    try:
        index=argv.index("-i")+1
        fin=argv[index]

        index=argv.index("-o")+1
        fout=argv[index]
    except ValueError as err:
        print(f"参数出错: {err}")
        return 0x01

    compress_video(fin, fout)
    return 0x00

if __name__=="__main__":
    excode=main()
    exit(excode)