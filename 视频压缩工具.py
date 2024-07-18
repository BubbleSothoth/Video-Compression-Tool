#coding:gbk
import subprocess
from sys import argv

def compress_video(input_file, output_file):
    try:
        # ����FFmpeg����
        command = [
            'ffmpeg',
            '-i', input_file,
            '-vf', 'scale=1920:1080',  # ���÷ֱ���
            '-r', '23.98',             # ����֡��
            '-c:a', 'copy',            # ������Ƶ���벻��
            output_file
        ]
        
        # ����FFmpeg����
        subprocess.run(command, check=True)
        
        print(f"��Ƶ�ѳɹ�ѹ��������Ϊ {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"ѹ����Ƶʱ����: {e}")

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
        print("""ʹ��˵��:
%s -i InputVideo -o OutputVideo")
-i InputVideo:\t������Ƶ�ļ�
-o OutputVideo:\t�����Ƶ�ļ�"""%(__back(__file__.split('\\')))
        )
        return 0x00

    try:
        index=argv.index("-i")+1
        fin=argv[index]

        index=argv.index("-o")+1
        fout=argv[index]
    except ValueError as err:
        print(f"��������: {err}")
        return 0x01

    compress_video(fin, fout)
    return 0x00

if __name__=="__main__":
    excode=main()
    exit(excode)