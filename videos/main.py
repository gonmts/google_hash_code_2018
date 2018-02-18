from readFile import read_videos_file
import numpy as np

class main:

	def __init__(self):
		pass



	def pontuacao_endpoint_video(self, requests, latency, size):
		return requests*latency

	def pontuacao_endpoint_video_tamanho(self, requests, latency, size):
		return size



	def main(self):
		fname = 'datasets/me_at_the_zoo.in'
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

		print(self.caches)
		print()
		print(np.sum(list(self.cacheCapacity.values())))





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




def getkey(tup):
	return tup[1]

def getkey2(triple):
	return triple[2]
