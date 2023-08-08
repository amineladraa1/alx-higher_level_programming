#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - check the code for
 *
 * @head: pointer to the head of the list
 * @number: the node number
 * Return: adress or NULL.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *temp = NULL;
	
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	
	temp = *head;

	while (temp->next && number > temp->next->n)
		temp = temp->next;

	new->next = temp->next;
	temp->next = new;

	return (new);
}
