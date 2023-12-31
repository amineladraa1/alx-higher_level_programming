#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, idx;
	PyObject *object;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (idx = 0; idx < size; idx++)
	{
		printf("Element %d: ", idx);
		object = PyList_GetItem(p, idx);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}	
}
