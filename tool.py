txtfiles = ['2010_v2.txt','2014_v2.txt','2017_v2.txt','2021_v2.txt']



while True:
    nums = []
    for txtfile in txtfiles:
        with open(txtfile,'r') as f:
            lines = f.readlines()
            nums.append(len(lines))
    print('\r' + '{} {} {} {}'.format(nums[0], nums[1], nums[2], nums[3]),end='')