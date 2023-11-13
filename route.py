from azure.maps.route import MapsRouteClient
from azure.core.credentials import AzureKeyCredential


def get_drive_time(subscription_key):
    # Create a client
    credential = AzureKeyCredential(subscription_key)
    client = MapsRouteClient(credential)

    # Calculate the route
    result = client.get_route_directions(route_points=[("41.708250", "-93.793730"), ("41.586834", "-93.624962")]);
    
    print("Get Route Directions with list of coordinates:")
    print(result.routes[0].summary)
    print(result.routes[0].sections[0])


# Example usage
subscription_key = "SUBSCRIPTION_KEY"
duration = get_drive_time(subscription_key)

