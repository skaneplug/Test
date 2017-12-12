"""
You must use hashlib to hash the node ('0.0.0.0:3000') and key ('mykey') combination.
Example: 
x = '0.0.0.0:3000' + 'my-key'
x = node + key
hash = hashlib.md5(x).hexdigest()

More@https://docs.python.org/2/library/hashlib.html
"""
# TODO: Add any required import
import hashlib
import grpc
import db_pb2
from client import DBClient

class RendezvousHash(object):
    """
    This class implements the Rendezvous (HRW) hashing logic.
    DO NOT USE ANY STATIC CLASS VARIABLES!
    """

    def __init__(self, nodes=None):
        """
        Initialize an instance with a node list and others.
        A node means a server host name and its listening port. E.g. '0.0.0.0:3000' 
        :param nodes: a list of DB server nodes to register.
        """
        # TODO
        self.nodes = []
        if nodes is not None:
            self.nodes = nodes
        self.hash = lambda x:hashlib.md5(x).hexdigest()
    
    def get_node(self, key):
        """
        Find the highest hash value via hash(node+key) and the node that generates the highest
        value among all nodes.
        :param key: a string key name.
        :return the highest node.
        """
        highest_node = None
        # TODO
        high_score = -1
        for node in self.nodes:
            x = str(node) + str(key)
            score = self.hash(x)
            if score > high_score:
                (high_score, highest_node) = (score, node)
            elif score == high_score:
                (high_score, highest_node) = (score, max(str(node), str(highest_node)))
        return highest_node


class RendezvousHashDBClient(RendezvousHash):
    """
    This class extends from the above RendezvousHash class and
    integrates DBClient (see@client.py) with RendezvousHash so that 
    client can PUT and GET to the DB servers while the rendezvous hash shards 
    the data across multiple DB servers.
    DO NOT USE ANY STATIC CLASS VARIABLES!
    """

    def __init__(self, db_servers=None):
        """
        1. Initialize the super/parent RendezvousHash class.
        Class inheritance@http://www.python-course.eu/python3_inheritance.php
        2. Create DBClient instance for all servers and save them in a dictionary.
        :param db_servers: a list of DB servers: ['0.0.0.0:3000', '0.0.0.0:3001', '0.0.0.0:3002']
        """
        # TODO
        RendezvousHash.__init__(self, nodes=db_servers)
        self.maps = {}
        if db_servers is not None:
            for node in db_servers:
                pairs = str(node).split(":")
                host = pairs[0]
                port = int(pairs[1])
                self.maps[str(node)] = grpc.insecure_channel('%s:%d' % (host, port))

    def put(self, key, value):
        """
        1. Get the highest Rendezvous node for the given key.
        2. Retrieve the DBClient instance reference by the node.
        3. Save the value into DB via client's put(). 
        :param key: a string key.
        :param value: a string key-value pair dictionary to be stored in DB. 
        :return a PutResponse - see@db.proto
        NOTE: Both key and value must be the string type.
        """
        # TODO
        highest_node = self.get_node(key)
        server_channel = self.maps[str(highest_node)]
        stub = db_pb2.DBStub(channel=server_channel)
        _data = db_pb2.Data(entry=value)
        req = db_pb2.PutRequest(id=key, data=_data)
        return stub.put(req)
    
    def get(self, key):
        """
        1. Get the highest Rendezvous node for the given key.
        2. Retrieve the DBClient instance reference by the node.
        3. Get the value by the key via client's get(). 
        :param key: a string key.
        :param value: a string key-value pair dictionary to be stored in DB. 
        :return a GetResposne - see@db.proto
        """
        # TODO
        highest_node = self.get_node(key)
        server_channel = self.maps[str(highest_node)]
        stub = db_pb2.DBStub(channel=server_channel)
        req = db_pb2.GetRequest(id=key)
        return stub.get(req)


    def info(self):
        """
        Return a list of InfoResponse from all servers.
        1. Invoke DB client's info() to retrieve server info for all servers.
        """
        server_info = []
        # TODO
        for k, v in self.maps.items():
            stub = db_pb2.DBStub(channel=v)
            server_info.append(stub.info(db_pb2.Empty()))
        return server_info

        
