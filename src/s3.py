import pandas as pd


class S3Handler:
    
    @staticmethod
    def read_from_s3(s3_url:str) -> pd.DataFrame:
        """
        uses s3 url for instance:
        s3://bob-dylan-songs/dylan_songs.parquet
        """
        return pd.read_parquet(s3_url)
