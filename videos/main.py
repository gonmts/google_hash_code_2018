from readFile import read_videos_file

class main:

	def __init__(self):
		pass



	def pontuacao_endpoint_video(self, requests, latency):
		return request*latency



	def main(self):
		fname = 'datasets/me_at_the_zoo.in'
		load_input(fname)

		#Main algorithm

		# 1 + 2
		endpoint_lists = {}
		gloibal_list = []
		for endpoint in range(self.nrEndpoints):
			endpoint_lists[endpoint] = []
			for video in self.videoRequests[endpoint]:
				score = pontuacao_endpoint_video( video[1], self.endpoints[endpoint][0] )
				endpoint_lists[endpoint] += [(video, score)] # [ (video, score) ]
				global_list += [(video, endpoint, score)]
			endpoint_lists[endpoint] = sorted(endpoint_lists[endpoint], key=getkey)


		# 3
		global_list = sorted(global_list, key=getkey2)

		# 4
		tratado = false
		for video_object in global_list:
			video = video_object[0]
			endpoint = video_object[1]
			score = video_object[2]

			for epcache in self.endpoints[endpoint][1:]:
				epcache = epcache[0]
				if (video in self.caches[cache]):
					tratado = true
					break

			if(tratado):
				continue

			sorted_ep_caches = sorted(self.endpoints[endpoint][1:], key=getkey)
			for epcache in sorted_ep_caches:
				if(has_capacity(epcache, video)):
					insert_cache(epcache, video)
					break





	def has_capacity(self, cache, video):
		return self.cacheCapacity[cache] >= self.videoSize[video]

	def insert_cache(self, cache, video):
		self.caches[cache].add(video)
		self.cacheCapacity[cache] -= self.videoSize(video)



	def load_input(self, fname):
		self.nrVideos, self.nrEndpoints, self.requests, self.nrCaches, self.cacheSize, self.videoSize, self.endpoints, self.videoRequests = read_videos_file(fname)

		self.caches = {}
		for cache in range(self.nrCaches):
			self.caches[cache] = set()
			self.cacheCapacity[cache] = self.cacheSize




def getkey(tup):
	return tup[1]

def getkey2(triple):
	return triple[2]
