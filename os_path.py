import os

# os.mkdir('new')
# os.makedirs(r'D:\UNITS\Python\Units\School\new_older\new1', exist_ok=True)
# ps = os.path.join(r'D:\UNITS\Python\Units\School\new_older', 'new1')
# ps = os.path.join('new/new_older')
# # ps = os.path.join('..')
# print(ps)
# p = os.path.abspath(ps)
# print(p)
# print(os.listdir(p))

def seek(target, target1=''):
    size = 0
    cnt_folders = 0
    cnt_files = 0
    ps = os.path.join(target, target1)
    print(ps)
    path_ = os.path.abspath(ps)
    print(path_)
    for obj in os.listdir(path_):
        # print(obj)
        ps = os.path.join(path_, obj)
        print(ps)
        if os.path.isfile(ps):
            cnt_files += 1
            size += os.path.getsize(ps)
        else:
            cnt_folders += 1
            # cnt_folders += seek(ps)[1]
            # size += seek(ps)[0]
            # cnt_files += seek(ps)[2]
            size1, cnt_folders1, cnt_files1 = seek(ps)
            size += size1
            cnt_folders += cnt_folders1
            cnt_files += cnt_files1


    return size, cnt_folders, cnt_files


print(seek('new'))