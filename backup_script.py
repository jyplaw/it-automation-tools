import shutil
import datetime
import os

def backup_folder(source, backup_dir="backups"):

    if not os.path.exists(backup_dir):
        os.mkdir(backup_dir)

    time_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"{backup_dir}/backup_{time_str}"

    shutil.make_archive(backup_name, 'zip', source)

    print("Backup created:", backup_name)

# 使用
backup_folder("test_data")