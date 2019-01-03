#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 11:13:21 2017

@author: ladhikari

This code will produce threshold vs performce plots for preOP results - Train data (Just to show )
"""

import pandas as pd
import os
import matplotlib.pyplot as plt



def plot_performance_measure(list_df,list_labels,cutoffs1,cutoffs2,x=10, y=5.7):
    
    font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 14,
        }
    
    font_cut = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 12,
        }
    
    #n=len(list_labels)
    #fig,axes = plt.subplots(nrows=n/2, ncols=2, figsize=(x*(2.1), y*(n/2+.2)))
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(x,y))
    for df,l,c, c2 in zip(list_df,list_labels,cutoffs1, cutoffs2):
        #ax.plot(df['thres'],df['acc'],'b',label='Accuracy')
        #ax.plot(df['thres'],df['ppv'],'r',label='Positive Predictive Value (PPV)')
        #ax.plot(df['thres'],df['npv'],'g',label='Negative Predictive Value (NPV)')
        ax.plot(df['thres'],df['yod_index'],'c',label='Youden Index')
        ax.plot([c,c],[0,1],'k:',label='')
        #ax.plot([c2,c2],[0,1],'k:',label='')
        #ax.grid()
        ax.legend(loc=5)
        ax.set_xlabel('Threshold',  fontdict=font)
        ax.set_ylabel('Performance',  fontdict=font)
        #ax.set_title(l,  fontdict=font)
        ax.text(0.44, 0.55, 'Cutoff \n 0.43', fontdict=font_cut)
        #ax.text(0.43, 0.73, 'Cutoff-2 \n 0.42', fontdict=font_cut)
        ax.grid(color='white', linestyle='-', linewidth=0.3)
        fig.tight_layout()
    return fig
    

if __name__ == '__main__':
    
    os.chdir('/run/user/2209058/gvfs/smb-share:server=ahcdfs.ahc.ufl.edu,share=files/dom/SHARE/2016_223 IDEALIST/ANALYTIC CORE/MySurgeryRisk PostOP V1.0/3 Users/Lasith/PreOp_model')
    #os.chdir('S:/2016_223 IDEALIST/ANALYTIC CORE/MySurgeryRisk PostOP V1.0/3 Users/Lasith/PreOp_model')

    # read performace dataset:
    #FILENAME_results = 'Results/AKI_7/yellow+green+purple_dropped_model/aki7Day_PreOp_trainBy2039_ROC_AUC_ACC_PPV_NPV_F1_trainData_yellow+green+purple_dropped.csv'
    FILENAME_results = 'Results/AKI_7/esrd_dropped_final_features_model/aki7Day_PreOp_trainBy2038_ROC_AUC_ACC_PPV_NPV_F1_trainData_esrd_dropped.csv'
    
    df_perf = pd.read_csv(FILENAME_results, index_col=False)
    
    list_df = [df_perf.iloc[0:100,]]
    list_labels = ['Preoprative predictive model performace for AKI-3day outcome']
    cutoffs1 = [0.43]
    cutoffs2 = [0.0]
    performance_fig = plot_performance_measure(list_df, list_labels, cutoffs1, cutoffs2)
    performance_fig.show()
    #performance_fig.savefig('Performance_plot-preOp_AKI3Day.png')
    #performance_fig.savefig('aki7_PreOp_trainBy2038_cutoffs_fromTrain.svg', format='svg', dpi=300)