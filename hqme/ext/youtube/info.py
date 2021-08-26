import youtube_dl
from youtube_dl import YoutubeDL

youtube_dl.utils.bug_reports_message = lambda: ""


yt_dl = YoutubeDL(params={})


class YouTubeService:
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
        Initialize the youtube service.

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
        self.data = self.ydl.extract_info(self.url, download=False)

    def get_title(self) -> str:
        """
        Get the title of the video.

        Returns:
            The title of the video.
        """
        return self.data["title"]

    def get_description(self) -> str:
        """
        Get the description of the video.

        Returns:
            The description of the video.
        """
        return self.data["description"]

    def get_duration(self) -> int:
        """
        Get the duration of the video.

        Returns:
            The duration of the video.
        """
        return self.data["duration"]

    def get_uploader(self) -> str:
        """
        Get the uploader of the video.

        Returns:
            The uploader of the video.
        """
        return self.data["uploader"]

    def get_upload_date(self) -> str:
        """
        Get the upload date of the video.

        Returns:
            The upload date of the video.
        """
        return self.data["upload_date"]

    def get_upload_time(self) -> str:
        """
        Get the upload time of the video.

        Returns:
            The upload time of the video.
        """
        return self.data["upload_time"]

    def get_thumbnail(self) -> str:
        """
        Get the thumbnail of the video.

        Returns:
            The thumbnail of the video.
        """
        return self.data["thumbnail"]

    def get_view_count(self) -> int:
        """
        Get the view count of the video.

        Returns:
            The view count of the video.
        """
        return self.data["view_count"]

    def get_like_count(self) -> int:
        """
        Get the like count of the video.

        Returns:
            The like count of the video.
        """
        return self.data["like_count"]

    def get_dislike_count(self) -> int:
        """
        Get the dislike count of the video.

        Returns:
            The dislike count of the video.
        """
        return self.data["dislike_count"]

    def get_comment_count(self) -> int:
        """
        Get the comment count of the video.

        Returns:
            The comment count of the video.
        """
        return self.data["comment_count"]

    def get_categories(self) -> list:
        """
        Get the categories of the video.

        Returns:
            The categories of the video.
        """
        return self.data["categories"]

    def get_tags(self) -> list:
        """
        Get the tags of the video.

        Returns:
            The tags of the video.
        """
        return self.data["tags"]

    def get_uploader_id(self) -> str:
        """
        Get the uploader id of the video.

        Returns:
            The uploader id of the video.
        """
        return self.data["uploader_id"]

    def get_uploader_url(self) -> str:
        """
        Get the uploader url of the video.

        Returns:
            The uploader url of the video.
        """
        return self.data["uploader_url"]

    def get_channel_id(self) -> str:
        """
        Get the channel id of the video.

        Returns:
            The channel id of the video.
        """
        return self.data["channel_id"]

    def get_channel_url(self) -> str:
        """
        Get the channel url of the video.

        Returns:
            The channel url of the video.
        """
        return self.data["channel_url"]

    def get_channel_title(self) -> str:
        """
        Get the channel title of the video.

        Returns:
            The channel title of the video.
        """
        return self.data["channel_title"]

    def get_video_url(self) -> str:
        """
        Get the video url of the video.

        Returns:
            The video url of the video.
        """
        return self.data["url"]
