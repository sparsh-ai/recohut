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