from constants.TiingoKeys import TiingoKeys


class KaryKeys(TiingoKeys):
    HIGH_RUNNING_MEAN = "high_running_mean"
    LOW_RUNNING_MEAN = "low_running_mean"
    CLOSE_RUNNING_MEAN = "close_running_mean"
    OPEN_RUNNING_MEAN = "open_running_mean"
    VOLUME_RUNNING_MEAN = "volume_running_mean"

    HIGH_RUNNING_STD = "high_running_std"
    LOW_RUNNING_STD = "low_running_std"
    CLOSE_RUNNING_STD = "close_running_std"
    OPEN_RUNNING_STD= "open_running_std"
    VOLUME_RUNNING_STD = "volume_running_std"

    HIGH_PLUS_STD = "high_plus_std"
    CLOSE_PLUS_STD = "close_plus_std"
    OPEN_PLUS_STD= "open_plus_std"
    VOLUME_PLUS_STD = "volume_plus_std"

    HIGH_MINUS_STD = "high_minus_std"
    CLOSE_MINUS_STD = "close_minus_std"
    OPEN_MINUS_STD = "open_minus_std"
    VOLUME_MINUS_STD = "volume_minus_std"
