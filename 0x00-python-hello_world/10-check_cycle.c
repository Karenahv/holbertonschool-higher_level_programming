#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - find the loop in a linked list
 * @list: first element of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
		return (0);
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			while (1)
			{
				slow = fast;
				while (fast->next != slow && fast->next != list)
					fast = fast->next;
				if (fast->next == list)
					break;
				list = list->next;
			}
			return (1);
		}

	}
	return (0);

}
