import pandas as pd

from util.random_nms import random_nms


def get_filtered_train_df(df: pd.DataFrame, iou_threshold, seed=42) -> pd.DataFrame:
    df_without_double_boxes = random_nms(df, iou_threshold, seed)
    return df_without_double_boxes