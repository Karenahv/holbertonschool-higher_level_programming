#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_list_info(PyObject *p)

{
	int i;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < Py_SIZE(p); i++)
	{
	       printf("Element %d: ", i);
	       printf("%s\n", Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}


}
