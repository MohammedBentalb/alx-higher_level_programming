#include "lists.h"

/**
* check_cycle - Function that check if there is a cycle in a list
* @list: the list
* Return: Return 0 || -1
*/

int check_cycle(listint_t *list)
{
	listint_t *first = list, *second = list;

	if (!list)
		return (0);

	while (first && second && second->next)
		{
			first = first->next;
			second = second->next->next;
		if(first == second)
			return (-1);
		}
return (0);
}
