# 1. Import the PayPal SDK client that was created in `Set up Server-Side SDK`.
from paypalcheckoutsdk.orders import OrdersGetRequest

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment

import sys

from pytz import unicode


class PayPalClient:
    def __init__(self):
        self.client_id = "Afdfrvax7g8d1Hi0SSkQ2X04UgETMG0mRGy3i6MQIBH1T1iXAckZDbBH09n1YauECOrMFmwRCZfb2XQk"
        self.client_secret = "EBwULqDK1cFohIpslMS2Q9LWleCpfxvRw9OAPg3fyQ9-oY_pxnczlswOfn3MRQrrllog61Sk5470Sndw"

        """Set up and return PayPal Python SDK environment with PayPal access credentials.
           This sample uses SandboxEnvironment. In production, use LiveEnvironment."""

        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)

        """ Returns PayPal HTTP client instance with environment that has access
            credentials context. Use this instance to invoke PayPal APIs, provided the
            credentials have access. """
        self.client = PayPalHttpClient(self.environment)

    def object_to_json(self, json_data):
        """
        Function to print all json data in an organized readable manner
        """
        result = {}
        if sys.version_info[0] < 3:
            itr = json_data.__dict__.iteritems()
        else:
            itr = json_data.__dict__.items()
        for key, value in itr:
            # Skip internal attributes.
            if key.startswith("__"):
                continue
            result[key] = self.array_to_json_array(value) if isinstance(value, list) else \
                self.object_to_json(value) if not self.is_primittive(value) else \
                    value
        return result

    def array_to_json_array(self, json_array):
        result = []
        if isinstance(json_array, list):
            for item in json_array:
                result.append(self.object_to_json(item) if not self.is_primittive(item) \
                                  else self.array_to_json_array(item) if isinstance(item, list) else item)
        return result

    def is_primittive(self, data):
        return isinstance(data, str) or isinstance(data, unicode) or isinstance(data, int)


class GetOrder(PayPalClient):
    # 2. Set up your server to receive a call from the client
    """You can use this function to retrieve an order by passing order ID as an argument"""

    def get_order(self, order_id):
        """Method to get order"""
        request = OrdersGetRequest(order_id)
        # 3. Call PayPal to get the transaction
        response = self.client.execute(request)
        # 4. Save the transaction in your database. Implement logic to save transaction to your database for future
        # reference.
        print('Status Code: ', response.status_code)
        print('Status: ', response.result.status)
        print('Order ID: ', response.result.id)
        print('Intent: ', response.result.intent)
        print('Links:')
        for link in response.result.links:
            print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
        print(
            f'Gross Amount: {response.result.purchase_units[0].amount.currency_code} {response.result.purchase_units[0].amount.value}')
        return response
