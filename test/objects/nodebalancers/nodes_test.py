from datetime import datetime

from test.base import ClientBaseCase
from linode.objects.base import MappedObject

from linode.objects import NodeBalancerNode


class NodeBalancerConfigTest(ClientBaseCase):
    """
    Tests methods of the NodeBalancerNode class
    """
    def test_update_not_populated_saves(self):
        """
        Tests that updating an unpopulated object sends the correct request
        """
        node = NodeBalancerNode(self.client, 24680, 65432, 123456)

        with self.mock_put('/nodebalancers/123456/configs/65432/nodes/24680') as m:
            node.weight = 100
            self.assertEqual(node._populated, False)
            node.save()

            self.assertEqual(m.call_data['weight'], 100)


