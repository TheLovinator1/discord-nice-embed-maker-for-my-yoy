from __future__ import annotations

import logging
import sys
from dataclasses import dataclass

import ffmpeg

from discord_embed import settings

logger: logging.Logger = logging.getLogger("uvicorn.error")


@dataclass
class Resolution:
    """Video resolution.

    height: Height of video.
    width: Width of video.
    """

    height: int
    width: int


def video_resolution(path_to_video: str) -> Resolution:
    """Find video resolution.

    Args:
        path_to_video: Path to video file.

    Returns:
        Returns height and width.
    """
    probe = ffmpeg.probe(path_to_video)
    video_stream = next(
        (stream for stream in probe["streams"] if stream["codec_type"] == "video"),
        None,
    )
    if video_stream is None:
        logger.critical("No video stream found")
        sys.exit(1)

    width: int = int(video_stream["width"])
    height: int = int(video_stream["height"])

    return Resolution(height, width)


def make_thumbnail(path_video: str, file_filename: str) -> str:
    """Make thumbnail for Discord. This is a screenshot of the video.

    Args:
        path_video: Path where video file is stored.
        file_filename: File name for URL.

    Raises:
        ffmpeg.Error: If there is an error creating the thumbnail.

    Returns:
        Returns thumbnail filename.
    """
    output_path: str = f"{settings.upload_folder}/{file_filename}.jpg"
    try:
        (
            ffmpeg.input(path_video, ss="1")
            .output(output_path, vframes=1, format="image2", update=1)
            .overwrite_output()
            .run()
        )
    except ffmpeg.Error:
        logger.exception("Error creating thumbnail")
        raise

    logger.info("Thumbnail created: %s", output_path)

    # Return URL for thumbnail.
    return f"{settings.serve_domain}/{file_filename}.jpg"
