import pystac_client
from dask_gateway import GatewayCluster
import planetary_computer
import dask.dataframe as dd
import os


def get_taxa_gbif_pc(taxa=[], bbox=[], years=[1980,2022], outfile=''):
    catalog = pystac_client.Client.open(
        "https://planetarycomputer.microsoft.com/api/stac/v1",
    )

    client=get_cluster()

    search = catalog.search(collections=["gbif"])
    items = search.get_all_items()
    items = {x.id: x for x in items}
    item = list(items.values())[0]

    signed_asset = planetary_computer.sign(item).assets["data"]
    signed_asset.extra_fields["table:storage_options"]

    filters=[]
    for t in taxa:
      filters.append([('species', '==', t), ('decimallatitude','<',float(bbox[3])), ('decimallatitude','>',float(bbox[1])), ('decimallongitude','>',float(bbox[0])), ('decimallongitude','<',float(bbox[2])), ('year','>',int(years[0])), ('year','<',int(years[1]))])
    
    
    df = dd.read_parquet(
        signed_asset.href,
        storage_options=signed_asset.extra_fields["table:storage_options"],
        filters=filters,
        dataset={"require_extension": None},
        engine="pyarrow",
    )
    res=df.compute() # CHECK TO SEE WHY to_csv IS NOT WORKING WITH DASK WORKERS
    res.to_csv(outfile, sep ='\t')
    return(outfile)


def get_cluster():
    cluster = GatewayCluster(
     "https://pccompute.westeurope.cloudapp.azure.com/compute/services/dask-gateway",
     proxy_address="gateway://pccompute-dask.westeurope.cloudapp.azure.com:80",
     auth="jupyterhub",
     image="mcr.microsoft.com/planetary-computer/python:latest"
    )
    cluster.scale(30)
    client = cluster.get_client()
    print(cluster.dashboard_link)
    return(client)