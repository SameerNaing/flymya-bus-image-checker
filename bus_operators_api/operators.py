from typing import List
import os
import time
from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport

from .query import operators_query


def get_operators() -> List[str]:
    """Function to fetch operators from BE server and list all the operator names

    Returns:
        List[str]: list of all operator names
    """

    URL = os.getenv("BE_SERVER")
    TOKEN = os.getenv("ACCESS_TOKEN")
    PRODUCT_TYPE_ID = os.getenv("PRODUCT_TYPE_ID")

    transport = AIOHTTPTransport(
        url=URL, headers={"Authorization": f"Bearer {TOKEN}"})

    client = Client(transport=transport, fetch_schema_from_transport=True)
    page = 1
    operator_names = []

    while True:
        variable = {"filter": [
            {"field": "product_type.id", "operator": "=",
                "value": int(PRODUCT_TYPE_ID)}
        ], "first": 30, "page": page}
        try:
            result = client.execute(
                operators_query, variable_values=variable)
            data = result["operators"]["data"]

            for operator in data:
                code = operator["code"]
                name = operator["name"]
                name = name.replace(f"{code} - ", "")
                operator_names.append(name)

            if not result["operators"]["paginatorInfo"]["hasMorePages"]:
                break

            # Not to overload the server
            time.sleep(5)
            page += 1

            continue

        except Exception as e:
            print(e)
            print("ERROR")
            break

    return operator_names
