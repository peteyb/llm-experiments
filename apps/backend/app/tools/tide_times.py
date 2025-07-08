import logging

import requests
from openai.types.responses import ToolParam

from ..core.config import settings

logger = logging.getLogger("uvicorn.error")


def get_tide_times(location_name):
    response = requests.get(
        f"https://admiraltyapi.azure-api.net/uktidalapi/api/V1/Stations?name={location_name}",
        headers={
            "Ocp-Apim-Subscription-Key": settings.oci_api_key,
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": "true",
            "Accept": "application/json",
        },
    )
    if data := response.json():
        location = data["features"][0]["properties"]["Id"]
        logger.info(f"location::{location_name}:{location}")

        response = requests.get(
            f"https://admiraltyapi.azure-api.net/uktidalapi/api/V1/Stations/{location}/TidalEvents?duration=1",
            headers={
                "Ocp-Apim-Subscription-Key": settings.oci_api_key,
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": "true",
                "Accept": "application/json",
            },
        )
        return response.json()


tide_times_tool: ToolParam = {
    "type": "function",
    "name": "get_tide_times",
    "description": "Get list of tide times for a given location and time.",
    "parameters": {
        "type": "object",
        "properties": {
            "location_name": {"type": "string"},
        },
        "required": ["location_name"],
        "additionalProperties": False,
    },
    "strict": True,
}
