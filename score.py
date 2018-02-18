#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 12:06:45 2018

@author: RitaRamos
"""

from operator import itemgetter

import numpy as np


endpoints_cache={0:[1000, 0,1,2], 1:[1000] }

endpoints_cache_latency={0:[100, 300 ,200], 1:[1000] }

global_caches_dict={ 0:[],1:[3,1],2:[0,1] }

endpoint_videos={0:[ (3,1500), (4,500), (1,1000) ], 1:[(0, 1000)]}


saved_per_endp=0
avarage=0
endpoint=0
for my_caches in endpoints_cache.values():
    
    print("ENDDDDDPOINT", endpoint)
    
    lantency_data_center=my_caches[0]
    print ("lantency data", lantency_data_center)
    
    
    
    
    

        
    for video_req in endpoint_videos[endpoint]:
        
        video=video_req[0]
        req=video_req[1]
        
        print("video", video)
        
        my_caches_with_videos=[]
        
        for my_cache in my_caches[1:]:
            
            print ("nmy chace", my_cache)
            
            if video in global_caches_dict[my_cache]:
                
                my_caches_with_videos+=[my_cache]
                            
        print("my_caches_with_videos", my_caches_with_videos)
        
        
        if len(my_caches_with_videos)>0:
            #print("é isto", itemgetter(*my_caches_with_videos)(endpoints_cache_latency[endpoint]))
            
            lantecy_caches=np.array(endpoints_cache_latency[endpoint])[my_caches_with_videos]
            
            print("lantecy_caches", lantecy_caches)
            
            saved_per_endp+=(lantency_data_center-np.min(lantecy_caches))*req
            
            
        print("saved", saved_per_endp)
        avarage+=req
    endpoint+=1

            
output_end=(saved_per_endp/avarage)*1000

            
            
            #saved_per_endp=np.array(endpoints_cache_latency[endpoint])*
            
            
            
            
                
            
            #print("olaaa", endpoints_cache_latency[my_caches_with_videos])
            
            #latency_of_caches = itemgetter(*my_caches_with_videos)(endpoints_cache_latency)
            
           #print("heyye" latency_of_caches)
            
            #min_latent_cache=min(my_caches_with_videos)
            
            #print ("min_latent_cache", min_latent_cache)
            
            #latency=min(lantency_data_center,min_latent_cache)
            
            #output=(lantency_data_center-latency)
