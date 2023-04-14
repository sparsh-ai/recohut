# Install Jupyter Notebook

There are many free options to run jupyter notebooks:

- Jupyter lab and Jupyter notebook - Anaconda also provide Jupyter lab and Jupyter notebook tools in local machine
- Google colab - https://colab.research.google.com
- Amazon SageMaker Studio Lab - https://studiolab.sagemaker.aws
- Databricks - For free community edition, use this: https://community.cloud.databricks.com
- Jupyter-try - https://jupyter.org/try
- VS Code Jupyter notebook - This can be accessed by installing `Jupyter` extension in VS code

```makefile
writefile_custom:
# The existing writefile magic command do not allow passing variables, so this custom magic will help in passing the variables also while writing something from IPython notebooks into a file.
	#!/usr/bin/python
	from IPython.core.magic import register_line_cell_magic
	@register_line_cell_magic
	def writefile(line, cell):
		with open(line, 'w') as f:
			f.write(cell.format(**globals()))

sql_config:
	%config SqlMagic.autopandas=True
	%config SqlMagic.displaycon=False
	%config SqlMagic.feedback=False
	%config SqlMagic.displaylimit=5
	%reload_ext sql

watermark:
	%reload_ext watermark
	%watermark -a "Sparsh A." -m -iv -u -t -d
```