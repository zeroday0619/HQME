import asyncio
import functools

import yt_dlp
from hqme.exceptions.youtube import (
    CategoryNotFound,
    ChannelIdNotFound,
    ChannelTitleNotFound,
    ChannelUrlNotFound,
    CommentCountNotFound,
    DescriptionNotFound,
    DislikeCountNotFound,
    DurationNotFound,
    LikeCountNotFound,
    SearchListNotFound,
    TegsNotFound,
    ThumbnailNotFound,
    TitleNotFound,
    UploadDateNotFound,
    UploaderIdNotFound,
    UploaderNotFound,
    UploaderUrlNotFound,
    VideoUrlNotFound,
    ViewCountNotFound,
)
from validator_collection.checkers import is_url
from yt_dlp import YoutubeDL

yt_dlp.utils.bug_reports_message = lambda: ""
yt_dl = YoutubeDL()


class YouTube:
    """
    You can use this class to get information about a youtube video.
    """

    def __init__(
        self,
        url: str,
        geo_bypass: bool = True,
        quiet: bool = True,
        ignoreerrors: bool = True,
        no_playlist: bool = True,
        no_warnings: bool = True,
        simulate: bool = True,
        skip_download: bool = True,
        nocheckcertificate: bool = True,
        no_part: bool = True,
        updatetime: bool = True,
    ) -> None:
        """
        Args:
            url: The url of the video.
            geo_bypass: Bypass geographic restriction.
            quiet: If True, youtube_dl will not print anything to stdout.
            ignoreerrors: If True, youtube_dl will not stop when it encounters an error.
            no_playlist: If True, youtube_dl will not download the playlist.
            no_warnings: If True, youtube_dl will not print anything to stdout.
            simulate: If True, youtube_dl will not download the video.
            skip_download: If True, youtube_dl will not download the video.
            nocheckcertificate: If True, youtube_dl will not verify the server certificate.
            no_part: If True, youtube_dl will not download the video.
            updatetime: If True, youtube_dl will not download the video.

        """
        self.url = url
        self.ydl = yt_dl
        self.ydl.params["format"] = "bestaudio/best"
        self.ydl.params["geo-bypass"] = geo_bypass
        self.ydl.params["quiet"] = quiet
        self.ydl.params["ignoreerrors"] = ignoreerrors
        self.ydl.params["noplaylist"] = no_playlist
        self.ydl.params["no_warnings"] = no_warnings
        self.ydl.params["simulate"] = simulate
        self.ydl.params["skip_download"] = skip_download
        self.ydl.params["nocheckcertificate"] = nocheckcertificate
        self.ydl.params["nopart"] = no_part
        self.ydl.params["updatetime"] = updatetime
        self.ydl.params["default_search"] = "auto"
        self.data = None

    async def sync(self) -> None:
        """
        Sync the data of the video.
        """

        loop = asyncio.get_running_loop()
        partial = functools.partial(self.ydl.extract_info, self.url, download=False)
        self.data = await loop.run_in_executor(None, partial)

    async def get_title(self) -> str:
        """
        Get the title of the video.

        Returns:
            The title of the video.
        """

        if self.data is None:
            await self.sync()

        if "entries" in self.data:
            entries = self.data["entries"][0]

        _title = entries.get("title")

        if type(_title) is not str:
            raise TitleNotFound("No title of the video.")
        else:
            title = str(_title)
        return title

    async def get_description(self) -> str:
        """
        Get the description of the video.

        Returns:
            The description of the video.
        """

        if self.data is None:
            await self.sync()

        if "entries" in self.data:
            entries = self.data["entries"]

        _description = entries.get("description")
        if type(_description) is None:
            raise DescriptionNotFound("No description of the video.")
        else:
            description = str(_description)
        return description

    async def get_duration(self) -> int:
        """
        Get the duration of the video.

        Returns:
            The duration of the video.
        """

        if self.data is None:
            await self.sync()

        if "entries" in self.data:
            entries = self.data["entries"][0]

        _duration = entries.get("duration")

        if _duration is None:
            raise DurationNotFound("No duration of the video.")
        else:
            duration = int(_duration)
        return duration

    async def get_uploader(self) -> str:
        """
        Get the uploader of the video.

        Returns:
            The uploader of the video.
        """

        if self.data is None:
            await self.sync()

        if "entries" in self.data:
            entries = self.data["entries"][0]

        _uploader = entries.get("uploader")
        if _uploader is None:
            raise UploaderNotFound("No uploader of the video.")
        else:
            uploader = str(_uploader)
        return uploader

    async def get_upload_date(self) -> str:
        """
        Get the upload date of the video.

        Returns:
            The upload date of the video.
        """

        if self.data is None:
            await self.sync()

        if "entries" in self.data:
            entries = self.data["entries"][0]

        _upload_date = entries.get("upload_date")

        if _upload_date is None:
            raise UploadDateNotFound("No upload date of the video.")
        else:
            upload_date = str(_upload_date)
        return upload_date

    async def get_upload_time(self) -> str:
        """
        Get the upload time of the video.

        Returns:
            The upload time of the video.
        """

        if self.data is None:
            await self.sync()

        if "entries" in self.data:
            entries = self.data["entries"][0]

        _upload_time = entries.get("upload_time")
        if _upload_time is None:
            raise UploadDateNotFound("No upload time of the video.")
        else:
            upload_time = str(_upload_time)
        return upload_time

    async def get_thumbnail(self) -> str:
        """
        Get the thumbnail of the video.

        Returns:
            The thumbnail of the video.
        """

        if self.data is None:
            await self.sync()

        if "entries" in self.data:
            entries = self.data["entries"][0]

        _thumbnail = entries.get("thumbnail")
        if _thumbnail is None:
            raise ThumbnailNotFound("No thumbnail of the video.")
        else:
            thumbnail = str(_thumbnail)
        return thumbnail

    async def get_view_count(self) -> int:
        """
        Get the view count of the video.

        Returns:
            The view count of the video.
        """

        if self.data is None:
            await self.sync()

        if "entries" in self.data:
            entries = self.data["entries"][0]

        _view_count = entries.get("view_count")
        if _view_count is None:
            raise ViewCountNotFound("No view count of the video.")
        else:
            view_count = int(_view_count)
        return view_count

    async def get_like_count(self) -> int:
        """
        Get the like count of the video.

        Returns:
            The like count of the video.
        """

        if self.data is None:
            await self.sync()

        if "entries" in self.data:
            entries = self.data["entries"][0]

        _like_count = entries.get("like_count")
        if _like_count is None:
            raise LikeCountNotFound("No like count of the video.")
        else:
            like_count = int(_like_count)
        return like_count

    async def get_dislike_count(self) -> int:
        """
        Get the dislike count of the video.

        Returns:
            The dislike count of the video.
        """

        if self.data is None:
            await self.sync()

        if "entries" in self.data:
            entries = self.data["entries"][0]

        dislike_count = entries.get("dislike_count")
        if dislike_count is None:
            raise DislikeCountNotFound("No dislike count of the video.")
        else:
            dislike_count = int(dislike_count)
        return dislike_count

    async def get_comment_count(self) -> int:
        """
        Get the comment count of the video.

        Returns:
            The comment count of the video.
        """

        if self.data is None:
            await self.sync()

        if "entries" in self.data:
            entries = self.data["entries"][0]

        _comment_count = entries.get("comment_count")
        if _comment_count is None:
            raise CommentCountNotFound("No comment count of the video.")
        else:
            comment_count = int(_comment_count)
        return comment_count

    async def get_categories(self) -> list:
        """
        Get the categories of the video.

        Returns:
            The categories of the video.
        """

        if self.data is None:
            await self.sync()

        if "entries" in self.data:
            entries = self.data["entries"][0]

        _categories = entries.get("categories")
        if _categories is None:
            raise CategoryNotFound("No categories of the video.")
        else:
            categories = list(_categories)
        return categories

    async def get_tags(self) -> list:
        """
        Get the tags of the video.

        Returns:
            The tags of the video.
        """

        if self.data is None:
            await self.sync()

        if "entries" in self.data:
            entries = self.data["entries"][0]

        _tags = entries.get("tags")
        if _tags is None:
            raise TegsNotFound("No tags of the video.")
        else:
            tags = list(_tags)
        return tags

    async def get_uploader_id(self) -> str:
        """
        Get the uploader id of the video.

        Returns:
            The uploader id of the video.
        """

        if self.data is None:
            await self.sync()

        if "entries" in self.data:
            entries = self.data["entries"][0]

        _uploader_id = entries.get("uploader_id")
        if _uploader_id is None:
            raise UploaderIdNotFound("No uploader id of the video.")
        else:
            uploader_id = str(_uploader_id)
        return uploader_id

    async def get_uploader_url(self) -> str:
        """
        Get the uploader url of the video.

        Returns:
            The uploader url of the video.
        """

        if self.data is None:
            await self.sync()

        if "entries" in self.data:
            entries = self.data["entries"][0]

        _uploader_url = entries.get("uploader_url")
        if _uploader_url is None:
            raise UploaderUrlNotFound("No uploader url of the video.")
        else:
            uploader_url = str(_uploader_url)
        return uploader_url

    async def get_channel_id(self) -> str:
        """
        Get the channel id of the video.

        Returns:
            The channel id of the video.
        """

        if self.data is None:
            await self.sync()

        if "entries" in self.data:
            entries = self.data["entries"][0]

        _channel_id = entries.get("channel_id")
        if _channel_id is None:
            raise ChannelIdNotFound("No channel id of the video.")
        else:
            channel_id = str(_channel_id)
        return channel_id

    async def get_channel_url(self) -> str:
        """
        Get the channel url of the video.

        Returns:
            The channel url of the video.
        """

        if self.data is None:
            await self.sync()

        if "entries" in self.data:
            entries = self.data["entries"][0]

        _channel_url = entries.get("channel_url")
        if _channel_url is None:
            raise ChannelUrlNotFound("No channel url of the video.")
        else:
            channel_url = str(_channel_url)
        return channel_url

    async def get_channel_title(self) -> str:
        """
        Get the channel title of the video.

        Returns:
            The channel title of the video.
        """

        if self.data is None:
            await self.sync()

        if "entries" in self.data:
            entries = self.data["entries"][0]

        _channel_title = entries.get("channel_title")
        if _channel_title is None:
            raise ChannelTitleNotFound("No channel title of the video.")
        else:
            channel_title = str(_channel_title)
        return channel_title

    async def get_video_url(self) -> str:
        """
        Get the video url of the video.

        Returns:
            The video url of the video.
        """

        if self.data is None:
            await self.sync()

        if "entries" in self.data:
            entries = self.data["entries"][0]

        _url = entries.get("url")
        if _url is None:
            raise VideoUrlNotFound("No url of the video.")
        else:
            url = str(_url)
        return url


class YouTubeSearch(YouTube):
    """
    Class for searching YouTube.
    """

    def __init__(self, source: str, max_result: int = 10) -> None:
        """
        Youtebe Search
        ``````````````

        Args:
            source: Youtbe search query. query is youtube url or search word.
            max_result: Maximum number of results. default is 10.
        """
        self.source = "%s%s:%s" % ("ytsearch", max_result, "".join(source))
        super(YouTubeSearch, self).__init__(url=self.source)

    async def parse_duration(self, duration: int) -> str:
        """
        Get the duration of the video.

        Args:
            duration: The duration of the video.

        Returns:
            The duration of the video.
        """

        value = None
        if duration > 0:
            minutes, seconds = divmod(duration, 60)
            hours, minutes = divmod(minutes, 60)
            days, hours = divmod(hours, 24)

            duration = []
            _duration = duration.append
            if days > 0:
                _duration(f"{days} days")
            if hours > 0:
                _duration(f"{hours} hours")
            if minutes > 0:
                _duration(f"{minutes} minutes")
            if seconds > 0:
                _duration(f"{seconds} seconds")

            value = ", ".join(duration)

        elif duration == 0:
            value = "LIVE STREAM"
        return value

    async def get_search_list(self) -> list:
        """
        Get the search list of the video.

        Returns:
            The search list of the query.
        """
        if not is_url(self.url):
            if self.data is None:
                await self.sync()

            if "entries" in self.data:
                entries = self.data["entries"]
            else:
                raise SearchListNotFound("Not Found")

            search_list = []
            _search_list = search_list.append
            for entry in entries:
                _search_list(
                    {
                        "title": entry.get("title"),
                        "url": entry.get("url"),
                        "thumbnail": entry.get("thumbnail"),
                        "description": entry.get("description"),
                        "webpage_url": entry.get("webpage_url"),
                        "uploader": entry.get("uploader"),
                        "uploader_url": entry.get("uploader_url"),
                        "uploader_id": entry.get("uploader_id"),
                        "channel_url": entry.get("channel_url"),
                        "view_count": entry.get("view_count"),
                        "like_count": entry.get("like_count"),
                        "dislike_count": entry.get("dislike_count"),
                        "duration": await self.parse_duration(entry.get("duration")),
                        "upload_date": entry.get("upload_date"),
                        "age_limit": entry.get("age_limit"),
                    }
                )
            return search_list
        else:
            raise Warning("Invalid url.")
