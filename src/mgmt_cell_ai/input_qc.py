"""Conservative, deterministic input checks for public image handling.

These checks are non-biological safeguards. They decide whether an uploaded
file is suitable for review; they do not classify cells or estimate biology.
"""
from dataclasses import dataclass
from typing import Tuple

from PIL import Image, ImageFilter, ImageStat


@dataclass(frozen=True)
class InputAssessment:
    accepted_for_review: bool
    status: str
    reasons: Tuple[str, ...]
    width: int
    height: int
    mean_gray: float
    gray_std: float


def assess_image(image: Image.Image) -> InputAssessment:
    """Return a conservative, deterministic QC assessment for an image."""
    width, height = image.size
    reasons = []
    gray = image.convert("L")
    stats = ImageStat.Stat(gray)
    mean_gray = float(stats.mean[0])
    gray_std = float(stats.stddev[0])

    if width < 64 or height < 64:
        reasons.append("image is extremely small")
    if width > 12000 or height > 12000 or width * height > 25_000_000:
        reasons.append("image resolution exceeds the supported review limit")
    if gray_std < 1.0:
        reasons.append("image is blank or nearly blank")
    if mean_gray < 4.0:
        reasons.append("image is extremely dark")
    if mean_gray > 251.0:
        reasons.append("image is extremely bright")
    if gray_std < 5.0 and not reasons:
        reasons.append("image contrast is too low for reliable review")

    edge_mean = float(ImageStat.Stat(gray.filter(ImageFilter.FIND_EDGES)).mean[0])
    if edge_mean < 1.0 and gray_std < 12.0 and not reasons:
        reasons.append("image has insufficient visible structure")

    accepted = not reasons
    status = "Reviewable input" if accepted else "Manual review required"
    return InputAssessment(
        accepted_for_review=accepted,
        status=status,
        reasons=tuple(reasons),
        width=width,
        height=height,
        mean_gray=round(mean_gray, 4),
        gray_std=round(gray_std, 4),
    )

