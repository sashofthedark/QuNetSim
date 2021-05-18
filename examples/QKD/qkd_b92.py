#This example implements the B92 QKD protocol in QuNetSim

import numpy as np
from qunetsim.components import Host, Network
from qunetsim.objects import Qubit, Logger
from qunetsim.backends import EQSNBackend
from random import randint

Logger.DISABLED = True

def build_network_b92(eve_interception):
    #this function builds the network for the b92 protocol

    network = Network.get_instance()

    nodes = ['Alice','Bob','Eve']
    network.start(nodes)

    host_alice = Host('Alice')
    host_bob = Host('Bob')
    host_eve = Host('Eve')

    #adding the connections - Alice wants to transfer an encrypted message to Bob
    #Alice---Eve---Bob

    host_alice.add_connection('Eve')
    host_eve.add_connection('Alice')
    host_eve.add_connection('Bob')
    host_bob.add_connection('Eve')

    #starting
    host_alice.start()
    host_bob.start()
    host_eve.start()

    network.add_host(host_alice)
    network.add_host(host_bob)
    network.add_host(host_eve)

    if eve_interception == True:
        #if it's true, then Eve is eavesdropping and measuring all the qubits being transferred
        host_eve.quantum_relay_sniffing = True
        host_eve.set_quantum_relay_sniffing_function(eve_sniffing_quantum)
    
    hosts = [host_alice,host_bob,host_eve]

    return network, hosts
    #and Eve might eavesdrop

def generate_key(key_length):
    #generate an encrypted key of a certain length
    generated_key = []
    for i in range(key_length):
        generated_key.append(randint(0,1))

def sender_qkd(alice, msg_buff, secret_key, receiver):
    #Alice sends the key to Bob
    #the key is an array of binary numbers
    pass

def receiver_qkd(bob, msg_buff, key_size, sender):
    pass

def check_key_sender(alice, msg_buff, lenght_of_check, receiver):
    pass

def check_key_receiver(bob, msg_buff, length_of_check,sender):
    pass

def eve_sniffing_quantum(sender,receiver,qubit):
    base = randint(0,1)
    if base == 1:
        qubit.H()
        #measure the qubit in the diagonal basis basis
        qubit.measure()
    elif base == 0:
        #measure the qubit in the rectilinear basis
        qubit.measure()

def alice_func(alice):
    #everything Alice does will go here
    pass

def bob_func(bob):
    #everything Bob does will go here
    pass

def b92_protocol(eve_interception):
    network, hosts = build_network_b92(eve_interception)
    thread_1 = hosts[0].run_protocol(alice_func,())
    thread_2 = hosts[1].run_protocol(bob_func,())

    thread_1.join()
    thread_2.join()


if __name__ == '__main__':
    b92_protocol(eve_interception = True)