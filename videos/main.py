from readFile import read_videos_file, write_file
import numpy as np

class main:

	def __init__(self):
		pass

	def pontuacao_endpoint_video(self, requests, latency, size):
		return requests*latency

	def pontuacao_endpoint_video_tamanho(self, requests, latency, size):
		return size

	def main(self):
		fname = 'datasets/kittens.in.txt'
		self.load_input(fname)

		#Main algorithm

		# 1 + 2
		endpoint_lists = {}
		global_list = []
		for endpoint in range(self.nrEndpoints):
			endpoint_lists[endpoint] = []
			for video in self.videoRequests[endpoint]:
				score = self.pontuacao_endpoint_video_tamanho( video[1], self.endpoints[endpoint][0], self.videoSize[video[0]])
				endpoint_lists[endpoint] += [(video, score)] # [ (video, score) ]
				global_list += [(video[0], endpoint, score)]
			endpoint_lists[endpoint] = sorted(endpoint_lists[endpoint], key=getkey, reverse=True)


		# 3
		global_list = sorted(global_list, key=getkey2, reverse=True)

		# 4
		for video_object in global_list:
			tratado = False
			video = video_object[0]
			endpoint = video_object[1]
			score = video_object[2]
			for epcache in self.endpoints[endpoint][1:]:
				epcache = epcache[0]
				if (video in self.caches[epcache]):
					tratado = True
					break

			if(tratado):
				continue

			sorted_ep_caches = sorted(self.endpoints[endpoint][1:], key=getkey)
			for epcache in sorted_ep_caches:
				if(self.has_capacity(epcache[0], video)):
					self.insert_cache(epcache[0], video)
					break

		print(self.score())
		write_file(self.caches, "out.txt")


	def score(self):
		saved_per_endp=0
		avarage=0
		endpoint=0
		for my_caches in self.endpoints_cache.values():


		    lantency_data_center=my_caches[0]
		    for video_req in self.videoRequests[endpoint]:

		        video=video_req[0]
		        req=video_req[1]


		        my_caches_with_videos=[]

		        my_index = 0
		        for my_cache in my_caches[1:]:


		            if video in self.caches[my_cache]:
		                my_caches_with_videos+=[my_index]
		            my_index += 1



		        if len(my_caches_with_videos)>0:
		            lantecy_caches=np.array(self.endpoints_cache_latency[endpoint])[my_caches_with_videos]
		            saved_per_endp+=(lantency_data_center-np.min(lantecy_caches))*req


		        avarage+=req
		    endpoint+=1

		output = (saved_per_endp/avarage)*1000

		return output




	def has_capacity(self, cache, video):
		return self.cacheCapacity[cache] >= self.videoSize[video]

	def insert_cache(self, cache, video):
		self.caches[cache].add(video)
		self.cacheCapacity[cache] -= self.videoSize[video]



	def load_input(self, fname):
		self.nrVideos, self.nrEndpoints, self.requests, self.nrCaches, self.cacheSize, self.videoSize, self.endpoints, self.videoRequests = read_videos_file(fname)

		self.caches = {}
		self.cacheCapacity = {}
		for cache in range(self.nrCaches):
			self.caches[cache] = set()
			self.cacheCapacity[cache] = self.cacheSize



		self.endpoints_cache = {}
		self.endpoints_cache_latency = {}
		for endpoint in range(self.nrEndpoints):
			self.endpoints_cache[endpoint] = []
			self.endpoints_cache_latency[endpoint] = []
			self.endpoints_cache[endpoint] += [self.endpoints[endpoint][0]]
			for cache in self.endpoints[endpoint][1:]:
				self.endpoints_cache[endpoint] += [cache[0]]
				self.endpoints_cache_latency[endpoint] += [cache[1]]




def getkey(tup):
	return tup[1]

def getkey2(triple):
	return triple[2]
