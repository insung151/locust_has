import random
from locust import TaskSet, task
import hlsplayer as hlsplayer

SECONDS = 1000  # ms in seconds

class UserBehavior(TaskSet):

    @task
    def play_lgi_vxpl(self):
        url = "https://media.readyq.tv/live/test/playlist.m3u8"
        duration = random.randint(60, 600)
        self.client.play(url, duration=duration)

#    @task
#    def play_sky_vxpl(self):
#        url = "https://media.readyq.tv/live/test2/playlist.m3u8%22"
#        duration = random.randint(60, 600)
#        self.client.play(url, duration=duration)
#
class HLSUser(hlsplayer.HLSLocust):
    task_set = UserBehavior
    min_wait = 2 * SECONDS  # 2 seconds
    max_wait = 15 * SECONDS  # 5 seconds
