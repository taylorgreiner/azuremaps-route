from azure.maps.route import MapsRouteClient
from azure.core.credentials import AzureKeyCredential


def get_drive_time(start_address, end_address, subscription_key):
    # Create a client
    credential = AzureKeyCredential(subscription_key)
    client = MapsRouteClient(credential)

    # Calculate the route
    result = client.get_route_directions(route_points=[("41.708250", "-93.793730"), ("41.586834", "-93.624962")]);
    
    print("Get Route Directions with list of coordinates:")
#    print(result.routes[0].summary)
    print(result.routes[0].sections[0])


# Example usage
subscription_key = "PdP957cAfxLMNkAEMe0U1r1tKHK7PPiIlHUcKI5EHek"
start_address = "105 NE 24th Ct, Grimes IA 50111"
end_address = "100 E Southside Dr, Polk City IA 50226"
duration = get_drive_time(start_address, end_address, subscription_key)
print(f"Drive time in seconds: {duration}")

