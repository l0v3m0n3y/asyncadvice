# asyncadvice.py

async lib for fucking-great-advice.ru

![2d1cf0156dda1fb46f42222c6221b13d](https://github.com/aminobotskek/fucking_great_advice/assets/94906343/ef03bd1e-cdac-44a3-a66e-bc5a33e519c7)

# Install
```
git clone https://github.com/aminobotskek/asyncadvice
```

### Example
```python3
import asyncadvice
import asyncio
async def main():
	client=asyncadvice.AsyncAdvice()
	data= await client.random_advices()
	print(data)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
