# -*- coding: utf-8 -*-
"""
@author: Uwe Ziegenhagen
"""

from trello import TrelloClient

client = TrelloClient(
    api_key='<secret_api_key>',
    token='<secret_token>'
)


def list_all_boards(client):
    """
        get list of all boards to determine the ID
        for further functions
    """
    all_boards = client.list_boards()
    for counter, board in enumerate(all_boards):
        print(counter, board.name)

## comment if not needed
# list_all_boards(client)

def print_cards_from_board(board_id, client):
    """
        Access board with ID board_id in the client instance
        and print all non-archived lists with their non-archived cards 
    """
    all_boards = client.list_boards()
    my_board = all_boards[board_id] # 15 = my someday projects
    all_lists_on_board = my_board.list_lists()

    for list in all_lists_on_board:
        if not list.closed:
            for card in list.list_cards():
                if not card.closed:
                    print(list.name, ':' , card.name)
                
print_cards_from_board(15, client)
