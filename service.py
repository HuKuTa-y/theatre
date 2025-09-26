from repository import TicketRepository
from ticket import Ticket


class TicketService:
    def __init__(self, repository: TicketRepository):
        self.repository = repository

    def create_ticket(self, ticket: Ticket):
        """Добавление билета"""
        return self.repository.create_ticket(ticket)

    def get_all(self):
        '''Получить все билеты'''
        return self.repository.get_all()

    def get_by_id(self, ticket_id: int):
        '''Получить билет по id'''
        return self.repository.get_by_id(ticket_id)

    def update_ticket(self, ticket: Ticket):
        """Изменить существующий билет.
            Если билета не существует, ничего не делать."""
        return self.repository.update_ticket(ticket)

    def delete_ticket(self, ticket_id: int):
        """Удалить существующий билет.
            Если билета не существует, ничего не делать."""
        return self.repository.delete_ticket(ticket_id)