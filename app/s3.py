import pandas as pd
import awswrangler as wr


class S3Handler:
    @staticmethod
    def read_from_s3(s3_url:str) -> pd.DataFrame:
        """
        uses s3 url for instance:
        s3://bob-dylan-songs/dylan_songs.parquet
        """
        return wr.s3.read_parquet(s3_url)
