import warnings 
from functools import wraps 
from parameterized.parameterized import inspect 
from parameterized.parameterized import parameterized 
from parameterized.parameterized import default_doc_func 
from parameterized.parameterized import default_name_func 
from parameterized.parameterized import skip_on_empty_helper
from parameterized.parameterized import reapply_patches_if_need 
from parameterized.parameterized import delete_patches_if_need 
from parameterized import parameterized_class

def data(input, name_func=None, doc_func=None, skip_on_empty=False, **legacy): 
	doc_func = doc_func or default_doc_func 
	name_func = name_func or default_name_func 

	def parameterized_expand_wrapper(f, instance=None):
		stack = inspect.stack() 
		frame = stack[1]
		frame_locals = frame[0].f_locals 

		parameters = parameterized.input_as_callable(input)()

		if not parameters: 
			if not skip_on_empty: 
				raise ValueError(
					"Parameter iterable is empty (hint: use "
					"`parameterized.expand([], skip_on_empty=True)` to skip "
					"this test when the input is empty)"
				)
			return wraps(f)(lambda: skip_on_empty_helper())
		
		digits = len(str(len(parameters) - 1))
		for num, p in enumerate(parameters): 
			name = name_func(f, "{num:0>{digits}}".format(digits=digits, num=num), p)
			nf = reapply_patches_if_need(f)
			frame_locals[name] = parameterized.param_as_standalone_func(p, nf, name) 
			frame_locals[name].__doc__ = doc_func(f, num, p) 
		
		delete_patches_if_need(f) 

		f.__test__ = False 
	
	return parameterized_expand_wrapper 

def data_class(attrs, input_values):
	return parameterized_class(attrs, input_values) 