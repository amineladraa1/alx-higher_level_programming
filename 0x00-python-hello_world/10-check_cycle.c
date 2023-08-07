#include "lists.h"

/**
 * check_cycle - Entry point
 *
 * Description: 'it checks if there is a loop in the link list'
 *
 * @list: pointer to list
 *
 * Return:  1 (Success) 0 (failure)
 */

int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *rabbit = list;

	while (turtle && rabbit && rabbit->next)
	{
		turtle = turtle->next;
		rabbit = rabbit->next->next;

		if (turtle == rabbit)
			return (1);
	}
	return (0);
}
