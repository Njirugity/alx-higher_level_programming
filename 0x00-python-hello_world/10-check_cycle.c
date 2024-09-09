#include <stdio.h>
#include "lists.h"

/**
*check_cycle - checks if a singly linked list has a cycle
*@list: singly list to check
*
*Return: 0 if there is no cyclye 1 if there is
**/

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
	{
		return (0);
	}

	slow = list;
	fast = list->next;
	while (slow && fast && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}

		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
