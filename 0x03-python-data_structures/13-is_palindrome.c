#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - return 1 if it is palindrome or 0 if it´s not
 * @head: pointer to head of list
 * Return: number of nodes
 */
int is_palindrome(listint_t **head)
{
	int len, i, flag = 0;
	listint_t *temp = NULL;
	listint_t *temp2 = NULL;
	listint_t *new = NULL;
	listint_t *reverse = NULL;

	if (*head == NULL || head == NULL)
		return (1);
	temp = *head;
	for (len = 0; temp != NULL; len++)
		temp = temp->next;
	new = malloc(len * sizeof(listint_t));
	temp2 = *head;
	for (i = 0; temp2 != NULL; i++)
	{
		new[i].n = temp2->n;
		new[i].next = &new[i + 1];
		temp2 = temp2->next;
	}
	new[len - 1].next = NULL;
	reverse = reverse_listint(head);
	while (reverse != NULL)
	{
		if (new->n == reverse->n)
		{
			new = new->next;
			reverse = reverse->next;
		}
		else
		{
			flag = 1;
			break;
		}
	}
	if (flag == 0)
		return (1);
	return (0);
}
/**
 * reverse_listint - reverse a linked list
 * @head: first element of the list
 * Return: the value of a n node.
 */
listint_t *reverse_listint(listint_t **head)
{
	struct listint_s *next = NULL;
	struct listint_s *prev = NULL;

	if (*head == NULL)
		return (NULL);
	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = (*head);
		(*head) = next;
	}
	(*head) = prev;
	return (*head);
}
