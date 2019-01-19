import os



os.system('python ./main_log3.py --model=nature2 --vec_conv=8 --vec_dense=16 --iter_train=0 --iter_test=0 --leaky=False --accumulate=True --act_p=norm --act_r=lrelu --caps_channel=8 --dataset=fashion_mnist --step1=20000 --step2=25000 --step3=30000')