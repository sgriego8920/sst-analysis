import xarray as xr

def read_latest_sst(sst):
    with xr.open_dataset(sst) as ds:
        latest_sst=ds['sst'].isel(time=-1).values
        return latest_sst