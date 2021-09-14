import youtube_dl
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
from youtube_dl import YoutubeDL

youtube_dl.utils.bug_reports_message = lambda: ""


yt_dl = YoutubeDL(params={})


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

        self.data: dict[str, str | int] = self.ydl.extract_info(
            self.url, download=False
        )

    def get_title(self) -> str:
        """
        Get the title of the video.

        Returns:
            The title of the video.
        """

        _title = self.data.get("title")

        if type(_title) is not str:
            raise TitleNotFound("No title of the video.")
        else:
            title = str(_title)
        return title

    def get_description(self) -> str:
        """
        Get the description of the video.

        Returns:
            The description of the video.
        """

        _description = self.data.get("description")
        if type(_description) is None:
            raise DescriptionNotFound("No description of the video.")
        else:
            description = str(_description)
        return description

    def get_duration(self) -> int:
        """
        Get the duration of the video.

        Returns:
            The duration of the video.
        """

        _duration = self.data.get("duration")
        if _duration is None:
            raise DurationNotFound("No duration of the video.")
        else:
            duration = int(_duration)
        return duration

    def get_uploader(self) -> str:
        """
        Get the uploader of the video.

        Returns:
            The uploader of the video.
        """
        _uploader = self.data.get("uploader")
        if _uploader is None:
            raise UploaderNotFound("No uploader of the video.")
        else:
            uploader = str(_uploader)
        return uploader

    def get_upload_date(self) -> str:
        """
        Get the upload date of the video.

        Returns:
            The upload date of the video.
        """
        _upload_date = self.data["upload_date"]
        if _upload_date is None:
            raise UploadDateNotFound("No upload date of the video.")
        else:
            upload_date = str(_upload_date)
        return upload_date

    def get_upload_time(self) -> str:
        """
        Get the upload time of the video.

        Returns:
            The upload time of the video.
        """
        _upload_time = self.data["upload_time"]
        if _upload_time is None:
            raise UploadDateNotFound("No upload time of the video.")
        else:
            upload_time = str(_upload_time)
        return upload_time

    def get_thumbnail(self) -> str:
        """
        Get the thumbnail of the video.

        Returns:
            The thumbnail of the video.
        """
        _thumbnail = self.data["thumbnail"]
        if _thumbnail is None:
            raise ThumbnailNotFound("No thumbnail of the video.")
        else:
            thumbnail = str(_thumbnail)
        return thumbnail

    def get_view_count(self) -> int:
        """
        Get the view count of the video.

        Returns:
            The view count of the video.
        """
        _view_count = self.data["view_count"]
        if _view_count is None:
            raise ViewCountNotFound("No view count of the video.")
        else:
            view_count = int(_view_count)
        return view_count

    def get_like_count(self) -> int:
        """
        Get the like count of the video.

        Returns:
            The like count of the video.
        """
        _like_count = self.data["like_count"]
        if _like_count is None:
            raise LikeCountNotFound("No like count of the video.")
        else:
            like_count = int(_like_count)
        return like_count

    def get_dislike_count(self) -> int:
        """
        Get the dislike count of the video.

        Returns:
            The dislike count of the video.
        """
        dislike_count = self.data["dislike_count"]
        if dislike_count is None:
            raise DislikeCountNotFound("No dislike count of the video.")
        else:
            dislike_count = int(dislike_count)
        return dislike_count

    def get_comment_count(self) -> int:
        """
        Get the comment count of the video.

        Returns:
            The comment count of the video.
        """
        _comment_count = self.data["comment_count"]
        if _comment_count is None:
            raise CommentCountNotFound("No comment count of the video.")
        else:
            comment_count = int(_comment_count)
        return comment_count

    def get_categories(self) -> list:
        """
        Get the categories of the video.

        Returns:
            The categories of the video.
        """
        _categories = self.data["categories"]
        if _categories is None:
            raise CategoryNotFound("No categories of the video.")
        else:
            categories = list(_categories)
        return categories

    def get_tags(self) -> list:
        """
        Get the tags of the video.

        Returns:
            The tags of the video.
        """
        _tags = self.data["tags"]
        if _tags is None:
            raise TegsNotFound("No tags of the video.")
        else:
            tags = list(_tags)
        return tags

    def get_uploader_id(self) -> str:
        """
        Get the uploader id of the video.

        Returns:
            The uploader id of the video.
        """
        _uploader_id = self.data["uploader_id"]
        if _uploader_id is None:
            raise UploaderIdNotFound("No uploader id of the video.")
        else:
            uploader_id = str(_uploader_id)
        return uploader_id

    def get_uploader_url(self) -> str:
        """
        Get the uploader url of the video.

        Returns:
            The uploader url of the video.
        """
        _uploader_url = self.data["uploader_url"]
        if _uploader_url is None:
            raise UploaderUrlNotFound("No uploader url of the video.")
        else:
            uploader_url = str(_uploader_url)
        return uploader_url

    def get_channel_id(self) -> str:
        """
        Get the channel id of the video.

        Returns:
            The channel id of the video.
        """
        _channel_id = self.data["channel_id"]
        if _channel_id is None:
            raise ChannelIdNotFound("No channel id of the video.")
        else:
            channel_id = str(_channel_id)
        return channel_id

    def get_channel_url(self) -> str:
        """
        Get the channel url of the video.

        Returns:
            The channel url of the video.
        """
        _channel_url = self.data["channel_url"]
        if _channel_url is None:
            raise ChannelUrlNotFound("No channel url of the video.")
        else:
            channel_url = str(_channel_url)
        return channel_url

    def get_channel_title(self) -> str:
        """
        Get the channel title of the video.

        Returns:
            The channel title of the video.
        """
        _channel_title = self.data["channel_title"]
        if _channel_title is None:
            raise ChannelTitleNotFound("No channel title of the video.")
        else:
            channel_title = str(_channel_title)
        return channel_title

    def get_video_url(self) -> str:
        """
        Get the video url of the video.

        Returns:
            The video url of the video.
        """
        _url = self.data["url"]
        if _url is None:
            raise VideoUrlNotFound("No url of the video.")
        else:
            url = str(_url)
        return url
