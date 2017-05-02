import os
from PIL import Image


def copy_file(source_file, target_file):
    """赋值文件"""
    if os.path.isfile(source_file):
        if os.path.isfile(target_file):
            print("{}已存在".format(target_file))
        else:
            with open(target_file, "wb") as f:
                f.write(open(source_file, "rb").read())


def delete_file_folder(src):
    """删除文件夹（及文件）"""
    if os.path.isfile(src):
        try:
            os.remove(src)
        except OSError:
            print("删除{}错误".format(src))
    elif os.path.isdir(src):
        for item in os.listdir(src):
            item_src = os.path.join(src, item)
            delete_file_folder(item_src)
        try:
            os.rmdir(src)
        except OSError:
            print("删除{}错误".format(src))


user_home = os.path.expanduser("~")
father_folder = os.path.join(user_home, "Pictures")
old_folder = os.path.join(user_home,
                          "AppData\Local\Packages\Microsoft.Windows"
                          + ".ContentDeliveryManager_cw5n1h2txyewy\\"
                          + "LocalState\Assets")
tmp_folder = os.path.join(father_folder, "聚焦临时")
new_folder = os.path.join(father_folder, "聚焦")
横图 = os.path.join(new_folder, "横图")
竖图 = os.path.join(new_folder, "竖图")

for each in (tmp_folder, new_folder):
    if not os.path.exists(each):
        os.mkdir(each)

# 复制文件到临时文件夹
for file in os.listdir(old_folder):
    sourceFile = os.path.join(old_folder, file)
    targetFile = os.path.join(tmp_folder, file + ".jpg")
    copy_file(sourceFile, targetFile)

# 写照片
for file in os.listdir(tmp_folder):
    sourceFile = os.path.join(tmp_folder, file)
    if os.path.isfile(sourceFile):
        try:
            with Image.open(sourceFile) as img:
                a, b = img.size
                if a >= 1000 and b > 1000:
                    if a > b:
                        targetFile = os.path.join(横图, file)
                        copy_file(sourceFile, targetFile)
                        print(f"复制{targetFile}")
                    else:
                        targetFile = os.path.join(竖图, file)
                        copy_file(sourceFile, targetFile)
                        print(f"复制竖图{targetFile}")
                else:
                    print(f"{targetFile}出寸太小")
        except OSError:
            print(f"{sourceFile}不是图片")

delete_file_folder(tmp_folder)
