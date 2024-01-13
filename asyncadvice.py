import aiohttp,asyncio
class AsyncAdvice():
	def __init__(self):
		self.session = aiohttp.ClientSession()
		self.api="https://fucking-great-advice.ru/api/v2"
		self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}
	def __del__(self):
		try:
		          loop = asyncio.get_event_loop()
		          loop.create_task(self._close_session())
		except RuntimeError:
		          loop = asyncio.new_event_loop()
		          loop.run_until_complete(self._close_session())
	async def _close_session(self):
		if not self.session.closed: await self.session.close()
	async def random_advices(self):
		async with self.session.get(f"{self.api}/random-advices",headers=self.headers) as req:
			return await req.json()
	async def random_advices_by_tag(self,tag):
		async with self.session.get(f"{self.api}/random-advices-by-tag?tag={tag}",headers=self.headers) as req:
			return await req.json()