#Author: JC
#Date: 9/9/2018
#Version: 1.0


# Assumes node_to_delete is not tail.
def delete_node(note_to_delete):
    note_to_delete.data = note_to_delete.next.data
    note_to_delete.next = note_to_delete.next.next