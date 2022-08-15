from src import s3
import pandas as pd
PUBLIC_KEY = 'https://bob-dylan-songs.s3.amazonaws.com/dylan_songs.parquet'


s3_handler = s3.S3Handler()
class TestS3Handler:
    def test_dataframe_from_s3(self):
        df:pd.DataFrame = s3_handler.read_from_s3(PUBLIC_KEY)
        assert list(df.columns) == ['release_year', 'album', 'title', 'lyrics']
        assert df.shape == (345, 4)
        assert sum(df.isnull().sum().values) == 0
        assert df[df.duplicated()].empty == True

