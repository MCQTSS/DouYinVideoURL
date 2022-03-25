import requests


class DouYin:
	def __init__(self):
		self._headers = {
			'Accept': '*/*',
			'Accept-Encoding': 'gzip,deflate,sdch',
			'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
			'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0;'
			              ' Nexus 5 Build/MRA58N)'
			              'AppleWebKit/537.36 (KHTML, like Gecko) '
			              'Chrome/66.0.3359.181 Mobile Safari/537.36',
		}

	def get_info(self, item_id):  # 通过itemid获取视频下载地址等信息
		ret = requests.get('https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={}'.format(item_id),
		                   headers=self._headers).json()
		print('作者名:{}'.format(ret['item_list'][0]['author']['nickname']))
		print('抖音号:{}'.format(ret['item_list'][0]['author']['unique_id']))
		print('视频标题:{}'.format(ret['item_list'][0]['desc']))
		print('视频下载URL:{}'.format(ret['item_list'][0]['video']['play_addr']['url_list'][0]))

	def get_item_id(self, share_url):
		url = requests.get(share_url, headers=self._headers, allow_redirects=False).next.url
		start = url.find('/video/')
		if start >= 0:
			start += len('/video/')
			end = url.find('/?', start)
			if end >= 0:
				return url[start:end].strip()


if __name__ == "__main__":
	DY = DouYin()
	DY.get_info(DY.get_item_id('https://v.douyin.com/Na9Nc8R/'))
