import os

def main():
    i=1
    path="./namechanger/" #forward slash and not backward
    for filename in os.listdir(path):
        my_dest="files"+str(i)+".txt"
        my_source=path+filename
        my_dest=path+my_dest
        os.rename(my_source,my_dest)
        i+=1

if __name__ =='__main__':
    main()