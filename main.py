import asyncio
from hqme.ext.platform import YouTube

async def main():
    yt = YouTube(url="https://www.youtube.com/watch?v=X7zxC6mKOgI")
    title = await yt.get_title()
    print(f"title: {title}")
    description = await yt.get_description()
    print(f"description: {description}")
    thumbnail = await yt.get_thumbnail()
    print(f"thumbnail: {thumbnail}")
    duration = await yt.get_duration()
    print(f"duration: {duration}")
    views = await yt.get_view_count()
    print(f"views: {views}")
    likes = await yt.get_like_count()
    print(f"likes: {likes}")
    url = await yt.get_video_url()
    print(f"url: {url}")

    

if __name__ == '__main__':
    asyncio.run(main())
