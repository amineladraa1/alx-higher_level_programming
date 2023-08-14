#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

/**
 * is_palindrome - check if a linked list is polendrome
 * @head: pointer to head of list
 * Return: 1 (success) 0 (failure)
 */
int is_palindrome(listint_t **head)
{
	listint_t *turtle = *head;
	listint_t *rabbit = *head;
	listint_t *cur = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while(rabbit->next != NULL && rabbit->next->next != NULL)
	{
		turtle = turtle->next;
		rabbit = rabbit->next->next;
	}
	turtle->next = reverseList(turtle->next);
	turtle = turtle->next;
	cur = *head;

	while (turtle != NULL)
	{
		if (cur->n != turtle->n)
			return (0);
		cur = cur->next;
		turtle = turtle->next;
	}
	return (1);
}

/**
 * reverseList - reverse a linked list
 * @head: pointer to head of list
 * Return: a pointer to the first node
 */
listint_t* reverseList(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *cur = head;
	listint_t *next;

	while (cur != NULL)
	{
	next = cur->next;
	cur->next = prev;
	prev = cur;
	cur = next;
	}

	return (prev);
}
