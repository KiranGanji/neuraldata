# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 17:14:06 2014

@author: Kiran Ganji
"""
import numpy as np
import matplotlib.pylab as plt

def load_file(filename):
    data = np.load(filename)
    return data['stages'], int(data['srate'])

def plot_hypnogram(eeg, stages, srate):
    fig,ax1 = plt.subplots()  #Needed for the multiple y-axes
    
    #Use the specgram function to draw the spectrogram as usual

    #Label your x and y axes and set the y limits for the spectrogram
    z= (len(stages)+1)*30    
    ax1.specgram(eeg,NFFT=256, Fs=srate)
    ax1.set_ylabel('Frequency(Hz)',color='b')
    ax1.set_xlabel('time (s)')
    ax1.set_xlim(0,z)
    ax1.set_ylim(0,30)
    ax2 = ax1.twinx() #Necessary for multiple y-axes
    
    #Use ax2.plot to draw the hypnogram.  Be sure your x values are in seconds
    #HINT: Use drawstyle='steps' to allow step functions in your plot

    #Label your right y-axis and change the text color to match your plot
    time = np.arange(30,z,30)    
    ax2.set_ylabel('NREM Stage',color='b')
    ax2.plot(time, stages,drawstyle='steps')
    ax2.set_xlim(0,z)
    #Set the limits for the y-axis 
 
    #Only display the possible values for the stages
    ax2.set_yticks(np.arange(-1,9))
    
    #Change the left axis tick color to match your plot
    for t1 in ax2.get_yticklabels():
        t1.set_color('b')
    
    #Title your plot  
    ax1.set_title('Hypnogram-Subject-1-Bad Sleep-1st Hour')

def time_spent_in_stages(stages):
    i=0
    timespent_array=[]
    for i in range(8):
        indices=plt.find(stages==i)
        j=len(indices)*30
        timespent_array.append(j)
    return timespent_array


def plot_data_psds(data,rate):  
    
    plt.figure()
    plt.psd(data[3],NFFT=256,Fs=rate)
    #plt.psd(data[1],NFFT=256,Fs=rate)
    #plt.psd(data[2],NFFT=256,Fs=rate)
    #plt.psd(data[3],NFFT=256,Fs=rate)
    #plt.psd(data[4],NFFT=256,Fs=rate)
    #plt.psd(data[5],NFFT=256,Fs=rate)
    plt.xlim(0,65)
    plt.title('Subject 1 - Channel 4 - Good Sleep')
    plt.show()

def plot_hourly_data(stages):
    i=1
    for i in range(1,11):    
        initial_epoch_value=(i-1)*120
        final_epoch_value=((i-1)*120)+119
        #final_epoch_value2=((i-1)*120)+65
        stages_hourly=stages[initial_epoch_value:final_epoch_value]    
        z=len(stages_hourly)
        plt.figure()
        time= np.arange(1,z+1)
        plt.plot(time, stages_hourly,drawstyle='steps')
        plt.title('Subject 1 - Bad Sleep - Hour'+' '+str(i))
        plt.xlabel('Epochs')
        plt.ylabel('Stages')
        plt.yticks(np.arange(-1,9))
        plt.show()
        plt.savefig('hour-'+str(i))

def plot_hourly_comparisions(s1,s2,s3,s4,s5,s6,s7,s8):
    stages_array=[]    
    stages_array.append(s1)
    stages_array.append(s2)
    stages_array.append(s3)
    stages_array.append(s4)
    stages_array.append(s5)
    stages_array.append(s6)
    stages_array.append(s7)
    stages_array.append(s8)
    i=1
    for i in range(1,11):    
        initial_epoch_value=(i-1)*120
        final_epoch_value=((i-1)*120)+119
        #final_epoch_value2=((i-1)*120)+65
        stages_hourly=stages_array[6][initial_epoch_value:final_epoch_value]
        stages_hourly2=stages_array[7][initial_epoch_value:final_epoch_value]
        #stages_hourly3=stages_array[5][initial_epoch_value:final_epoch_value]
        #stages_hourly4=stages_array[7][initial_epoch_value:final_epoch_value]
        z=len(stages_hourly)
        plt.figure()
        time= np.arange(1,z+1)
        plt.plot(time, stages_hourly,drawstyle='steps',label='Good Sleep')
        plt.plot(time, stages_hourly2,drawstyle='steps',label='Bad Sleep')
        #plt.plot(time, stages_hourly3,drawstyle='steps',label='Subject3')
        #plt.plot(time, stages_hourly4,drawstyle='steps',label='Subject4')
        plt.title('Subject4- Comparision - Hour'+' '+str(i))
        plt.xlabel('Epochs')
        plt.ylabel('Stages')
        plt.yticks(np.arange(-1,9))
        plt.legend(bbox_to_anchor=(0.65, 1), loc=2, borderaxespad=0.)
        plt.show()
        plt.savefig('hour-'+str(i))

def rem_nrem(stages):
    timespent_array=time_spent_in_stages(stages)
    time_nrem=timespent_array[1]+timespent_array[2]+timespent_array[3]+timespent_array[4]
    time_rem=timespent_array[5]
    split=[(time_rem*100/(time_nrem+time_rem)),(time_nrem*100/(time_nrem+time_rem))]
    plt.figure()
    labels=['REM Sleep', 'NREM Sleep']
    plt.pie(split,labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('Subject 2- Bad Sleep - REM/NREM Splitup')
    plt.show()

def plot_timespent(array):
    j=(sum(array))
    array2=[]
    i=0
    for i in range(len(array)):
        array2.append(array[i]*100/j)
    plt.figure()
    x=np.arange(0,8)
    plt.bar(x,array2, align='center',width=0.5)
    plt.ylabel('Scale(No units)')
    plt.xlabel('Stages')
    plt.ylim(0,50)
    plt.title('Subject-3- REC-Normalized Time Spent in each Stage')
    plt.show()

def plot_whole_night(s1,s2,s3,s4,s5,s6,s7,s8):
    #time=np.arange(1,len(s3)+1)
    time2=np.arange(1,len(s2)+1)    
    plt.figure()
    #plt.plot(time, s1[0:len(s3)],drawstyle='steps',label='Subject 1')
    #plt.plot(time, s3,drawstyle='steps',label='Subject 2')
    #plt.plot(time, s5[0:len(s3)],drawstyle='steps',label='Subject 3')
    #plt.plot(time, s7[0:len(s3)],drawstyle='steps',label='Subject 4')
    plt.plot(time2, s2,drawstyle='steps',label='Subject 1')
    #plt.plot(time2, s4[0:len(s2)],drawstyle='steps',label='Subject 2')
    plt.plot(time2, s6[0:len(s2)],drawstyle='steps',label='Subject 3')
    #plt.plot(time2, s2[0:len(s2)],drawstyle='steps',label='Subject 4')
    plt.title('Subjects REC Sleep')
    plt.xlabel('Epochs')
    plt.ylabel('Stages')
    plt.xlim(0,len(s2)+20)
    plt.yticks(np.arange(-1,9))
    plt.legend(bbox_to_anchor=(0., 1., 1., 0.),ncol=4,loc=1,mode="expand", borderaxespad=0.)
    plt.show()
    
if __name__ == "__main__":
    stages_1g, srate=load_file('S1_BSL.npz')
    stages_1b, srate=load_file('S1_REC.npz')
    stages_2g, srate=load_file('S2_BSL.npz')
    stages_2b, srate=load_file('S2_REC.npz')
    stages_3g, srate=load_file('S3_BSL.npz')
    stages_3b, srate=load_file('S3_REC.npz')
    stages_4g, srate=load_file('S4_BSL.npz')
    stages_4b, srate=load_file('S4_REC.npz')
    #plot_hypnogram(data[0][0:460800],stages[0:120],srate)
    timespent_array = time_spent_in_stages(stages_4b)
    print timespent_array
    #plot_timespent(timespent_array)
    #plot_data_psds(data,srate)
    #plot_hourly_data(stages)
    #plot_hourly_comparisions(stages_1g,stages_1b,stages_2g,stages_2b,stages_3g,stages_3b,stages_4g,stages_4b)
    #rem_nrem(stages_2b)
    #plot_whole_night(stages_1g,stages_1b,stages_2g,stages_2b,stages_3g,stages_3b,stages_4g,stages_4b)
    
