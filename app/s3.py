import pandas as pd
import awswrangler as wr


class S3Handler:
    @staticmethod
    def read_from_s3(public_key: str) -> pd.DataFrame:
        return wr.s3.read_parquet(public_key)
